#Program for question 1 and question 2 have been written togeather.

class Student:
	def __init__(self, rollno, name, age):
		try:
			if age<18:
				raise ValueError(age) 
			self.roll=rollno 
			self.name=name 
			self.age=age
		except ValueError:
			print("Age should be above 17")
	
	def display(self):
		print(f 'Roll No. is {self.roll}\nName is {self.name}\nAge is {self.age}')

try:
	s1 = Student(1 , 'Siddhant Mantri' , 19)
	s1.display()
	s2 = Student(2 , 'John Bohn' , 17)
	s2.display()
except:
	print('Object does not exist')
