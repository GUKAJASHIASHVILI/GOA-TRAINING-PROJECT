import random


#Telling user to type a number
user_number = input("Type a number: ")

if user_number.isdigit():
    user_number = int(user_number)
    if user_number <= 0:
        print("Please type greater number than 0 next time")
        quit()
else:
    print("Please type a number next time")
    quit()        
        

#generating random random
random_number = random.randint(0, user_number) 
guesses = 0

while True:
    guesses = guesses + 1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please type a number next time")
        continue

    if user_guess == random_number:
        print("You got it!")
        break
    elif user_guess > random_number:
        print("You were above the number!")
    else:
        print("You were below the number!")    


print(f"It took you {guesses} tries")