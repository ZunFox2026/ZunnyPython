# Bài 16: Làm việc với thời gian

# Import thư viện thời gian
from datetime import datetime, timedelta

# Lấy thời gian hiện tại
thoi_gian_hien_tai = datetime.now()
print("Thời gian hiện tại: ", thoi_gian_hien_tai)

# Tạo thời gian cụ thể
thoi_gian_cung_theo = datetime(2022, 1, 1, 12, 0, 0)
print("Thời gian cụ thể: ", thoi_gian_cung_theo)

# Thêm thời gian vào thời gian hiện tại
them_thoi_gian = thoi_gian_hien_tai + timedelta(days=1, hours=2, minutes=30)
print("Thời gian sau khi thêm: ", them_thoi_gian)

# Trừ thời gian từ thời gian hiện tại
tru_thoi_gian = thoi_gian_hien_tai - timedelta(days=1, hours=2, minutes=30)
print("Thời gian sau khi trừ: ", tru_thoi_gian)

# So sánh thời gian
if thoi_gian_hien_tai > thoi_gian_cung_theo:
    print("Thời gian hiện tại lớn hơn thời gian cụ thể")
else:
    print("Thời gian hiện tại nhỏ hơn hoặc bằng thời gian cụ thể")