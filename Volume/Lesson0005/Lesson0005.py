# Bài 5: Xử lý chuỗi
# Chương trình này sẽ thực hiện các phép toán cơ bản trên chuỗi

# Khai báo một chuỗi
chuoi = "Xin chào thế giới"

# In chuỗi
print("Chuỗi gốc:", chuoi)

# Độ dài của chuỗi
print("Độ dài của chuỗi:", len(chuoi))

# Chuyển chuỗi sang chữ hoa
print("Chuỗi sang chữ hoa:", chuoi.upper())

# Chuyển chuỗi sang chữ thường
print("Chuỗi sang chữ thường:", chuoi.lower())

# Cắt chuỗi
print("Cắt chuỗi từ vị trí 4 đến 9:", chuoi[4:9])

# Thay thế chuỗi
print("Thay thế 'thế' bằng 'mới':", chuoi.replace("thế", "mới"))

# Tìm kiếm chuỗi
print("Vị trí của 'giới' trong chuỗi:", chuoi.find("giới"))

# Tách chuỗi
chuoi_tach = "Hello,World,Python"
print("Tách chuỗi bằng dấu phẩy:", chuoi_tach.split(","))

# Ghép chuỗi
chuoi1 = "Xin"
chuoi2 = "chào"
print("Ghép chuỗi bằng dấu cộng:", chuoi1 + " " + chuoi2)

# Định dạng chuỗi
ten = "Nguyễn Văn A"
tuoi = 20
print("Định dạng chuỗi bằng format:", "Tên: {} - Tuổi: {}".format(ten, tuoi))