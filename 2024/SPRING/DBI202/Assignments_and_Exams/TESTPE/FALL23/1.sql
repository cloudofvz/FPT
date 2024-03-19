
CREATE TABLE Customers
(
	custID VARCHAR(50) PRIMARY KEY,
	custName NVARCHAR(100),
	custAddress NVARCHAR(200)
);

CREATE TABLE Rooms
(
	roomID VARCHAR(50) PRIMARY KEY,
	roomPrice MONEY
);

CREATE TABLE Services
(
	serviceID VARCHAR(50) PRIMARY KEY,
	serviceName NVARCHAR(100),
	servicePrice MONEY
);

CREATE TABLE Contracts
(
	contractID VARCHAR(50) PRIMARY KEY,
	quantity INT,
	custID VARCHAR(50) FOREIGN KEY 
	REFERENCES Customers(custID),
	roomID VARCHAR(50) FOREIGN KEY
	REFERENCES Rooms(roomID),
	serviceID VARCHAR(50) FOREIGN KEY
	REFERENCES Services(serviceID)
);
