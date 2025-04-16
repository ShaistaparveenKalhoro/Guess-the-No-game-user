import random

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    
    print(f"\nThink of a number between 1 and {x}!")
    print("After each guess, tell me if it's too high (H), too low (L), or correct (C).")
    
    while feedback != 'C':
        # Make a guess using binary search approach
        guess = random.randint(low, high)
        
        # Get user feedback
        feedback = input(f"\nIs {guess} too high (H), too low (L), or correct (C)? ").upper()
        
        if feedback == 'H':
            high = guess - 1
        elif feedback == 'L':
            low = guess + 1
        elif feedback != 'C':
            print("Please enter 'H', 'L', or 'C'.")
            
    print(f"\nYay! The computer guessed your number, {guess}, correctly!")

def main():
    print("Welcome to the Number Guessing Game!")
    print("In this game, you'll think of a number, and the computer will try to guess it.")
    
    while True:
        try:
            max_number = int(input("\nEnter the maximum number for the range (e.g., 100): "))
            if max_number > 1:
                break
            else:
                print("Please enter a number greater than 1.")
        except ValueError:
            print("Please enter a valid number.")
    
    computer_guess(max_number)
    
    play_again = input("\nWould you like to play again? (yes/no): ").lower()
    while play_again == 'yes':
        while True:
            try:
                max_number = int(input("\nEnter the maximum number for the range (e.g., 100): "))
                if max_number > 1:
                    break
                else:
                    print("Please enter a number greater than 1.")
            except ValueError:
                print("Please enter a valid number.")
        computer_guess(max_number)
        play_again = input("\nWould you like to play again? (yes/no): ").lower()
    
    print("\nThanks for playing! Goodbye!")

if __name__ == "__main__":
    main()
