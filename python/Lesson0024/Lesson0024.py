# Bài 24: Làm việc với tệp ZIP
# Import thư viện zipfile để làm việc với tệp ZIP
import zipfile

# Tạo một tệp ZIP mới
# Mở tệp ZIP ở chế độ viết (w)
with zipfile.ZipFile('example.zip', 'w') as zip_file:
    # Thêm tệp vào ZIP
    # Write tên tệp, dữ liệu
    zip_file.writestr('file1.txt', 'Nội dung tệp 1')
    zip_file.writestr('file2.txt', 'Nội dung tệp 2')

# Đọc nội dung của tệp ZIP
# Mở tệp ZIP ở chế độ đọc (r)
with zipfile.ZipFile('example.zip', 'r') as zip_file:
    # In thông tin về tệp ZIP
    print('Thông tin tệp ZIP:')
    print(zip_file.printdir())
    
    # Đọc nội dung của một tệp trong ZIP
    # Sử dụng tên tệp để đọc
    with zip_file.open('file1.txt', 'r') as file:
        print('Nội dung tệp 1:')
        print(file.read().decode('utf-8'))

# Xóa tệp ZIP
import os
os.remove('example.zip')