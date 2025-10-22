

def xu_ly_chuoi():
    s = input("Nhập chuỗi: ")

    dem_in_hoa = 0
    dem_in_thuong = 0
    dem_chu_so = 0
    dem_ky_tu_dac_biet = 0
    dem_khoang_trang = 0
    dem_nguyen_am = 0
    dem_phu_am = 0

    nguyen_am = "aeiouAEIOU"

    for ch in s:
        if ch.isupper():
            dem_in_hoa += 1
        elif ch.islower():
            dem_in_thuong += 1
        elif ch.isdigit():
            dem_chu_so += 1
        elif ch.isspace():
            dem_khoang_trang += 1
        else:
            dem_ky_tu_dac_biet += 1

        if ch.isalpha():
            if ch in nguyen_am:
                dem_nguyen_am += 1
            else:
                dem_phu_am += 1

    print("\n📊 KẾT QUẢ PHÂN TÍCH CHUỖI:")
    print("Số chữ IN HOA:", dem_in_hoa)
    print("Số chữ thường:", dem_in_thuong)
    print("Số chữ số:", dem_chu_so)
    print("Số ký tự đặc biệt:", dem_ky_tu_dac_biet)
    print("Số khoảng trắng:", dem_khoang_trang)
    print("Số chữ Nguyên Âm:", dem_nguyen_am)
    print("Số chữ Phụ Âm:", dem_phu_am)

# Gọi hàm
xu_ly_chuoi()
