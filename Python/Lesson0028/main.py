### Ví dụ 1: Đọc file an toàn với try-except-finally
try:
    file = open("data.txt", "r", encoding="utf-8")
    content = file.read()
    print("Nội dung file:", content)
except FileNotFoundError:
    print("Lỗi: Không tìm thấy file 'data.txt'")
except PermissionError:
    print("Lỗi: Không có quyền đọc file")
else:
    print("Đọc file thành công!")
finally:
    try:
        file.close()
        print("File đã được đóng.")
    except NameError:
        # Trường hợp file chưa được mở
        print("File không tồn tại để đóng.")


### Ví dụ 2: Xử lý lỗi chuyển đổi dữ liệu
print("\n--- Ví dụ 2: Chuyển đổi chuỗi sang số ---")
user_input = input("Nhập một số nguyên: ")

try:
    number = int(user_input)
except ValueError:
    print(f"'{user_input}' không phải là số nguyên hợp lệ.")
else:
    print(f"Bạn đã nhập số: {number}")
    if number % 2 == 0:
        print("Đây là số chẵn.")
    else:
        print("Đây là số lẻ.")


### Ví dụ 3: Tạo và sử dụng ngoại lệ tùy chỉnh
print("\n--- Ví dụ 3: Ngoại lệ tùy chỉnh ---")

class TuoiKhongHopLeError(Exception):
    """Ngoại lệ khi tuổi không nằm trong khoảng hợp lệ"""
    def __init__(self, tuoi, message="Tuổi phải từ 1 đến 120"):
        self.tuoi = tuoi
        self.message = message
        super().__init__(self.message)


def kiem_tra_tuoi(tuoi):
    if tuoi < 1 or tuoi > 120:
        # Gây ra ngoại lệ tùy chỉnh
        raise TuoiKhongHopLeError(tuoi)
    print(f"Tuổi hợp lệ: {tuoi} tuổi")


# Thử nghiệm với giá trị không hợp lệ
try:
    kiem_tra_tuoi(150)
except TuoiKhongHopLeError as e:
    print(f"Lỗi tuổi: {e.message} (tuổi nhập: {e.tuoi})")

# Thử với giá trị hợp lệ
try:
    kiem_tra_tuoi(25)
except TuoiKhongHopLeError as e:
    print(f"Lỗi tuổi: {e.message} (tuổi nhập: {e.tuoi})")