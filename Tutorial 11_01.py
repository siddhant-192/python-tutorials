list_data=['\nName: Emma\n', '\n\nAddress: 221, Some street\n', '\nCity:Mumbai']
fp=open("demo.txt","w") #"a+
fp.writelines(list_data)
fp.close()
with open("demo.txt","r") as f:
    data=f.read()
    lines=data.splitlines()
    for line in lines:
        if (line!=''):
            print(line)
f.close()