import random

def choi_game():
    # Máy chọn ngẫu nhiên 1 số trong [1, 100]
    so_may = random.randint(1, 100)
    so_lan_doan = 0
    gioi_han = 7

    print("\n🎯 Máy đã chọn 1 số trong khoảng [1, 100].")
    print("Bạn có tối đa 7 lần để đoán đúng!\n")

    while so_lan_doan < gioi_han:
        try:
            doan = int(input(f"Lần đoán thứ {so_lan_doan + 1}: Nhập số bạn đoán: "))
        except ValueError:
            print("⚠️ Vui lòng nhập một số nguyên hợp lệ!")
            continue

        so_lan_doan += 1

        if doan == so_may:
            print(f"🎉 Chúc mừng! Bạn đã đoán đúng số {so_may} sau {so_lan_doan} lần.\n")
            break
        elif doan < so_may:
            print("🔼 Số bạn đoán nhỏ hơn số của máy.")
        else:
            print("🔽 Số bạn đoán lớn hơn số của máy.")

        print(f"👉 Còn lại {gioi_han - so_lan_doan} lần đoán.\n")

    # Nếu đoán sai quá 7 lần
    if so_lan_doan == gioi_han and doan != so_may:
        print(f"😢 Bạn đã đoán sai quá {gioi_han} lần. Số đúng là {so_may}.\n")

def main():
    while True:
        choi_game()
        tiep_tuc = input("👉 Bạn có muốn chơi lại không? (c/k): ").lower()
        if tiep_tuc != 'c':
            print("\n👋 Cảm ơn bạn đã chơi! Hẹn gặp lại!\n")
            break

# --- Chạy chương trình ---
if __name__ == "__main__":
    main()
