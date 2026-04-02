# Làm quen với thư viện NumPy
## Giới thiệu
Thư viện NumPy (Numerical Python) là một thư viện quan trọng trong ngôn ngữ lập trình Python, đặc biệt là trong lĩnh vực khoa học dữ liệu và học máy. NumPy cung cấp các cấu trúc dữ liệu và hàm toán học để xử lý dữ liệu số, giúp tăng tốc độ và hiệu suất của chương trình.

NumPy được sử dụng rộng rãi trong nhiều lĩnh vực, bao gồm phân tích dữ liệu, học máy, thị giác máy tính, và xử lý tín hiệu. Thư viện này cung cấp các tính năng như tạo và xử lý mảng nhiều chiều, thực hiện các phép toán cơ bản như cộng, trừ, nhân, chia, và các phép toán phức tạp hơn như giải hệ phương trình tuyến tính.

## Lý thuyết
NumPy cung cấp các cấu trúc dữ liệu chính sau:
- Mảng (array): là một cấu trúc dữ liệu cơ bản trong NumPy, dùng để lưu trữ dữ liệu số.
- Mảng nhiều chiều (ndarray): là một cấu trúc dữ liệu nhiều chiều, dùng để lưu trữ dữ liệu số nhiều chiều.

Các hàm toán học trong NumPy bao gồm:
- Các phép toán cơ bản: cộng, trừ, nhân, chia.
- Các phép toán thống kê: tính trung bình, tính độ lệch chuẩn.
- Các phép toán tuyến tính: giải hệ phương trình tuyến tính, tìm eigenvalue và eigenvector.

## Ví dụ
Dưới đây là một số ví dụ minh họa về cách sử dụng NumPy:
```python
import numpy as np

# Tạo mảng
arr = np.array([1, 2, 3, 4, 5])
print(arr)

# Tạo mảng nhiều chiều
arr_2d = np.array([[1, 2], [3, 4]])
print(arr_2d)

# Thực hiện phép toán cơ bản
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
print(np.add(arr1, arr2))

# Tính trung bình
arr = np.array([1, 2, 3, 4, 5])
print(np.mean(arr))
```

## Bài tập
Bài tập 1: Tạo mảng có 5 phần tử với giá trị từ 1 đến 5.
Bài tập 2: Tính trung bình của mảng có giá trị [1, 2, 3, 4, 5].
Bài tập 3: Thực hiện phép toán cộng hai mảng [1, 2, 3] và [4, 5, 6].
Bài tập 4: Tạo mảng nhiều chiều với kích thước 2x3 và giá trị từ 1 đến 6.
Bài tập 5: Tính độ lệch chuẩn của mảng có giá trị [1, 2, 3, 4, 5].