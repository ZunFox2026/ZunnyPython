# Bài 49: Python Cơ bản

## Giới thiệu
Chào mừng bạn đến với Bài 49 – một bước đệm quan trọng giúp hệ thống hóa nền tảng lập trình Python. Bài học tập trung vào **định nghĩa hàm (functions)**, **quản lý phạm vi biến** và **xử lý ngoại lệ cơ bản**. Dù mang nhãn "Cơ bản", nội dung được thiết kế để giúp bạn chuyển từ việc viết script tuyến tính sang tư duy module, từ đó giảm lặp code, tăng tính tái sử dụng và sẵn sàng cho các dự án thực tế hoặc chủ đề nâng cao như OOP.

## Lý thuyết
Hàm trong Python được khai báo bằng từ khóa `def`, theo sau là tên hàm (viết thường, dùng `_`) và tham số trong ngoặc đơn. Một số nguyên tắc cốt lõi:
- **Tham số linh hoạt:** Hỗ trợ giá trị mặc định, `*args` (tuple vị trí), `**kwargs` (dict từ khóa).
- **Giá trị trả về:** Dùng `return`. Nếu vắng mặt, hàm tự động trả về `None`.
- **Phạm vi biến:** Biến trong hàm là cục bộ (local). Tránh lạm dụng `global`; thay vào đó, truyền dữ liệu qua tham số.
- **Tài liệu hóa:** Luôn viết docstring ngay dưới dòng `def` để mô tả mục đích, kiểu dữ liệu đầu vào/ra. Điều này hỗ trợ mạnh cho `help()` và các công cụ IDE.
- **Xử lý lỗi cơ bản:** Dùng `try...except` để bắt lỗi dự kiến, giúp chương trình không bị dừng đột ngột khi gặp dữ liệu xấu.

## Ví dụ
Minh họa hàm tính điểm trung bình kèm kiểm tra dữ liệu và xử lý ngoại lệ:
```python
def tinh_diem_trung_binh(diem_so, lam_tron=2):
    """Tính trung bình cộng danh sách điểm, làm tròn theo yêu cầu."""
    if not isinstance(diem_so, (list, tuple)) or len(diem_so) == 0:
        raise ValueError("Input phải là danh sách/tuple không rỗng.")
    avg = sum(diem_so) / len(diem_so)
    return round(avg, lam_tron)

# Thử nghiệm
try:
    print(tinh_diem_trung_binh([7.5, 8.0, 9.5]))      # Output: 8.33
    print(tinh_diem_trung_binh([10], lam_tron=0))      # Output: 10
except ValueError as e:
    print(f"Lỗi dữ liệu: {e}")
```

## Bài tập
1. **Hàm số học:** Viết `tinh_tong_binh_phuong(lst)` trả về tổng bình phương các phần tử. Nếu list rỗng, trả về `0`.
2. **Xử lý chuỗi:** Tạo `chuan_hoa_hoten(full_name)` cắt khoảng trắng thừa, viết hoa chữ cái đầu mỗi từ. Ví dụ: `"  nguyen   van  a "` → `"Nguyen Van A"`.
3. **Tổng hợp:** Viết script nhập danh sách điểm từ bàn phím (cách nhau bởi dấu phẩy), gọi hàm ở Bài 1 & ví dụ trên, in kết quả đẹp mắt. Bắt lỗi khi người dùng nhập chữ thay vì số.

💡 *Mẹo trợ giảng:* Luôn test với edge case (danh sách rỗng, số âm, chuỗi đặc biệt). Code sạch quan trọng hơn code ngắn. Chúc bạn luyện tập hiệu quả! 🐍