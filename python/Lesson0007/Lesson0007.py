# Mở tệp để đọc
file = open("test.txt", "r")

# Đọc nội dung tệp
noidung = file.read()
print("Nội dung tệp:")
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
print("Nội dung tệp sau khi ghi:")
print(noidung)

# Ghi thêm nội dung vào tệp
file.write(" Đây là nội dung được thêm vào.")

# Đóng tệp
file.close()

# Xóa tệp
import os
os.remove("test.txt")

# Tạo thư mục
import os
os.mkdir("thumuc")

# Xóa thư mục
import os
os.rmdir("thumuc")