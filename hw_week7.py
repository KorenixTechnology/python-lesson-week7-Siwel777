import random

def hw_week7(secret_number):
    i = 0   #count
    while True :
        i = i + 1   #counter
        print('Take a guess.')
        guess = int(input())
        if guess == secret_number:
            print('Good job! You guessed my number in ' + str(i) + ' guesses!')
            break
        elif guess > secret_number:
            print('Your guess is too high.')
        elif guess < secret_number:
            print('Your guess is too low.')
            


if __name__ == '__main__':
    hw_week7(random.randint(1, 100))
