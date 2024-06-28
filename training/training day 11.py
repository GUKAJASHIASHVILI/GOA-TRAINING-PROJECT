print("Hello Welcome to my adventure game!")

name = str(input("What is your name? "))

answer =input("You are in forest and come to an end and you can go left or right. Which way do u go?\n")

if answer == "right":

    answer = input("You came to a river and bridge is destroyed, you can swim or walk around it. Which one whould you choose?\n")
    
    if answer == "swim":
        print("You drowned. You lose!\n")
        
    elif answer == "walk around it":

        answer = input("You are lost. Now choose call 911 or try to find the way\n")

        if answer == "call 911":
            print("They found you!.Congrats You win!\n")
        
        elif answer == "try to find the way":

            answer = input("You came to a bear. chose run or act like ur dead.\n")

            if answer == "run":
                print("Bear catches you and kills you. You lose!\n")

            elif answer == "act likee ur dead":
                print("Bear thought you were dead so it walked away. Congrats you won!\n")

            else:
                print("Not a valid option.\n")

        else:
            print("Not a valid option.\n")

    else:
        print("Not a valid option.\n")

elif answer =="left":

    answer = input("You came to a bear. chose run or act like ur dead.\n")

    if answer == "run":
        print("Bear catches you and kills you. You lose!\n")

    elif answer == "act like ur dead":
        print("Bear thought you were dead so it walked away. Congrats you won!\n")

    else:
        print("Not a valid option.\n")

else:
    print("Not a valid option.\n")
