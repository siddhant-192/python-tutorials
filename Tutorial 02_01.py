#Accept three sides of a triangle and print if the triangle is equilateral, isosceles or scalene. 

a=int(input("Enter side a : "))
b=int(input("Enter side b : "))
c=int(input("Enter side c : "))

if a==b==c:
    print("Equilateral")
elif a==b or b==c or c==a:
    print("Isosceles")
else:
    print("Scalene")
