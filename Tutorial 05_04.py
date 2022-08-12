#Print the numbers in words
num=('Zero','One','Two','Three','Four','Five','Six','Seven','Eight','Nine')
a=int(input("Enter a number : "))
st=''
b=a
while b > 0:
    temp=b-((b//10)*10)
    st=str(num[temp])+' '+st
    b=b//10
print(st)
