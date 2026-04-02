# Bài 5: Làm việc với tệp
# Mở tệp và đọc nội dung
def doc_tepp():
    try:
        # Mở tệp với quyền đọc
        f = open('test.txt', 'r')
        # Đọc nội dung tệp
        noi_dung = f.read()
        # In nội dung
        print(noi_dung)
        # Đóng tệp
        f.close()
    except FileNotFoundError:
        print("Tệp không tồn tại")

# Ghi nội dung vào tệp
def ghi_tepp():
    try:
        # Mở tệp với quyền ghi
        f = open('test.txt', 'w')
        # Ghi nội dung vào tệp
        f.write("Xin chào thế giới!")
        # Đóng tệp
        f.close()
    except Exception as e:
        print("Lỗi:", str(e))

# Chương trình chính
if __name__ == "__main__":
    # Ghi nội dung vào tệp
    ghi_tepp()
    # Đọc nội dung từ tệp
    doc_tepp()