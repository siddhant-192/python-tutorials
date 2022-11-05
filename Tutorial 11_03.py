fp=open("demo1.txt","r")
count=0
print(fp.read())
print("file pointer is at",fp.tell())
#to move the file pointer to start of the file so first character
fp.seek(0)
print("file pointer is at",fp.tell())

for line in fp:
    if line[0] not in 'T':
        count+=1

print("Number of lines not starting with T: ",count)
fp.close()