import mysql.connector 
import pandas

connection = mysql.connector.connect(host = 'localhost', user = 'root', password = '1234', database = 'hotel_hotel')
cursor_obj = connection.cursor()


#enter new customer details    
def check_in():
  c_id = int(input('Enter the customer ID: '))
  name = input('Enter the customer full name: ')
  address = input('Enter the primary address: ')
  phnumber = input("Enter the customer's phone number: ")
  room_no = input('Enter the room number of the allotted suite: ')
  check_in = input('Enter the check-in date (YYYY/MM/DD): ')
  check_out = input('Enter the check-out date (YYYY/MM/DD): ')
  peopleno = int(input('Enter the number of people: '))

  st1="'"+name.upper()+"'"
  st2="'"+address.upper()+"'"
  st3="'"+phnumber+"'"
  st4="'"+room_no+"'"
  st5="'"+check_in+"'"
  st6="'"+check_out+"'"
  
  cursor_obj.execute('INSERT INTO customers VALUES({},{},{},{},{},{},{},{})'.format(c_id,st1, st2, st3, st4, st5, st6, peopleno))
  connection.commit()
  cursor_obj.execute('UPDATE rooms SET Availability = "OCCUPIED" WHERE room_no = {}'.format(st4))
  connection.commit()
  print('New customer details entered successfully')
  
  
  
 #check out a customer
 def check_out():
  enter_id = int(input('Enter the customer ID: '))
  #search for the room number the customer was staying in
  cursor_obj.execute('SELECT room_no FROM rooms NATURAL JOIN customers WHERE c_id = {}'.format(enter_id))
  records = cursor_obj.fetchall()
  for i in records:
    room_num = i[0]
    
  cursor_obj.execute('DELETE FROM customers WHERE c_id = {}'.format(enter_id))
  connection.commit()
  
  #update the availability status to vacant
  cursor_obj.execute('UPDATE rooms SET Availability = "VACANT" WHERE room_no = "{}"'.format(room_num))
  connection.commit()
  print('Check-out successful!')
  

#enter new employee details
def newemp():
  emp_id = int(input('Enter the employee ID: '))
  e_name = input('Enter the employee full name: ')
  e_address = input('Enter the primary address: ')
  e_phnumber = input("Enter the employee's phone number: ")
  working_hours = int(input('Enter the number of hours he/she works: '))
  salary = int(input('Enter the annual salary: '))
  dept = input('Enter the department of duty: ')
  
  st1="'"+e_name.upper()+"'"
  st2="'"+e_address.upper()+"'"
  st3="'"+e_phnumber+"'"
  st4="'"+dept.upper()+"'"

  cursor_obj.execute('INSERT into employee VALUES({},{},{},{},{},{},{})'.format(emp_id, st1, st2, st3, working_hours, salary, st4))
  connection.commit()
  print('New employee details entered successfully')

  

#display the types of suites in the hotel
def suites():
  cursor_obj.execute('SELECT * FROM roomtypes;')
  records = cursor_obj.fetchall()
  for row in records:
    print('ID: ', row[0])
    print('Type: ', row[1])
    print('Description: ', row[2])
    print('Rent per night: ', row[3])
    
    
    
#display the available rooms in the hotel
data = []
def available():
  cursor_obj.execute('SELECT count(*) FROM rooms WHERE Availability = "VACANT"')
  for i in cursor_obj:
    print('The number of available rooms: ', i[0])
    
  cursor_obj.execute('SELECT * FROM rooms WHERE Availability = "VACANT"')
  roomdata = cursor_obj.fetchall()
  for row in roomdata:
      room_no = row[0]
      floor = row[1]
      avail = row[3]
      data.append([room_no, floor, avail])

headers1 = [' 1 |',' 2 |',' 3 |',' 4 |',' 5 |',' 6 |',' 7 |',' 8 |',' 9 |','10 |','11 |','12 |','13 |','14 |','15 |','16 |','17 |','18 |']
headers=["Room no.", "Floor", "Status"]
df = pandas.DataFrame(data,headers1,headers)
print(df)
print('                                         ')

    
  
  
 
#counts the number of nights
def numberofnights(custid1):
  cursor_obj.execute('SELECT datediff(check_out, check_in) FROM customers WHERE c_id = {}'. format(custid1))
  days = cursor_obj.fetchall()
  for i in days:
    x = int(i[0])
  return x



#generates the final bill
def bill():
  total_cost = 0
  custid1 = int(input('Enter the customer ID: '))
  
  cursor_obj.execute(' SELECT rent FROM customers NATURAL JOIN rooms,roomtypes WHERE rooms.room_id = roomtypes.room_id AND c_id = {};'.format(custid1))
  data1 = cursor_obj.fetchall()
  for row1 in data1:
    rentx = row1[0]
    rentint = int(rentx[1:])
  no_nights = numberofnights(custid1)  #function call to get the number of nights
  total_cost_room = rentint*no_nights #gives the total rent for x number of nights
  total_cost += total_cost_room

  while True:
      total_service = 0
      serv = input('DID THE CUSTOMER OPT ANY SERVICE(S)? (Y/N): ')
      if serv == 'Y' or serv == 'y':
          cursor_obj.execute('SELECT * FROM services')
          records = cursor_obj.fetchall()
          for row2 in records:
              print('Service ID:', row2[0])
              print('Service Name:', row2[1])
              print('Charges: ', row2[2]) #print all the service details
          serviceID = input('ENTER THE SERVICE ID: ')
          cursor_obj.execute('SELECT s_charge FROM services WHERE s_no = "{}"'.format(serviceID))
          charge = cursor_obj.fetchall()
          for y in charge:
              servicecost = y[0]
              servicecostint = int(servicecost[1:])
          total_cost += servicecostint
             
      else:
          break
  print('Your Total Bill is: ',total_cost, 'including VAT \n',
        'Room bill:', total_cost_room)
    
    
    
    
#display the employee details
def empdetails():
  cursor_obj.execute('SELECT * FROM employee;')
  details = cursor_obj.fetchall()
  for k in details:
    print('Employee ID:', k[0])
    print('Full Name:', k[1])
    print('Primary Address:', k[2])
    print('Phone number:', k[3])
    print('Working hours:', k[4])
    print('Annual Salary:', k[5])
    print('Department:', k[6])
    
    
  
  
  
#display the number of staff in each department
def empnumber():
  cursor_obj.execute('SELECT Department, Count(*) FROM employees GROUP BY Department;')
  details = cursor_obj.fetchall()
  for k in details:
    print(k[0], k[1])
  
  
  
  
  
#display the bookings between two dates
def bookings():
    start_date = input('Enter the start date (YYYY/MM/DD): ')
    end_date = input('Enter the end date (YYYY/MM/DD): ')
    cursor_obj.execute('SELECT * FROM customers WHERE Check_in BETWEEN "{}" AND "{}"'.format(start_date, end_date))
    bookingdata= cursor_obj.fetchall()
    for i in range(len(bookingdata)):
        print('Booking #',i+1)
        print('Name: ', bookingdata[i][1])
        print('Room_no: ', bookingdata[i][4])
        print('Check_in: ', bookingdata[i][5])
        print('Check_out: ', bookingdata[i][6])
        print('                               ')
      

  
 
  
 cusdata=[]
def custdetails():
    cursor_obj.execute('SELECT * FROM customers')
    details = cursor_obj.fetchall()
    for row in details:
      cus_id = row[0]
      name = row[1]
      address = row[2]
      phone = row[3]
      room = row[4]
      checkin = row[5]
      cusdata.append([cus_id, name, address, phone, room, checkin])

    headers1 = []
    for i in range(len(details)):
        headers1.append('→')
    headers=["ID", "Name", "Address", "Phone", "Room", "Check-in"]
    df = pandas.DataFrame(cusdata,headers1,headers)
    print(df)
    print('                                         ')

    

    
    
  
#menu driven execution of functions
while True:
  print(' 1. Check In \n',
      '2. Check Out \n',
      '3. Generate total bill \n',
      '4. Show suite types \n',
      '5. Available Rooms \n',
      '6. Employees details \n',
      '7. New employee \n',
      '8. Departments \n',
      '9. Customer details \n',
      '10. Bookings for the month \n',
       )
  user_inp = int(input('Enter the option'))
  if user_inp == 1:
    check_in()
    
  elif user_inp == 2:
    check_out()
    
  elif user_inp = 3:
    bill()
    
  elif user_inp = 4:
    suites()
    
  elif user_inp = 5:
    available()
    
  elif user_inp = 6:
    empdetails()
    
  elif user_inp = 7:
    newemp()
    
  elif user_inp == 8:
    empnumber()
    
  elif user_inp == 9:
    custdetails()
      
  elif user_inp == 10:
    bookings()
  
  
  


