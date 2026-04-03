# Lời giải bài tập xử lý ngoại lệ

# Bài 1: Hàm chia hai số, xử lý chia cho 0
def chia(a, b):
    try:
        ket_qua = a / b
        return ket_qua
    except ZeroDivisionError:
        print("Lỗi: Không thể chia cho 0")
        return None

# Kiểm thử
# print(chia(10, 2))
# print(chia(10, 0))

# Bài 2: Đọc file và đếm số dòng
def dem_dong_file(filename):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            so_dong = len(f.readlines())
        print(f"File '{filename}' có {so_dong} dòng.")
        return so_dong
    except FileNotFoundError:
        print(f"Lỗi: Không tìm thấy file '{filename}'")
    except PermissionError:
        print(f"Lỗi: Không có quyền truy cập file '{filename}'")
    except Exception as e:
        print(f"Lỗi không xác định: {e}")
    finally:
        print("Hoàn tất kiểm tra file.")

# Bài 3: Tạo lớp ngoại lệ NegativeAgeError và kiểm tra tuổi
class NegativeAgeError(Exception):
    """Ngoại lệ khi tuổi âm"""
    def __init__(self, tuoi):
        self.tuoi = tuoi
        super().__init__(f"Tuổi không thể âm: {tuoi}")

def kiem_tra_tuoi(tuoi):
    try:
        if tuoi < 0:
            raise NegativeAgeError(tuoi)
        print(f"Tuổi hợp lệ: {tuoi}")
    except NegativeAgeError as e:
        print(f"Lỗi tuổi: {e}")
    except TypeError:
        print("Lỗi: Tuổi phải là một số")

# Bài 4: Chuyển đổi chuỗi thành danh sách số
def chuyen_doi_chuoi_thanh_so(chuoi):
    try:
        # Tách chuỗi theo dấu phẩy và chuyển từng phần thành số
        danh_sach_chuoi = chuoi.split(',')
        danh_sach_so = [float(x.strip()) for x in danh_sach_chuoi]
        print(f"Danh sách số: {danh_sach_so}")
        return danh_sach_so
    except ValueError as e:
        print(f"Lỗi định dạng số: {e}")
        return []
    except Exception as e:
        print(f"Lỗi không xác định: {e}")
        return []

# Bài 5: Tìm giá trị lớn nhất trong danh sách
def tim_max(danh_sach):
    try:
        if len(danh_sach) == 0:
            raise ValueError("Danh sách rỗng, không thể tìm giá trị lớn nhất")
        return max(danh_sach)
    except ValueError as e:
        print(f"Lỗi: {e}")
        return None
    except TypeError as e:
        print(f"Lỗi: Danh sách chứa phần tử không so sánh được - {e}")
        return None

# Gợi ý kiểm thử các hàm:
# chia(10, 2)
# dem_dong_file("test.txt")
# kiem_tra_tuoi(-5)
# chuyen_doi_chuoi_thanh_so("1, 2.5, abc, 3")
# tim_max([])