# Mở tệp tin trong chế độ đọc
f = open('test.txt', 'r')

# Đọc nội dung tệp tin
noidung = f.read()

# In nội dung tệp tin
print(noidung)

# Đóng tệp tin
f.close()

# Mở tệp tin trong chế độ ghi
f = open('test.txt', 'w')

# Ghi nội dung vào tệp tin
f.write('Xin chào thế giới!')

# Đóng tệp tin
f.close()

# Mở tệp tin trong chế độ đọc và ghi
f = open('test.txt', 'r+')

# Đọc nội dung tệp tin
noidung = f.read()

# In nội dung tệp tin
print(noidung)

# Xóa nội dung tệp tin
f.seek(0)
f.truncate()

# Ghi nội dung vào tệp tin
f.write('Xin chào thế giới mới!')

# Đóng tệp tin
f.close()

# Mở tệp tin trong chế độ thêm
f = open('test.txt', 'a')

# Thêm nội dung vào tệp tin
f.write(' Thêm nội dung này')

# Đóng tệp tin
f.close()