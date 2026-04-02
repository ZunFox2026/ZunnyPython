# Mở tệp tin trong chế độ đọc (read)
file = open("test.txt", "r")

# Đọc nội dung tệp tin
noidung = file.read()
print("Nội dung tệp tin:")
print(noidung)

# Đóng tệp tin
file.close()

# Mở tệp tin trong chế độ ghi (write)
file = open("test.txt", "w")

# Ghi nội dung vào tệp tin
file.write("Xin chào thế giới!")
file.write("\nĐây là nội dung mới.")

# Đóng tệp tin
file.close()

# Mở tệp tin trong chế độ thêm (append)
file = open("test.txt", "a")

# Thêm nội dung vào tệp tin
file.write("\nNội dung được thêm vào cuối tệp tin.")

# Đóng tệp tin
file.close()

# Mở tệp tin trong chế độ đọc và ghi (read and write)
file = open("test.txt", "r+")

# Đọc nội dung tệp tin
noidung = file.read()
print("\nNội dung tệp tin sau khi thêm:")
print(noidung)

# Đóng tệp tin
file.close()