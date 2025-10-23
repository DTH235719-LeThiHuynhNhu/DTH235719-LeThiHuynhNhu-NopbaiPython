import tkinter as tk

def tinh_bmi():
    try:
        can_nang = float(entry_weight.get())
        chieu_cao = float(entry_height.get()) / 100  # cm → m
        bmi = can_nang / (chieu_cao ** 2)
        label_bmi.config(text=f"BMI của bạn: {bmi:.2f}")

        if bmi < 18.5:
            ket_qua = "Gầy"
        elif bmi < 25:
            ket_qua = "Bình thường"
        elif bmi < 30:
            ket_qua = "Thừa cân"
        else:
            ket_qua = "Béo phì"

        label_result.config(text=f"Tình trạng: {ket_qua}")
    except:
        label_bmi.config(text="Lỗi nhập dữ liệu!")
        label_result.config(text="")

root = tk.Tk()
root.title("Tính chỉ số BMI")
root.geometry("300x200")
root.configure(bg="lightyellow")

tk.Label(root, text="Nhập cân nặng (kg):", bg="lightyellow").pack(pady=5)
entry_weight = tk.Entry(root)
entry_weight.pack()

tk.Label(root, text="Nhập chiều cao (cm):", bg="lightyellow").pack(pady=5)
entry_height = tk.Entry(root)
entry_height.pack()

tk.Button(root, text="Tính BMI", command=tinh_bmi, bg="lightblue").pack(pady=5)
label_bmi = tk.Label(root, text="", bg="lightyellow", font=("Arial", 10, "bold"))
label_bmi.pack()
label_result = tk.Label(root, text="", bg="lightyellow", font=("Arial", 10, "bold"))
label_result.pack()

root.mainloop()
