# Mở tệp tin và đọc nội dung
def doc_teptin():
    # Mở tệp tin với quyền đọc
    file = open("test.txt", "r")
    # Đọc toàn bộ nội dung tệp tin
    noi_dung = file.read()
    # In nội dung tệp tin
    print(noi_dung)
    # Đóng tệp tin
    file.close()

# Mở tệp tin và ghi nội dung
def ghi_teptin():
    # Mở tệp tin với quyền ghi
    file = open("test.txt", "w")
    # Ghi nội dung vào tệp tin
    file.write("Xin chào, thế giới!")
    # Đóng tệp tin
    file.close()

# Mở tệp tin và thêm nội dung
def them_teptin():
    # Mở tệp tin với quyền thêm
    file = open("test.txt", "a")
    # Thêm nội dung vào tệp tin
    file.write("\nTôi là lập trình viên Python!")
    # Đóng tệp tin
    file.close()

# Chương trình chính
def main():
    # Ghi nội dung vào tệp tin
    ghi_teptin()
    # Đọc nội dung từ tệp tin
    doc_teptin()
    # Thêm nội dung vào tệp tin
    them_teptin()
    # Đọc lại nội dung từ tệp tin
    doc_teptin()

# Thực thi chương trình chính
if __name__ == "__main__":
    main()