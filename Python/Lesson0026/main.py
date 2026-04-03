### Ví dụ 1: Xử lý lỗi khi đọc file số và tính trung bình

def tinh_trung_binh_tu_file(ten_file):
    try:
        with open(ten_file, 'r', encoding='utf-8') as f:
            so_str = f.read().strip().split()
            if not so_str:
                raise ValueError("File rỗng")
            cac_so = [float(x) for x in so_str]
            trung_binh = sum(cac_so) / len(cac_so)
    except FileNotFoundError:
        print(f"Lỗi: Không tìm thấy file '{ten_file}'")
    except ValueError as e:
        print(f"Lỗi dữ liệu: {e}")
    except Exception as e:
        print(f"Lỗi không xác định: {e}")
    else:
        print(f"Trung bình: {trung_binh:.2f}")
    finally:
        print("Hoàn tất xử lý file.")

# Gọi thử hàm
print("=== Ví dụ 1: Tính trung bình từ file ===")
tinh_trung_binh_tu_file("so.txt")

tinh_trung_binh_tu_file("file_khong_ton_tai.txt")


### Ví dụ 2: Tạo ngoại lệ tùy chỉnh cho tài khoản ngân hàng

class DuoiSoDuError(Exception):
    """Ngoại lệ khi rút tiền vượt quá số dư"""
    pass

class SoTienAmError(Exception):
    """Ngoại lệ khi nạp/rút tiền âm"""
    pass

class TaiKhoanNganHang:
    def __init__(self, so_du=0):
        self.so_du = so_du

    def nap_tien(self, so_tien):
        if so_tien <= 0:
            raise SoTienAmError("Số tiền nạp phải lớn hơn 0")
        self.so_du += so_tien
        print(f"Nạp thành công {so_tien}. Số dư hiện tại: {self.so_du}")

    def rut_tien(self, so_tien):
        if so_tien <= 0:
            raise SoTienAmError("Số tiền rút phải lớn hơn 0")
        if so_tien > self.so_du:
            raise DuoiSoDuError("Số dư không đủ để rút")
        self.so_du -= so_tien
        print(f"Rút thành công {so_tien}. Số dư hiện tại: {self.so_du}")

# Sử dụng lớp tài khoản
print("\n=== Ví dụ 2: Tài khoản ngân hàng với ngoại lệ tùy chỉnh ===")
try:
    tk = TaiKhoanNganHang(100)
    tk.nap_tien(50)
    tk.rut_tien(30)
    tk.rut_tien(150)  # Gây lỗi
except DuoiSoDuError as e:
    print(f"Lỗi giao dịch: {e}")
except SoTienAmError as e:
    print(f"Lỗi tiền tệ: {e}")
except Exception as e:
    print(f"Lỗi không xác định: {e}")


### Ví dụ 3: Xử lý đầu vào người dùng với else và finally

print("\n=== Ví dụ 3: Nhập số từ người dùng ===")
try:
    n = float(input("Nhập một số thực: "))
except ValueError:
    print("Bạn đã nhập sai định dạng số!")
else:
    print(f"Bạn đã nhập số: {n}")
finally:
    print("Cảm ơn bạn đã sử dụng chương trình!")