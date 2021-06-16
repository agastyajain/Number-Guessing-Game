import random
print('Welcome To The Number Guessing Game !!!')
number = random.randint(1,9)
chances = 0
print('Guess a number between 1 and 9 ...')

while chances < 5:
    guess = int(input('Enter your guess: '))
    if guess == number:  
        print('Congrats! You Won')
        break
    elif guess < number:
        print('Your guess is too low. Guess a number higher than ', guess)
    else:
        print('Your guess was too high. Guess a number lower than ', guess)
    chances = chances + 1

if not chances < 5:
    print('YOU LOSE !!! And the number was ', number)
