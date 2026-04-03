# solutions.py - Lời giải Bài 25

# Bài 1: Nhập và in tổng hai số
# Xử lý lỗi nhập không phải số
def nhap_va_in_tong():
    try:
        a = float(input("Nhập số thứ nhất: "))
        b = float(input("Nhập số thứ hai: "))
        tong = a + b
        print(f"Tổng là: {tong}")
    except ValueError:
        print("Lỗi: Vui lòng nhập một số hợp lệ!")
    except Exception as e:
        print(f"Đã xảy ra lỗi: {e}")


# Bài 2: Đọc dòng đầu tiên của file với xử lý lỗi
# Bao gồm cả khối finally
def doc_dong_dau_tien(ten_file):
    try:
        with open(ten_file, 'r', encoding='utf-8') as f:
            dong_dau = f.readline().strip()
            if dong_dau:
                print(f"Dòng đầu tiên: {dong_dau}")
            else:
                print("File trống hoặc không có dòng nào.")
    except FileNotFoundError:
        print(f"Lỗi: Không tìm thấy file '{ten_file}'!")
    except PermissionError:
        print(f"Lỗi: Không có quyền đọc file '{ten_file}'!")
    except Exception as e:
        print(f"Lỗi không xác định khi đọc file: {e}")
    finally:
        print("Hoàn tất cố gắng đọc file.")


# Bài 3: Ngoại lệ tùy chỉnh cho tên không hợp lệ
class TenKhongHopLeError(Exception):
    """Ngoại lệ khi tên người dùng không hợp lệ"""
    def __init__(self, ten, tin_nhan="Tên không hợp lệ"):
        self.ten = ten
        self.tin_nhan = tin_nhan
        super().__init__(self.tin_nhan)

    def __str__(self):
        return f"TenKhongHopLeError: {self.tin_nhan} (tên nhập: '{self.ten}')"

def kiem_tra_ten(ho_ten):
    try:
        if not ho_ten or ho_ten.strip() == "":
            raise TenKhongHopLeError(ho_ten, "Tên không được để trống")
        if len(ho_ten.strip()) > 50:
            raise TenKhongHopLeError(ho_ten, "Tên không được vượt quá 50 ký tự")
        print(f"Tên hợp lệ: {ho_ten.strip()}")
    except TenKhongHopLeError as e:
        print(e)
    except Exception as e:
        print(f"Lỗi không mong muốn: {e}")
