create database Hotel_Hotel;
use Hotel_Hotel;
create table customers(c_id int, Full_name varchar(255), Address varchar(255), Phone_no int, Room_id int, Check_in varchar(255), Check_out varchar(255), no_of_people int);
create table employee(emp_id int, Full_name varchar(255), Address varchar(255), Phone_no int, Working_hours int, Salary int, Department varchar(255));
create table rooms(room_type varchar(255),room_id int,description varchar(255));
create table services(s_no int,s_name varchar(255),emp_id int);
create table restaurant(emp_id int, hierarchy varchar(255),name varchar(255));

