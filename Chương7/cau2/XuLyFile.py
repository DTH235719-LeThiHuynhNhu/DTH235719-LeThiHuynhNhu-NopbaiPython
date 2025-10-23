

def LuuFile(path, data):
    """Lưu một dòng dữ liệu vào file (thêm dòng mới mỗi lần gọi)."""
    file = open(path, 'a', encoding='utf-8')
    file.writelines(data)
    file.writelines("\n")
    file.close()


def DocFile(path):
    """Đọc dữ liệu từ file, trả về danh sách các dòng (mỗi dòng là 1 list số)."""
    arrSo = []
    file = open(path, 'r', encoding='utf-8')
    for line in file:
        data = line.strip()        # bỏ ký tự xuống dòng
        if data != "":             # bỏ dòng trống (nếu có)
            arr = data.split(',')  # tách thành mảng theo dấu phẩy
            arrSo.append(arr)
    file.close()
    return arrSo
