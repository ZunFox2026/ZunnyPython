# Bài học Python nâng cao số 60: Lập trình phản xạ (Reflection) và sử dụng `inspect` module

Trong bài học này, chúng ta sẽ tìm hiểu về một chủ đề nâng cao trong Python: **lập trình phản xạ (reflection)** và cách sử dụng module `inspect` để khám phá, phân tích và thao tác với mã nguồn tại thời điểm chạy. Đây là kỹ năng quan trọng trong phát triển framework, công cụ debug, tự động hóa test, hoặc xây dựng các hệ thống plugin.

## Mục tiêu bài học

- Hiểu khái niệm lập trình phản xạ (reflection) trong Python.
- Biết cách sử dụng module `inspect` để lấy thông tin về các đối tượng: hàm, lớp, phương thức, tham số, stack...
- Áp dụng `inspect` để xây dựng các công cụ phân tích mã nguồn động.
- Nắm được các tình huống thực tế sử dụng reflection trong thực tế.

## Lý thuyết chi tiết

### 1. Lập trình phản xạ (Reflection) là gì?

Lập trình phản xạ là khả năng của một chương trình để tự kiểm tra, phân tích và thay đổi cấu trúc hoặc hành vi của chính nó trong lúc chạy. Trong Python, mọi thứ đều là đối tượng, do đó bạn có thể:

- Kiểm tra kiểu của một đối tượng với `type()`.
- Liệt kê các thuộc tính và phương thức với `dir()`.
- Kiểm tra xem một đối tượng có thuộc tính nào đó không với `hasattr()`.
- Lấy giá trị thuộc tính với `getattr()`.
- Thiết lập giá trị thuộc tính với `setattr()`.

Ví dụ:

```python
class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Xin chào, tôi là {self.name}"

p = Person("Anh")

print(type(p))            # <class '__main__.Person'>
print(dir(p))             # ['name', 'greet', ...]
print(hasattr(p, 'age'))  # False
print(getattr(p, 'name')) # Anh
```

### 2. Module `inspect`

Module `inspect` cung cấp các hàm mạnh mẽ để thu thập thông tin chi tiết về các đối tượng trong Python như hàm, lớp, stack frame, v.v.

Một số hàm quan trọng:

- `inspect.getmembers(obj)`: Trả về danh sách các cặp (tên, giá trị) của tất cả thành viên trong đối tượng.
- `inspect.isfunction(obj)`, `inspect.isclass(obj)`: Kiểm tra loại đối tượng.
- `inspect.signature(func)`: Lấy chữ ký của hàm (tham số, kiểu, giá trị mặc định).
- `inspect.getsource(obj)`: Lấy mã nguồn của đối tượng (nếu có).
- `inspect.stack()`: Lấy thông tin về các frame trong stack gọi hàm.

Ví dụ:

```python
import inspect

def hello(name, age=20):
    return f"Xin chào {name}, bạn {age} tuổi."

# Lấy chữ ký hàm
sig = inspect.signature(hello)
print(sig)  # (name, age=20)

for param in sig.parameters.values():
    print(param.name, param.default)
```

## Ví dụ minh họa

### Ví dụ 1: Tự động tạo tài liệu (documentation) cho các hàm trong một module

Chúng ta sẽ viết một công cụ nhỏ để in ra mô tả của tất cả các hàm trong một module, bao gồm tên, tham số, giá trị mặc định và docstring.

### Ví dụ 2: Ghi log tự động tên hàm và tham số khi gọi

Sử dụng `inspect.stack()` để xác định tên hàm gọi và tham số, rất hữu ích trong debug.

### Ví dụ 3: Kiểm tra và in mã nguồn của một lớp

Dùng `inspect.getsource()` để in ra mã nguồn của một lớp, giúp kiểm tra nhanh mã mà không cần mở file.

## Bài tập thực hành

1. Viết hàm `list_functions(module)` nhận một module và in ra danh sách tất cả các hàm trong đó cùng với docstring.
2. Viết một decorator `@log_call` sử dụng `inspect` để in ra tên hàm và các tham số khi được gọi.
3. Viết hàm `analyze_class(cls)` in ra tất cả các phương thức và thuộc tính của một lớp, bao gồm kiểu và giá trị mặc định.
4. Viết hàm `find_functions_with_defaults(module)` trả về danh sách các hàm có tham số có giá trị mặc định.
5. Viết hàm `print_caller_info()` in ra tên hàm gọi nó, tên file và số dòng.

## Tổng kết

Lập trình phản xạ và module `inspect` mang lại sức mạnh lớn để viết các chương trình thông minh, tự động phân tích và tương tác với mã nguồn. Tuy nhiên, cần sử dụng cẩn trọng vì có thể làm mã khó đọc, khó bảo trì nếu lạm dụng.

Các ứng dụng thực tế:
- Framework như Flask, Django dùng reflection để ánh xạ route.
- Công cụ test tự động phát hiện test case.
- Debuggers và IDEs hiển thị thông tin chi tiết về mã.
- Plugin systems tự động tải và gọi hàm từ module.

Hãy luyện tập kỹ để làm chủ kỹ năng này!