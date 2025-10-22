import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

root = tk.Tk()
root.title("HỆ THỐNG QUẢN LÝ TIVI")
root.geometry("1150x700")
root.resizable(False, False)

notebook = ttk.Notebook(root)
notebook.pack(fill="both", expand=True)

# ==========================================================
# ========== TAB 1: QUẢN LÝ SẢN PHẨM =======================
# ==========================================================

tab_product = ttk.Frame(notebook)
notebook.add(tab_product, text="Quản lý sản phẩm (Tivi)")

frame_input = tk.LabelFrame(tab_product, text="Thông tin sản phẩm", padx=10, pady=10)
frame_input.pack(fill="x", padx=10, pady=10)

labels = [
    "Mã sản phẩm", "Tên sản phẩm", "Hãng", "Kích thước (inch)",
    "Loại", "Giá nhập", "Giá bán", "Số lượng", "Tình trạng", "Mô tả"
]
entries = {}
for i, label in enumerate(labels):
    tk.Label(frame_input, text=label).grid(row=i//2, column=(i % 2)*2, padx=5, pady=5, sticky="e")
    entry = tk.Entry(frame_input, width=40, state="disabled")
    entry.grid(row=i//2, column=(i % 2)*2 + 1, padx=5, pady=5)
    entries[label] = entry

frame_table = tk.LabelFrame(tab_product, text="Danh sách sản phẩm")
frame_table.pack(fill="both", expand=True, padx=10, pady=10)

columns = labels
tree = ttk.Treeview(frame_table, columns=columns, show="headings")
for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=100, anchor="center")
tree.pack(fill="both", expand=True)

products = []
edit_index = None
mode = None  # "add" hoặc "edit"

# ======== Hàm tiện ích ========
def clear_entries():
    for e in entries.values():
        e.config(state="normal")
        e.delete(0, tk.END)

def lock_entries():
    for e in entries.values():
        e.config(state="disabled")

def fill_entries(data):
    for label, value in zip(labels, data):
        entries[label].config(state="normal")
        entries[label].delete(0, tk.END)
        entries[label].insert(0, value)

def get_entry_data():
    return [entries[label].get().strip() for label in labels]

# ======== Các chức năng ========
def add_product():
    global mode
    mode = "add"
    clear_entries()
    messagebox.showinfo("Thêm sản phẩm", "Nhập thông tin sản phẩm mới rồi nhấn 'Lưu'.")

def save_product():
    global mode, edit_index
    data = get_entry_data()
    if not data[0]:
        messagebox.showwarning("Thiếu thông tin", "Mã sản phẩm không được để trống!")
        return

    if mode == "add":
        products.append(data)
        tree.insert("", tk.END, values=data)
        messagebox.showinfo("Thành công", "Đã thêm sản phẩm mới.")
    elif mode == "edit" and edit_index is not None:
        tree.item(edit_index, values=data)
        for i, p in enumerate(products):
            if p[0] == data[0]:
                products[i] = data
        messagebox.showinfo("Cập nhật", "Đã sửa thông tin sản phẩm.")
    else:
        messagebox.showwarning("Lỗi", "Không có thao tác hợp lệ.")

    mode = None
    edit_index = None
    clear_entries()
    lock_entries()

def edit_product():
    global mode, edit_index
    selected = tree.selection()
    if not selected:
        messagebox.showwarning("Chưa chọn", "Hãy chọn sản phẩm cần sửa!")
        return
    edit_index = selected[0]
    values = tree.item(edit_index, "values")
    fill_entries(values)
    mode = "edit"
    messagebox.showinfo("Chỉnh sửa", "Chỉnh sửa thông tin rồi nhấn 'Lưu'.")

def cancel_action():
    global mode, edit_index
    clear_entries()
    lock_entries()
    mode = None
    edit_index = None
    messagebox.showinfo("Hủy", "Đã hủy thao tác.")

def delete_product():
    selected = tree.selection()
    if not selected:
        messagebox.showwarning("Chưa chọn", "Hãy chọn sản phẩm cần xóa!")
        return
    if not messagebox.askyesno("Xác nhận", "Bạn có chắc muốn xóa sản phẩm này?"):
        return
    for s in selected:
        tree.delete(s)
    messagebox.showinfo("Đã xóa", "Đã xóa sản phẩm được chọn!")

# ======== Nút điều khiển ========
frame_buttons = tk.Frame(tab_product)
frame_buttons.pack(pady=10)

tk.Button(frame_buttons, text="Thêm", width=15, command=add_product).grid(row=0, column=0, padx=5)
tk.Button(frame_buttons, text="Lưu", width=15, command=save_product).grid(row=0, column=1, padx=5)
tk.Button(frame_buttons, text="Sửa", width=15, command=edit_product).grid(row=0, column=2, padx=5)
tk.Button(frame_buttons, text="Hủy", width=15, command=cancel_action).grid(row=0, column=3, padx=5)
tk.Button(frame_buttons, text="Xóa", width=15, command=delete_product).grid(row=0, column=4, padx=5)
tk.Button(frame_buttons, text="Thoát", width=15, command=root.destroy).grid(row=0, column=5, padx=5)

# ==========================================================
# ========== TAB 2: QUẢN LÝ KHO HÀNG ========================
# ==========================================================

tab_stock = ttk.Frame(notebook)
notebook.add(tab_stock, text="Quản lý kho hàng")

frame_stock_input = tk.LabelFrame(tab_stock, text="Thông tin nhập/xuất hàng", padx=10, pady=10)
frame_stock_input.pack(fill="x", padx=10, pady=10)

tk.Label(frame_stock_input, text="Loại giao dịch:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
transaction_type = ttk.Combobox(frame_stock_input, values=["Nhập hàng", "Xuất hàng"], width=37)
transaction_type.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame_stock_input, text="Mã sản phẩm:").grid(row=0, column=2, padx=5, pady=5, sticky="e")
product_id_entry = tk.Entry(frame_stock_input, width=40)
product_id_entry.grid(row=0, column=3, padx=5, pady=5)

tk.Label(frame_stock_input, text="Số lượng:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
qty_entry = tk.Entry(frame_stock_input, width=40)
qty_entry.grid(row=1, column=1, padx=5, pady=5)

tk.Label(frame_stock_input, text="Nhà cung cấp:").grid(row=1, column=2, padx=5, pady=5, sticky="e")
supplier_entry = tk.Entry(frame_stock_input, width=40)
supplier_entry.grid(row=1, column=3, padx=5, pady=5)

tk.Label(frame_stock_input, text="Ngày giao dịch:").grid(row=2, column=0, padx=5, pady=5, sticky="e")
date_entry = tk.Entry(frame_stock_input, width=40)
date_entry.grid(row=2, column=1, padx=5, pady=5)
date_entry.insert(0, datetime.now().strftime("%d/%m/%Y"))

# Bảng kho hàng
frame_stock_table = tk.LabelFrame(tab_stock, text="Lịch sử nhập/xuất hàng")
frame_stock_table.pack(fill="both", expand=True, padx=10, pady=10)

stock_columns = ["Loại giao dịch", "Mã sản phẩm", "Số lượng", "Nhà cung cấp", "Ngày"]
stock_tree = ttk.Treeview(frame_stock_table, columns=stock_columns, show="headings")
for col in stock_columns:
    stock_tree.heading(col, text=col)
    stock_tree.column(col, width=150, anchor="center")
stock_tree.pack(fill="both", expand=True)

stock_data = []

def add_transaction():
    data = [
        transaction_type.get(),
        product_id_entry.get().strip(),
        qty_entry.get().strip(),
        supplier_entry.get().strip(),
        date_entry.get().strip()
    ]
    if not data[0] or not data[1] or not data[2]:
        messagebox.showwarning("Thiếu thông tin", "Vui lòng nhập đủ thông tin!")
        return
    stock_data.append(data)
    stock_tree.insert("", tk.END, values=data)
    messagebox.showinfo("Thành công", "Đã ghi nhận giao dịch!")

def clear_stock():
    for i in stock_tree.get_children():
        stock_tree.delete(i)
    stock_data.clear()

frame_stock_buttons = tk.Frame(tab_stock)
frame_stock_buttons.pack(pady=10)
tk.Button(frame_stock_buttons, text="Ghi nhận giao dịch", width=20, command=add_transaction).grid(row=0, column=0, padx=5)
tk.Button(frame_stock_buttons, text="Xóa tất cả giao dịch", width=20, command=clear_stock).grid(row=0, column=1, padx=5)

root.mainloop()
