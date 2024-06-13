#welcome to my mini python quiz

print("Hello welcome to my python quiz!")

#asks user if he wants to play

playing = input("Do you want to play? \n")
score = 0


if playing.lower() != "yes":
    quit()


#first question
print("Okay thats good, lets play!")

answer1 = input('What is this case called? "first_name"?\n')

if answer1.lower() == "snake_case":
    print("Correct!")
    score = score +1
else:
    print("Incorrect!")



#second question
answer2 = input('What symbol is used to write a comment in Python?\n')

if answer2.lower() == "#":
    print("Correct!")
    score = score +1
else:
    print("Incorrect!")


#third question
answer1 = input("Is Python a case-sensitive language?\n")

if answer1.lower() == "yes":
    print("Correct!")
    score = score +1
else:
    print("Incorrect!")    


#fourth question
answer1 = input("Write down the shortened versions of these words 1.string 2.integer 3.boolean 4.float\n")

if answer1.lower() == "1.str 2.int 3.bool 4.float":
    print("Correct!")
    score = score +1
else:
    print("Incorrect!")


#third question

print("Okay this is a bonus question!")

answer1 = input("What is missing from this code? print(Hello world)?\n")

if answer1.lower() == "quotation marks":
    print("Correct!")
    score = score +1
else:
    print("Incorrect!")  

print(f"Congrats! you got {score} questions right!")
print(f"Congrats! you got {score / 5 * 100}%!")