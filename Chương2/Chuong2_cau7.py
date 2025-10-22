# Trình bày một số cách nhập dữ liệu từ bàn phím trong Python

# ------------------------------------------------------------
# 1) Nhập một giá trị (kiểu chuỗi)
print("=== Cách 1: Nhập một giá trị (string) ===")
name = input("Nhập tên của bạn: ")
print("Bạn vừa nhập:", name)

# ------------------------------------------------------------
# 2) Nhập và ép kiểu thành số nguyên / số thực
print("\n=== Cách 2: Nhập số nguyên / số thực ===")
age = int(input("Nhập tuổi (số nguyên): "))
height = float(input("Nhập chiều cao (số thực): "))
print("Tuổi:", age, "- Chiều cao:", height)

# ------------------------------------------------------------
# 3) Nhập nhiều giá trị trên một dòng (dùng split + map)
print("\n=== Cách 3: Nhập nhiều giá trị trên 1 dòng ===")
x, y = map(int, input("Nhập 2 số nguyên, cách nhau bởi khoảng trắng: ").split())
print("Hai số nguyên đã nhập:", x, y)

# ------------------------------------------------------------
# 4) Nhập nhiều phần tử thành list
print("\n=== Cách 4: Nhập nhiều số thành danh sách ===")
numbers = list(map(int, input("Nhập dãy số nguyên (cách nhau bởi khoảng trắng): ").split()))
print("Danh sách số vừa nhập:", numbers)

# ------------------------------------------------------------
# 5) Nhập nhanh bằng sys.stdin (dùng khi cần tốc độ, ví dụ lập trình thi đấu)
print("\n=== Cách 5: Nhập bằng sys.stdin ===")
import sys
print("Nhập một dòng văn bản (sẽ đọc bằng sys.stdin):")
line = sys.stdin.readline().strip()
print("Dòng vừa nhập:", line)

# ------------------------------------------------------------
# 6) Nhập nhiều dòng liên tiếp bằng vòng lặp
print("\n=== Cách 6: Nhập nhiều dòng liên tiếp ===")
print("Nhập 3 dòng văn bản:")
lines = []
for i in range(3):
    s = input(f"Dòng {i+1}: ")
    lines.append(s)
print("Các dòng vừa nhập:", lines)
