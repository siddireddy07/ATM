pin = int(input("Enter you pin:")) #pin -- 2222
balance = 902345
c_number=8142724313
if pin ==2222:
    print("welcome to python bank")
    print("1.Balance enquiry ")
    print("2.withdraw")
    print("3.deposit")
    print("4.update ur contact number")
    print("5.update ur pin number")
    print("6.help")
    option = int(input("enter the option:"))
    if option==1:
        print("your balance is:",balance,"rs/-")
    elif option==2:
        w_amount = int(input("enter withdraw amount:"))
        if w_amount<=balance:
            balance = balance-w_amount
            print("your updated balance is:",balance)
        else:
            print("Insufficient balance")
    elif option==3:
        d_amount = int(input("enter dp amount:"))
        print("your previous balance is:",balance)
        balance = balance+d_amount
        print("your updated balance is:",balance)
    elif option==4:
        if c_number==8142724313:
            print("your present number is:",c_number)
            c_number=str(c_number)
            n_number=str(int(input("enter ur mobile number:")))
            c_number= c_number.replace("8142724313",n_number)
            c_number=int(c_number)
            print("your updated mobile number is:",c_number)
    elif option==5:
        o_pin=int(input("enter your previous pin:"))
        if o_pin == pin:
            print("your previous pin number is:",pin)
            pin=str(pin)
            n_pin=str(int(input("enter ur new pin number:")))
            pin=pin.replace(pin,n_pin)
            pin=int(pin)
            print("your updated pin number is:",pin)
    elif option==6:
            print("contact us at python city")        
    else:
         print("invalid option")

else:
    print("invalid pin")
