# Hàm tính tổng các ước số (trừ chính nó)
def tong_uoc(n):
    tong = 0
    for i in range(1, n):
        if n % i == 0:
            tong += i
    return tong


# a) Hàm kiểm tra số hoàn thiện
def so_hoan_thien(n):
    return tong_uoc(n) == n


# b) Hàm kiểm tra số thịnh vượng
def so_thinh_vuong(n):
    return tong_uoc(n) > n


# --- Chạy kiểm thử ---
for num in [6, 12, 28, 15, 18]:
    print(f"{num}: ", end='')
    if so_hoan_thien(num):
        print("→ Là số hoàn thiện")
    elif so_thinh_vuong(num):
        print("→ Là số thịnh vượng")
    else:
        print("→ Không phải 2 loại trên")
