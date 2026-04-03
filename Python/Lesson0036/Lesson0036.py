"""
Bài học: Python 36 Cấp Cơ Bản - Chương 1: Cấu trúc dữ liệu cơ bản và vòng lặp
Tác giả: Học viên Python
Ngày: 2025-04-05
Mục tiêu: Làm quen với list, tuple, dict, vòng lặp for và while, hàm đơn giản
"""

def vidu_list():
    """
    Ví dụ 1: Sử dụng danh sách (list) và vòng lặp for
    """
    print("=== VÍ DỤ 1: Danh sách và vòng lặp for ===")
    # Tạo một danh sách các số
    danh_sach_so = [1, 3, 5, 7, 9, 11]
    
    # In từng phần tử trong danh sách
    print("Các số lẻ từ 1 đến 11:")
    for so in danh_sach_so:
        print(f"Số: {so}")
    
    # Tính tổng các số
    tong = 0
    for so in danh_sach_so:
        tong += so
    print(f"Tổng các số là: {tong}")


def vidu_tuple_va_dict():
    """
    Ví dụ 2: Sử dụng tuple và từ điển (dict)
    """
    print("\n=== VÍ DỤ 2: Tuple và Từ điển ===")
    
    # Tuple: dùng để lưu dữ liệu bất biến (không thay đổi)
    toa_do = (10, 20)
    print(f"Tọa độ điểm: x={toa_do[0]}, y={toa_do[1]}")
    
    # Từ điển: lưu dữ liệu theo cặp khóa - giá trị
    sinh_vien = {
        "ten": "Nguyễn Văn A",
        "tuoi": 20,
        "lop": "K68CNTT"
    }
    
    print(f"Sinh viên: {sinh_vien['ten']}, {sinh_vien['tuoi']} tuổi, lớp {sinh_vien['lop']}")
    
    # Duyệt từ điển bằng vòng lặp
    print("Thông tin chi tiết:")
    for khoa, gia_tri in sinh_vien.items():
        print(f"  {khoa}: {gia_tri}")


def vidu_vong_lap_while():
    """
    Ví dụ 3: Vòng lặp while và hàm đơn giản
    """
    print("\n=== VÍ DỤ 3: Vòng lặp while và hàm ===")
    
    def doan_so():
        """Hàm trò chơi đoán số đơn giản"""
        so_bi_an = 7
        so_lan_doan = 0
        print("Đoán số bí ẩn từ 1 đến 10!")
        
        while True:
            doan = int(input("Nhập số bạn đoán: "))
            so_lan_doan += 1
            if doan == so_bi_an:
                print(f"Chúc mừng! Bạn đoán đúng sau {so_lan_doan} lần.")
                break
            elif doan < so_bi_an:
                print("Số bí ẩn lớn hơn!")
            else:
                print("Số bí ẩn nhỏ hơn!")
    
    # Gọi hàm (chỉ bật khi chạy ví dụ)
    # doan_so()  # Bỏ dấu # để chơi thử


def bai_tap_nho():
    """
    Bài tập nhỏ: Viết chương trình tính điểm trung bình của 5 môn học
    Yêu cầu: Sử dụng list, vòng lặp, và in kết quả
    """
    print("\n=== BÀI TẬP NHỎ: Tính điểm trung bình ===")
    
    # Danh sách tên các môn học
    cac_mon = ["Toán", "Lý", "Hóa", "Văn", "Anh"]
    diem = []  # Danh sách lưu điểm
    
    print("Nhập điểm cho 5 môn học:")
    
    # Dùng vòng lặp để nhập điểm
    for mon in cac_mon:
        while True:
            try:
                d = float(input(f"Nhập điểm môn {mon}: "))
                if 0 <= d <= 10:
                    diem.append(d)
                    break
                else:
                    print("Điểm phải từ 0 đến 10!")
            except ValueError:
                print("Vui lòng nhập số hợp lệ!")
    
    # Tính điểm trung bình
    diem_tb = sum(diem) / len(diem)
    
    # In kết quả
    print("\n--- Kết quả ---")
    for i in range(len(cac_mon)):
        print(f"{cac_mon[i]}: {diem[i]}")
    print(f"Điểm trung bình: {diem_tb:.2f}")
    
    # Xếp loại
    if diem_tb >= 8.0:
        print("Xếp loại: Giỏi")
    elif diem_tb >= 6.5:
        print("Xếp loại: Khá")
    elif diem_tb >= 5.0:
        print("Xếp loại: Trung bình")
    else:
        print("Xếp loại: Yếu")


def main():
    """
    Hàm chính chạy chương trình
    """
    print("🎉 CHÀO MỪNG ĐẾN VỚI KHÓA HỌC PYTHON 36 CẤP CƠ BẢN 🎉")
    print("=" * 50)
    
    # Chạy các ví dụ
    vidu_list()
    vidu_tuple_va_dict()
    vidu_vong_lap_while()  # Gợi ý, không chạy tự động để không gián đoạn
    bai_tap_nho()
    
    print("\n✅ Học xong bài 1! Tiếp tục luyện tập nhé!")


# Gọi hàm chính
if __name__ == "__main__":
    main()
```

---

**Hướng dẫn sử dụng:**
1. Lưu mã vào file `python_bai1.py`
2. Chạy bằng lệnh: `python python_bai1.py`
3. Làm theo hướng dẫn trong bài tập để nhập điểm

**Tính năng đã học:**
- `list`, `tuple`, `dict`
- Vòng lặp `for` và `while`
- Hàm, nhập xuất dữ liệu
- Xử lý lỗi đơn giản với `try-except`
- Định dạng in ra màn hình

> 💡 Gợi ý: Bạn có thể mở rộng bài tập bằng cách thêm chức năng lưu điểm vào file!