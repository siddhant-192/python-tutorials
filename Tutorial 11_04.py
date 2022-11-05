n=int(input("Enter line number: "))
with open ('demo1.txt','r') as fp:
    lines=fp.readlines()
    ptr=1
    with open('demo1.txt','w') as fw:
        for line in lines:
            if ptr!=n:
                fw.write(line)
            ptr+=1
    fw.close()
    print("Deleted")
    fp.seek(0)
    print(fp.read())
fp.close()