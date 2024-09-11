import random
num = random.randint(1, 100)   #generate a random number
print("Guess the number in 5 chances")
chance = 5
count = 0

# count should never exceed the chance
while count < chance:
    count += 1
    guess = int(input("Guess the number (between 0 to 100): "))

    # if at all the number is == guessed number
    if num == guess:
        print(f'The number is {guess} and you found it right !! in the {count} attempt')
        break
    
    # if number of chances is exhausted and number is not guessed correctly
    elif count >= chance and guess != num:
        print(f"Sorry, you didn't guess the number {num}. You ran out of chances")
        break

    # if number is greater
    elif guess > num:
        print("Youre guess is high")

    # if number is smaller
    elif guess < num:
        print("Youre guess is low")