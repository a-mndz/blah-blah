age=int(input("Enter your age: "))
if age<0:
    print("Invalid age entered. Age cannot be negative.")
else:
    balance=age-18
    balance1=abs(balance)
    if age>=18:
        print("You are eligible for a voting.")
    else:
        print("You are not eligible for a voting yet, atleast try again after ",balance1," years.")
