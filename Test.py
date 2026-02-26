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





