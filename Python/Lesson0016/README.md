# Python 16: Lập Trình Hướng Đối Tượng Cơ Bản

## Giới thiệu

Lập trình hướng đối tượng (Object-Oriented Programming - OOP) là một phương pháp lập trình phổ biến, giúp tổ chức mã nguồn một cách rõ ràng và dễ bảo trì. Thay vì viết các hàm rời rạc, OOP nhóm dữ liệu và hành vi vào các **đối tượng** dựa trên các **lớp (class)**. Trong bài học này, bạn sẽ làm quen với các khái niệm cơ bản như lớp, đối tượng, thuộc tính và phương thức trong Python.

## Lý thuyết

Trong Python, **lớp (class)** là bản mẫu để tạo ra các **đối tượng (object)**. Mỗi đối tượng có thể có:
- **Thuộc tính (attributes)**: dữ liệu mô tả đối tượng (ví dụ: tên, tuổi).
- **Phương thức (methods)**: các hàm định nghĩa hành vi của đối tượng.

Từ khóa `class` dùng để khai báo một lớp. Hàm `__init__` là hàm khởi tạo, được gọi khi tạo đối tượng mới để gán giá trị ban đầu cho các thuộc tính.

## Ví dụ

Dưới đây là ví dụ về lớp `SinhVien` mô tả một sinh viên:

```python
class SinhVien:
    def __init__(self, ten, tuoi):
        self.ten = ten
        self.tuoi = tuoi

    def gioi_thieu(self):
        print(f"Xin chào, mình tên là {self.ten},今年 {self.tuoi} tuổi.")

# Tạo đối tượng từ lớp SinhVien
sv1 = SinhVien("An", 20)
sv1.gioi_thieu()  # Kết quả: Xin chào, mình tên là An,今年 20 tuổi.
```

Trong ví dụ trên:
- `SinhVien` là lớp.
- `sv1` là đối tượng của lớp.
- `__init__` khởi tạo thuộc tính `ten` và `tuoi`.
- `gioi_thieu()` là phương thức in thông tin sinh viên.

## Bài tập

1. Tạo lớp `HinhChuNhat` với các thuộc tính `chieu_dai` và `chieu_rong`, và phương thức `dien_tich()` để tính diện tích.
2. Viết chương trình tạo hai đối tượng hình chữ nhật, nhập dữ liệu từ người dùng, rồi in ra diện tích của từng hình.
3. Mở rộng lớp bằng phương thức `chu_vi()` và hiển thị kết quả.