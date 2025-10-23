import tkinter as tk

def convert_year():
    can = ["Canh", "Tân", "Nhâm", "Quý", "Giáp", "Ất", "Bính", "Đinh", "Mậu", "Kỷ"]
    chi = ["Thân", "Dậu", "Tuất", "Hợi", "Tý", "Sửu", "Dần", "Mão", "Thìn", "Tỵ", "Ngọ", "Mùi"]

    try:
        year = int(entry_year.get())
        can_chi = can[year % 10] + " " + chi[year % 12]
        label_result.config(text=f"Năm âm: {can_chi}")
    except:
        label_result.config(text="Nhập sai định dạng!")

root = tk.Tk()
root.title("Chuyển năm Dương lịch sang Âm lịch")
root.geometry("300x150")
root.configure(bg="lightyellow")

tk.Label(root, text="Nhập năm dương:", bg="lightyellow").pack(pady=5)
entry_year = tk.Entry(root)
entry_year.pack()

tk.Button(root, text="Chuyển", command=convert_year, bg="lightblue").pack(pady=5)
label_result = tk.Label(root, text="", bg="lightyellow", font=("Arial", 10, "bold"))
label_result.pack(pady=5)

root.mainloop()
