## Giới thiệu
Chào mừng bạn đến với **Bài 43: Python Cơ bản**! Bài học này được thiết kế dành cho người mới bắt đầu hoặc những bạn muốn hệ thống lại kiến thức nền tảng. Mục tiêu chính là giúp bạn làm chủ cú pháp, hiểu cách Python xử lý dữ liệu và xây dựng tư duy lập trình thuật toán. Sau khi hoàn thành, bạn sẽ tự tin viết được các script xử lý chuỗi, danh sách và điều khiển luồng chương trình, tạo đà vững chắc cho các bài học nâng cao.

## Lý thuyết
Python nổi bật với cú pháp gọn gàng và khả năng đọc hiểu cao. Bài học tập trung vào ba khối kiến thức trọng tâm:
- **Biến & Kiểu dữ liệu:** Python là ngôn ngữ định kiểu động. Bạn chỉ cần gán giá trị, trình thông dịch sẽ tự nhận diện kiểu (`int`, `float`, `str`, `list`, `bool`).
- **Điều kiện & Vòng lặp:** `if-elif-else` xử lý phân nhánh. `for` thường dùng để duyệt iterable (danh sách, chuỗi, `range`), trong khi `while` lặp khi điều kiện còn đúng.
- **Hàm (Function):** Xây dựng bằng `def`, giúp đóng gói logic, tái sử dụng và dễ bảo trì. Hàm có thể nhận tham số mặc định, trả về nhiều giá trị dưới dạng tuple.
*Lưu ý quan trọng:* Python dùng thụt lề (4 khoảng trắng) để định nghĩa khối lệnh. Thụt lề sai sẽ gây lỗi `IndentationError`.

## Ví dụ
Đoạn code sau minh họa cách kết hợp hàm, vòng lặp và điều kiện:
```python
def tinh_trung_binh(diem_so):
    if not diem_so:
        return 0.0
    return sum(diem_so) / len(diem_so)

diem_hoc_vien = [7.5, 8.0, 6.0, 9.5]
tb = tinh_trung_binh(diem_hoc_vien)

for i, diem in enumerate(diem_hoc_vien):
    print(f"Bài {i+1}: {diem} điểm")

print(f"Điểm trung bình: {tb:.2f}")
if tb >= 8:
    print("Xếp loại: Giỏi")
elif tb >= 6.5:
    print("Xếp loại: Khá")
else:
    print("Xếp loại: Trung bình")
```

## Bài tập
1. Viết hàm `kiem_tra_nguyen_to(n)` trả về `True` nếu `n` là số nguyên tố, ngược lại `False`.
2. Cho chuỗi `text = "lap_trinh_python_co_ban"`. Viết code dùng vòng lặp để đếm số ký tự số và ký tự chữ cái.
3. Tạo danh sách `hoc_sinh` chứa dict `{"ten": "...", "diem": ...}`. Viết chương trình lọc ra danh sách học sinh có điểm >= 7 và sắp xếp giảm dần theo điểm.
*Hướng dẫn:* Hãy comment từng bước logic trước khi code. Sử dụng `print()` để debug biến trung gian. Nếu bí, hãy chia nhỏ bài toán thành các hàm con. Chúc bạn code vui!