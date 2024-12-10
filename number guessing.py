from random import randint

EASY = 10
HARD = 5


def decision(guess, answer):
    if guess > answer:
        print('You are too high')
    elif guess < answer:
        print('You are too low')
    else:
        print(f'You guessed correctly! The answer was {answer}')
        return True  # Return True when the guess is correct
    return False  # Return False if the guess is incorrect


def difficult():
    dif = input('Choose difficulty level: Type "easy" or "hard": ').lower()
    if dif == 'easy':
        return EASY
    else:
        return HARD


# Main program
print('WELCOME TO THE NUMBER GUESSING GAME')
print('I AM THINKING OF A NUMBER BETWEEN 1 AND 100...')
answer = randint(1, 100)
turns = difficult()

print(f'You have {turns} attempts to guess the number.')

while turns > 0:
    guess = int(input('Enter your guess: '))
    correct = decision(guess, answer)
    if correct:
        break
    turns -= 1
    if turns > 0:
        print(f'You have {turns} attempts remaining.')
    else:
        print("You've run out of guesses. You lose!")
