# Bài 51: Python Cơ bản
# Mô tả: Tổng hợp kiến thức nền tảng: biến, kiểu dữ liệu, câu lệnh điều kiện,
# vòng lặp, hàm, danh sách, từ điển và xử lý ngoại lệ cơ bản.

def tinh_trung_binh(danh_sach_diem):
    """Tính điểm trung bình từ danh sách các điểm số."""
    if not danh_sach_diem:  # Kiểm tra danh sách rỗng
        return 0.0
    tong_diem = sum(danh_sach_diem)
    return tong_diem / len(danh_sach_diem)

def xep_loai_hoc_luc(diem_trung_binh):
    """Xếp loại học lực dựa trên điểm trung bình."""
    if diem_trung_binh >= 9.0:
        return "Xuất sắc"
    elif diem_trung_binh >= 8.0:
        return "Giỏi"
    elif diem_trung_binh >= 6.5:
        return "Khá"
    elif diem_trung_binh >= 5.0:
        return "Trung bình"
    else:
        return "Yếu"

def main():
    """Hàm chính chạy chương trình."""
    print("=" * 40)
    print("BÀI 51: PYTHON CƠ BẢN")
    print("Chương trình tính điểm và xếp loại học sinh")
    print("=" * 40)

    # Khởi tạo từ điển lưu thông tin
    thong_tin_hoc_sinh = {
        "ho_ten": "",
        "danh_sach_mon_hoc": [],
        "danh_sach_diem": []
    }

    try:
        # 1. Nhập liệu cơ bản với xử lý ngoại lệ
        thong_tin_hoc_sinh["ho_ten"] = input("\nNhập họ tên học sinh: ").strip()
        if not thong_tin_hoc_sinh["ho_ten"]:
            raise ValueError("Tên học sinh không được để trống.")

        so_mon = int(input("Nhập số môn học: "))
        if so_mon <= 0:
            raise ValueError("Số môn học phải là số nguyên dương.")

        # 2. Sử dụng vòng lặp for để nhập điểm từng môn
        for i in range(1, so_mon + 1):
            while True:
                try:
                    ten_mon = input(f"  - Tên môn học {i}: ").strip()
                    diem_so = float(input(f"  - Điểm môn '{ten_mon}' (0-10): "))

                    if 0 <= diem_so <= 10:
                        thong_tin_hoc_sinh["danh_sach_mon_hoc"].append(ten_mon)
                        thong_tin_hoc_sinh["danh_sach_diem"].append(diem_so)
                        break
                    else:
                        print("    -> Cảnh báo: Điểm phải từ 0 đến 10. Vui lòng nhập lại.")
                except ValueError:
                    print("    -> Cảnh báo: Vui lòng nhập số hợp lệ cho điểm.")

        # 3. Xử lý dữ liệu: tính toán và xếp loại
        diem_tb = tinh_trung_binh(thong_tin_hoc_sinh["danh_sach_diem"])
        xep_loai = xep_loai_hoc_luc(diem_tb)

        # 4. Xuất kết quả sử dụng f-string và định dạng số
        print("\n" + "-" * 40)
        print("KẾT QUẢ HỌC TẬP:")
        print(f"Họ tên       : {thong_tin_hoc_sinh['ho_ten']}")
        print("Điểm chi tiết :")
        
        # Duyệt danh sách bằng zip để ghép tên môn và điểm
        for mon, diem in zip(thong_tin_hoc_sinh["danh_sach_mon_hoc"], thong_tin_hoc_sinh["danh_sach_diem"]):
            print(f"  + {mon:<15} : {diem:.1f}")
            
        print(f"Điểm TB      : {diem_tb:.2f}")
        print(f"Xếp loại     : {xep_loai}")
        print("-" * 40)

    except ValueError as loi:
        print(f"\nLỗi nhập liệu: {loi}")
        print("Vui lòng chạy lại chương trình và nhập đúng định dạng.")
    except Exception as loi_chung