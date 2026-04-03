# Bài học Python nâng cao số 78: Lập trình phản xạ (Reflection) và sử dụng `inspect`

Trong bài học này, chúng ta sẽ tìm hiểu về **lập trình phản xạ (reflection)** trong Python — một kỹ thuật nâng cao cho phép chương trình tự kiểm tra, phân tích và thậm chí thay đổi cấu trúc hoặc hành vi của chính nó trong lúc chạy. Đây là một chủ đề quan trọng trong phát triển framework, thư viện, công cụ debug, và các ứng dụng tự động hóa.

Chúng ta sẽ tập trung vào module `inspect` — một công cụ mạnh mẽ để khám phá các đối tượng Python như hàm, lớp, phương thức, stack frame, và hơn thế nữa.

---

## Mục tiêu bài học

Sau bài học này, học viên sẽ có thể:
- Hiểu khái niệm lập trình phản xạ trong Python.
- Sử dụng module `inspect` để lấy thông tin về hàm, lớp, phương thức, và stack.
- Phân tích tham số, docstring, và mã nguồn của các đối tượng.
- Ứng dụng `inspect` trong các tình huống thực tế như ghi log, tạo framework, hoặc kiểm thử tự động.

---

## Lý thuyết chi tiết

### 1. Lập trình phản xạ là gì?

Lập trình phản xạ (reflection) là khả năng của một chương trình để:
- Xem xét, phân tích cấu trúc của chính nó (các hàm, lớp, thuộc tính...).
- Gọi phương thức hoặc truy cập thuộc tính một cách động.
- Tạo hoặc thay đổi đối tượng trong lúc chạy.

Python hỗ trợ phản xạ mạnh mẽ nhờ vào đặc điểm là một ngôn ngữ động và mọi thứ trong Python đều là đối tượng.

### 2. Module `inspect`

Module `inspect` cung cấp nhiều hàm hữu ích để:
- Lấy thông tin về hàm, phương thức, lớp.
- Xem tham số, giá trị mặc định, kiểu dữ liệu (nếu có annotation).
- Đọc docstring và mã nguồn.
- Kiểm tra stack gọi hàm (call stack).

#### Một số hàm quan trọng:

- `inspect.getmembers(obj)`: Lấy danh sách các thành viên (thuộc tính, phương thức) của đối tượng.
- `inspect.isfunction(obj)`, `inspect.isclass(obj)`: Kiểm tra loại đối tượng.
- `inspect.signature(func)`: Lấy chữ ký của hàm (tham số, mặc định, annotation).
- `inspect.getsource(obj)`: Lấy mã nguồn của hàm hoặc lớp.
- `inspect.getdoc(obj)`: Lấy docstring.
- `inspect.stack()`: Lấy thông tin về stack gọi hàm.

### 3. Ví dụ đơn giản

```python
import inspect

def hello(name: str, age: int = 20):
    """Chào một người với tên và tuổi."""
    print(f"Xin chào {name}, bạn {age} tuổi.")

# Lấy chữ ký hàm
sig = inspect.signature(hello)
print(sig)  # (name: str, age: int = 20)

# Lấy docstring
print(inspect.getdoc(hello))

# Lấy mã nguồn
print(inspect.getsource(hello))
```

---

## Ví dụ minh họa

### Ví dụ 1: Kiểm tra và in thông tin về một lớp

Chúng ta sẽ tạo một lớp `Person` và sử dụng `inspect` để in ra tất cả các phương thức, thuộc tính, và docstring.

### Ví dụ 2: Trích xuất thông tin tham số hàm

Viết một hàm trích xuất chi tiết các tham số của một hàm bất kỳ: tên, kiểu dữ liệu, giá trị mặc định.

### Ví dụ 3: Ghi log tự động tên hàm và tham số gọi

Tạo một decorator sử dụng `inspect` để ghi log tên hàm và các tham số khi được gọi — hữu ích trong debug.

---

## Bài tập thực hành

1. Viết hàm `print_class_info(cls)` nhận một lớp và in ra tất cả các phương thức public cùng docstring của chúng.
2. Viết hàm `analyze_function_params(func)` để in chi tiết từng tham số của hàm (tên, có annotation không, có giá trị mặc định không).
3. Tạo decorator `@log_call` sử dụng `inspect` để in ra tên hàm, tham số đầu vào, và dòng mã gọi hàm.
4. Viết hàm `find_functions_in_module(module, min_params=2)` tìm tất cả các hàm trong một module có ít nhất `min_params` tham số.
5. Kiểm tra xem một phương thức có được gọi từ phương thức khác trong cùng lớp không, bằng cách kiểm tra stack.

**Gợi ý:** Dùng `inspect.stack()`, `inspect.getmembers()`, và `inspect.signature()`.

---

## Tổng kết

Lập trình phản xạ và module `inspect` là công cụ mạnh mẽ giúp ta viết mã linh hoạt, thông minh và tự động. Việc hiểu rõ cách sử dụng `inspect` sẽ giúp bạn:
- Phát triển các framework như Flask, Django (có dùng reflection để map route).
- Tạo công cụ kiểm thử, ghi log, hoặc phân tích mã nguồn.
- Viết decorator thông minh và hệ thống plugin.

Tuy nhiên, cần sử dụng phản xạ một cách cẩn trọng vì có thể làm mã khó đọc và giảm hiệu năng. Chỉ dùng khi thực sự cần thiết.

Hãy luyện tập các bài tập để thành thạo kỹ năng này!
