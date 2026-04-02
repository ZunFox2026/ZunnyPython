# Bài 39: Làm việc với thư viện thời gian
# Thư viện time trong Python cung cấp các chức năng để làm việc với thời gian

import time

# Lấy thời gian hiện tại
thoi_gian_hien_tai = time.time()
print("Thời gian hiện tại (số giây từ 1/1/1970): ", thoi_gian_hien_tai)

# Chuyển thời gian hiện tại sang định dạng dễ đọc
thoi_gian_dang_doc = time.localtime(thoi_gian_hien_tai)
print("Thời gian hiện tại (định dạng dễ đọc): ", thoi_gian_dang_doc)

# Lấy các thành phần của thời gian
nam = thoi_gian_dang_doc.tm_year
thang = thoi_gian_dang_doc.tm_mon
ngay = thoi_gian_dang_doc.tm_mday
gio = thoi_gian_dang_doc.tm_hour
phut = thoi_gian_dang_doc.tm_min
giay = thoi_gian_dang_doc.tm_sec

print("Năm: ", nam)
print("Tháng: ", thang)
print("Ngày: ", ngay)
print("Giờ: ", gio)
print("Phút: ", phut)
print("Giây: ", giay)

# Dừng chương trình trong 5 giây
print("Dừng chương trình trong 5 giây...")
time.sleep(5)
print("Chương trình tiếp tục...")

# Tính thời gian thực hiện một đoạn code
print("Tính thời gian thực hiện một đoạn code...")
thoi_gian_bat_dau = time.time()
# Đoạn code cần tính thời gian
for i in range(10000000):
    pass
thoi_gian_ket_thuc = time.time()
thoi_gian_thuc_hien = thoi_gian_ket_thuc - thoi_gian_bat_dau
print("Thời gian thực hiện: ", thoi_gian_thuc_hien, " giây")