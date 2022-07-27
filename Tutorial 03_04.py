#Display the Fibonacci sequence up to nth term where n is provided by the user (use while loop).

n = int(input("Enter the number of Fibonacci terms to be displayed : "))

a=0
b=1
print("Fibonacci series : ",end='')
print(a,end=',')

while n>2:
    temp=a+b
    a=b
    b=temp
    print(a,end=',')
    n-=1
print(b)
