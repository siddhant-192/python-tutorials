n=int(input("Enter number of students : "))
student = {}
for i in range(0,n):
    roll = int(input("Enter Roll Number : "))
    Name = input("Enter Name : ")
    student[Name]= roll
newdict = {key: ('Odd' if value%2==1 else 'Even') for(key,value) in student.items()}
print(newdict)
