# Mở tệp để đọc
file = open("test.txt", "r")

# Đọc nội dung tệp
noidung = file.read()

# In nội dung tệp
print("Nội dung tệp là:")
print(noidung)

# Đóng tệp
file.close()

# Mở tệp để ghi
file = open("test.txt", "w")

# Ghi nội dung vào tệp
file.write("Xin chào, thế giới!")

# Đóng tệp
file.close()

# Mở tệp để đọc và ghi
file = open("test.txt", "r+")

# Đọc nội dung tệp
noidung = file.read()

# In nội dung tệp
print("Nội dung tệp sau khi ghi là:")
print(noidung)

# Đóng tệp
file.close()

# Xóa tệp
import os
os.remove("test.txt")

# Kiểm tra tệp đã được xóa
if os.path.exists("test.txt"):
    print("Tệp vẫn còn tồn tại")
else:
    print("Tệp đã được xóa")