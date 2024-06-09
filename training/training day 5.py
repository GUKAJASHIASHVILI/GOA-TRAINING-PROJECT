#lets go into a bank

print("Hello welcome to V.I.P Bank\n")

name = input("What is your name: ")

print(f"Hello {name} lets create your account first.\n")

account_username = input("Enter your account name here: ")

account_password = input("Type your password here, for an account: ")

print("Well done your account is created!\n")

print("Now which service whould you like? " "1 ""or ""2?")

service = input("1.transfer money\n2.loan\n")


# 1. transfering money
if service == "1":
    print("Okay so you need to transfer your money.")

    password_confirmation  = input("To transfer your money enter your account password: ")

    if password_confirmation == account_password:

        print("Successfully register\n")

        personal_number = input("Enter the person's personal number to transfer money to him: ")

        amount_of_money = int(input("Specify how much you want to transfer: "))

        print("Transfering.....\n")

        import time

        time.sleep(5)  # Pause for 5 seconds

        commission = 1

        commission_money = amount_of_money * 1 /100

        transfered_money = amount_of_money - commission_money

        print(f"Transferd {transfered_money}$\ncommision is 1%\n")
    
        print("Thanks for using our V.I.P Bank")
        exit()

    else:
        print("It seems that you are not the owner of this account")
        exit()


    

# 2.loan
if service == "2":
    print("Okay so you need a loan.")

    password_confirmation  = input("To ger your loan enter your account password: ")

    if password_confirmation == account_password:

        print("Successfully register\n")

        amount_of_money = int(input("How much loan do you want?: "))
    
        notice_of_work = input("okay, do you have work first?: ")
        if notice_of_work == "No":
            print("Oh sorry, you can't get a loan because you don't have a job")
            exit()
        if notice_of_work == "Yes":
            income = int(input("How much do you earn per month?\n"))
            if income < amount_of_money/24:

               print("You will not be able to make a loan because of your income is very low for that money.")
               exit()

            else:
                print("Very good, you will be able to take out a loan\n")

                print("Transfering......\n")

                import time

                time.sleep(5)  # Pause for 5 seconds


                amount_to_be_paid_every_month = amount_of_money/24 * 3 / 100 + amount_of_money/6

                print(f"Okay your {amount_of_money}$ is on your credit card sir.")
                print(f"You need to pay {amount_to_be_paid_every_month}$ every month")