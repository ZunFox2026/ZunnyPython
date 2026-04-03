# Bài học Python số 29 - Cấp độ Trung cấp

## Chủ đề: Làm việc với Decorators trong Python

Trong bài học này, chúng ta sẽ tìm hiểu về **decorators** — một trong những tính năng mạnh mẽ và thông minh của Python, cho phép mở rộng chức năng của các hàm hoặc phương thức mà không cần thay đổi nội dung bên trong chúng. Đây là một khái niệm quan trọng ở cấp độ trung cấp, được sử dụng phổ biến trong các thư viện, framework (như Flask, FastAPI) và lập trình hướng đối tượng.

---

### 1. Mục tiêu bài học

- Hiểu được khái niệm **decorator** là gì và tại sao nên dùng.
- Biết cách tạo và sử dụng decorator đơn giản.
- Áp dụng decorator với tham số.
- Hiểu cách sử dụng `@wraps` để bảo toàn thông tin hàm gốc.
- Vận dụng decorator vào các tình huống thực tế như: đo thời gian thực thi, xác thực, ghi log.

---

### 2. Lý thuyết chi tiết

#### a) Hàm là đối tượng đầu lớp một (First-class objects)

Trong Python, hàm có thể được gán vào biến, truyền vào hàm khác, hoặc trả về từ một hàm. Điều này là nền tảng để hiểu decorator.

```python
def xin_chao():
    return "Xin chào!"

greet = xin_chao  # Gán hàm vào biến
print(greet())    # Gọi hàm qua biến
```

#### b) Hàm lồng nhau (Nested functions)

Python cho phép định nghĩa hàm bên trong hàm khác.

```python
def chao_ten(ten):
    def noi(x):
        return f"Xin chào {ten}, {x}"
    return noi("bạn khỏe không?")
```

#### c) Decorator là gì?

Một **decorator** là một hàm nhận vào một hàm khác, thêm hành vi cho hàm đó, rồi trả về một hàm mới.

Cú pháp phổ biến:

```python
@decorator
def func():
    pass
```

Tương đương với:

```python
func = decorator(func)
```

#### d) Cấu trúc cơ bản của một decorator

```python
def decorator(func):
    def wrapper(*args, **kwargs):
        # Làm gì đó trước khi gọi hàm
        result = func(*args, **kwargs)
        # Làm gì đó sau khi gọi hàm
        return result
    return wrapper
```

#### e) Sử dụng `@wraps` từ `functools`

Khi dùng decorator, thông tin như tên hàm, docstring có thể bị mất. Dùng `@wraps` để giữ lại thông tin gốc.

```python
from functools import wraps

def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper
```

---

### 3. Ví dụ minh họa

Xem trong file `main.py` để chạy các ví dụ sau:

- **Ví dụ 1**: Đo thời gian thực thi hàm.
- **Ví dụ 2**: Xác thực người dùng trước khi thực hiện hành động.
- **Ví dụ 3**: Ghi log mỗi khi hàm được gọi.

---

### 4. Bài tập thực hành

Xem trong file `exercises.py`. Hãy hoàn thành các hàm sau:

1. Tạo decorator `retry` để thử lại hàm nếu xảy ra lỗi.
2. Tạo decorator `only_admin` cho phép thực thi chỉ nếu người dùng là admin.
3. Tạo decorator `cache_result` để lưu kết quả hàm và trả lại nếu gọi lại với cùng tham số.

Gợi ý: Sử dụng `*args, **kwargs` để linh hoạt với mọi hàm.

---

### 5. Tổng kết

- Decorator là công cụ mạnh để **tái sử dụng mã nguồn** và **tách biệt logic** (ví dụ: xác thực, ghi log, xử lý lỗi).
- Hiểu và sử dụng đúng `*args`, `**kwargs` và `@wraps` là chìa khóa để viết decorator tốt.
- Decorator có thể được lồng ghép và tham số hóa để tăng tính linh hoạt.
- Đây là nền tảng cho nhiều tính năng nâng cao trong Python như context managers, class decorators, và các framework web.

Hãy luyện tập nhiều để thành thạo kỹ năng này!
