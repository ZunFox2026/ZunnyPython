# Bài 21: Làm việc với tệp tin

# Mở tệp tin và đọc nội dung
def doc Tep():
    # Mở tệp tin 'test.txt' ở chế độ đọc ('r')
    f = open('test.txt', 'r')
    # Đọc nội dung tệp tin
    content = f.read()
    # In nội dung tệp tin
    print(content)
    # Đóng tệp tin
    f.close()

# Ghi nội dung vào tệp tin
def ghi Tep():
    # Mở tệp tin 'test.txt' ở chế độ ghi ('w')
    f = open('test.txt', 'w')
    # Ghi nội dung vào tệp tin
    f.write('Xin chào thế giới!')
    # Đóng tệp tin
    f.close()

# Thêm nội dung vào tệp tin
def them Tep():
    # Mở tệp tin 'test.txt' ở chế độ thêm ('a')
    f = open('test.txt', 'a')
    # Thêm nội dung vào tệp tin
    f.write('\nThế giới lập trình!')
    # Đóng tệp tin
    f.close()

# Chương trình chính
if __name__ == "__main__":
    # Ghi nội dung vào tệp tin
    ghi Tep()
    # Đọc nội dung tệp tin
    doc Tep()
    # Thêm nội dung vào tệp tin
    them Tep()
    # Đọc lại nội dung tệp tin
    doc Tep()