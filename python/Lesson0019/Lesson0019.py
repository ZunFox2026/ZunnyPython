# Bài 19: Làm quen với thư viện matplotlib

# Nhập thư viện matplotlib
import matplotlib.pyplot as plt

# Tạo dữ liệu mẫu
x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]

# Tạo biểu đồ đường
# Comment: Hàm plot() dùng để vẽ biểu đồ đường
plt.plot(x, y)

# Thêm tiêu đề cho biểu đồ
# Comment: Hàm title() dùng để thêm tiêu đề cho biểu đồ
plt.title('Biểu đồ đường')

# Thêm nhãn cho trục x và trục y
# Comment: Hàm xlabel() và ylabel() dùng để thêm nhãn cho trục x và trục y
plt.xlabel('Trục x')
plt.ylabel('Trục y')

# Hiển thị biểu đồ
# Comment: Hàm show() dùng để hiển thị biểu đồ
plt.show()

# Tạo biểu đồ cột
# Comment: Hàm bar() dùng để vẽ biểu đồ cột
plt.bar(x, y)

# Thêm tiêu đề cho biểu đồ
plt.title('Biểu đồ cột')

# Thêm nhãn cho trục x và trục y
plt.xlabel('Trục x')
plt.ylabel('Trục y')

# Hiển thị biểu đồ
plt.show()

# Tạo biểu đồ tròn
# Comment: Hàm pie() dùng để vẽ biểu đồ tròn
plt.pie(y)

# Thêm tiêu đề cho biểu đồ
plt.title('Biểu đồ tròn')

# Hiển thị biểu đồ
plt.show()