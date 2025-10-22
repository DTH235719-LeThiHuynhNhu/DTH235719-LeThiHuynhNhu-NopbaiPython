import random

print("Chương trình minh họa hàm randrange(0, 100)")
print("------------------------------------------------")

# In thử 20 giá trị ngẫu nhiên từ randrange(0, 100)
print("20 giá trị ngẫu nhiên được sinh ra:")
for i in range(20):
    value = random.randrange(0, 100)
    print(value, end=' ')
print("\n------------------------------------------------")

# Kiểm tra các giá trị cụ thể
test_values = [4.5, 34, -1, 100, 0, 99]

print("Kiểm tra xem các giá trị có thể xuất hiện trong randrange(0, 100) hay không:")
for val in test_values:
    if isinstance(val, int) and 0 <= val < 100:
        print(f"✅ {val} có thể xuất hiện (nằm trong đoạn [0, 99])")
    else:
        print(f"❌ {val} KHÔNG thể xuất hiện")

print("------------------------------------------------")
print("Kết luận: Các giá trị có thể xuất hiện là 0, 34, 99 (số nguyên trong đoạn 0..99).")
