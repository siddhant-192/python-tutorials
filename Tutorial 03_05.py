#Accept password from user give five chances (use while with else).

password="N0tpass@765"
cnt=5
while cnt>0:
    str=input("Enter the password : ")
    cnt-=1
    if str==password:
        print("Correct.")
        break
    else:
        print("Wrong password. {} attempts left.".format(cnt))
else:
    print("You have exceeded your 5 attempts.")
