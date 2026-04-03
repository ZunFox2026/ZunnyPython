from datetime import datetime, date, timedelta, timezone

# Bài tập 1: Tính số ngày còn lại đến Tết Dương lịch 2026
def tinh_ngay_con_lai():
    hom_nay = date.today()
    tet_2026 = date(2026, 1, 1)
    so_ngay = (tet_2026 - hom_nay).days
    return so_ngay

print(f"Còn {tinh_ngay_con_lai()} ngày đến Tết Dương lịch 2026")

# Bài tập 2: Kiểm tra ngày có phải cuối tuần không
def la_cuoi_tuan(ngay):
    # Thứ trong tuần: thứ Hai = 0, ..., Chủ nhật = 6
    thu_trong_tuan = ngay.weekday()
    # Cuối tuần là thứ 7 (5) và Chủ nhật (6)
    return thu_trong_tuan >= 5

ngay_thu_7 = date(2025, 7, 19)  # Thứ 7
print(f"{ngay_thu_7} là cuối tuần? {la_cuoi_tuan(ngay_thu_7)}")

# Bài tập 3: Tính thời gian làm việc giữa hai thời điểm (trừ 1 giờ nghỉ trưa)
def tinh_gio_lam_viec(thoi_diem_bat_dau, thoi_diem_ket_thuc):
    # Giả sử nghỉ trưa từ 12:00 đến 13:00
    nghi_trua_bat_dau = thoi_diem_bat_dau.replace(hour=12, minute=0, second=0, microsecond=0)
    nghi_trua_ket_thuc = thoi_diem_bat_dau.replace(hour=13, minute=0, second=0, microsecond=0)
    
    # Tính tổng thời gian làm việc
    tong_thoi_gian = thoi_diem_ket_thuc - thoi_diem_bat_dau
    
    # Nếu ca làm việc có giao với giờ nghỉ trưa
    if thoi_diem_bat_dau < nghi_trua_ket_thuc and thoi_diem_ket_thuc > nghi_trua_bat_dau:
        tong_thoi_gian -= timedelta(hours=1)  # Trừ 1 giờ nghỉ
    
    return tong_thoi_gian

bat_dau = datetime(2025, 7, 15, 8, 0)
ket_thuc = datetime(2025, 7, 15, 17, 0)
gio_lam = tinh_gio_lam_viec(bat_dau, ket_thuc)
print(f"Thời gian làm việc: {gio_lam}")

# Bài tập 4: Chuyển chuỗi thành datetime
def chuyen_doi_chuoi(thoi_gian_chuoi):
    # Định dạng: "15-07-2025 20:30"
    return datetime.strptime(thoi_gian_chuoi, "%d-%m-%Y %H:%M")

thoi_gian = chuyen_doi_chuoi("15-07-2025 20:30")
print(f"Thời gian sau khi chuyển đổi: {thoi_gian}")

# Bài tập 5: Trả về thời gian hiện tại ở 3 múi giờ
def hien_thi_thoi_gian_quoc_te():
    thoi_gian_hien_tai_utc = datetime.now(timezone.utc)
    
    # Việt Nam: UTC+7
    tz_vn = timezone(timedelta(hours=7))
    vn_time = thoi_gian_hien_tai_utc.astimezone(tz_vn)
    
    # London: UTC+0
    tz_lon = timezone(timedelta(hours=0))
    lon_time = thoi_gian_hien_tai_utc.astimezone(tz_lon)
    
    # Tokyo: UTC+9
    tz_tokyo = timezone(timedelta(hours=9))
    tokyo_time = thoi_gian_hien_tai_utc.astimezone(tz_tokyo)
    
    print(f"Việt Nam: {vn_time.strftime('%H:%M:%S')}")
    print(f"London: {lon_time.strftime('%H:%M:%S')}")
    print(f"Tokyo: {tokyo_time.strftime('%H:%M:%S')}")

hien_thi_thoi_gian_quoc_te()