

CREATE TABLE itemVariants(
	variantID INT PRIMARY KEY,
	detail NVARCHAR(200),
	color NVARCHAR(50),
	size NVARCHAR(30));
GO

CREATE TABLE items(
	itemID INT PRIMARY KEY,
	name NVARCHAR(255),
	price FLOAT);
GO

CREATE TABLE categories(
	catID INT PRIMARY KEY,
	name NVARCHAR(255));
GO

CREATE TABLE belongTo(
	itemID INT,
	catID INT,
	PRIMARY KEY (itemID,catID),
	FOREIGN KEY (catID) REFERENCES categories(catID),
	FOREIGN KEY (itemID) REFERENCES items(itemID));

