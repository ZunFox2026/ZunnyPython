# Bài học 74: Lập trình phản xạ (Reflection) trong Python

## Mục tiêu bài học
- Hiểu được khái niệm lập trình phản xạ (Reflection) và vai trò của nó trong Python.
- Biết cách sử dụng các hàm built-in như `getattr`, `setattr`, `hasattr`, `delattr`, và `inspect` để thao tác với đối tượng, thuộc tính, phương thức một cách động.
- Áp dụng phản xạ để xây dựng các ứng dụng linh hoạt như framework, plugin hệ thống, hoặc serialize object.
- Nắm vững các tình huống thực tế sử dụng reflection một cách an toàn và hiệu quả.

## Lý thuyết chi tiết

Lập trình phản xạ (Reflection) là khả năng của một chương trình có thể tự kiểm tra, thao tác hoặc sửa đổi cấu trúc và hành vi của chính nó trong lúc chạy (runtime). Trong Python, điều này được hỗ trợ rất mạnh mẽ nhờ vào bản chất động (dynamic) của ngôn ngữ.

### Các hàm phản xạ quan trọng

- `hasattr(obj, name)`: Kiểm tra xem đối tượng có thuộc tính nào đó không.
- `getattr(obj, name[, default])`: Lấy giá trị của thuộc tính.
- `setattr(obj, name, value)`: Thiết lập giá trị cho thuộc tính.
- `delattr(obj, name)`: Xóa thuộc tính.

Ngoài ra, module `inspect` cho phép ta kiểm tra sâu hơn về hàm, lớp, tham số, stack call, v.v.

### Ví dụ cơ bản
```python
class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Xin chào, tôi là {self.name}"

p = Person("Anh")

# Kiểm tra thuộc tính
does_have_name = hasattr(p, 'name')  # True

# Lấy giá trị thuộc tính
got_name = getattr(p, 'name')  # 'Anh'

greet_func = getattr(p, 'greet')  # Lấy phương thức
greeting = greet_func()  # Gọi phương thức
```

### Module inspect

Module `inspect` hỗ trợ kiểm tra các thành phần mã nguồn:
- `inspect.getmembers(obj)`: Lấy danh sách tất cả thành viên của đối tượng.
- `inspect.isfunction(obj)`, `inspect.ismethod(obj)`: Kiểm tra loại.
- `inspect.signature(func)`: Lấy thông tin tham số của hàm.

## Ví dụ minh họa

### Ví dụ 1: Tự động in tất cả thuộc tính và phương thức của một đối tượng
### Ví dụ 2: Xây dựng hàm gọi phương thức theo tên từ chuỗi
### Ví dụ 3: Serialize một đối tượng thành từ điển một cách động

## Bài tập thực hành
1. Viết hàm kiểm tra và gọi một phương thức nếu tồn tại.
2. Tự động tạo đối tượng từ tên lớp (chuỗi).
3. Xây dựng hàm sao chép (deep copy) một cách thủ công dùng reflection.
4. In ra tất cả các phương thức public của một đối tượng.
5. Xây dựng một decorator ghi log tất cả tham số đầu vào của hàm bằng inspect.

## Tổng kết
Lập trình phản xạ là công cụ mạnh mẽ giúp Python trở nên linh hoạt, đặc biệt trong việc xây dựng framework, công cụ debug, hệ thống plugin, hoặc serialize dữ liệu. Tuy nhiên, cần sử dụng cẩn trọng để tránh lạm dụng, gây khó hiểu hoặc lỗi runtime. Nắm vững `getattr`, `setattr`, `hasattr`, và `inspect` sẽ mở ra nhiều khả năng nâng cao trong phát triển Python.
