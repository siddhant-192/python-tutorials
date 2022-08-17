#apply set function to find the count of number of vowels in a given string
str=input("Enter a string : ")

s={'a','e','i','o','u','A','E','I','O','U'}
count=0

for char in str:
    if char in s:
        count+=1

print("Number of vowels in string is : ",count)
