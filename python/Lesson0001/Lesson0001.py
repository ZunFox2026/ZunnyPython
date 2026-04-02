# Bài 1: Giới thiệu Python

# Đây là một chương trình Python đơn giản
# In ra màn hình dòng chữ "Xin chào, thế giới!"
print("Xin chào, thế giới!")

# Khai báo biến và gán giá trị
# Biến 'ten' có kiểu dữ liệu là string
ten = "Nguyễn Văn A"
# In ra màn hình giá trị của biến 'ten'
print("Tên của bạn là:", ten)

# Nhập dữ liệu từ người dùng
# Sử dụng hàm input() để nhập dữ liệu
tuoi = input("Nhập tuổi của bạn: ")
# In ra màn hình giá trị vừa nhập
print("Tuổi của bạn là:", tuoi)

# Sử dụng câu lệnh if để kiểm tra điều kiện
# Nếu tuổi lớn hơn 18 thì in ra "Bạn đã thành niên"
if int(tuoi) > 18:
    print("Bạn đã thành niên")
else:
    print("Bạn chưa thành niên")

# Sử dụng vòng lặp for để in ra các số từ 1 đến 5
# Vòng lặp for sẽ chạy 5 lần
for i in range(1, 6):
    print(i)

# Sử dụng hàm để tính tổng của hai số
def tinh_tong(a, b):
    # Hàm này sẽ trả về tổng của a và b
    return a + b

# Gọi hàm tinh_tong và in ra kết quả
ket_qua = tinh_tong(5, 7)
print("Tổng của 5 và 7 là:", ket_qua)