fp=open("demo1.txt","w+")
while True:
    data=input("Enter data: ")
    fp.write(data)
    ans=input("Do you want to continue (y/n)")
    if ans in ('n','N'):
        break    

fp.close()

f=open("demo1.txt","r")
count=0
data=f.read()
print(data)
words=data.split()

for eachword in words:
    if eachword[-1]=='e':
        count+=1

print("Number of words ending with 'e': ", count)

f.close()