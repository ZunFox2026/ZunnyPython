# Bài học Python nâng cao số 67: Lập trình phản xạ (Reflection) và sử dụng `inspect`

Trong bài học này, chúng ta sẽ tìm hiểu về **lập trình phản xạ (reflection)** trong Python và cách sử dụng module `inspect` để khám phá, phân tích và thao tác với mã nguồn chương trình tại **thời gian chạy (runtime)**. Đây là một chủ đề nâng cao, rất hữu ích khi xây dựng các framework, công cụ kiểm thử, serializer, hoặc các hệ thống plugin.

## Mục tiêu bài học
- Hiểu được khái niệm lập trình phản xạ trong Python.
- Biết cách sử dụng module `inspect` để lấy thông tin về hàm, lớp, tham số, stack frame.
- Ứng dụng `inspect` vào các tình huống thực tế như ghi log tự động, validation tham số, xây dựng decorator linh hoạt.
- Thành thạo các hàm phổ biến: `inspect.getmembers()`, `inspect.signature()`, `inspect.stack()`.

## Lý thuyết chi tiết

### 1. Lập trình phản xạ là gì?
Lập trình phản xạ (reflection) là khả năng của một chương trình trong việc **tự quan sát và thay đổi cấu trúc, hành vi của chính nó** tại thời gian chạy. Trong Python, mọi thứ đều là object, và bạn có thể kiểm tra kiểu, thuộc tính, phương thức, tham số… thông qua các hàm built-in và module `inspect`.

### 2. Module `inspect`
Module `inspect` cung cấp nhiều công cụ mạnh mẽ để:
- Lấy danh sách thành viên của một đối tượng: `inspect.getmembers(obj)`
- Lấy chữ ký (signature) của hàm: `inspect.signature(func)`
- Kiểm tra stack frame hiện tại: `inspect.stack()`
- Lấy mã nguồn: `inspect.getsource(obj)`
- Kiểm tra xem một đối tượng có phải là hàm, lớp, method: `inspect.isfunction()`, `inspect.isclass()`...

### Ví dụ cơ bản
```python
import inspect

def greet(name, age=20):
    return f"Xin chào {name}, bạn {age} tuổi."

# Lấy chữ ký hàm
callable_sig = inspect.signature(greet)
for param in callable_sig.parameters.values():
    print(param.name, param.default)
```

## Ví dụ minh họa

### Ví dụ 1: Tự động ghi log tham số đầu vào của hàm
Viết một decorator sử dụng `inspect` để in ra các tham số được truyền vào hàm khi gọi.

### Ví dụ 2: Kiểm tra kiểu tham số tại runtime
Xây dựng một decorator `@validate_types` để kiểm tra kiểu dữ liệu của tham số dựa trên type hints.

### Ví dụ 3: Liệt kê tất cả phương thức và thuộc tính của một lớp
Sử dụng `inspect.getmembers()` để phân tích cấu trúc của một lớp tại runtime.

## Bài tập thực hành
1. Viết decorator `@debug_calls` ghi log tên hàm, tham số, và giá trị trả về.
2. Viết hàm `list_public_methods(cls)` liệt kê các phương thức công khai của một lớp.
3. Viết decorator `@require_kwargs` yêu cầu tất cả tham số phải được truyền dưới dạng keyword.
4. Viết hàm `get_caller_info()` trả về tên hàm gọi nó và tên file.
5. Viết decorator `@log_execution_time` kết hợp với `inspect` để ghi log thời gian thực thi và thông tin hàm.

## Tổng kết
- `inspect` là công cụ mạnh mẽ để thực hiện reflection trong Python.
- Có thể dùng `inspect` để xây dựng các decorator thông minh, công cụ debug, hoặc framework tự động hóa.
- Luôn cân nhắc hiệu năng và tính rõ ràng của mã nguồn khi dùng reflection.
- Đây là kỹ năng thiết yếu khi phát triển thư viện hoặc hệ thống lớn.

> ✅ Hãy thực hành kỹ các ví dụ và bài tập để làm chủ kỹ thuật này!
