# Bài 30: Làm quen với thư viện NumPy

# Import thư viện NumPy
import numpy as np

# Tạo một mảng NumPy từ một danh sách
danh_sach = [1, 2, 3, 4, 5]
mang_numpy = np.array(danh_sach)
print("Mảng NumPy từ danh sách:", mang_numpy)

# Tạo một mảng NumPy với các giá trị ngẫu nhiên
mang_ngau_nhien = np.random.rand(3, 3)
print("Mảng NumPy với giá trị ngẫu nhiên:\n", mang_ngau_nhien)

# Các phương thức cơ bản của mảng NumPy
# - shape: Trả về kích thước của mảng
# - size: Trả về số lượng phần tử trong mảng
# - dtype: Trả về kiểu dữ liệu của các phần tử trong mảng
mang_so = np.array([1, 2, 3, 4, 5])
print("Kích thước của mảng:", mang_so.shape)
print("Số lượng phần tử trong mảng:", mang_so.size)
print("Kiểu dữ liệu của các phần tử trong mảng:", mang_so.dtype)

# Các phép toán cơ bản trên mảng NumPy
mang_so_1 = np.array([1, 2, 3, 4, 5])
mang_so_2 = np.array([5, 4, 3, 2, 1])
print("Tổng của hai mảng:", mang_so_1 + mang_so_2)
print("Hiệu của hai mảng:", mang_so_1 - mang_so_2)
print("Tích của hai mảng:", mang_so_1 * mang_so_2)

# Indexing và slicing trong mảng NumPy
mang_chi_so = np.array([1, 2, 3, 4, 5])
print("Phần tử tại chỉ số 2:", mang_chi_so[2])
print("Các phần tử từ chỉ số 1 đến 3:", mang_chi_so[1:4])

# Thay đổi giá trị của các phần tử trong mảng
mang_thay_doi = np.array([1, 2, 3, 4, 5])
mang_thay_doi[2] = 10
print("Mảng sau khi thay đổi giá trị:", mang_thay_doi)