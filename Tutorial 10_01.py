class Account():
  def __init__(self,number,balance):
    self.number=number
    self.balance=balance
  def withdraw(self, amount):
    if amount>self.balance: 
      print("Not enough balance") 
      return
    self.balance=self.balance-amount 
    print("Transaction sucessful") 
    print("Final Balance :", self.balance)
  def deposit(self, amount): 
    self.balance=self.balance+amount 
    print("Transaction sucessful") 
    print("Final Balance :", self.balance)
class Customer(Account):
  def __init__(self,number,balance,name,address,dob):
    super().__init__(number,balance) 
    self.name=name 
    self.address=address 
    self.dob=dob
  def display(self): 
    n=int(input("1.Withdraw 2.Deposit: ")) 
    if n==1:
      amt=int(input("Enter amount: "))
      self.withdraw(amt) 
    else:
      amt=int(input("Enter amount: "))
      self.deposit(amt) 
c1=Customer(58,4100,"Siddhant","Mumbai","2003") 
c1.display()
