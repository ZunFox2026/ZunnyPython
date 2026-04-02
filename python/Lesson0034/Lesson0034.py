# Bài 34: Làm quen với thư viện NumPy

# Import thư viện NumPy
import numpy as np

# Tạo một mảng NumPy từ danh sách
danh_sach = [1, 2, 3, 4, 5]
mang_numpy = np.array(danh_sach)
print("Mảng NumPy từ danh sách:", mang_numpy)

# Tạo một mảng NumPy với đầy đủ giá trị 0
mang_zero = np.zeros(5)
print("Mảng NumPy với đầy đủ giá trị 0:", mang_zero)

# Tạo một mảng NumPy với đầy đủ giá trị 1
mang_one = np.ones(5)
print("Mảng NumPy với đầy đủ giá trị 1:", mang_one)

# Tạo một mảng NumPy với giá trị tăng dần từ 0 đến 4
mang_tang_dan = np.arange(5)
print("Mảng NumPy với giá trị tăng dần từ 0 đến 4:", mang_tang_dan)

# Tạo một mảng NumPy với giá trị ngẫu nhiên
mang_ngau_nhien = np.random.rand(5)
print("Mảng NumPy với giá trị ngẫu nhiên:", mang_ngau_nhien)

# Thực hiện các phép toán cơ bản trên mảng NumPy
mang_a = np.array([1, 2, 3, 4, 5])
mang_b = np.array([6, 7, 8, 9, 10])

# Cộng hai mảng
mang_cong = mang_a + mang_b
print("Mảng cộng:", mang_cong)

# Trừ hai mảng
mang_tru = mang_a - mang_b
print("Mảng trừ:", mang_tru)

# Nhân hai mảng
mang_nhan = mang_a * mang_b
print("Mảng nhân:", mang_nhan)

# Chia hai mảng
mang_chia = mang_a / mang_b
print("Mảng chia:", mang_chia)