import math

print("=== Câu 7: Tính độ dài đoạn AB ===")
xA = float(input("Nhập hoành độ A: "))
yA = float(input("Nhập tung độ A: "))
xB = float(input("Nhập hoành độ B: "))
yB = float(input("Nhập tung độ B: "))

dAB = math.sqrt((xB - xA)**2 + (yB - yA)**2)
print(f"Độ dài đoạn AB = {dAB:.4f}")
