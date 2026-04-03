# Bài học Python Nâng cao số 51: Lập trình phản xạ (Reflection) và sử dụng `inspect` module

## Mục tiêu bài học
- Hiểu được khái niệm **lập trình phản xạ (reflection)** trong Python.
- Biết cách sử dụng module `inspect` để kiểm tra và thao tác với các đối tượng trong thời gian chạy.
- Ứng dụng `inspect` để ghi log tự động, gỡ lỗi, hoặc xây dựng các công cụ phát triển.
- Nâng cao kỹ năng lập trình linh hoạt và tự động hóa xử lý code.

## Lý thuyết chi tiết

### 1. Lập trình phản xạ (Reflection) là gì?
Lập trình phản xạ là khả năng của một chương trình trong việc kiểm tra, thay đổi cấu trúc, hành vi của chính nó trong lúc chạy. Python hỗ trợ mạnh mẽ lập trình phản xạ thông qua các hàm như `getattr`, `hasattr`, `setattr`, `dir`, `type`, và đặc biệt là module `inspect`.

### 2. Module `inspect`
Module `inspect` cung cấp nhiều hàm hữu ích để lấy thông tin về các đối tượng như: hàm, lớp, phương thức, tham số, khung gọi (call stack), v.v.

Một số hàm quan trọng:
- `inspect.getmembers(obj)`: Lấy danh sách các thành viên của đối tượng.
- `inspect.isfunction(obj)`, `inspect.isclass(obj)`: Kiểm tra loại đối tượng.
- `inspect.getsource(obj)`: Lấy mã nguồn của đối tượng.
- `inspect.signature(obj)`: Lấy chữ ký (tham số) của hàm.
- `inspect.stack()`: Lấy thông tin về call stack (gọi hàm).

### Ví dụ minh họa

#### Ví dụ 1: Kiểm tra thành viên của một lớp
```python
import inspect

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Xin chào, tôi là {self.name}"

# In tất cả thành viên của lớp Person
print(inspect.getmembers(Person))
```

#### Ví dụ 2: Lấy mã nguồn của hàm
```python
import inspect

def hello(name):
    """Hàm chào hỏi một người."""
    print(f"Xin chào {name}!")

# In mã nguồn của hàm
print(inspect.getsource(hello))
```

#### Ví dụ 3: Kiểm tra tham số của hàm
```python
import inspect

print(inspect.signature(hello))  # (name)
```

## Bài tập thực hành
1. Viết hàm `log_call()` in ra tên hàm và tham số khi một hàm được gọi.
2. Viết hàm `print_class_info(cls)` in ra tất cả phương thức và thuộc tính của một lớp.
3. Viết hàm `find_functions_in_module(module)` trả về danh sách tên các hàm trong một module.
4. Viết một decorator `@debug_calls` sử dụng `inspect` để in thông tin khi một hàm được gọi.

## Tổng kết
Module `inspect` là công cụ mạnh mẽ trong Python để thực hiện lập trình phản xạ. Nó giúp ta hiểu rõ hơn về cấu trúc code, hỗ trợ gỡ lỗi, tự động hóa tài liệu, và xây dựng các công cụ phát triển. Khi làm việc ở cấp độ nâng cao, việc sử dụng `inspect` sẽ mở rộng khả năng kiểm soát chương trình trong thời gian chạy.

---
> 📌 **Lưu ý**: Sử dụng `inspect` một cách thận trọng vì có thể làm giảm hiệu năng và tăng độ phức tạp. Chỉ dùng khi thực sự cần thiết như debug, framework, hoặc công cụ phân tích code.