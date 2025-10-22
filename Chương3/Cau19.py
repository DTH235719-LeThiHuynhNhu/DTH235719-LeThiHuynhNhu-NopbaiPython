# Tính S(x,n) = x + x^3/3! + x^5/5! + ... + x^(2n+1)/(2n+1)!
def tinh_S(x, n):
    if n < 0:
        raise ValueError("n phải là số nguyên không âm")
    # bắt đầu với i = 0: term = x^(1)/1! = x
    term = x  # phần tử i = 0
    S = 0.0
    for i in range(n + 1):
        S += term
        # cập nhật term cho i+1: term_{i+1} = term_i * x^2 / ((2i+2)*(2i+3))
        denom_factor = (2 * i + 2) * (2 * i + 3)
        term = term * (x * x) / denom_factor
    return S

# --- Chương trình chính ---
if __name__ == "__main__":
    try:
        x = float(input("Nhập x: "))
        n = int(input("Nhập n (số nguyên không âm): "))
        if n < 0:
            print("n phải là số nguyên không âm.")
        else:
            result = tinh_S(x, n)
            print("S(x, n) = {:.12f}".format(result))  # in với 12 chữ số thập phân
    except ValueError:
        print("Dữ liệu nhập không hợp lệ. Vui lòng nhập x là số, n là số nguyên.")
