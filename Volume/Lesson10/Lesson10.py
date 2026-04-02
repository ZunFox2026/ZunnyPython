# Mở tệp tin để đọc
file = open("test.txt", "r")

# Đọc nội dung tệp tin
noidung = file.read()

# In nội dung tệp tin
print(noidung)

# Đóng tệp tin
file.close()

# Mở tệp tin để ghi
file = open("test.txt", "w")

# Ghi nội dung vào tệp tin
file.write("Xin chào, thế giới!")

# Đóng tệp tin
file.close()

# Mở tệp tin để追加
file = open("test.txt", "a")

# Ghi nội dung vào tệp tin
file.write(" Đây là nội dung追加.")

# Đóng tệp tin
file.close()

# Mở tệp tin để đọc
file = open("test.txt", "r")

# Đọc nội dung tệp tin
noidung = file.read()

# In nội dung tệp tin
print(noidung)

# Đóng tệp tin
file.close()