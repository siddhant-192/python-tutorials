class Customer:
	def __init__(self,f_name,last_name,age,city,country):
		self.f_name=f_name 
		self.l_name=last_name 
		self.age=age 
		self.city=city 
		self.country=country


import sqlite3
from cust import Customer


connection=sqlite3.connect('customer.db') 
cursor=connection.cursor()

cursor.execute('''drop table customer''')
cursor.execute('''create table customer(first_name text, last_name text, age integer, city text, country text);''')

def create_customer(customer): 
	with connection:
		cursor.execute("insert into customer values (:first,:last,:age,:city,:country)",{'first':customer.f_name,'last':customer.l_name,'age':customer.age,'city':customer.city,' country':customer.country})

def update_city(customer,mcity):
	with connection:
		cursor.execute("update customer set city=:city where first_name=:first", {'first':customer.f_name,'city':mcity})

def delete_customer(customer): 
	with connection:
		cursor.execute("delete from customer where first_name=:first", {'first':customer.f_name})

def get_customer(): 
	with connection:
		cursor.execute("select * from customer;") 
		return cursor.fetchall()

customer_1=Customer('John','May',30,'Mumbai','India') 
customer_2=Customer('jill','Saint',23,'Mumbai','India')

create_customer(customer_1) 
create_customer(customer_2)

print(get_customer())


update_city(customer_1,'Delhi') 
print(get_customer())

delete_customer(customer_2) 
print(get_customer())

connection.close()