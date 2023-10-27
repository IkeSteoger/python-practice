import random
import logging

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - ' '%(levelname)s - %(message)s')

logging.debug('Start of program')
guess = ''

logging.debug('Guess coin')
while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()

logging.debug('The coin is tossed') 
toss = random.randint(0, 1) # 0 is tails, 1 is heads

logging.debug('Convert randint into heads/tails')
if toss == 0:
    toss = 'tails'
if toss == 1:
    toss = 'heads'

logging.debug('Does ' + str(toss) + ' equal ' + str(guess) + '?')

if toss == guess:
    print('You got it!')
else:
    print('Nope! Guess again!')
    guess = input()
    if toss == guess:
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')