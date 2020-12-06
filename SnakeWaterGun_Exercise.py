# Snake water gun
# Create a snake water gun game in Python!
# Search Snake water gun game in google if you need help on rules and how to play the game!
import random
ListA = ["Snake", "Water", "Gun"]
#print(computerchoice)
computerpoint = 0
yourpoint = 0
i = 1
while i<=10:
    i+=1
    computerchoice = random.choice(ListA)
    UserChoice = input("Enter Choices 1)Snake or 2)Water or 3)Gun : ")
    if UserChoice == "Snake":
        if computerchoice == "Snake":
            computerpoint = computerpoint + 1
            yourpoint = yourpoint + 1
            print("Match Draw Between Computer and You.Computer Point is:"+str(computerpoint)+"Your Point is"+str(yourpoint))
            continue
        elif computerchoice == "Water":
            yourpoint = yourpoint+1
            print("You won this match because snake will drink all the water. Your Points are :"+str(yourpoint))
            continue
        elif computerchoice == "Gun":
            computerpoint = computerpoint+1
            print("Computer won this match because gun will shoot the snake. Computer Points are :" + str(computerpoint))
            continue

    elif UserChoice == "Water":
        if computerchoice == "Water":
            computerpoint = computerpoint + 1
            yourpoint = yourpoint + 1
            print("Match Draw Between Computer and You.Computer Point is:"+str(computerpoint)+"Your Point is"+str(yourpoint))
            continue
        elif computerchoice == "Gun":
            yourpoint = yourpoint+1
            print("You won this match because gun will get drowned in water. Your Points are :"+str(yourpoint))
            continue
        elif computerchoice == "Snake":
            computerpoint = computerpoint+1
            print("Computer won this match because snake will drink all the water. Computer Points are :" + str(computerpoint))
            continue

    elif UserChoice == "Gun":
        if computerchoice == "Gun":
            computerpoint = computerpoint + 1
            yourpoint = yourpoint + 1
            print("Match Draw Between Computer and You.Computer Point is:"+str(computerpoint)+"Your Point is"+str(yourpoint))
            continue
        elif computerchoice == "Snake":
            yourpoint = yourpoint+1
            print("You won this match because gun will shoot the snake. Your Points are :"+str(yourpoint))
            continue
        elif computerchoice == "Water":
            computerpoint = computerpoint+1
            print("Computer won this match because gun will get drowned in the water. Computer Points are :" + str(computerpoint))
            continue






