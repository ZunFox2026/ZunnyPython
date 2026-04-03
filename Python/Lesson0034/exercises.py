#############################################
# BÀI TẬP DECORATORS - Bài học 34
# Sinh viên hoàn thiện các decorator dưới đây
#############################################

# Bài 1: Viết decorator @gioi_han_thoi_gian
# Nếu hàm chạy quá 1 giây, in cảnh báo
# Gợi ý: dùng time.time() và so sánh

def gioi_han_thoi_gian(func):
    # Viết code tại đây
    pass

# Bài 2: Viết decorator @kiem_tra_loi
# Bắt ngoại lệ và in lỗi thay vì để chương trình dừng

def kiem_tra_loi(func):
    # Viết code tại đây
    pass

# Bài 3: Viết decorator @chay_n_nhieu_lan(n)
# Chạy hàm lặp lại n lần
# Gợi ý: decorator có tham số -> cần 3 lớp hàm

def chay_n_nhieu_lan(n):
    # Viết code tại đây
    pass

# Bài 4: Viết decorator @cache_ket_qua
# Lưu kết quả theo tham số đầu vào để tránh tính lại
# Gợi ý: dùng dictionary để lưu (args, kwargs) -> result

def cache_ket_qua(func):
    # Viết code tại đây
    pass

# Bài 5: Viết decorator @yeu_cau_dang_nhap
# Kiểm tra tham số 'da_dang_nhap' có bằng True không
# Nếu không, in thông báo và không chạy hàm

def yeu_cau_dang_nhap(func):
    # Viết code tại đây
    pass