CREATE DATABASE Hotel_Hotel;
use Hotel_Hotel;
CREATE TABLE customers(c_id INT, Full_name VARCHAR(255), Address VARCHAR(255), Phone_no INT, Room_id INT, Check_in VARCHAR(255), Check_out VARCHAR(255), no_of_people INT);
CREATE TABLE employee(emp_id INT, Full_name varchar(255), Address VARCHAR(255), Phone_no INT, Working_hours INT, Salary INT, Department VARCHAR(255));
CREATE TABLE rooms(room_type VARCHAR(255), room_id INT, description VARCHAR(255));
CREATE TABLE services(s_no INT, s_name VARCHAR(255), emp_id INT);
CREATE TABLE restaurant(emp_id INT, hierarchy VARCHAR(255), name VARCHAR(255));
