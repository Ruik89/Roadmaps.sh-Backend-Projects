import random
#to add or remove difficultys then remove or add to the below list. everything else will auto correct 
difficulty = [[7,"easy"],[5,"medium"],[3,"hard"]]


def gameSetup():
    print("Welcome to the Number Guessing Game!\nPlease select the difficulty level:")
    counter = 1
    for difficuly in difficulty:
        print(f"{counter}. {difficuly[1]} ({difficuly[0]} chances)")
        counter += 1
    userChoice = int(input())

    while userChoice > len(difficulty):
        print(f"please choose a number bettween 1 and {len(difficulty)}")
        userChoice = int(input())

    print(f"""Great! You have selected the {difficulty[userChoice - 1][1]} difficulty level.
    Let's start the game!""")
    chances = difficulty[userChoice - 1][0]
    randomNumber = random.randint(0,100)
    print(randomNumber)
    tries = 0
    return chances,randomNumber,tries
    
def guessingGeme(tries,randomNumber,chances):
    continueGame = True
    while tries < chances and continueGame == True:
        tries += 1
        print("Enter your guess: ")
        numberGuessed = int(input())
        if numberGuessed == randomNumber:
            print(f"Congratulations! You guessed the correct number in {tries} attempts.")
            continueGame = contineGame()
        elif numberGuessed > randomNumber:
            print(f"Incorrect! The number is less than {numberGuessed}.")
        else:
           print(f"Incorrect! The number is greater than {numberGuessed}.")

        if tries == chances:
            print(f"Game Over! The correct number was {randomNumber}")
            contineGame() 

def contineGame():
    print("\nwould you like to play again (y or n)")
    userChoise = input().lower()
    if userChoise[0] != "y":
        continueGame = False
        return continueGame
    else:
        chances, randomNumber, tires = gameSetup()
        guessingGeme(tires,randomNumber,chances)

        
chances, randomNumber, tires = gameSetup()
guessingGeme(tires,randomNumber,chances)
