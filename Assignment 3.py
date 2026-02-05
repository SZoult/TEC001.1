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
    cm = inch * 2.54
    print(f"{inch} inch = {inch * 2.54} centimeters")