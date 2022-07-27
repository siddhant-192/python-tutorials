#Accept a sentence and print the reverse of each words using for and range().

sen=input("Enter a sentence : ")
n=len(sen)
rev=''

for i in range(n):
    rev+=sen[n-1-i]

print("Reversed string : ",rev)
