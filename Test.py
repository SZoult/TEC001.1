import random
code_3_digits = ""
for _ in range(3):
    code_3_digits += str(random.randint(0, 9))
code_4_digits = ""
for _ in range(4):
    code_4_digits += str(random.randint(1, 6))
print("Mã khóa 3 chữ số (0–9):", code_3_digits)
print("Mã khóa 4 chữ số (1–6):", code_4_digits)
