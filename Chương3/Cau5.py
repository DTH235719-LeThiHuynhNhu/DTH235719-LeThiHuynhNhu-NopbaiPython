# Chương trình kiểm tra thứ tự của i, j, k

def kiem_tra(i, j, k):
    print(f"\nTrường hợp: i={i}, j={j}, k={k}")
    if i < j and j < k:
        print("Kết quả: Tăng dần")
    elif i > j and j > k:
        print("Kết quả: Giảm dần")
    else:
        print("Kết quả: Không theo thứ tự tăng hay giảm")

# Các trường hợp theo đề
kiem_tra(3, 5, 7)   # (a)
kiem_tra(3, 7, 5)   # (b)
kiem_tra(5, 3, 7)   # (c)
kiem_tra(5, 7, 3)   # (d)
kiem_tra(7, 3, 5)   # (e)
kiem_tra(7, 5, 3)   # (f)
