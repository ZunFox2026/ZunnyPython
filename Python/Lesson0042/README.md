## Giới thiệu
Chào mừng bạn đến với **Bài 42: Python Cơ bản**. Bài học này là bước đệm quan trọng cho người mới bắt đầu, tập trung xây dựng tư duy lập trình nền tảng. Python được thiết kế với triết lý "đọc code như đọc tiếng Anh", giúp bạn tiếp cận nhanh chóng mà không bị ám ảnh bởi cú pháp phức tạp. Qua bài học, bạn sẽ biết cách khai báo biến, xử lý luồng điều khiển và viết những chương trình tương tác đơn giản với người dùng. Nội dung phù hợp cho sinh viên, người chuyển ngành hoặc bất kỳ ai muốn làm chủ công cụ lập trình phổ biến nhất hiện nay.

## Lý thuyết
Python là ngôn ngữ thông dịch, định kiểu động và hỗ trợ đa mô hình. Ở mức cơ bản, trọng tâm bao gồm:
- **Biến & Kiểu dữ liệu:** Không cần khai báo kiểu tường minh. Các kiểu thường dùng: `int`, `float`, `str`, `bool`, `list`.
- **Toán tử:** Số học (`+`, `-`, `*`, `/`, `//`, `%`, `**`), so sánh (`==`, `!=`, `>`, `<`), logic (`and`, `or`, `not`) và gán (`=`, `+=`, `-=`).
- **Cấu trúc điều khiển:** `if/elif/else` cho rẽ nhánh đa hướng. `for` kết hợp `range()` hoặc duyệt iterable. `while` lặp khi điều kiện đúng. Dùng `break` và `continue` để điều khiển vòng lặp.
- **Thụt lề & Cú pháp:** Python bắt buộc thụt lề (4 khoảng trắng) để phân chia khối code. Dòng lệnh kết thúc bằng xuống dòng, không cần dấu `;`.

## Ví dụ
```python
# Bài 42: Tổng hợp nhập liệu, điều kiện và vòng lặp
name = input("Nhập tên đầy đủ: ")
try:
    score = float(input("Nhập điểm số (0-10): "))
except ValueError:
    print("Lỗi: Vui lòng nhập số hợp lệ!")
    score = -1

if score >= 0:
    grade = "Đạt" if score >= 5.0 else "Chưa đạt"
    print(f"\n👋 Chào {name}, kết quả: {grade}")

print("\n📊 Thống kê nhanh:")
for i in range(1, 6):
    print(f" - Lượt {i}: {'✅' if i <= 3 else '⏳'}")
```

## Bài tập
1. **Tính giai thừa:** Nhập số nguyên dương `n`, dùng vòng lặp `for` hoặc `while` tính `n!`.
2. **Kiểm tra số nguyên tố:** Viết hàm kiểm tra một số có phải nguyên tố không, trả về `True`/`False`.
3. **Đổi đơn vị nhiệt độ:** Chuyển đổi giữa Celsius và Fahrenheit dựa trên lựa chọn người dùng.
💡 *Yêu cầu:* Sử dụng `try-except` để bắt lỗi nhập liệu. Chạy thử nhiều case để kiểm tra tính ổn định. Hoàn thành bài tập sẽ giúp bạn sẵn sàng cho Bài 43 về Cấu trúc dữ liệu nâng cao.