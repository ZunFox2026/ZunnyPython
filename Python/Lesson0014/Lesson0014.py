"""
Python 14: Lập Trình Hướng Đối Tượng Cơ Bản
File: oop_basic.py

Mục tiêu:
- Hiểu khái niệm lớp (class) và đối tượng (object)
- Tạo lớp với thuộc tính và phương thức
- Sử dụng phương thức khởi tạo __init__
- Minh họa tính đóng gói cơ bản
"""

class SinhVien:
    """
    Lớp SinhVien mô phỏng thông tin và hành động của một sinh viên.
    
    Thuộc tính:
        ho_ten (str): Họ tên sinh viên
        mssv (str): Mã số sinh viên
        tuoi (int): Tuổi của sinh viên
        diem (float): Điểm trung bình (mặc định 0)
    
    Phương thức:
        hien_thi_thong_tin(): In thông tin sinh viên
        cap_nhat_diem(diem_moi): Cập nhật điểm mới
        xep_loai(): Trả về xếp loại học lực dựa trên điểm
    """
    
    def __init__(self, ho_ten, mssv, tuoi):
        """
        Phương thức khởi tạo đối tượng SinhVien.
        Được gọi khi tạo một đối tượng mới.
        """
        self.ho_ten = ho_ten
        self.mssv = mssv
        self.tuoi = tuoi
        self.diem = 0.0  # Điểm mặc định là 0
    
    def hien_thi_thong_tin(self):
        """In ra thông tin đầy đủ của sinh viên."""
        print(f"Họ tên: {self.ho_ten}")
        print(f"MSSV: {self.mssv}")
        print(f"Tuổi: {self.tuoi}")
        print(f"Điểm: {self.diem}")
        print(f"Xếp loại: {self.xep_loai()}")
        print("-" * 25)
    
    def cap_nhat_diem(self, diem_moi):
        """
        Cập nhật điểm cho sinh viên.
        Chỉ cho phép điểm từ 0 đến 10.
        """
        if 0 <= diem_moi <= 10:
            self.diem = diem_moi
            print(f"Đã cập nhật điểm cho {self.ho_ten} thành {diem_moi}")
        else:
            print("Lỗi: Điểm phải nằm trong khoảng 0 đến 10!")
    
    def xep_loai(self):
        """Trả về xếp loại học lực dựa trên điểm số."""
        if self.diem < 4.0:
            return "Yếu"
        elif self.diem < 6.5:
            return "Trung bình"
        elif self.diem < 8.0:
            return "Khá"
        elif self.diem < 9.0:
            return "Giỏi"
        else:
            return "Xuất sắc"


class Sach:
    """
    Lớp đơn giản hơn: mô tả một cuốn sách.
    Minh họa thêm về OOP với ít thuộc tính hơn.
    """
    
    def __init__(self, tieu_de, tac_gia, nam_xuat_ban):
        self.tieu_de = tieu_de
        self.tac_gia = tac_gia
        self.nam_xuat_ban = nam_xuat_ban
    
    def hien_thi(self):
        print(f"'{self.tieu_de}' - {self.tac_gia} ({self.nam_xuat_ban})")


def bai_tap_nho():
    """
    Bài tập nhỏ: Tạo 2 sinh viên, cập nhật điểm và in thông tin.
    Người học thử tạo thêm một đối tượng sách.
    """
    print("=== BÀI TẬP NHỎ: Làm việc với lớp SinhVien và Sach ===\n")
    
    # Tạo 2 đối tượng sinh viên
    sv1 = SinhVien("Nguyễn Văn A", "SV001", 20)
    sv2 = SinhVien("Trần Thị B", "SV002", 19)
    
    # Cập nhật điểm cho sinh viên
    sv1.cap_nhat_diem(8.5)
    sv2.cap_nhat_diem(7.2)
    
    # In thông tin
    sv1.hien_thi_thong_tin()
    sv2.hien_thi_thong_tin()
    
    # Tạo đối tượng sách (bài tập cho người học mở rộng)
    print("Thông tin sách:")
    sach = Sach("Lập trình Python", "Nguyễn Minh", 2023)
    sach.hien_thi()
    print("\n✅ Bài tập hoàn thành! Hãy thử tạo thêm đối tượng và phương thức.")


def vi_du_1():
    """Ví dụ 1: Tạo và sử dụng đối tượng SinhVien cơ bản."""
    print(">>> VÍ DỤ 1: Tạo sinh viên và cập nhật điểm")
    sv = SinhVien("Lê Văn C", "SV003", 21)
    sv.hien_thi_thong_tin()
    sv.cap_nhat_diem(9.0)
    sv.hien_thi_thong_tin()


def vi_du_2():
    """Ví dụ 2: Tạo nhiều đối tượng và in thông tin."""
    print(">>> VÍ DỤ 2: Tạo danh sách sinh viên")
    danh_sach = [
        SinhVien("Phạm Thị D", "SV004", 20),
        SinhVien("Hoàng Văn E", "SV005", 22)
    ]
    
    # Cập nhật điểm
    danh_sach[0].cap_nhat_diem(5.5)
    danh_sach[1].cap_nhat_diem(9.8)
    
    # In tất cả
    for sv in danh_sach:
        sv.hien_thi_thong_tin()


def main():
    """Hàm chính chạy chương trình."""
    print("📘 PYTHON 14: LẬP TRÌNH HƯỚNG ĐỐI TƯỢNG CƠ BẢN\n")
    
    # Chạy các ví dụ
    vi_du_1()
    print()
    vi_du_2()
    
    # Bài tập nhỏ
    bai_tap_nho()
    
    print("\n💡 Gợi ý tự học:")
    print("1. Thêm phương thức 'len_lop()' cho SinhVien")
    print("2. Tạo lớp 'GiaoVien' tương tự")
    print("3. Thử truy cập thuộc tính trực tiếp: sv1.ho_ten")


if __name__ == "__main__":
    main()
```

---

✅ **Tổng kết bài học:**
- Lớp (class) là bản thiết kế, đối tượng (object) là thể hiện cụ thể.
- Dùng `__init__` để khởi tạo đối tượng.
- Thuộc tính lưu dữ liệu, phương thức là hành động.
- Encapsulation: dữ liệu và hành động đi cùng nhau.

Chạy file để thấy kết quả và làm bài tập nhỏ!