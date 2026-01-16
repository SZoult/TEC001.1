Hours = int(input("Enter Hours: "))
Rate = int(input("Enter Rate: "))
if Hours > 40:
    print("Pay: ", (40 * Rate) + ((Hours - 40) * Rate * 1.5))
else:
    print("Pay: ", Hours * Rate)