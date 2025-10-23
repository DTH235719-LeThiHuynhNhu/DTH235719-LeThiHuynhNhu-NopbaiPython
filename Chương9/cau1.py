import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# ===============================
# DỮ LIỆU HUẤN LUYỆN
# ===============================
# Chiều cao (cm) - X cần dạng ma trận cột (n x 1)
X = np.array([147,150,153,158,163,165,168,170,173,175,178,180,183]).reshape(-1,1)

# Cân nặng (kg)
y = np.array([49,50,51,54,58,59,60,62,63,64,66,67,68])

# ===============================
# XÂY DỰNG MÔ HÌNH HỒI QUY TUYẾN TÍNH
# ===============================
model = LinearRegression()
model.fit(X, y)

# Hiển thị hệ số của mô hình
print("Hệ số hồi quy (w1):", model.coef_[0])
print("Hệ số chệch (w0):", model.intercept_)

# ===============================
# NHẬP CHIỀU CAO DỰ ĐOÁN KẾT QUẢ
# ===============================
yourHeight = float(input("Nhập chiều cao của bạn (cm): "))
yourWeight = model.predict([[yourHeight]])

print(f"→ Chiều cao bạn nhập: {yourHeight} cm")
print(f"→ Dự đoán cân nặng: {yourWeight[0]:.2f} kg")

# ===============================
# VẼ BIỂU ĐỒ
# ===============================
# Vẽ dữ liệu thật
plt.scatter(X, y)

# Vẽ đường hồi quy dự đoán
y_pred = model.predict(X)
plt.plot(X, y_pred)

plt.xlabel("Chiều cao (cm)")
plt.ylabel("Cân nặng (kg)")
plt.title("Dự đoán cân nặng dựa theo chiều cao - Linear Regression")

plt.show()
