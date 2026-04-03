"""
Python 40 Cấp Cơ Bản: Hành Trình Từ Con Số 0 Đến Tự Tin Lập Trình
File: basic_python_journey.py
Mô tả: Bài học đầu tiên về các khái niệm cơ bản trong Python: biến, kiểu dữ liệu, nhập xuất, điều kiện, vòng lặp và hàm.
"""

def main():
    # 1. Biến và Kiểu dữ liệu cơ bản
    # Python tự động nhận diện kiểu dữ liệu
    ten = "An"              # Chuỗi (string)
    tuoi = 16               # Số nguyên (int)
    chieu_cao = 1.75        # Số thực (float)
    da_tot_nghiep = False   # Boolean (True/False)

    print("=== THÔNG TIN CÁ NHÂN ===")
    print(f"Tên: {ten}")
    print(f"Tuổi: {tuoi}")
    print(f"Chiều cao: {chieu_cao} m")
    print(f"Đã tốt nghiệp: {da_tot_nghiep}")

    # 2. Nhập dữ liệu từ người dùng
    print("\n=== NHẬP THÔNG TIN ===")
    ten_moi = input("Nhập tên của bạn: ")
    nam_sinh = int(input("Nhập năm sinh: "))
    tuoi_moi = 2024 - nam_sinh

    print(f"Chào {ten_moi}! Năm nay bạn {tuoi_moi} tuổi.")

    # 3. Cấu trúc điều kiện (if-elif-else)
    print("\n=== KIỂM TRA ĐỘ TUỔI ===")
    if tuoi_moi < 13:
        print("Bạn là thiếu nhi.")
    elif tuoi_moi < 18:
        print("Bạn là thanh thiếu niên.")
    else:
        print("Bạn đã trưởng thành.")

    # 4. Vòng lặp for - in
    print("\n=== IN CÁC SỐ CHẴN TỪ 0 ĐẾN 10 ===")
    for i in range(0, 11, 2):  # Bắt đầu từ 0, kết thúc trước 11, bước nhảy 2
        print(i, end=" ")
    print()  # Xuống dòng

    # 5. Vòng lặp while - đếm ngược
    print("\n=== ĐẾM NGƯỢC TỪ 5 ===")
    dem = 5
    while dem > 0:
        print(dem)
        dem -= 1
    print("Hết giờ!")

    # 6. Định nghĩa và sử dụng hàm
    print("\n=== SỬ DỤNG HÀM TÍNH DIỆN TÍCH HÌNH CHỮ NHẬT ===")
    chieu_dai = 8
    chieu_rong = 4
    dien_tich = tinh_dien_tich_hcn(chieu_dai, chieu_rong)
    print(f"Diện tích hình chữ nhật: {dien_tich}")

    # 7. Danh sách (list) cơ bản
    print("\n=== DANH SÁCH MÔN HỌC ===")
    mon_hoc = ["Toán", "Văn", "Anh", "Lý"]
    print("Các môn học yêu thích:", mon_hoc)
    mon_hoc.append("Hóa")  # Thêm phần tử
    print("Sau khi thêm Hóa:", mon_hoc)

    # Bài tập nhỏ: Viết chương trình kiểm tra số chẵn/lẻ
    print("\n=== BÀI TẬP NHỎ: KIỂM TRA SỐ CHẴN LẺ ===")
    so = int(input("Nhập một số nguyên: "))
    if so % 2 == 0:
        print(f"{so} là số chẵn.")
    else:
        print(f"{so} là số lẻ.")

    # Gợi ý mở rộng: Tính tổng các số từ 1 đến n
    print("\n=== BÀI TẬP NHỎ: TÍNH TỔNG 1 + 2 + ... + N ===")
    n = int(input("Nhập n: "))
    tong = 0
    for i in range(1, n + 1):
        tong += i
    print(f"Tổng từ 1 đến {n} là: {tong}")


# Hàm tính diện tích hình chữ nhật
def tinh_dien_tich_hcn(dai, rong):
    """
    Hàm trả về diện tích hình chữ nhật
    Input: chiều dài, chiều rộng
    Output: diện tích
    """
    return dai * rong


# Gọi hàm chính khi chạy chương trình
if __name__ == "__main__":
    main()


"""
Ví dụ 1: 
    Input: tên = "Bình", năm sinh = 2008
    Output: Chào Bình! Năm nay bạn 16 tuổi. → Bạn là thanh thiếu niên.

Ví dụ 2:
    Nhập số: 7 → 7 là số lẻ.

Bài tập nhỏ:
1. Viết hàm kiểm tra một số có phải là số nguyên tố không.
2. Tạo danh sách các số lẻ từ 1 đến 20 và in ra.
3. Viết chương trình tính điểm trung bình của 3 môn học.

Chúc bạn học tốt và tự tin trên hành trình lập trình với Python!
"""
```