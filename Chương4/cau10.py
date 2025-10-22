import time

print("=== Câu 10: Vẽ hình dùng sleep ===")

# Hình 1
for i in range(1, 6):
    print("* " * i)
time.sleep(5)

# Hình 2
for i in range(5, 0, -1):
    print("* " * i)
time.sleep(5)

# Hình 3
for i in range(1, 6):
    print(" " * (5 - i) + "* " * i)
time.sleep(5)

# Hình 4
for i in range(5, 0, -1):
    print(" " * (5 - i) + "* " * i)
