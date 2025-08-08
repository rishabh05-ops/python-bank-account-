def add():
    a=int(input("Enter how many numbers you want to add:"))
    b=0
    for i in range(a):
        x=int(input("Enter the number:"))
        b+=x
    print(f"The sum of the numbers is {b}.")

def multiplication():
    a=int(input("Enter how many numbers you want to multiply:"))
    b=1
    for i in range(a):
        x=int(input("Enter the number:"))
        b*=x
    print(f"The product of the numbers is {b}.")

def division():
    a=int(input("Enter the dividend:"))
    b=int(input("Enter the divisor:"))
    c=a/b
    print(f"The quotent of the numbers is {c}.")

def subtraction():
    a=int(input("Enter the First number:"))
    b=int(input("Enter the Second number:"))
    c=a-b
    print(f"The subtraction of the numbers is {c}.")

while True:
    print('''    MENU   
          0: Exit  
          1: Addition
          2: Subtraction
          3: Multiplication
          4: Division
          ''')
    ch=int(input("Enter your request:"))
    if ch==0:
        break
    elif ch==1:
        add()
    elif ch==2:
        subtraction()
    elif ch==3:
        multiplication()
    elif ch==4:
        division()
    else:
        print("Please enter a valid request!!!")

