#Lets go into coffe shop

print("Hello, welcome to my coffe shop!")

name = input("What is your name?\n")

if name == "Mate" or name == "Dato":
 #lets see if he likes programming :D
 programmer_status = input("Are you programmer?\n")
 if programmer_status == "No" or programmer_status == "no" or programmer_status == "NO":
     love_for_programming = input("Do you love programming?\n")
     if love_for_programming == "No" or love_for_programming == "no" or love_for_programming == "NO":
        print("You are not allowed here! " + name + ", get out!!!!!!")
        exit()
     if love_for_programming == "Yes" or love_for_programming == "yes":
        print("Oh so you are one of good " + name + "'s sorry for that question come in!!")
 if programmer_status == "Yes" or programmer_status == "yes":
    hours_of_programming = int(input("How many hour have you been programming today?\n"))
    if hours_of_programming < 3:
       print("You are not allowed here! " + name + ", get out!!!!!!")    
       exit()     
else:
    print("Hello " + name + ", thank you for comming in today\n")

menu = "Black Coffe 5$\nEspresso 7$\nLatte 6$\nCappucino 8$\n\n"

order = input(name + ", what whould you like from our menu today? Here is what we are serving.\n\n" + menu)

if order == "Black Coffe":
    price = 5
elif order == "Espresso":
  price = 7
elif order == "Latte":
   price = 6
elif order == "Cappucino":
  price = 8
else:
   print("Sorry we dont have "  + order + " here.")
   exit()

if order == "Latte":
   whipped_cream_status = input("Do you want whipped cream?\n")
   if whipped_cream_status == "Yes":
      print("Ok, but just so you know the price has gone up by $2")
      price = 8
   else:
      price = 6

quantity = input("How many " + order + "'s would you like?\n")

total = price * int(quantity)

print("Thank you. Your total is $" + str(total))

print("We will have your " + quantity + " " + order + " ready in a moment.")
 
