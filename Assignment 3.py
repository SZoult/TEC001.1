#Ex1
i = 1
while i <= 1000:
    if i % 3 == 0:
        print(i)
    i = i + 1

#Ex2
while True:
    inch = float(input("Enter length in inches (negative to quit): "))
    if inch < 0:
        print("Program ends.")
        break
    print(f"{inch} inch = {inch * 2.54} centimeters")

#Ex3
numbers = []
while True:
    user_input = input("Enter a number (press Enter to quit): ")
    if user_input == "":
        break
    numbers.append(float(user_input))
if len(numbers) > 0:
    print("The smallest number is:", min(numbers))
    print("The largest number is:", max(numbers))
else:
    print("You haven't entered any numbers.")

#Ex4
import random
secret_number = random.randint(1, 10)
print("Welcome to the Guessing Game!")
print("I'm thinking of a number between 1 and 10.")
while True:
    guess = input("Enter your guess: ")
    if not guess.isdigit():
        print("Please enter a valid number.")
        continue
    guess = int(guess)
    if guess < secret_number:
        print("Too low!")
    elif guess > secret_number:
        print("Too high!")
    else:
        print("Correct!")
        break

#Ex5
correct_username = "python"
correct_password = "rules"
attempts = 0
max_attempts = 5
while attempts < max_attempts:
    username = input("Enter username: ")
    password = input("Enter password: ")
    if username == correct_username and password == correct_password:
        print("Welcome")
        break
    else:
        print("Username or password is incorrect.")
        attempts = attempts + 1
if attempts == max_attempts:
    print("Access denied")

#Ex6
print("Enter the string to get the middle letter(s)")
def getmiddle(s):
    n = len(s)
    if n % 2 == 0:
        return s[n//2 - 1 : n//2 + 1]
    else:
        return s[n//2]
n=input("Enter the string: ")
print("Middle letters: " + getmiddle(n))

#Ex7
def acronym(phrase):
    words = phrase.split()
    result = ""
    for word in words:
        result += word[0].upper()
    return result
p=input("Enter the phrase: ")
print((acronym(p)))
