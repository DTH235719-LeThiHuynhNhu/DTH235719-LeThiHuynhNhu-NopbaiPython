import math

print("=== Câu 8: Tính log_a(x) ===")
x = float(input("Nhập x (>0): "))
a = float(input("Nhập a (>0, a ≠ 1): "))

if x > 0 and a > 0 and a != 1:
    log_a_x = math.log(x) / math.log(a)
    print(f"log_{a}({x}) = {log_a_x:.6f}")
else:
    print("Giá trị không hợp lệ! Cần x>0, a>0 và a≠1.")
