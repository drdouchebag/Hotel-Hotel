import mysql.connector
myconn = mysql.connector.connect(host = 'localhost', user = 'root', password = '1234', database = 'hotel_hotel')
cursor_obj = connection_object.cursor()

#for table customers
c_id = input('Enter the customer ID: ')
name = input('Enter the customer full name: ')
address = input('Enter the primary address: ')
phnumber = input("Enter the customer's phone number: ")
room_id = input('Enter the room number of the allotted suite: ')
check_in = input('Enter the check-in date (YYYY/MM/DD): ')
check_out = input('Enter the check-out date (YYYY/MM/DD): ')
peopleno = input('Enter the number of people: ')

cursor_obj.execute('INSERT INTO customers VALUES({}{}{}{}{}{}{}{}'.format(c_id,name,address,phnumber,room_id,check_in,check_out,peopleno))

#for table employee
emp_id = input('Enter the employee ID: ')
e_name = input('Enter the employee full name: ')
e_address = input('Enter the primary address: ')
e_phnumber = input("Enter the employee's phone number: ")
workinghours = input('Enter the number of hours he/she works: ')
salary = input("Enter the salary he/she recieves: ")
department= input("Enter the department he/she works in: ")

cursor_obj.execute('INSERT INTO employee VALUES({}{}{}{}{}{}{}{}'.format(emp_id,e_name,e_address,e_phnumber,workinghours,salary,department))
