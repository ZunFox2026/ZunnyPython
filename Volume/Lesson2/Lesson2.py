# Bài 2: Làm việc với chuỗi

# Chuỗi là một chuỗi các ký tự, được đặt trong dấu nháy đơn hoặc nháy đôi
chuoi = "Xin chào"
print(chuoi)  # In ra màn hình chuỗi "Xin chào"

# Các phương thức thường dùng với chuỗi
chuoi = "Hello World"
print(len(chuoi))  # Độ dài của chuỗi
print(chuoi.upper())  # Chuyển chuỗi sang chữ hoa
print(chuoi.lower())  # Chuyển chuỗi sang chữ thường
print(chuoi.split())  # Tách chuỗi thành danh sách các từ
print(chuoi.replace("World", "Python"))  # Thay thế từ trong chuỗi

# Cắt chuỗi
chuoi = "Hello World"
print(chuoi[0:5])  # Cắt từ vị trí 0 đến 5
print(chuoi[6:])  # Cắt từ vị trí 6 đến hết

# F-String: cách mới để định dạng chuỗi
ten = "Nguyễn Văn A"
tuoi = 25
print(f"Xin chào {ten}, tuổi {tuoi}")  # In ra màn hình với dữ liệu được thay thế

# Bài tập: Tạo một chuỗi và thực hiện các phương thức với nó
chuoi = input("Nhập một chuỗi: ")
print("Độ dài của chuỗi:", len(chuoi))
print("Chuỗi sang chữ hoa:", chuoi.upper())
print("Chuỗi sang chữ thường:", chuoi.lower())
print("Danh sách các từ:", chuoi.split())