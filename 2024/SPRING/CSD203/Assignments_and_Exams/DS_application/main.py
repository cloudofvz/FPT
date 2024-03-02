from tkinter import *
import pygame
from tkinter import filedialog
import tkinter.messagebox
import time
from mutagen.mp3 import MP3
import tkinter.ttk as ttk
import os
root = Tk()
# root.wm_attributes('-transparentcolor', 'grey')
# root.overrideredirect(1)
# root.geometry('100x100')

# Initialze Pygame Mixer
pygame.mixer.init()


# def move_app(e):
#     root.geometry(f'+{e.x_root}+{e.y_root}')

# frame_photo = PhotoImage(file='images/frame.png')
# frame_label = Label(root,border=0,bg='grey',image=frame_photo)
# frame_label.pack()
# frame_label.bind('<B1-Motion>',move_app)

class Song:
    def __init__(self,file):
        self.path = str(file)
        audio = MP3(file)
        self.title = str(audio["TIT2"])
        self.artist = str(audio["TPE1"])
        self.album = str(audio["TALB"])
        self.duration = audio.info.length
       
class Node:
    def __init__(self, data):
        self.data = Song(data)
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def addToHead(self, x): # thêm một nút có giá trị x vào đầu .
        new_node = Node(x)  
        new_node.next = self.head
        self.head = new_node      

    def addToTail(self, x): # thêm một nút có giá trị x vào cuối .
        new_node = Node(x)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node   


def play():
    global paused
    try:
        paused
    except NameError:
        
            global current_song
            pygame.mixer.music.load(current_song.data.path)
            pygame.mixer.music.play(loops=0)
            
            Button(controls_frame, image=pause_btn_img, borderwidth=0,command=play).grid(row=0, column=1, padx=10)
            paused=False
            play_time()
            return
        
    
    else:
        if paused:
            
            pygame.mixer.music.unpause()
            paused=False
            
            Button(controls_frame, image=pause_btn_img, borderwidth=0,command=play).grid(row=0, column=1, padx=10)
            play_time()
            print("Music resumed.")
        else: 
            pygame.mixer.music.pause()
            play_button = Button(controls_frame, image=play_btn_img, borderwidth=0,command=play).grid(row=0, column=1, padx=10)
            play_time()
            print("Music paused.")
            paused=True

      
          
def play_time():
    global current_song
    global paused
    current_time = pygame.mixer.music.get_pos() / 1000
    print(current_time)
    converted_song_length = time.strftime('%M:%S', time.gmtime(current_song.data.duration)) 
    converted_current_time = time.strftime('%M:%S', time.gmtime(current_time))
	# Increase current time by 1 second
    current_time +=1
	
    if int(my_slider.get()) == int(current_song.data.duration):
        status_bar.config(text=f'Time Elapsed: {converted_current_time}  of  {converted_song_length}  ')
    elif paused:
        pass
    elif int(my_slider.get()) == int(current_time):
        # Update Slider To position
        slider_position = int(current_song.data.duration)
        my_slider.config(to=slider_position, value=int(current_time))

    else:
        # Update Slider To position
        slider_position = int(current_song.data.duration)
        my_slider.config(to=slider_position, value=int(my_slider.get()))
        
        # convert to time format
        converted_current_time = time.strftime('%M:%S', time.gmtime(int(my_slider.get())))

        # Output time to status bar
        status_bar.config(text=f'Time Elapsed: {converted_current_time}  of  {converted_song_length}  ')

        # Move this thing along by one second
        next_time = int(my_slider.get()) + 1
        my_slider.config(value=next_time)

    # update time
    status_bar.after(1000, play_time)

def stop():
	
	pygame.mixer.music.stop()
	
      
def next_song():
    status_bar.config(text='')
    my_slider.config(value=0)
    global current_song
    current_song= current_song.next
    pygame.mixer.music.load(current_song.data.path)
    pygame.mixer.music.play(loops=0)
    

def slide(x):
    global current_song
    pygame.mixer.music.load(current_song.data.path)
    slider_label.config(text=f'{int(my_slider.get())} of {int(current_song.data.duration)}')   
    pygame.mixer.music.play(loops=0, start=int(my_slider.get()))
def cr(lit):

    current_song_info = lit.head
    row_x = 0
    while current_song_info:
        # Tạo music_info
        music_info = Frame(song_box, bg="blue", width=335, height=74.6)
        music_info.grid_propagate(False)
        music_info.grid(row=row_x, column=0)

        index =  Label(music_info, text=row_x+1, fg="white", bg="grey", height=2)
        index.config(font=("Helvetica", 10))
        index.grid(row=0, column=0 )

        music_player_subtitle = Frame(music_info, bg="white", width=200, height=74.6)
        music_player_subtitle.grid_propagate(False)
        music_player_subtitle.grid(row=0, column=1)
        # Tạo và đặt music_title
        music_title = Label(music_player_subtitle, text=current_song_info.data.title, fg="white", bg="black", height=2)
        music_title.config(font=("Helvetica", 10))
        music_title.grid(row=0, column=0)

        # Tạo và đặt music_artist
        music_artist = Label(music_player_subtitle, text=current_song_info.data.artist, fg="white", bg="black", height=1)
        music_artist.config(font=("Helvetica", 9))
        music_artist.grid(row=1, column=0)


        # Tạo và đặt music_time
        music_time = Label(music_info, text=time.strftime('%M:%S',time.gmtime(current_song_info.data.duration)), fg="white", bg="black", height=1)
        music_time.grid(row=0, column=2, pady=(10, 0))
        row_x +=1
        current_song_info = current_song_info.next


listsong = SinglyLinkedList()
for file in os.listdir('list_song'):
    full_path = os.path.join('list_song', file)
    _, file_extension = os.path.splitext(full_path)
    if os.path.isfile(full_path) and file_extension== '.mp3':
        listsong.addToTail(full_path)
current_song = listsong.head       


root.title(' MP3 Player')
root.geometry("500x400")




# Create Master Frame
master_frame = Frame(root)
master_frame.pack(pady=20)

# Create Playlist Box
# Tạo song_box
song_box = Frame(master_frame, bg="red", width=335, height=274)
song_box.grid_propagate(False)
song_box.grid(row=0, column=0)

cr(listsong)


# Define Player Control Button Images
back_btn_img = PhotoImage(file='images/back50.png')
forward_btn_img =  PhotoImage(file='images/forward50.png')
play_btn_img =  PhotoImage(file='images/play50.png')
pause_btn_img =  PhotoImage(file='images/pause50.png')
stop_btn_img =  PhotoImage(file='images/stop50.png')

# Define Volume Control Images
global vol0
global vol1
global vol2
global vol3
global vol4
vol0 = PhotoImage(file='images/volume0.png')
vol1 = PhotoImage(file='images/volume1.png')
vol2 = PhotoImage(file='images/volume2.png')
vol3 = PhotoImage(file='images/volume3.png')
vol4 = PhotoImage(file='images/volume4.png')

# Create Player Control Frame
controls_frame = Frame(master_frame)
controls_frame.grid(row=1, column=0, pady=20)

# Create Volume Meter
volume_meter = Label(master_frame, image=vol0)
volume_meter.grid(row=1, column=1, padx=10)

# Create Volume Label Frame
volume_frame = LabelFrame(master_frame, text="Volume")
volume_frame.grid(row=0, column=1, padx=30)

# Create Player Control Buttons
back_button = Button(controls_frame, image=back_btn_img, borderwidth=0)
forward_button = Button(controls_frame, image=forward_btn_img, borderwidth=0,command=next_song)
play_button = Button(controls_frame, image=play_btn_img, borderwidth=0,command=play)
pause_button = Button(controls_frame, image=pause_btn_img, borderwidth=0)
stop_button =  Button(controls_frame, image=stop_btn_img, borderwidth=0,command=stop)

back_button.grid(row=0, column=0, padx=10)
forward_button.grid(row=0, column=2, padx=10)
play_button.grid(row=0, column=1, padx=10)
pause_button.grid(row=0, column=3, padx=10)
stop_button.grid(row=0, column=4, padx=10)



# Create Status Bar
status_bar = Label(root, text='', bd=1, relief=GROOVE, anchor=E)
status_bar.pack(fill=X, side=BOTTOM, ipady=2)

# Create Music Position Slider
my_slider = ttk.Scale(master_frame, from_=0, to=100, orient=HORIZONTAL, value=0,command=slide, length=360)
my_slider.grid(row=2, column=0, pady=10)

# Create Volume Slider
volume_slider = ttk.Scale(volume_frame, from_=0, to=1, orient=VERTICAL, value=1, length=125)
volume_slider.pack(pady=10)

# Create Temporary Slider Label
slider_label = Label(root, text="0")
slider_label.pack(pady=10)

 
root.mainloop()            
