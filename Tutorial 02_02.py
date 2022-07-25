#A function f is defined as follows :
#f(x) = ax3 – bx2 + cx –d, if x > k
#= 0, if x = k
#= -ax3 + bx2 – cx +d, if x < k
#Write a program that reads a, b, c, d, k and x and prints the value of f(x).

from math import pow

a=int(input("Enter a : "))
b=int(input("Enter b : "))
c=int(input("Enter c : "))
d=int(input("Enter d : "))
x=int(input("Enter x : "))
k=int(input("Enter k : "))

if x>k:
    f=a*pow(x,3) - b*pow(x,2) + c*x - d
    print(f)
elif x==k:
    print(0)
else:
    f= -a*pow(x,3) + b*pow(x,2) - c*x + d
    print(f)
