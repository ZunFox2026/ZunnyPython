# Bài 45: Làm việc với tệp tin

# Mở tệp tin để đọc
file = open("test.txt", "r")

# Đọc nội dung tệp tin
noidung = file.read()

# In nội dung tệp tin
print("Nội dung tệp tin:")
print(noidung)

# Đóng tệp tin
file.close()

# Mở tệp tin để ghi
file = open("test.txt", "w")

# Ghi nội dung vào tệp tin
file.write("Xin chào, thế giới!")

# Đóng tệp tin
file.close()

# Mở tệp tin để đọc và ghi
file = open("test.txt", "r+")

# Đọc nội dung tệp tin
noidung = file.read()

# In nội dung tệp tin
print("Nội dung tệp tin sau khi ghi:")
print(noidung)

# Đóng tệp tin
file.close()

# Xóa tệp tin
import os
if os.path.exists("test.txt"):
    os.remove("test.txt")
    print("Tệp tin đã được xóa")
else:
    print("Tệp tin không tồn tại")