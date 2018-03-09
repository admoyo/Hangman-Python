def instructions():
    print("Guess the word before the hangman is hung!")
    back = input ("Enter any key to return to the menu")
    main()

def game():
    wordActual = input ("Enter word: ")
    wordHidden = ["_"] * len(wordActual)
    playerGuess = ""
    guesses = 10
    letterCounter = 0
    correctGuess = 0
    win = False

    while guesses != 0 and win == False:
        print (wordHidden)
        playerGuess = input("Guess a letter: ")
        print (letterCounter)
        
        letterCounter = 0
        
        while letterCounter < len(wordActual):
            if wordActual[letterCounter] == playerGuess:
                wordHidden[letterCounter] = playerGuess
                correctGuess += 1

            else:
                guesses -= 1

            letterCounter += 1

        if correctGuess == len(wordActual):
            win = True



    if guesses == 0:
        print ("Game over, you lose!")

    else:
        print ("You win!", correctGuess, "tries.")
   

    
    
def main():
    print ("------------------------------------")
    print ("Welcome to hangman \n Please select:")
    print ("1 - Play Game")
    print ("2 - Instructions")
    print ("3 - Quit")
    print ("------------------------------------")

    tryAgain = True
    while tryAgain == True:
        userSelect = input ("Enter 1, 2 or 3.")

        if userSelect == "1":
            tryAgain = False
            game()

        elif userSelect == "2":
            tryAgain = False
            instructions()

        elif userSelect == "3":
            tryAgain = False
            prompt = input("Are you sure you want to quit? (y/n)")
            if prompt == "y":                
                print ("------------------------------------")
                print ("Thanks for playing!")
                print ("------------------------------------")
            else:
                main()
                
main()
