

def sum(val):
    s = 0
    while val > 0:
        s += 1
        val -= 1
    return s

def sum2():
    global val
    s = 0
    while val > 0:
        s += 1
        val -= 1
    return s

def sum3():
    s = 0
    for i in range(val, 0, -1):
        s += 1
    return s


# ===== Trường hợp 1 =====
def main_case1():
    global val
    val = 5
    print("---- Trường hợp 1 ----")
    print("sum(15) =", sum(15))
    print("sum2()  =", sum2())
    print("sum3()  =", sum3())
    print("-----------------------\n")


# ===== Trường hợp 2 =====
def main_case2():
    global val
    val = 5
    print("---- Trường hợp 2 ----")
    print("sum2()  =", sum2())
    print("sum(15) =", sum(15))
    print("sum3()  =", sum3())
    print("-----------------------\n")


# ===== Trường hợp 3 =====
def main_case3():
    global val
    val = 5
    print("---- Trường hợp 3 ----")
    print("sum3()  =", sum3())
    print("sum(15) =", sum(15))
    print("sum2()  =", sum2())
    print("-----------------------\n")


# ==========================
# Gọi chạy toàn bộ 3 trường hợp
# ==========================
main_case1()
main_case2()
main_case3()
