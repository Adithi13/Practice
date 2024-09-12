import random

print("Rules of the game are as follows:\n")
print("Rock vs Paper -> Paper wins \n")
print("Rock vs Scissors -> Rock wins \n")
print("Paper vs Scissors -> Scissors wins \n")

# Start the game loop
while True:
    print("Enter your choice\n 1] Rock\n 2] Paper\n 3] Scissors\n ")
    
    # Ask for user input
    user_choice = input("Enter your choice (1/2/3): ")

    # Ensure valid input by checking if it's one of the accepted strings
    while user_choice not in ['1', '2', '3']:
        user_choice = input("Oops!\nEnter number between 1-3: ")

    # Convert the valid input string to an integer for comparisons
    user_choice = int(user_choice)
    
    # Assign the name to the user's choice
    if user_choice == 1:
        user_choice_name = "Rock"
    elif user_choice == 2:
        user_choice_name = "Paper"
    else:
        user_choice_name = "Scissors"
    
    # Display the user's choice
    print("Your choice is:", user_choice_name)

    print("It's the computer's turn...")

    # Computer makes a random choice
    computer_choice = random.randint(1, 3)

    # Assign the name to the computer's choice
    if computer_choice == 1:
        computer_choice_name = "Rock"
    elif computer_choice == 2:
        computer_choice_name = "Paper"
    else:
        computer_choice_name = "Scissors"
    
    # Display the computer's choice
    print("Computer's choice is:", computer_choice_name)
    
    # Determine the winner
    if user_choice == computer_choice:
        result = "DRAW"
    elif (user_choice == 1 and computer_choice == 2) or (user_choice == 2 and computer_choice == 1):
        result = 'Paper'
    elif (user_choice == 1 and computer_choice == 3) or (user_choice == 3 and computer_choice == 1):
        result = 'Rock'
    elif (user_choice == 2 and computer_choice == 3) or (user_choice == 3 and computer_choice == 2):
        result = 'Scissors'
    
    # Print the result
    if result == "DRAW":
        print("<== It's a tie! ==>")
    elif result == user_choice_name:
        print("<== You win! ==>")
    else:
        print("<== Computer wins! ==>")

    # Ask if the user wants to play again
    print("Do you want to play again? (Y/N)")
    ans = input().lower()
    if ans == 'n':
        break

# After exiting the loop, print thanks for playing
print("Thanks for playing!")
