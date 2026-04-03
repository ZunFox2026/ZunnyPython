# Bài học Python số 34: Làm việc với Decorators (Trang trí hàm)

## Mục tiêu bài học
- Hiểu được khái niệm và vai trò của **decorator** trong Python.
- Biết cách tạo và sử dụng decorator đơn giản và nâng cao.
- Áp dụng decorator để xử lý các tình huống thực tế như: đo thời gian thực thi, kiểm tra đầu vào, ghi log.
- Nâng cao kỹ năng lập trình hàm bậc cao (higher-order functions).

## Lý thuyết chi tiết

### 1. Hàm là đối tượng bậc nhất (First-class functions)
Trong Python, hàm được xem như một đối tượng bình thường. Điều này có nghĩa là:
- Có thể gán hàm cho biến.
- Truyền hàm như tham số cho hàm khác.
- Trả về hàm từ một hàm.

Ví dụ:
```python
def xin_chao():
    return "Xin chào!"

temp = xin_chao
print(temp())  # In ra: Xin chào!
```

### 2. Hàm lồng nhau (Nested functions)
Hàm có thể được định nghĩa bên trong một hàm khác.

```python
def chao_ten(ten):
    def tao_chuoi():
        return f"Xin chào {ten}!"
    return tao_chuoi()
```

### 3. Closure
Khi một hàm lồng nhau truy cập biến từ hàm bên ngoài, nó tạo thành một **closure**.

### 4. Decorator là gì?
**Decorator** là một hàm nhận vào một hàm khác, thêm hành vi cho hàm đó mà **không thay đổi nội dung hàm gốc**, rồi trả về một hàm mới.

Cú pháp sử dụng: `@tên_decorator`

Cấu trúc cơ bản:
```python
def decorator(func):
    def wrapper(*args, **kwargs):
        # Làm gì đó trước khi gọi hàm
        result = func(*args, **kwargs)
        # Làm gì đó sau khi gọi hàm
        return result
    return wrapper
```

## Ví dụ minh họa

### Ví dụ 1: Đo thời gian thực thi hàm
Tạo decorator `@do_thoi_gian` để in thời gian thực thi một hàm.

### Ví dụ 2: Kiểm tra đầu vào
Tạo decorator `@kiem_tra_duong` để đảm bảo tất cả tham số đầu vào là số dương.

### Ví dụ 3: Ghi log hoạt động
Tạo decorator `@log_thao_tac` để ghi lại khi một hàm được gọi.

## Bài tập thực hành
1. Viết decorator `@gioi_han_thoi_gian` chỉ cho phép hàm chạy nếu thời gian thực thi dưới 1 giây.
2. Viết decorator `@kiem_tra_loi` để bắt lỗi và in ra thông báo thay vì để chương trình crash.
3. Viết decorator `@chay_n_nhieu_lan(n)` cho phép chạy một hàm lặp lại `n` lần.
4. Viết decorator `@cache_ket_qua` để lưu trữ kết quả của hàm theo tham số (giống memoization).
5. Viết decorator `@yeu_cau_dang_nhap` mô phỏng kiểm tra đăng nhập trước khi thực hiện hàm.

## Tổng kết
- Decorator là công cụ mạnh mẽ giúp tách biệt logic chính và logic phụ (cross-cutting concerns) như logging, caching, xác thực, đo hiệu năng...
- Sử dụng decorator giúp code gọn, dễ bảo trì và tái sử dụng.
- Cần lưu ý đến việc truyền đúng `*args` và `**kwargs`, và bảo toàn tên hàm (dùng `@functools.wraps`).
- Decorator có thể có tham số, khi đó cần thêm một lớp hàm bao ngoài.

Hãy thực hành nhiều để làm chủ kỹ năng này!