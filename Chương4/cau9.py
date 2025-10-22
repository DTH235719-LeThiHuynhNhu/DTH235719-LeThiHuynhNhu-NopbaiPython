import math

print("=== Câu 9: Tính S(n) = √(2+√(2+...)) ===")
n = int(input("Nhập n: "))

S = 0
for i in range(n):
    S = math.sqrt(2 + S)

print(f"S({n}) = {S:.6f}")
