# Mở file và đọc nội dung
def doc_file():
    # Mở file với quyền đọc
    file = open('test.txt', 'r')
    # Đọc nội dung file
    noi_dung = file.read()
    # In nội dung
    print(noi_dung)
    # Đóng file
    file.close()

# Mở file và ghi nội dung
def ghi_file():
    # Mở file với quyền ghi
    file = open('test.txt', 'w')
    # Ghi nội dung vào file
    file.write('Xin chào thế giới!')
    # Đóng file
    file.close()

# Mở file và thêm nội dung
def them_file():
    # Mở file với quyền thêm
    file = open('test.txt', 'a')
    # Thêm nội dung vào file
    file.write('\nThế giới Python!')
    # Đóng file
    file.close()

# Chương trình chính
def main():
    # Tạo file mới hoặc mở file đã có
    ghi_file()
    # Thêm nội dung vào file
    them_file()
    # Đọc và in nội dung file
    doc_file()

# Chạy chương trình chính
if __name__ == "__main__":
    main()