### VÍ DỤ 1: Xử lý nhiều loại ngoại lệ
try:
    a = int(input("Nhập số a: "))
    b = int(input("Nhập số b: "))
    ket_qua = a / b
    print(f"Kết quả: {ket_qua}")
except ValueError:
    print("Lỗi: Vui lòng nhập số nguyên!")
except ZeroDivisionError:
    print("Lỗi: Không thể chia cho 0!")
except Exception as e:
    print(f"Một lỗi không mong muốn đã xảy ra: {e}")
else:
    print("Phép tính thành công!")
finally:
    print("Cảm ơn bạn đã sử dụng chương trình.")


### VÍ DỤ 2: Tạo ngoại lệ tùy chỉnh cho tuổi không hợp lệ
class TuoiKhongHopLeError(Exception):
    """Ngoại lệ khi tuổi nhập vào không hợp lệ (âm hoặc quá lớn)"""
    def __init__(self, tuoi, message="Tuổi không hợp lệ"):
        self.tuoi = tuoi
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"{self.message}: {self.tuoi}"

def kiem_tra_tuoi(tuoi):
    if tuoi < 0:
        raise TuoiKhongHopLeError(tuoi, "Tuổi không thể là số âm")
    if tuoi > 150:
        raise TuoiKhongHopLeError(tuoi, "Tuổi không thể lớn hơn 150")
    return True

# Sử dụng
try:
    tuoi = int(input("Nhập tuổi của bạn: "))
    kiem_tra_tuoi(tuoi)
    print(f"Tuổi của bạn là: {tuoi}")
except TuoiKhongHopLeError as e:
    print(f"Lỗi nhập liệu: {e}")
except ValueError:
    print("Vui lòng nhập một số nguyên!")


### VÍ DỤ 3: Xử lý lỗi khi làm việc với danh sách và chỉ số
def lay_phan_tu(danh_sach, chi_so):
    try:
        return danh_sach[chi_so]
    except IndexError:
        print(f"Lỗi: Chỉ số {chi_so} nằm ngoài danh sách (độ dài: {len(danh_sach)})")
        return None
    except TypeError:
        print("Lỗi: Chỉ số phải là số nguyên!")
        return None

# Kiểm thử
ds = [10, 20, 30, 40]
print(lay_phan_tu(ds, 2))   # 30
print(lay_phan_tu(ds, 10))  # Lỗi IndexError
print(lay_phan_tu(ds, 'a')) # Lỗi TypeError