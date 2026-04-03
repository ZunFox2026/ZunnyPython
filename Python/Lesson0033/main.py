import math
import json

# Ví dụ 1: Xử lý nhập số từ người dùng
def nhap_so_nguyen():
    while True:
        try:
            n = int(input("Nhập một số nguyên: "))
            return n
        except ValueError:
            print("Lỗi: Bạn phải nhập một số nguyên!")

# Gọi hàm (bỏ comment dòng dưới để chạy)
# so = nhap_so_nguyen()
# print(f"Bạn đã nhập: {so}")


# Ví dụ 2: Đọc file an toàn
def doc_file_an_toan(ten_file):
    try:
        with open(ten_file, 'r', encoding='utf-8') as f:
            noi_dung = f.read()
            print("Nội dung file:")
            print(noi_dung)
    except FileNotFoundError:
        print(f"Lỗi: Không tìm thấy file '{ten_file}'!")
    except PermissionError:
        print(f"Lỗi: Không có quyền đọc file '{ten_file}'!")
    except Exception as e:
        print(f"Lỗi không xác định: {e}")
    else:
        print("Đọc file thành công!")
    finally:
        print("Hoàn tất thao tác đọc file.")

# Gọi hàm (bỏ comment dòng dưới để chạy, đảm bảo file data.txt tồn tại hoặc không)
# doc_file_an_toan("data.txt")


# Ví dụ 3: Tính trung bình danh sách số
def tinh_trung_binh(danh_sach):
    try:
        # Kiểm tra danh sách có rỗng không
        if len(danh_sach) == 0:
            raise ValueError("Danh sách rỗng, không thể tính trung bình.")
        
        tong = 0
        for gia_tri in danh_sach:
            try:
                so = float(gia_tri)
                tong += so
            except (ValueError, TypeError):
                print(f"Cảnh báo: Bỏ qua giá trị không hợp lệ: {gia_tri}")
        
        trung_binh = tong / len(danh_sach)
        return trung_binh
        
    except Exception as e:
        print(f"Lỗi khi tính trung bình: {e}")
        return None

# Gọi hàm
# ds1 = [1, 2, 3, 4, 5]
# print(f"Trung bình ds1: {tinh_trung_binh(ds1)}")
#
# ds2 = [1, 'a', 3, None, 5]
# print(f"Trung bình ds2: {tinh_trung_binh(ds2)}")
#
# ds3 = []
# print(f"Trung bình ds3: {tinh_trung_binh(ds3)}")