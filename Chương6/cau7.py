def nhap_day_tang():
    while True:
        try:
            n = int(input("Nhập số phần tử của dãy: "))
            if n <= 0:
                print("Vui lòng nhập số phần tử > 0.")
                continue

            lst = []
            for i in range(n):
                x = float(input(f"Nhập phần tử thứ {i+1}: "))
                lst.append(x)

            # Kiểm tra dãy có tăng hay không
            tang = all(lst[i] < lst[i+1] for i in range(len(lst)-1))
            if tang:
                print("✅ Dãy hợp lệ (tăng dần).")
                return lst
            else:
                print("❌ Dãy không tăng dần. Nhập lại toàn bộ!\n")

        except ValueError:
            print("Vui lòng nhập số hợp lệ!")

# Chương trình chính
day_tang = nhap_day_tang()
print("\nDãy số sau khi nhập:")
print(day_tang)
