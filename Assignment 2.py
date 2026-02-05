#Ex1
chieudaitoithieu = 42
chieu_dai = float(input("Enter the length of a zander in centimeters: "))
if chieu_dai < chieudaitoithieu:
    thieu = chieudaitoithieu - chieu_dai
    print("The fish have not reached the required size; please release them back into the pond.")
    print(f"The fish is {thieu:.1f} cm shorter than the required size.")
else:
    print("Congratulations! The fish meets the required size.")
#Ex2
hang = input("Enter the cabin class of a cruise ship (LUX, A, B, C): ").upper()
if hang == "LUX":
    print("Upper-deck cabin with a balcony.")
elif hang == "A":
    print("Above the car deck, equipped with a window.")
elif hang == "B":
    print("Windowless cabin above the car deck.")
elif hang == "C":
    print("Windowless cabin below the car deck.")
else:
    print("Invalid cabin class")
#Ex3
gioi_tinh = input("Enter biological sex (male/female): ").lower()
hemoglobin = float(input("Enter hemoglobin value (g/l): "))
if gioi_tinh == "female":
    if hemoglobin < 117:
            print("Low hemoglobin level.")
    elif hemoglobin <= 155:
            print("Normal hemoglobin level.")
    else:
            print("High hemoglobin level.")
elif gioi_tinh == "male":
    if hemoglobin < 134:
            print("Low hemoglobin level.")
    elif hemoglobin <= 167:
            print("Normal hemoglobin level.")
    else:
            print("High hemoglobin level.")
else:
        print("Invalid gender.")
#Ex4
nam = int(input("Enter a year: "))
if nam % 400 == 0:
    print(f"{nam} is a leap year.")
elif nam % 100 == 0:
    print(f"{nam} is not a leap year.")
elif nam % 4 == 0:
    print(f"{nam} is a leap year.")
else:
    print(f"{nam} is not a leap year.")
#Ex5
print("Pizza 1:")
d1 = float(input("Enter the diameter of a round pizza in centimeters: "))
g1 = float(input("Enter the price (USD): "))

print("Pizza 2:")
d2 = float(input("Enter the diameter of a round pizza in centimeters: "))
g2 = float(input("Enter the price (USD): "))

giatri1 = g1/(d1**2 * 3.14)
giatri2 = g2/(d2**2 * 3.14)

if giatri1 < giatri2:
    print("Pizza 1 provides better value for money.")
elif giatri2 < giatri1:
    print("Pizza 2 provides better value for money.")
else:
    print("Both pizzas have the same value.")