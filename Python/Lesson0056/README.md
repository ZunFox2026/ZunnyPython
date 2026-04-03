# Bài học Python Nâng cao số 56: Lập trình phản xạ (Reflection) với `inspect` và `getattr/setattr` trong Python

Trong bài học này, chúng ta sẽ tìm hiểu về **lập trình phản xạ (reflection)** — một kỹ thuật nâng cao trong Python cho phép chương trình tự kiểm tra, phân tích và thay đổi cấu trúc hoặc hành vi của chính nó trong lúc chạy (runtime). Đây là một chủ đề quan trọng trong phát triển framework, thư viện, debug tool và những hệ thống đòi hỏi tính linh hoạt cao.

Chúng ta sẽ tập trung vào hai công cụ chính:

- `getattr`, `setattr`, `hasattr`, `delattr`
- Module `inspect` để truy xuất thông tin về hàm, lớp, tham số, stack...

---

## 1. Mục tiêu bài học

Sau bài học này, học viên sẽ có khả năng:

- Hiểu được khái niệm lập trình phản xạ trong Python.
- Sử dụng `getattr`, `setattr`, `hasattr` để truy cập thuộc tính một cách linh hoạt.
- Khai thác module `inspect` để lấy thông tin về hàm, lớp, tham số, và stack call.
- Ứng dụng phản xạ để xây dựng các công cụ tự động như serializer, validator, hoặc debug helper.
- Giải quyết các tình huống thực tế cần kiểm tra hoặc thay đổi đối tượng tại runtime.

---

## 2. Lý thuyết chi tiết

### 2.1. Truy cập thuộc tính động với `getattr`, `setattr`, `hasattr`

Thay vì truy cập thuộc tính theo cách truyền thống (`obj.name`), bạn có thể dùng chuỗi để đọc/ghi thuộc tính:

- `getattr(obj, 'attr_name', default)` — lấy giá trị thuộc tính.
- `setattr(obj, 'attr_name', value)` — gán giá trị cho thuộc tính.
- `hasattr(obj, 'attr_name')` — kiểm tra sự tồn tại của thuộc tính.

**Ví dụ:**

```python
class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

user = User("An", 25)
print(getattr(user, 'name'))  # 'An'
setattr(user, 'age', 26)
print(user.age)  # 26
```

### 2.2. Module `inspect`: Khám phá cấu trúc chương trình

Module `inspect` cho phép bạn kiểm tra mã nguồn, tham số hàm, lớp, và thậm chí cả stack gọi hàm.

Một số hàm phổ biến:

- `inspect.getmembers(obj)` — trả về danh sách (tên, giá trị) của tất cả thành viên.
- `inspect.isfunction(obj)` — kiểm tra có phải hàm.
- `inspect.signature(func)` — lấy thông tin về tham số của hàm.
- `inspect.stack()` — xem lịch sử gọi hàm.

**Ví dụ:**

```python
import inspect

def greet(name, greeting="Hello"):
    pass

sig = inspect.signature(greet)
for param in sig.parameters.values():
    print(param.name, param.default)
# name <class 'inspect._empty'>
# greeting Hello
```

---

## 3. Ví dụ minh họa

### Ví dụ 1: Tự động in thông tin đối tượng (Object Debugger)

Tạo hàm `debug_obj(obj)` dùng `inspect.getmembers` để in tất cả thuộc tính và phương thức của một đối tượng.

### Ví dụ 2: Cấu hình động từ chuỗi

Từ danh sách cặp key-value dạng chuỗi, dùng `setattr` để gán thuộc tính cho đối tượng.

### Ví dụ 3: Kiểm tra tham số hàm tại runtime

Viết decorator `@validate_types` dùng `inspect.signature` để kiểm tra kiểu dữ liệu đầu vào của hàm.

---

## 4. Bài tập thực hành

1. Viết hàm `safe_getattr(obj, attr_path, default=None)` để truy cập thuộc tính lồng nhau, ví dụ: `safe_getattr(user, 'profile.email')`.
2. Viết hàm `list_public_methods(cls)` trả về danh sách tên các phương thức công khai của một lớp.
3. Viết decorator `@log_calls` dùng `inspect.stack()` để in ra tên hàm gọi và tên hàm bị gọi.
4. Tạo một hàm `create_object_from_dict(cls, data)` dùng `setattr` để gán thuộc tính từ dictionary.
5. Viết hàm `find_functions_with_annotation(module, annotation)` tìm tất cả hàm trong một module có chú thích (annotation) cụ thể.

---

## 5. Tổng kết

Lập trình phản xạ là một công cụ mạnh mẽ giúp Python trở nên linh hoạt và động. Khi sử dụng đúng cách, nó giúp:

- Tự động hóa việc xử lý đối tượng.
- Xây dựng các công cụ debug, serialization, validation.
- Tăng khả năng mở rộng cho hệ thống.

Tuy nhiên, cần lưu ý:

- Lạm dụng phản xạ có thể làm code khó đọc, khó debug.
- Ảnh hưởng hiệu năng nếu dùng quá nhiều tại runtime.
- Có nguy cơ bảo mật nếu dùng `eval` hoặc thay đổi đối tượng ngẫu nhiên.

Hãy dùng phản xạ một cách có chủ đích, rõ ràng và minh bạch.

---

> 📘 **Gợi ý học tiếp**: Tìm hiểu về `__getattr__`, `__getattribute__`, `__dict__`, và metaclass để kiểm soát hành vi truy cập thuộc tính sâu hơn.