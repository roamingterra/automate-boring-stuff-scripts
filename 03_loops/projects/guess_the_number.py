import random

def guessNumber():
    continueGuessing = True
    
    while continueGuessing: 
        print("Take a guess")

        number = input()

        try:
            return int(number)
        except ValueError:
            print("That is not a number")

# Ask user for name
print("Hello. What is your name?")

name = input()

# Ask user to guess number between two numbers
minNumber = 1
maxNumber = 20
maxNumOfGuesses = 6 # User has x number of tries
totalNumOfUserGuesses = 0
randomNumber = random.randint(minNumber, maxNumber) # Generate a random number between the min and max values, and store it in a variable

print(f"Well, {name}, I am thinking of a number betweem {minNumber} and {maxNumber}.")

for x in range(maxNumOfGuesses + 1):
    if(x == maxNumOfGuesses): # If user does not guess the number before x number of tries, the user loses
        print(f"Nope. The number I was thinking of was {randomNumber}")
        break

    totalNumOfUserGuesses += 1
    
    guess = guessNumber()

    if(guess == randomNumber): # If user guesses the number before x number of tries, the user wins
        print(f"Good job, {name}! You guessed my number in {totalNumOfUserGuesses} guesses!")
        break
    elif(guess > randomNumber): # If user's guess is too high, tell user it's too high
        print("Your guess is too high.")
    elif(guess < randomNumber): # If user's guess is too low, tell user it's too low
        print("Your guess is too low.")

    




    
    
    
    
    
    

