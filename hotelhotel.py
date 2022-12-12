import mysql.connector
myconn = mysql.connector.connect(host = 'localhost', user = 'root', password = '1234', database = 'hotel_hotel')
cursor_obj = connection_object.cursor()


#enter new customer details    
def newcust():
  c_id = input('Enter the customer ID: ')
  name = input('Enter the customer full name: ')
  address = input('Enter the primary address: ')
  phnumber = input("Enter the customer's phone number: ")
  room_no = input('Enter the room number of the allotted suite: ')
  check_in = input('Enter the check-in date (YYYY/MM/DD): ')
  check_out = input('Enter the check-out date (YYYY/MM/DD): ')
  peopleno = input('Enter the number of people: ')
  
  cursor_obj.execute('INSERT INTO customers VALUES({}{}{}{}{}{}{}{}'.format(c_id,name,address,phnumber,room_no,check_in,check_out,peopleno))
  cursor_obj.execute('UPDATE rooms SET Availability = "Occupied" WHERE room_no = {}'.format(room_no))
  print('New details entered successfully')
  

#for table employee
def newemp():
  emp_id = input('Enter the employee ID: ')
  e_name = input('Enter the employee full name: ')
  e_address = input('Enter the primary address: ')
  e_phnumber = input("Enter the employee's phone number: ")
  working_hours = input('Enter the number of hours he/she works: ')
  salary = input('Enter the annual salary: ')
  dept = input('Enter the department of duty')

  cursor_obj.execute('INSERT into employees VALUES{}{}{}{}{}{}{}'.format(emp_id,e_name,e_address,e_phnumber,working_hours,salary,dept))
  print('New details entered successfully')


#display the types of suites in the hotel
def suites():
  cursor_obj.execute('SELECT * FROM roomtypes;')
  records = cursor_obj.fetchall()
  for row in records:
    print('ID:', row[0])
    print('Type', row[1])
    print('Description', row[2])
    print('Rent per night', row[3])
    
#display the count of available rooms in the hotel
def available():
  cursor_obj.execute('SELECT count(*) FROM rooms WHERE Availability = "Vacant";')
  for i in cursor_obj:
    print(i)
    
 

#count the number of nights
def numberofnights():
  custid = input('Enter the customer ID')
  cursor_obj.execute('SELECT datediff(check_out, check_in) FROM customers WHERE c_id = {};', format(custid))
  days = cursor_obj.fetchall()
  for i in days:
    x = int(i)
 return x




#generate the final bill
def bill():
  total_cost = 0
  custid = input('Enter the customer ID')
  cursor_obj.execute(' SELECT rent FROM customers NATURAL JOIN rooms,roomtypes WHERE rooms.room_id = roomtypes.room_id AND c_id = {};'.format(custid))
  data1 = cursor_obj.fetchall()
  for row1 in data1:
    rentx = row1[0]
  no_nights = numberofnights()  #function call to get the number of nights
  total_cost += rentx*no_nights #gives the total rent for x number of nights
  
  serv = input('DID THE CUSTOMER OPT ANY SERVICE(S)? (Y/N): ')
  if serv = 'Y':
    cursor_obj.execute('SELECT * FROM services')
    records = cursor_obj.fetchall()
    for row2 in records:
    print('ID:', row2[0])
    print('Service Name', row2[1])
    print('Charges', row[2]) #print all the service details
    
    
    service1 = input('ENTER THE NAME OF THE SERVICE: ')
    cursor_obj.execute('SELECT s_charge FROM services WHERE s_name = "{}"'.format(service1))
    charge = cursor_obj.fetchall()
    for y in charge:
      servicecost = y[0]
    total_cost += servicecost
    print(total_cost) #prints cost including rent and service charges
    
  else:
    print(total_cost) #prints only the rent
    
    
#display the employee details
def empdetails():
  cursor_obj.execute('SELECT * FROM employees;')
  details = cursor_obj.fetchall()
  for k in details:
    print('ID', k[0])
    print('Name', k[1])
    print('Address', k[2])
    print('Phone number', k[3])
    print('Working hours', k[4])
    print('Salary', k[5])
    print('Department', k[6])
    
  
#display the number of staff in each department
def empnumber():
  cursor_obj.execute('SELECT Department, Count(*) FROM employees GROUP BY Department;')
  details = cursor_obj.fetchall()
  for k in details:
    print(k[0], k[1])
  
  
  
  
  
#menu driven execution of functions
while True:
  print(' 1. Enter new customer details \n',
      '2. Enter new employee details \n',
      '3. Show suite types \n',
      '4. How many rooms are available \n',
      '5. Generate a bill \n',
      '6. Display employee details \n',
      '7. How many employees in each department')
  user_inp = int(input('Enter the option'))
  if user_inp = 1:
    newcust()
  elif user_inp = 2:
    newemp()
  elif user_inp = 3:
    suites()
  elif user_inp = 4:
    available()
  



