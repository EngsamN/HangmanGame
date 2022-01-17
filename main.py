##this import for random model to use random function to select random word from word list
import  random
# import colorama
class myhangGame:
    wrongLetters = ''
    correctLetters = ''
    hangManShape = ['''
             +---+
             |   |
                 |
                 |
                 |
                 |
            =========''', '''

            +---+
            |   |
            O   |
                |
                |
                |
           =========''', '''

            +---+
            |   |
            O   |
            |   |
                |
                |
          =========''', '''

           +---+
           |   |
           O   |
          /|   |
               |
               |
         =========''', '''
          +---+
          |   | 
          O   |
         /|\  |
              |
              |
        =========''', '''
          +---+
          |   |
          O   |
         /|\  |
         /    |
              |
        =========''', ''' 
         +---+
         |   |
         O   |
        /|\  |
        / \  |
             |
        =========''']
    words = "ant samaih badger samaih samaih beaver camel cat clam cobra cougar " \
            "coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk lion \
    lizard llama mole monkey moose mouse mule newt otter owl panda parrot pigeon \
    samaih \
    spider stork swan tiger toad trout turkey turtle weasel whale wolf wombat \
    zebra".split()


    def getRandomWord(self,wordlist):
        ##this line to  store a random index for this list in the wordIndex variable
        wordIndex = random.randint(0, len(wordlist) - 1)
        return wordlist[wordIndex]

        ''' this function ask player to guss letter and check if he enter one letter or not '''

    def gussletter(self,alreadyGuessed):
        while True:
            gussLetter = input("Gusee a letter:")
            gussLetter = gussLetter.lower()
            if len(gussLetter) != 1:
                print("you must enter only one letter")
            elif (gussLetter in alreadyGuessed):
                print("this letter gussed please enter another")
            elif (gussLetter not in "abcdefghijklmnopqrstuvwxyz"):
                print('Please enter only engilsh  letter')
            else:
                return gussLetter

        '''this function to show the shape of hangman and when player guss error letter
              the head is appeare and in the first will be blank also show the correct letters which player guss it'''

    def showManStatus(self,hangShap, wrongLetter, correctLetter, secrtWord):
        print("\033[2;91m {} \033[00m".format( hangShap[len(wrongLetter)]))

        print("\033[1;33m Wrong letters:", end=' ')
        for letter in wrongLetter:
            print(letter, end=' ')
        print()

        blanks = '_' * len(secrtWord)
        # replace blanks with correctly guessed letters
        # samiah
        for i in range(len(secrtWord)):
            if secrtWord[i] in correctLetter:
                blanks = blanks[:i] + secrtWord[i] + blanks[i + 1:]
            # show the secret word with spaces  between  letters
        for letter in blanks:
            print(letter, end=' ')
        print()

        '''this function to ask play if he want to play again if yes return true else false '''

    def playAgain(self):
        print('Do you want to play again? (yes or no)')
        return input().lower().startswith('y')

    def gameloop(self,hangManShape,wrongLetters,correctLetters,secretWord):
        while True:
            gameIsDone,foundAllLetters=False,False
            self.showManStatus(hangManShape, wrongLetters, correctLetters, secretWord)
            # Let the player type in a letter.
            guess = self.gussletter(wrongLetters + correctLetters)
            print("guss number")
            if guess in secretWord:
                correctLetters = correctLetters + guess
                if (len(correctLetters) == len(secretWord)):
                    foundAllLetters = True
                # Check if the player has won
                for i in range(len(secretWord)):
                    if secretWord[i] not in correctLetters:
                        foundAllLetters = False
                        break
            if foundAllLetters:
                print('Yes! The secret word is "' + secretWord + '"! You have won!')
                gameIsDone = True
            else:
                wrongLetters = wrongLetters + guess
                if len(wrongLetters) == len(hangManShape) - 1:
                    self.showManStatus(hangManShape, wrongLetters, correctLetters, secretWord)
                    print(
                        'You have run out of guesses!\nAfter ' + str(len(wrongLetters)) + ' missed guesses and ' + str(
                            len(correctLetters)) + 'correct guesses, the word was "' + secretWord + '"')
                    gameIsDone = True

            # Ask the player if they want to play again (but only if the game is done).
            if gameIsDone:
                if self.playAgain():
                    wrongLetters = ''
                    correctLetters = ''
                    gameIsDone = False
                    ecretWord =self.getRandomWord(self.words)
                else:
                    break
        else:
            print("error")

## call and excute the first time
print("\033[1;35m ـــــــــــH A N G M A Nـــــــــــ\n", end=' ')
instruction=input('enter h  to know how play it Or s to start fun:')
if(instruction=="h"):
    pass
elif(instruction=="s"):
    calclass=myhangGame()
    secrtword=calclass.getRandomWord(calclass.words)
    gameIsDone = False
    calclass.gameloop(calclass.hangManShape,calclass.wrongLetters,calclass.correctLetters,secrtword)


