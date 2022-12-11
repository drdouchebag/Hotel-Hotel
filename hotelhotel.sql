CREATE DATABASE Hotel_Hotel;
use Hotel_Hotel;
CREATE TABLE customers(c_id INT, Full_name VARCHAR(255), Address VARCHAR(255), Phone_no INT, room_no INT, Check_in VARCHAR(255), Check_out VARCHAR(255), no_of_people INT);
CREATE TABLE employee(emp_id INT, Full_name varchar(255), Address VARCHAR(255), Phone_no INT, Working_hours INT, Salary INT, Department VARCHAR(255));

CREATE TABLE roomtypes(room_id INT PRIMARY KEY, room_type VARCHAR(255), description VARCHAR(255), rent VARCHAR(10));
INSERT INTO roomtypes VALUES(101, 'Standard Suite Room', 'Living room connected to 2 bedrooms w/ 2 bathrooms', '$550');
INSERT INTO roomtypes VALUES(102, 'Junior Suite Room', 'Living room connected to a bedroom w/ 1 bathroom', '$350');
INSERT INTO roomtypes VALUES(103, 'Presidential Suite Room', 'Luxurious living space connected to 2 bedrooms, 2 bathrooms, private balcony & unlimited access to entertainment area', '$1750');
INSERT INTO roomtypes VALUES(104, 'Honeymoon Suite room', 'Designed for couples; Private master bedroom equipped with en suite bath and a skyline view', '$1200');


/*table stating the availability of all 18 rooms in the hotel */
CREATE TABLE rooms(room_no VARCHAR(50), floor VARCHAR(50), room_id INT, Availability VARCHAR(50));
/* 6 standard suite rooms */ 
INSERT INTO rooms VALUES('S01', 'Floor 2' , 101 , 'VACANT');
INSERT INTO rooms VALUES('S02', 'Floor 2' , 101 , 'VACANT');
INSERT INTO rooms VALUES('S03', 'Floor 2' , 101 , 'VACANT');
INSERT INTO rooms VALUES('S04', 'Floor 3' , 101 , 'VACANT');
INSERT INTO rooms VALUES('S05', 'Floor 3' , 101 , 'VACANT');
INSERT INTO rooms VALUES('S06', 'Floor 3' , 101 , 'VACANT');

/* 6 junior suite rooms*/
INSERT INTO rooms VALUES('J01', 'Floor 4' , 102 , 'VACANT');
INSERT INTO rooms VALUES('J02', 'Floor 4' , 102 , 'VACANT');
INSERT INTO rooms VALUES('J03', 'Floor 4' , 102 , 'VACANT');
INSERT INTO rooms VALUES('J04', 'Floor 4' , 102 , 'VACANT');
INSERT INTO rooms VALUES('J05', 'Floor 4' , 102 , 'VACANT');
INSERT INTO rooms VALUES('J06', 'Floor 4' , 102 , 'VACANT');

/* 4 presidential suite rooms */
INSERT INTO rooms VALUES('P01', 'Floor 5' , 103 , 'VACANT');
INSERT INTO rooms VALUES('P02', 'Floor 6' , 103 , 'VACANT');
INSERT INTO rooms VALUES('P03', 'Floor 7' , 103 , 'VACANT');
INSERT INTO rooms VALUES('P04', 'Floor 8' , 103 , 'VACANT');

/* 2 honeymoon suite rooms */
INSERT INTO rooms VALUES('H01', 'Floor 9' , 104 , 'VACANT');
INSERT INTO rooms VALUES('H02', 'Floor 9' , 104 , 'VACANT');

CREATE TABLE services(s_no INT, s_name VARCHAR(255));
INSERT INTO services VALUES(001, 'Gaming Room');
INSERT INTO services VALUES(002, 'Swimming Pool');
INSERT INTO services VALUES(003, 'Spa & Jacuzzi');
INSERT INTO services VALUES(004, 'Private Theatre');

