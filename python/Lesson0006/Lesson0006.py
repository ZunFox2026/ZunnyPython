# Mở tệp tin
file = open("test.txt", "w")  # Mở tệp tin test.txt với quyền ghi

# Ghi nội dung vào tệp tin
file.write("Xin chào, thế giới!")  # Ghi chuỗi vào tệp tin
file.write("\nĐây là một tệp tin mẫu")  # Ghi tiếp một dòng khác

# Đóng tệp tin
file.close()  # Đóng tệp tin sau khi sử dụng

# Mở lại tệp tin với quyền đọc
file = open("test.txt", "r")  # Mở lại tệp tin với quyền đọc

# Đọc nội dung từ tệp tin
noidung = file.read()  # Đọc toàn bộ nội dung tệp tin
print(noidung)  # In nội dung ra màn hình

# Đóng tệp tin
file.close()  # Đóng tệp tin sau khi sử dụng

# Thử đọc từng dòng
file = open("test.txt", "r")  # Mở lại tệp tin
for line in file:  # Duyệt từng dòng trong tệp tin
    print(line.strip())  # In dòng đó, loại bỏ ký tự換 dòng

# Đóng tệp tin
file.close()  # Đóng tệp tin sau khi sử dụng

# Sử dụng with để tự động đóng tệp tin
with open("test.txt", "r") as file:  # Mở tệp tin với with
    noidung = file.read()  # Đọc nội dung tệp tin
    print(noidung)  # In nội dung ra màn hình

# Không cần gọi file.close() khi dùng with