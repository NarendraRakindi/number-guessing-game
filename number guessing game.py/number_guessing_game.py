import random
secret = random.randint(1, 100)
attempts = 0
print("Welcome to the Number Guessing Game!")
print("Guess a number between 1 and 100.")
while True:
     guess = int(input("Enter your guess: "))
     attempts += 1 

     if guess < secret:
      print("Too low! Try again.")
     elif guess > secret:
      print("Too high! Try again.")
     else:
      print(f"Congratulations! You guessed the number in {attempts} attempts.")
     break 