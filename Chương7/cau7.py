import xlsxwriter

# Tạo một file Excel mới và thêm 1 sheet
workbook = xlsxwriter.Workbook('demo.xlsx')
worksheet = workbook.add_worksheet('Sản phẩm')

# Thiết lập độ rộng cho các cột
worksheet.set_column('A:A', 5)    # STT
worksheet.set_column('B:B', 15)   # Mã sản phẩm
worksheet.set_column('C:C', 20)   # Tên sản phẩm
worksheet.set_column('D:D', 15)   # Số lượng
worksheet.set_column('E:E', 15)   # Đơn giá

# Định dạng in đậm cho tiêu đề
bold = workbook.add_format({'bold': True})

# Ghi tiêu đề cột
worksheet.write('A1', 'STT', bold)
worksheet.write('B1', 'MÃ SẢN PHẨM', bold)
worksheet.write('C1', 'TÊN SẢN PHẨM', bold)
worksheet.write('D1', 'SỐ LƯỢNG', bold)
worksheet.write('E1', 'ĐƠN GIÁ', bold)

# Thêm dữ liệu mẫu
worksheet.write('A2', 1)
worksheet.write('B2', 'SP1')
worksheet.write('C2', 'Coca')
worksheet.write('D2', 15)
worksheet.write('E2', 15000)

worksheet.write('A3', 2)
worksheet.write('B3', 'SP2')
worksheet.write('C3', 'Pepsi')
worksheet.write('D3', 20)
worksheet.write('E3', 18000)

# Chèn hình ảnh logo (phải có file ảnh trong cùng thư mục)
worksheet.insert_image('B5', 'logo_UEL.png')

# Lưu và đóng file Excel
workbook.close()

print("✅ Đã tạo file demo.xlsx thành công!")
