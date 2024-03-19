create table items(
	itemID INT PRIMARY KEY, 
	name nvarchar(255), 
	price float
)

create table itemVariants(
	variantID INT PRIMARY KEY, 
	detail nvarchar(200), 
	color nvarchar(50), 
	size nvarchar(30), 
	itemID INT,
	FOREIGN KEY (itemID) REFERENCES items(itemID)
)

create table categories(
	catID INT PRIMARY KEY, 
	name nvarchar(255)
)

create table belongTo(
	catID INT, 
	itemID INT, 
	PRIMARY KEY(catID, itemID), 
	FOREIGN KEY (catID) REFERENCES categories(catID),
	FOREIGN KEY (itemID) REFERENCES items(itemID)	
)