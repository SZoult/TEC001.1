if 
    try:
        Hours = int(input("Enter Hours: "))
        Rate = int(input("Enter Rate: "))
        print("Pay: ", (40 * Rate) + ((Hours - 40) * Rate * 1.5))
    except:
        print("Error")  
else:
    try:
        Hours = int(input("Enter Hours: "))
        Rate = int(input("Enter Rate: "))
        print("Pay: ", Hours * Rate)
    except:
        print("Error")  