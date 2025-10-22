print("=== Giải thích cách hoạt động của range() ===")

# (a)
print("a) range(5) =>", list(range(5)))
# Bắt đầu từ 0, kết thúc trước 5 → [0, 1, 2, 3, 4]

# (b)
print("b) range(5, 10) =>", list(range(5, 10)))
# Bắt đầu từ 5, kết thúc trước 10 → [5, 6, 7, 8, 9]

# (c)
print("c) range(5, 20, 3) =>", list(range(5, 20, 3)))
# Bắt đầu từ 5, mỗi lần tăng 3, dừng trước 20 → [5, 8, 11, 14, 17]

# (d)
print("d) range(20, 5, -1) =>", list(range(20, 5, -1)))
# Bắt đầu 20, giảm 1, dừng trước 5 → [20, 19, 18, ...,]()
