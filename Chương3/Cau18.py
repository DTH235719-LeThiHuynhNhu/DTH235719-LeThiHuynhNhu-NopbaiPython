# Câu 18: Vẽ các hình bằng dấu *

def hinh1(n):
    # Hình 1: Hình vuông rỗng (viền ngoài có *)
    for i in range(n):
        for j in range(n):
            if i == 0 or i == n - 1 or j == 0 or j == n - 1:
                print("*", end="")
            else:
                print(" ", end="")
        print()


def hinh2(n):
    # Hình 2: Tam giác vuông ở góc dưới trái
    for i in range(1, n + 1):
        print("*" * i)


def hinh3(n):
    # Hình 3: Tam giác vuông ở góc trên trái
    for i in range(n, 0, -1):
        print("*" * i)


def hinh4(n):
    # Hình 4: Tam giác phải (có khoảng trắng bên trái)
    for i in range(1, n + 1):
        print(" " * (n - i) + "*" * i)


# --- Chương trình chính ---
while True:
    print("\n=== VẼ CÁC HÌNH ===")
    print("1. Hình vuông rỗng")
    print("2. Tam giác vuông dưới trái")
    print("3. Tam giác vuông trên trái")
    print("4. Tam giác phải (nghiêng phải)")
    print("0. Thoát")

    chon = int(input("Nhập lựa chọn (0-4): "))
    if chon == 0:
        print("Kết thúc chương trình.")
        break

    n = int(input("Nhập chiều cao n: "))

    if chon == 1:
        hinh1(n)
    elif chon == 2:
        hinh2(n)
    elif chon == 3:
        hinh3(n)
    elif chon == 4:
        hinh4(n)
    else:
        print("Lựa chọn không hợp lệ!")
# Câu 18: Vẽ các hình bằng dấu *

def hinh1(n):
    # Hình 1: Hình vuông rỗng (viền ngoài có *)
    for i in range(n):
        for j in range(n):
            if i == 0 or i == n - 1 or j == 0 or j == n - 1:
                print("*", end="")
            else:
                print(" ", end="")
        print()


def hinh2(n):
    # Hình 2: Tam giác vuông ở góc dưới trái
    for i in range(1, n + 1):
        print("*" * i)


def hinh3(n):
    # Hình 3: Tam giác vuông ở góc trên trái
    for i in range(n, 0, -1):
        print("*" * i)


def hinh4(n):
    # Hình 4: Tam giác phải (có khoảng trắng bên trái)
    for i in range(1, n + 1):
        print(" " * (n - i) + "*" * i)


# --- Chương trình chính ---
while True:
    print("\n=== VẼ CÁC HÌNH ===")
    print("1. Hình vuông rỗng")
    print("2. Tam giác vuông dưới trái")
    print("3. Tam giác vuông trên trái")
    print("4. Tam giác phải (nghiêng phải)")
    print("0. Thoát")

    chon = int(input("Nhập lựa chọn (0-4): "))
    if chon == 0:
        print("Kết thúc chương trình.")
        break

    n = int(input("Nhập chiều cao n: "))

    if chon == 1:
        hinh1(n)
    elif chon == 2:
        hinh2(n)
    elif chon == 3:
        hinh3(n)
    elif chon == 4:
        hinh4(n)
    else:
        print("Lựa chọn không hợp lệ!")
