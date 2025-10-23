import csv

# Mở file CSV
with open('datacsv.csv', newline='', encoding='utf-8') as f:
    # Đọc file CSV, ngăn cách bởi dấu chấm phẩy ;
    reader = csv.reader(f, delimiter=';', quoting=csv.QUOTE_NONE)

    print("Mã\tTên sản phẩm")
    print("-" * 30)

    # Duyệt từng dòng trong file
    for row in reader:
        # row[0] = mã, row[1] = tên
        print(row[0], "\t", row[1])
