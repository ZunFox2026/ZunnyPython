# Bài học Python Nâng cao số 42: Lập trình phản xạ (Reflection) với `inspect` và `getattr`, `setattr`, `hasattr`

## Mục tiêu bài học
- Hiểu được khái niệm lập trình phản xạ (reflection) trong Python.
- Biết cách sử dụng các hàm `getattr`, `setattr`, `hasattr` để thao tác với thuộc tính đối tượng một cách linh hoạt.
- Sử dụng module `inspect` để khám phá thông tin về hàm, lớp, tham số và stack.
- Ứng dụng reflection vào các tình huống thực tế như tạo framework, serialize object, debug và tự động hóa.

## Lý thuyết chi tiết

### 1. Lập trình phản xạ là gì?
Lập trình phản xạ (reflection) là khả năng của một chương trình trong việc tự kiểm tra và thay đổi cấu trúc hoặc hành vi của chính nó trong lúc chạy. Python hỗ trợ reflection rất mạnh, cho phép:
- Kiểm tra thuộc tính và phương thức của một đối tượng.
- Gọi phương thức hoặc truy cập thuộc tính qua tên (dưới dạng chuỗi).
- Kiểm tra thông tin về hàm như tham số, kiểu trả về, giá trị mặc định.

### 2. Các hàm phản xạ cơ bản

- `getattr(obj, name, default)`: Lấy giá trị của thuộc tính `name` từ đối tượng `obj`. Nếu không tồn tại, trả về `default`.
- `setattr(obj, name, value)`: Thiết lập giá trị `value` cho thuộc tính `name` của `obj`.
- `hasattr(obj, name)`: Kiểm tra xem `obj` có thuộc tính `name` hay không.

```python
# Ví dụ
class Person:
    def __init__(self, name):
        self.name = name

p = Person("Anh")
print(getattr(p, "name"))  # Anh
setattr(p, "age", 25)
print(p.age)  # 25
print(hasattr(p, "age"))  # True
```

### 3. Module `inspect`
Module `inspect` cho phép kiểm tra sâu về mã nguồn: hàm, lớp, tham số, stack frame...

Một số hàm phổ biến:
- `inspect.getmembers(obj)`: Trả về danh sách các cặp (tên, giá trị) của mọi thuộc tính/phương thức.
- `inspect.isfunction(obj)`, `inspect.ismethod(obj)`: Kiểm tra loại.
- `inspect.signature(func)`: Lấy chữ ký hàm (tham số, giá trị mặc định...).

```python
import inspect

def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

sig = inspect.signature(greet)
for name, param in sig.parameters.items():
    print(name, param.default)  # in ra tên và giá trị mặc định
```

## Ví dụ minh họa

### Ví dụ 1: Tự động in tất cả thuộc tính của một đối tượng
Dùng `inspect.getmembers` để liệt kê và lọc ra các thuộc tính không phải là phương thức.

### Ví dụ 2: Gọi phương thức từ chuỗi tên
Dựa trên đầu vào người dùng, gọi phương thức tương ứng trong một lớp.

### Ví dụ 3: Debug tự động in thông tin hàm đang gọi
Dùng `inspect.stack()` để lấy thông tin về hàm gọi hiện tại.

## Bài tập thực hành
1. Viết hàm `print_object_info(obj)` in ra tất cả thuộc tính và giá trị của một đối tượng.
2. Viết một lớp `CommandRunner` có thể gọi phương thức qua tên từ người dùng.
3. Viết hàm `log_call()` in ra tên hàm và tham số khi được gọi, sử dụng `inspect`.
4. Tạo hàm `serialize_object(obj)` trả về dict chứa các thuộc tính dữ liệu của đối tượng.
5. Kiểm tra xem một phương thức có tham số bắt buộc hay không.

## Tổng kết
Lập trình phản xạ là công cụ mạnh mẽ giúp Python trở nên linh hoạt. Khi sử dụng đúng cách, nó hỗ trợ xây dựng các công cụ như serializer, framework, debuggers, và hệ thống plugin. Tuy nhiên, cần cẩn trọng vì làm giảm khả năng đọc mã và tiềm ẩn lỗi nếu không kiểm soát tốt. Luôn dùng reflection khi có lý do rõ ràng và ưu tiên tính minh bạch khi có thể.