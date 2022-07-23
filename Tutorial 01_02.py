#Compute areas of the following (Find the equation and implement in python):
#Circle
#Square
#Sphere
#Triangle
#Rectangle

PI=3.1415

r=float(input("Enter the radius of the circle : "))
area=PI*r*r
print("Area of circle of radius {} is {}".format(r,area))

s=float(input("Enter the length of side of square : "))
area=s*s
print("Area of square of side {} is {}".format(s,area))

r=float(input("Enter the radius of the sphere : "))
area=2*PI*r*r
print("Area of sphere of radius {} is {}".format(r,area))

b=float(input("Enter the breadth of triangle : "))
h=float(input("Enter the height of triangle : "))
area=0.5*b*h
print("Area of triangle is {}".format(area))

l=float(input("Enter the length of rectangle : "))
b=float(input("Enter the height of rectangle : "))
area=l*b
print("Area of rectangle is {}".format(area))
