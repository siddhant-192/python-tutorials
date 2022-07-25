#A cloth showroom has announced the following discounts on the purchase of specific items:
#Amount Shorts Pants Shits/T-Shirts
#0-100 – 3% 5%
#101-200 5% 8% 10%
#201-300 10% 12% 15%
#Above 300 18% 20% 22%
#Ask user to enter the amount and assign following code for the items such as s for shorts, p for pans and t for shirts/t-shirts.
#Compute the discount and net amount paid by customer.

cloth=input("Enter cloth type : ")
amt=int(input("Enter amount (s p t) : "))

if amt>=0 and amt<=100:
    if cloth=='s':
        bill=amt*1
    elif cloth=='p':
        bill=amt*0.97
    elif cloth=='t':
        bill=amt*0.95
    else:
        print("Invalid Input")
elif amt>=101 and amt<=200:
    if cloth=='s':
        bill=amt*0.95
    elif cloth=='p':
        bill=amt*0.92
    elif cloth=='t':
        bill=amt*0.9
    else:
        print("Invalid Input")
elif amt>=201 and amt<=300:
    if cloth=='s':
        bill=amt*0.9
    elif cloth=='p':
        bill=amt*0.88
    elif cloth=='t':
        bill=amt*0.85
    else:
        print("Invalid Input")
elif amt>300:
    if cloth=='s':
        bill=amt*0.82
    elif cloth=='p':
        bill=amt*0.8
    elif cloth=='t':
        bill=amt*0.78
    else:
        bill="Invalid Input"

print(bill)