; From K:\masm32\tutorial\console\demo3
;                 Build this with the "Project" menu using
;                       "Console Assemble and Link"

    .486                                    ; create 32 bit code
    .model flat, stdcall                    ; 32 bit memory model
    option casemap :none                    ; case sensitive
 
    include \masm32\include\windows.inc     ; always first
    include \masm32\macros\macros.asm       ; MASM support macros

  ; -----------------------------------------------------------------
  ; include files that have MASM format prototypes for function calls
  ; -----------------------------------------------------------------
    include \masm32\include\masm32.inc
    include \masm32\include\gdi32.inc
    include \masm32\include\user32.inc
    include \masm32\include\kernel32.inc

  ; ------------------------------------------------
  ; Library files that have definitions for function
  ; exports and tested reliable prebuilt code.
  ; ------------------------------------------------
    includelib \masm32\lib\masm32.lib
    includelib \masm32\lib\gdi32.lib
    includelib \masm32\lib\user32.lib
    includelib \masm32\lib\kernel32.lib

    .data
      txtmsg1 db "I am Present group",0
      txtmsg2 db "djtme lgbt",0
      


    .code                       ; Tell MASM where the code starts
; ллллллллллллллллллллллллллллллллллллллллллллллллллллллллллллллллллллллллл
start:                          ; The CODE entry point to the program
    call main                   ; branch to the "main" procedure
    exit
; ллллллллллллллллллллллллллллллллллллллллллллллллллллллллллллллллллллллллл

main proc
    print OFFSET txtmsg2 10        ; the "OFFSET" operator tells MASM that the text 
    print OFFSET txtmsg1
                                ; data is at an OFFSET within the file which means
                                ; in this instance that it is in the .DATA section

    ret                         ; return to the next instruction after "call"

main endp

; ллллллллллллллллллллллллллллллллллллллллллллллллллллллллллллллллллллллллл

end start                       ; Tell MASM where the program ends
