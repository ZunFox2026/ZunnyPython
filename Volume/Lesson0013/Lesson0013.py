# Bài 13: Cơ bản - Làm quen với Python
# Bài này giới thiệu các khái niệm cơ bản về Python

# In ra màn hình
print("Xin chào, đây là chương trình đầu tiên của bạn!")

# Biến và kiểu dữ liệu
# Python có các kiểu dữ liệu như số nguyên, số thực, chuỗi, boolean, danh sách, từ điển
x = 5  # số nguyên
y = 3.14  # số thực
ten = "Nguyễn Văn A"  # chuỗi
la_nam = True  # boolean
mon_hoc = ["Toán", "Lý", "Hóa"]  # danh sách
sinh_vien = {"name": "Nguyễn Văn A", "age": 20}  # từ điển

# In ra giá trị của biến
print("Giá trị của x:", x)
print("Giá trị của y:", y)
print("Tên:", ten)
print("Là nam:", la_nam)
print("Môn học:", mon_hoc)
print("Sinh viên:", sinh_vien)

# Toán tử
# Python có các toán tử như cộng, trừ, nhân, chia, mô-đun, số mũ
a = 5
b = 3
print("Tổng:", a + b)
print("Hiệu:", a - b)
print("Tích:", a * b)
print("Thương:", a / b)
print("Mô-đun:", a % b)
print("Số mũ:", a ** b)

# Câu điều kiện
# Python có các câu điều kiện như if, elif, else
if a > b:
    print("a lớn hơn b")
elif a == b:
    print("a bằng b")
else:
    print("a nhỏ hơn b")

# Vòng lặp
# Python có các vòng lặp như for, while
for i in range(5):
    print("Lần lặp thứ", i)

i = 0
while i < 5:
    print("Lần lặp thứ", i)
    i += 1

# Hàm
# Python có các hàm như def
def chao(ten):
    print("Xin chào", ten)

chao("Nguyễn Văn A")