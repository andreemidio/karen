from random import randint


def guess_number ():

    guess_number = randint(1,100)

    print(guess_number)

    print( "Guess the number between 1 - 100 \n")

    guessed_number =  False
   
    while guessed_number is False:
        user_guesses = int(input(" Put your number to guess > "))

        if user_guesses > 100:
            print (" Please, guess a number between 1 - 100 \n")
            print (f" {user_guesses} is greater than 100 \n ")

        elif user_guesses <= guess_number:
            print ("Your guess is too high, try again \n")

        elif user_guesses >= guess_number:
            print (" Your guess is too low, try again \n")

        if user_guesses == guess_number:
            print ("Congratulations! You guessed the number!!")


            print (" Would you like to play again? \n")
            question = input(" Press Y (yes) or N (not)  >> ")

            if question.lower() == 'y':
                guess_number = randint(1,100)
                print(guess_number)
                continue
            
            else:
                matched = True
                break

if __name__ == '__main__':
    guess_number ()
   