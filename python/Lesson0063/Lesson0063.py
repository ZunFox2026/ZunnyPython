# Mở tệp tin để đọc
f = open('test.txt', 'r', encoding='utf-8')

# Đọc nội dung tệp tin
noidung = f.read()

# In nội dung tệp tin
print(noidung)

# Đóng tệp tin
f.close()

# Mở tệp tin để ghi
f = open('test.txt', 'w', encoding='utf-8')

# Ghi nội dung vào tệp tin
f.write('Xin chào thế giới!')

# Đóng tệp tin
f.close()

# Mở tệp tin để đọc và ghi
f = open('test.txt', 'a', encoding='utf-8')

# Ghi tiếp nội dung vào tệp tin
f.write('\nChào lại thế giới!')

# Đóng tệp tin
f.close()

# Sử dụng with để mở tệp tin, không cần đóng tệp tin
with open('test.txt', 'r', encoding='utf-8') as f:
    # Đọc nội dung tệp tin
    noidung = f.read()
    # In nội dung tệp tin
    print(noidung)