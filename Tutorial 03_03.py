#Print prime numbers within an interval use (break, for with else).

num=int(input("Enter number to determine range : "))

if num<=1:
    print("No prime numbers.")

else:
    for i in range(2,num):
        for j in range(2,i-1):
            if i%j==0:
                break
        else:
            print("{} is a prime number.".format(i))
