# Mở tệp tin trong chế độ đọc
file = open("test.txt", "r")

# Đọc nội dung tệp tin
noidung = file.read()

# In nội dung tệp tin
print("Nội dung tệp tin:")
print(noidung)

# Đóng tệp tin
file.close()

# Mở tệp tin trong chế độ viết
file = open("test.txt", "w")

# Ghi nội dung vào tệp tin
file.write("Xin chào, thế giới!")

# Đóng tệp tin
file.close()

# Mở tệp tin trong chế độ đọc
file = open("test.txt", "r")

# Đọc nội dung tệp tin
noidung = file.read()

# In nội dung tệp tin
print("\nNội dung tệp tin sau khi ghi:")
print(noidung)

# Đóng tệp tin
file.close()

# Mở tệp tin trong chế độ thêm
file = open("test.txt", "a")

# Thêm nội dung vào tệp tin
file.write("\nThực hành lập trình Python")

# Đóng tệp tin
file.close()

# Mở tệp tin trong chế độ đọc
file = open("test.txt", "r")

# Đọc nội dung tệp tin
noidung = file.read()

# In nội dung tệp tin
print("\nNội dung tệp tin sau khi thêm:")
print(noidung)

# Đóng tệp tin
file.close()