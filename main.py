

import random
print("Welcome to Royal Bank Of India")
data={}
list1=["Name","Address","Gender","Contact","Govt_Id Type","Govt_Id Number","Account Type","Amount"]

while True:
    list2=[]
    ch = int(input("1.New Customer\n2.Existing Customer\n3.Exit\nENTER CHOICE:"))

    if ch==1:
        for item in list1:
            list2.append(input("Enter %s:"%item))

        acc_no=random.randrange(1000000,9999999998)
        data[acc_no] = dict(zip(list1,list2))
        print("Your Account Number is:",acc_no)
        print("Account Created")
        print("******************************************")
    elif ch==2:
        acc_no=int(input("Enter your account number:"))
        if acc_no not in data:
            print('No Record Found!!!!')
        else:
            if data[acc_no]["Gender"]=="M":
                print("WELCOME Mr",data[acc_no]["Name"])
            else:
                print("WELCOME Miss",data[acc_no]["Name"])
            ch1=int(input("1.Check Balance\n2.Withdraw\n3.Deposit\n4.Exit\nEnter Choice:"))
            if ch1 == 1:
                print("Available Balance:", data[acc_no]["Amount"])
                print("******************************************")
            elif ch1 == 2:
                amt = int(input("Enter amount to withdraw:"))
                Avl = int(data[acc_no]["Amount"])
                if amt > Avl:
                    print("Insufficient Balance")
                else:
                    Avl = Avl - amt
                    data[acc_no]["Amount"] = Avl
                    print("Please Collect Cash")
                    print("Your Account Balance:", Avl)
                    print("******************************************")
            elif ch1 == 3:
                amt = int(input("Enter amount to deposit:"))
                Avl = int(data[acc_no]["Amount"])
                Avl = Avl + amt
                print("Sucessfully Deposited Amount")
                print("Your Account Balance:", Avl)
                print("******************************************")
            elif ch1 == 4:
                print("You have sucessfully logged out")
                print("Thank you for Banking with us")
            else:
                print("Invalid Choice")


    elif ch==3:
        pass
    else:
        print("Invalid Choice")



