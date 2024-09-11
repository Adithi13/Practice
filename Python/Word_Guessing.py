import random

# here i will define a set a words
words = ['dog','cat','book','mouse','claw','pen','water','pouch','keyboard','paper','pencil','mobile','watch','charger','headphones']

# out of the pre-defined word computer will randomly choose one
word = random.choice(words)

print("Guess the letters of the words that i have picked")
print("You have 7 chance to guess")

guess = '' #this is defined like this because guess is character

chance = 7

# here i will use a while loop to keep asking the user for input until the user guesses the letters within 7 chance
while chance > 0:
    count = 0
    for char in word:
        if char in guess:
            print(char,end=" ")
        else:
            print("_")
            count += 1
    
    if count == 0:
        print(" Congratsss!!! You have guessed the word")
        print("The completer word is:",word)
        break

    print()
    guesss = input("Guess a letter: ").lower()

    guess += guesss

    if guesss not in word:
        chance -= 1
        print("Oops! The letter is not in the word")
        print("You have",chance,"chance left")

        if chance == 0:
            print("Game Over! The word was:",word)
        

 