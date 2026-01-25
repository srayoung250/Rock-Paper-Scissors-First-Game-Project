import random
number = random.randint(1, 10)
print("Welcome to the Secret Number Game!")
guess = (int(input("Guess a number between 1 and 10: ")))
if guess == number:
    print("Congradulations! You guessed the secret number.")
elif guess < number:
    print("To Low! The secret number was", number)
else:
    print("Too High! The secret number was ", number)
    
