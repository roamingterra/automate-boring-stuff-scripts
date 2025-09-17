import random, logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s -  %(levelname)s -  %(message)s')
logging.disable(logging.CRITICAL)

logging.debug('Start of program')                    

guess = ''
while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()
    
toss = random.randint(0, 1)  # 0 is tails, 1 is heads

if guess == 'tails':
    guess = 0
elif guess == 'heads':
    guess = 1

logging.debug('The variable type of toss is ' + str(type(toss)))
logging.debug('The variable type of guess is ' + str(type(guess)))
assert type(toss) == type(guess)

logging.debug('The value of toss is ' + str(toss))
logging.debug('The value of guess is ' + str(guess))

if toss == guess:
    print('You got it!')
else:
    print('Nope! Guess again!')
    guess = input()

    if guess == 'tails':
        guess = 0
    elif guess == 'heads':
        guess = 1

    logging.debug('The variable type of toss is ' + str(type(toss)))
    logging.debug('The variable type of guess is ' + str(type(guess)))
    assert type(toss) == type(guess)

    logging.debug('The value of toss is ' + str(toss))
    logging.debug('The value of guess is ' + str(guess))
    
    if toss == guess:
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')

logging.debug('End of program')
