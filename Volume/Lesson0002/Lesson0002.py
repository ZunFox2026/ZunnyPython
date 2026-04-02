# Bài 2: Xử lý chuỗi

# Khai báo một chuỗi
chuoi = "Xin chào, thế giới!"

# In chuỗi
print(chuoi)

# Độ dài của chuỗi
print("Độ dài của chuỗi:", len(chuoi))

# Chuyển chuỗi thành chữ hoa
print("Chuỗi thành chữ hoa:", chuoi.upper())

# Chuyển chuỗi thành chữ thường
print("Chuỗi thành chữ thường:", chuoi.lower())

# Cắt chuỗi
print("Cắt chuỗi từ vị trí 4:", chuoi[4:])

# Tìm kiếm trong chuỗi
print("Tìm kiếm 'thế giới' trong chuỗi:", chuoi.find("thế giới"))

# Thay thế trong chuỗi
print("Thay thế 'thế giới' bằng 'Python':", chuoi.replace("thế giới", "Python"))

# Tách chuỗi
chuoi_tach = "apple,banana,cherry"
print("Tách chuỗi:", chuoi_tach.split(","))

# Kết hợp chuỗi
chuoi_ket_hop = ["Xin", "chào", "thế", "giới"]
print("Kết hợp chuỗi:", "-".join(chuoi_ket_hop))