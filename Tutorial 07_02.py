n=int(input('Enter number of students : '))
student = {}
for i in range(0,n):
    roll = input("Enter Roll Number : ")
    Name = input("Enter Name : ")
    student[roll]= Name
print(student)
print(sorted(student.keys()))
print(sorted(student.items()))
print(sorted(student.values()))
print(sorted(student.keys(),reverse=True))
print(sorted(student.items(),reverse=True))
