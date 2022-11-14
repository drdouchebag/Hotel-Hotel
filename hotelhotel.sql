CREATE DATABASE Hotel_Hotel;
use Hotel_Hotel;
CREATE TABLE customers(c_id INT, Full_name VARCHAR(255), Address VARCHAR(255), Phone_no INT, Room_id INT, Check_in VARCHAR(255), Check_out VARCHAR(255), no_of_people INT);
CREATE TABLE employee(emp_id INT, Full_name varchar(255), Address VARCHAR(255), Phone_no INT, Working_hours INT, Salary INT, Department VARCHAR(255));

CREATE TABLE rooms(room_id INT, room_type VARCHAR(255), description VARCHAR(255), rent VARCHAR(10));
INSERT INTO rooms VALUES(101, 'Standard Suite Room', 'Living room connected to 2 bedrooms w/ 2 bathrooms', '$550');
INSERT INTO rooms VALUES(102, 'Junior Suite Room', 'Living room connected to a bedroom w/ 1 bathroom', '$350');
INSERT INTO rooms VALUES(103, 'Presidential Suite Room', 'Luxurious living space connected to 2 bedrooms, 2 bathrooms, private balcony & unlimited access to entertainment area', '$1750');
INSERT INTO rooms VALUES(104, 'Honeymoon Suite room', 'Designed for couples; Private master bedroom equipped with en suite bath and a skyline view', '$1200');

CREATE TABLE services(s_no INT, s_name VARCHAR(255));
INSERT INTO services VALUES(001, 'Gaming Room');
INSERT INTO services VALUES(002, 'Swimming Pool');
INSERT INTO services VALUES(003, 'Spa & Jacuzzi');
INSERT INTO services VALUES(004, 'Private Theatre');


CREATE TABLE restaurant(emp_id INT, hierarchy VARCHAR(255), name VARCHAR(255));
