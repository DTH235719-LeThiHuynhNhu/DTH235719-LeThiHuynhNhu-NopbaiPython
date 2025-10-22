import random

N = int(input("Nhập số phần tử của list: "))

if N > 101:
    print("Không thể tạo list vì chỉ có 101 số trong khoảng 0–100.")
else:
    lst = random.sample(range(0, 101), N)
    print("List ngẫu nhiên không trùng nhau là:")
    print(lst)
