# Mở tệp tin và đọc nội dung
def doc_tepp_tin(ten_tep):
    # Mở tệp tin ở chế độ đọc
    f = open(ten_tep, 'r')
    # Đọc nội dung tệp tin
    noi_dung = f.read()
    # Đóng tệp tin
    f.close()
    return noi_dung

# Ghi nội dung vào tệp tin
def ghi_tepp_tin(ten_tep, noi_dung):
    # Mở tệp tin ở chế độ ghi
    f = open(ten_tep, 'w')
    # Ghi nội dung vào tệp tin
    f.write(noi_dung)
    # Đóng tệp tin
    f.close()

# Program chính
ten_tep = 'example.txt'
noi_dung = 'Xin chào, thế giới!'

# Ghi nội dung vào tệp tin
ghi_tepp_tin(ten_tep, noi_dung)

# Đọc và in nội dung tệp tin
in_dung = doc_tepp_tin(ten_tep)
print(in_dung)