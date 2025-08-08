# python-bank-account-
from pathlib import Path
def fileopen():
    file_path= Path("accountdetails.txt")
    with open (file_path,"r") as f:
        a=f.read()
        return a

def changes(y):
    file_path= Path("accountdetails.txt")
    with open (file_path,"w") as f:
        p=str(y)
        f.write(p)

def deposit():
    amount=int(input("Enter the amount to be deposit:"))
    m=int(fileopen())
    v=m+amount
    changes(v)
    print("Amount deposited in the account successfully!!!")

def withdrawl():
    withdrawl_amount=int(input("Enter the withdrawl amount:"))
    m=int(fileopen())
    if withdrawl_amount>m :
        print("Insufficient balance!!!")
    else:
        v=m-withdrawl_amount
        changes(v)
        print("Amount withdrawl successful!!!")

def check_balance():
    file_path= Path("accountdetails.txt")
    with open (file_path,"r") as f:
        a=int(f.read())
        print(f"The balnce in your account is ${a}. ")

while True:
    print('''    MENU   
          0: Exit  
          1: Deposit Amount
          2: Amount Withdrawl
          3: Check Balance
          ''')
    ch=int(input("Enter your request:"))
    if ch==0:
        break
    elif ch==1:
        deposit()
    elif ch==2:
        withdrawl()
    elif ch==3:
        check_balance()
    else:
        print("Please enter a valid request!!!")
