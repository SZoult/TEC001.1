#E1
numbers = []
while True:
    user_input = input("Enter a number (or press Enter to quit): ")
    if user_input == "":
        break
    numbers.append(float(user_input))
numbers.sort(reverse=True)
print("The five greatest numbers are:")
for number in numbers[:5]:
    print(number)

#E2
number = int(input("Enter an integer: "))
if number <= 1:
    print(number, "is not a prime number.")
else:
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
            break
    if is_prime:
        print(number, "is a prime number.")
    else:
        print(number, "is not a prime number.")

#E3
cities = []
for i in range(5):
    city = input("Enter the name of 5 city one by one: ")
    cities.append(city)
print("The cities you entered are:")
for city in cities:
    print(city)

#E4
def sum_of_list(numbers):
    total = 0
    for num in numbers:
        total = total + num
    return total
my_list = [2,5,1,2,6,3,5,8]
result = sum_of_list(my_list)
print("The sum of the numbers is:", result)

#E5
def remove_odd_numbers(numbers):
    even_numbers = []
    for number in numbers:
        if number % 2 == 0:
            even_numbers.append(number)
    return even_numbers


def main():
    original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    new_list = remove_odd_numbers(original_list)

    print("Original list:", original_list)
    print("List without odd numbers:", new_list)


main()