#Count the number of odd and even numbers from a series of numbers 5 to 100 using for and range().

even_count=0
odd_count=0

for i in range(5,101):
    if i%2==0:
        even_count+=1
    else:
        odd_count+=1

print("Number of even number between 5 and 100 is {}.".format(even_count))
print("Number of odd number between 5 and 100 is {}.".format(odd_count))
