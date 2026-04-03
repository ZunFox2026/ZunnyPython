"""
Bài học: Python 39 - Lập Trình Hướng Đối Tượng Cơ Bản
Mục tiêu: Hiểu và sử dụng lớp (class), đối tượng (object), thuộc tính (attribute), phương thức (method)
"""

# 1. Định nghĩa một lớp đơn giản
class SinhVien:
    """
    Lớp SinhVien mô phỏng thông tin và hành động của một sinh viên.
    - Thuộc tính: ho_ten, tuoi, lop
    - Phương thức: hien_thi_thong_tin(), hoc_bai()
    """
    
    def __init__(self, ho_ten, tuoi, lop):
        """
        Hàm khởi tạo (constructor) để khởi tạo các thuộc tính cho đối tượng.
        Được gọi tự động khi tạo đối tượng mới.
        """
        self.ho_ten = ho_ten  # thuộc tính tên
        self.tuoi = tuoi      # thuộc tính tuổi
        self.lop = lop        # thuộc tính lớp
    
    def hien_thi_thong_tin(self):
        """Phương thức in ra thông tin sinh viên"""
        print(f"Họ tên: {self.ho_ten}")
        print(f"Tuổi: {self.tuoi}")
        print(f"Lớp: {self.lop}")
    
    def hoc_bai(self):
        """Phương thức mô phỏng hành động học bài"""
        print(f"{self.ho_ten} đang chăm chỉ học bài!")


# 2. Ví dụ sử dụng lớp SinhVien
def vi_du_1():
    """Ví dụ 1: Tạo một đối tượng sinh viên và hiển thị thông tin"""
    sv1 = SinhVien("Nguyễn Văn An", 20, "K60CNTT")
    print("=== Ví dụ 1: Hiển thị thông tin sinh viên ===")
    sv1.hien_thi_thong_tin()
    sv1.hoc_bai()


def vi_du_2():
    """Ví dụ 2: Tạo danh sách sinh viên"""
    print("\n=== Ví dụ 2: Danh sách sinh viên ===")
    danh_sach = [
        SinhVien("Trần Thị Bình", 19, "K60TOAN"),
        SinhVien("Lê Văn Cường", 21, "K59LY"),
        SinhVien("Phạm Thị Dung", 20, "K60HOA")
    ]
    
    for sv in danh_sach:
        sv.hien_thi_thong_tin()
        print("-" * 20)


# 3. Bài tập nhỏ: Tạo lớp HinhChuNhat
class HinhChuNhat:
    """
    Lớp mô phỏng hình chữ nhật.
    - Thuộc tính: chieu_dai, chieu_rong
    - Phương thức: tinh_dien_tich(), tinh_chu_vi(), hien_thi()
    """
    
    def __init__(self, chieu_dai, chieu_rong):
        self.chieu_dai = chieu_dai
        self.chieu_rong = chieu_rong
    
    def tinh_dien_tich(self):
        """Tính diện tích hình chữ nhật"""
        return self.chieu_dai * self.chieu_rong
    
    def tinh_chu_vi(self):
        """Tính chu vi hình chữ nhật"""
        return 2 * (self.chieu_dai + self.chieu_rong)
    
    def hien_thi(self):
        """Hiển thị thông tin hình chữ nhật"""
        print(f"Chiều dài: {self.chieu_dai}, Chiều rộng: {self.chieu_rong}")
        print(f"Diện tích: {self.tinh_dien_tich()}")
        print(f"Chu vi: {self.tinh_chu_vi()}")


def bai_tap():
    """Bài tập: Tạo 2 hình chữ nhật và in thông tin"""
    print("\n=== Bài tập: Hình chữ nhật ===")
    
    hcn1 = HinhChuNhat(5, 3)
    hcn2 = HinhChuNhat(10, 4)
    
    print("Hình chữ nhật 1:")
    hcn1.hien_thi()
    print()
    
    print("Hình chữ nhật 2:")
    hcn2.hien_thi()


# Hàm chính
def main():
    """Hàm chính thực thi các ví dụ và bài tập"""
    print("📘 BÀI HỌC: LẬP TRÌNH HƯỚNG ĐỐI TƯỢNG CƠ BẢN")
    print("=" * 50)
    
    vi_du_1()
    vi_du_2()
    bai_tap()
    
    print("\n✅ Kết thúc bài học. Bạn đã học được:")
    print("- Cách tạo lớp và đối tượng")
    print("- Sử dụng __init__, thuộc tính, phương thức")
    print("- Áp dụng vào bài toán thực tế")


# Chạy chương trình
if __name__ == "__main__":
    main()
```

---

**Giải thích ngắn:**

- **`class`**: Định nghĩa một lớp (bản thiết kế).
- **`__init__`**: Hàm khởi tạo, chạy khi tạo đối tượng.
- **`self`**: Tham chiếu đến chính đối tượng hiện tại.
- **Thuộc tính**: Dữ liệu của đối tượng (như `ho_ten`, `tuoi`).
- **Phương thức**: Hàm trong lớp, mô tả hành vi.

**Bài học rút ra**: Lập trình hướng đối tượng giúp tổ chức code rõ ràng, tái sử dụng tốt, dễ mở rộng.