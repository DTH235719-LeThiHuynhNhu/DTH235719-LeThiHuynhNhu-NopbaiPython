def LuuFile(path, data):
    # Ghi thêm 1 dòng vào file (mỗi sản phẩm là 1 dòng)
    with open(path, 'a', encoding='utf-8') as file:
        file.write(data + "\n")


def DocFile(path):
    arrProduct = []
    with open(path, 'r', encoding='utf-8') as file:
        for line in file:
            data = line.strip()  # Xóa ký tự xuống dòng
            if data:  # Nếu dòng không rỗng
                arr = data.split(';')  # Tách các trường theo dấu ';'
                arrProduct.append(arr)
    return arrProduct


# --- Ví dụ chạy ---
duongdan = "sanpham.txt"

# Ghi dữ liệu
LuuFile(duongdan, "SP01;Tivi Sony;10000;10")
LuuFile(duongdan, "SP02;Tu lanh Toshiba;8000;5")

# Đọc dữ liệu
ds = DocFile(duongdan)
print("Dữ liệu trong file:")
for sp in ds:
    print(sp)
