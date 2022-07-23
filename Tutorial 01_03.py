#Solve quadratic equation ax2+bx+c=0

print("ax2+bx+c=0")
a=int(input("Enter a :"))
b=int(input("Enter b :"))
c=int(input("Enter c :"))

temp= (b**2 - 4*a*c)**0.5
if a!=0:
  sol1= (-b + temp)/2*a
  sol2= (-b - temp)/2*a
  print("Solution to the qudratic equation is ",sol1,sol2)
else:
  if b!=0:
    sol3=-c/b
    print("Solution to the linear equation is ",sol3)
  else:
    print("The equation is invalid.")
