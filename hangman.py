from random import randint


def displayIntro():
    print(r"""_______________________________________________
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                       
_______________________________________________

_____________________Rules_____________________
Try to guess the hidden word one letter at a   
time. The number of dashes are equivalent to   
the number of letters in the word. If a player 
suggests a letter that occurs in the word,     
blank places containing this character will be 
filled with that letter. If the word does not  
contain the suggested letter, one new element  
of a hangman’s gallow is painted. As the game  
progresses, a segment of a victim is added for 
every suggested letter not in the word. Goal is
to guess the word before the man hangs!        
_______________________________________________

     ._______.   
     |/          
     |           
     |           
     |           
     |           
     |           
 ____|___     
""")
    return 1


def displayEnd(result):
    if result[1]:
        print(f"Hidden word was: {result[0]}")
        print(
            """
________________________________________________________________________
          _                                  _                          
         (_)                                (_)                         
__      ___ _ __  _ __   ___ _ __  __      ___ _ __  _ __   ___ _ __    
\ \ /\ / / | '_ \| '_ \ / _ \ '__| \ \ /\ / / | '_ \| '_ \ / _ \ '__|   
 \ V  V /| | | | | | | |  __/ |     \ V  V /| | | | | | | |  __/ |      
  \_/\_/ |_|_| |_|_| |_|\___|_|      \_/\_/ |_|_| |_|_| |_|\___|_|      
           | |   (_)    | |                  | (_)                      
        ___| |__  _  ___| | _____ _ __     __| |_ _ __  _ __   ___ _ __ 
       / __| '_ \| |/ __| |/ / _ \ '_ \   / _` | | '_ \| '_ \ / _ \ '__|
      | (__| | | | | (__|   <  __/ | | | | (_| | | | | | | | |  __/ |   
       \___|_| |_|_|\___|_|\_\___|_| |_|  \__,_|_|_| |_|_| |_|\___|_|   
________________________________________________________________________
""")
    else:
        print(f"Hidden word was: {result[0]}")
        print(
            """
       __     __           _           _   _                                    
 \ \   / /          | |         | | | |                                   
  \ \_/ /__  _   _  | | ___  ___| |_| |                                   
   \   / _ \| | | | | |/ _ \/ __| __| |                                   
    | | (_) | |_| | | | (_) \__ \ |_|_|                                   
    |_|\___/ \__,_| |_|\___/|___/\__(_)                                   
        _______ _                                        _ _          _ _ 
       |__   __| |                                      | (_)        | | |
          | |  | |__   ___   _ __ ___   __ _ _ __     __| |_  ___  __| | |
          | |  | '_ \ / _ \ | '_ ` _ \ / _` | '_ \   / _` | |/ _ \/ _` | |
          | |  | | | |  __/ | | | | | | (_| | | | | | (_| | |  __/ (_| |_|
          |_|  |_| |_|\___| |_| |_| |_|\__,_|_| |_|  \__,_|_|\___|\__,_(_)
__________________________________________________________________________  
""")


def displayHangman(state):
    states = {
        5:
            """              
     ._______.   
     |/          
     |           
     |           
     |           
     |           
     |           
 ____|___   
        """,
        4:
            """        
     ._______.   
     |/      |   
     |           
     |           
     |           
     |           
     |           
 ____|___""",
        3:
            """        
     ._______.   
     |/      |   
     |      (_)  
     |           
     |           
     |           
     |           
 ____|___""",
        2:
            """          
     ._______.   
     |/      |   
     |      (_)  
     |       |   
     |       |   
     |           
     |           
 ____|___""",
        1:
            """                         
     ._______.   
     |/      |   
     |      (_)  
     |      \|/  
     |       |   
     |           
     |           
 ____|___""",
        0:
            """         
     ._______.   
     |/      |   
     |      (_)  
     |      \|/  
     |       |   
     |      / \  
     |           
 ____|___"""
    }
    return states[state]


def playAgainPrompt():
    ask = str(input("Do you want to play again? (yes/no)\n"))

    if ask == "yes":
        hangman()
    else:
        return False


def getWord():
    ourWords = open("hangman-words.txt", "r")
    wordsArr = ourWords.readlines()
    ourWords.close()
    wordsArr = list(map(lambda w: w.strip('\n'), wordsArr))
    randomWord = wordsArr[randint(0, len(wordsArr) - 1)]
    randWord = randomWord
    return randWord


def valid(c):
    if len(c) != 1 or not c.islower() or c.isdigit() or not c.isalpha():
        return False
    else:
        return True


def validCinWord(c, word):
    for i in range(0, len(word)):
        if word[i] == c:
            return True

    return False


def play():
    lives = 5
    hiddenWord = []
    randomWord = list(getWord())
    for i in range(0, len(randomWord)):
        hiddenWord.append("*")
    hiddenWordFinal = "".join(str(i) for i in hiddenWord)

    while lives >= 0:
        guessTheWord = f"Guess the word: {hiddenWordFinal}"
        print(guessTheWord)
        enterALetter = str(input("Enter a letter:\n> "))
        while not valid(enterALetter):
            enterALetter = str(input("Enter a letter:\n> "))

        isItValid = validCinWord(enterALetter, randomWord)
        if isItValid:
            for i in range(0, len(randomWord)):
                if randomWord[i] == enterALetter:
                    hiddenWord[i] = enterALetter
            hiddenWordFinal = "".join(str(i) for i in hiddenWord)
            countKnownOnes = 0
            for i in range(0, len(hiddenWordFinal)):
                if hiddenWordFinal[i] != "*":
                    countKnownOnes += 1
            print(displayHangman(lives))
            if countKnownOnes == len(randomWord):
                thatWord = "".join(randomWord)
                twoElem = [thatWord, True]
                return twoElem
        else:
            lives -= 1
            print(displayHangman(lives))
            if lives == 0:
                thatWord = "".join(randomWord)
                twoElem = [thatWord, False]
                return twoElem


def hangman():
    while True:
        displayIntro()
        result = play()
        if result[1]:
            resultToEndWith = [result[0], True]
            displayEnd(resultToEndWith)
            again = playAgainPrompt()
            if not again:
                break
        else:
            resultToEndWith = [result[0], False]
            displayEnd(resultToEndWith)
            again = playAgainPrompt()
            if not again:
                break


if __name__ == "__main__":
    hangman()
