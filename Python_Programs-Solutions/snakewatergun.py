import random
lst=['s','w','g']
chance=10
no_of_chance =0
computer_point=0
human_point=0

print("-------\t\t\t\t Snake, Water, Gun Game---------\n\n")
print("s for Snake\nw for Water\ng for Gun \n")

#making the game in while
while no_of_chance < chance:
    option= input("Snake, Water, Gun :")
    rnum=random.choice(lst)

    if option== rnum:
        print("Tie Both 0 point to each \n")
    elif option == "s" and rnum== "g":
        computer_point = computer_point + 1
        print(f"your guess {option} and computer guess is {rnum}\n")
        print("Computer wins 1 point \n")
        print(f"computer point is {computer_point} and your point is {human_point}\n")

    elif option=="s" and rnum=="w":
        human_point=human_point + 1
        print(f"your guess {option} and computer guess is {rnum}\n")
        print("Human wins 1 point \n")
        print(f"computer point is {computer_point} and your point is {human_point}\n")

    elif option == "w" and rnum == "s":
        computer_point = computer_point + 1
        print(f"your guess {option} and computer guess is {rnum}\n")
        print("Computer wins 1 point \n")
        print(f"computer point is {computer_point} and your point is {human_point}\n")

    elif option == "w" and rnum == "g":
        human_point = human_point + 1
        print(f"your guess {option} and computer guess is {rnum}\n")
        print("Human wins 1 point \n")
        print(f"computer point is {computer_point} and your point is {human_point}\n")

    elif option == "g" and rnum == "s":
        human_point = human_point + 1
        print(f"your guess {option} and computer guess is {rnum}\n")
        print("Human wins 1 point \n")
        print(f"computer point is {computer_point} and your point is {human_point}\n")

    elif option == "g" and rnum == "w":
        computer_point = computer_point + 1
        print(f"your guess {option} and computer guess is {rnum}\n")
        print("Computer wins 1 point \n")
        print(f"computer point is {computer_point} and your point is {human_point}\n")

    else:
        print("You have input wrong\n")
    no_of_chance=no_of_chance+1
    print(f"{chance-no_of_chance} is left out of {chance}\n")
print("GAME OVER")

if computer_point == human_point:
    print("Its a Tie")
elif computer_point > human_point:
    print("Computer Wins and You Loose !!")
else:
    print("You Win and Computer loose!!")

print(f"Your Point is {human_point} and Computer Point is {computer_point}")

