#Ex1
Tien = input("Enter your name: ")
print("Hello, " + Tien + " !")
print("-----------------------------")
#Ex2
R=int(input("Enter radius of circle: "))
print("Circumference of circle is: ", 2*3.14*R)
print("-----------------------------")
#Ex3
Chieudai = float(input("Enter length of rectangle: "))
Chieurong = float(input("Enter width of rectangle: "))
print("Area of rectangle is: ", Chieudai * Chieurong)
print("Perimeter of rectangle is: ", 2 * (Chieudai + Chieurong))
print("-----------------------------")
#Ex4
a=int(input("Enter A: "))
b=int(input("Enter B: "))
c=int(input("Enter C: "))
print("Sum: ", a+b+c)
print("Product: ", a*b*c)
print("Average: ", (a+b+c)/3)
print("-----------------------------")
#Ex5
Talent=float(input("Enter talents: "))
Pound= float(input("Enter pounds: "))
Lot=float(input("Enter lots: "))
total_lots = Talent * 20 * 32 + Pound * 32 + Lot
total_grams = total_lots * 13.3
kilograms = int(total_grams // 1000)
grams = total_grams % 1000
print("The weight in modern units: ", kilograms, " kilograms and ",round(grams,2), " grams.")
print("-----------------------------")
#Ex6
import random
code_3_digits = ""
for _ in range(3):
    code_3_digits += str(random.randint(0, 9))
code_4_digits = ""
for _ in range(4):
    code_4_digits += str(random.randint(1, 6))
print("A 3-digit code where each number is between 0 and 9):", code_3_digits)
print("A 4-digit code where each number is between 1 and 6):", code_4_digits)