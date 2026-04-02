# Bài 1: Cơ bản

# Định nghĩa biến và gán giá trị
x = 5  # biến x có giá trị là 5
y = "Xin chào"  # biến y có giá trị là một chuỗi

# In giá trị của biến
print("Giá trị của x là:", x)  # in giá trị của biến x
print("Giá trị của y là:", y)  # in giá trị của biến y

# Nhập dữ liệu từ người dùng
ten = input("Nhập tên của bạn: ")  # nhập tên từ người dùng
tuoi = int(input("Nhập tuổi của bạn: "))  # nhập tuổi từ người dùng

# In thông tin của người dùng
print("Xin chào", ten, "tuổi của bạn là", tuoi)  # in thông tin của người dùng

# Điều kiện if-else
if tuoi > 18:
    print("Bạn đã thành niên")  # in thông báo nếu tuổi lớn hơn 18
else:
    print("Bạn chưa thành niên")  # in thông báo nếu tuổi nhỏ hơn hoặc bằng 18

# Vòng lặp for
danh_sach_so = [1, 2, 3, 4, 5]  # định nghĩa danh sách số
for so in danh_sach_so:
    print("Số hiện tại là:", so)  # in số hiện tại trong danh sách

# Hàm
def chao(ten):
    print("Xin chào", ten)  # in thông báo chào

chao("Nguyễn Văn A")  # gọi hàm chao với tham số tên là "Nguyễn Văn A"