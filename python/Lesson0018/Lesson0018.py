# Bài 18: Làm quen với thư viện matplotlib

# Thư viện matplotlib là một thư viện đồ họa mạnh mẽ trong Python, 
# thường được sử dụng để tạo ra các biểu đồ và hình ảnh.

# ImportError: Nếu chưa cài đặt thư viện matplotlib, chạy lệnh pip install matplotlib trong terminal

import matplotlib.pyplot as plt
import numpy as np

# Tạo mảng numpy từ 0 đến 10
x = np.arange(0, 10, 0.1)

# Tạo hàm y = sin(x)
y = np.sin(x)

# Tạo biểu đồ
plt.plot(x, y)

# Thêm tiêu đề cho biểu đồ
plt.title('Biểu đồ hàm sin(x)')

# Thêm nhãn cho trục x và y
plt.xlabel('x')
plt.ylabel('sin(x)')

# Hiển thị lưới
plt.grid(True)

# Hiển thị biểu đồ
plt.show()

# Ngoài ra, chúng ta cũng có thể tạo biểu đồ với nhiều đường
x = np.arange(0, 10, 0.1)
y1 = np.sin(x)
y2 = np.cos(x)

plt.plot(x, y1, label='sin(x)')
plt.plot(x, y2, label='cos(x)')

plt.title('Biểu đồ hàm sin(x) và cos(x)')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.legend()

plt.show()