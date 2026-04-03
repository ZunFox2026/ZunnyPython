# Bài học Python nâng cao số 58: Lập trình phản xạ (Reflection) và sử dụng `inspect`

## Mục tiêu bài học
- Hiểu được khái niệm lập trình phản xạ (reflection) trong Python.
- Biết cách sử dụng module `inspect` để khám phá mã nguồn, hàm, lớp, tham số và stack.
- Ứng dụng `inspect` để ghi log tự động, kiểm tra lỗi, tạo tài liệu hoặc xây dựng framework.
- Nâng cao khả năng debug và thiết kế hệ thống linh hoạt.

## Lý thuyết chi tiết

Lập trình **phản xạ (reflection)** là khả năng của một chương trình trong việc khám phá và thay đổi cấu trúc, hành vi của chính nó trong lúc chạy. Python hỗ trợ phản xạ rất mạnh mẽ thông qua các hàm như `getattr()`, `hasattr()`, `type()`, `dir()` và đặc biệt là module `inspect`.

Module `inspect` cung cấp các công cụ để:
- Lấy thông tin về hàm, phương thức, lớp, module.
- Kiểm tra tham số, default value, signature.
- Đọc mã nguồn.
- Duyệt stack gọi hàm.

### Một số hàm quan trọng trong `inspect`:

- `inspect.getmembers(object)`: Trả về danh sách các thành viên (thuộc tính, phương thức) của đối tượng.
- `inspect.isfunction(obj)`, `inspect.isclass(obj)`: Kiểm tra loại đối tượng.
- `inspect.signature(func)`: Lấy chữ ký hàm (tham số, kiểu, default).
- `inspect.getsource(obj)`: Lấy mã nguồn của đối tượng.
- `inspect.stack()`: Lấy thông tin stack gọi hàm (gọi từ đâu, dòng nào, file nào).

### Ví dụ cơ bản:

```python
import inspect

def hello(name, age=20):
    pass

sig = inspect.signature(hello)
for param in sig.parameters.values():
    print(param.name, param.default)
```

## Ví dụ minh họa

Dưới đây là 3 ví dụ thực tế minh họa việc sử dụng `inspect`:

1. **Tự động ghi log tham số đầu vào của hàm**
2. **Tạo tài liệu API tự động từ các hàm trong module**
3. **Debug: Xác định hàm nào đã gọi một hàm cụ thể**

## Bài tập thực hành

1. Viết hàm `print_caller_info()` in ra thông tin về hàm gọi nó (tên, file, dòng).
2. Viết hàm `analyze_function(func)` in ra chi tiết về một hàm: tên, tham số, default.
3. Viết decorator `@log_call` ghi log tên hàm và tham số khi được gọi.
4. Viết hàm `find_functions_with_default(module)` tìm tất cả hàm trong một module có tham số với giá trị mặc định.
5. Viết hàm `get_class_hierarchy(cls)` in ra toàn bộ cha mẹ của một lớp (sử dụng `inspect.getmro()`).

## Tổng kết

`inspect` là một công cụ mạnh mẽ cho các lập trình viên Python nâng cao, đặc biệt hữu ích khi:
- Xây dựng framework (Flask, Django sử dụng nhiều reflection).
- Gỡ lỗi và ghi log chi tiết.
- Tạo tài liệu tự động.
- Viết các công cụ phân tích mã nguồn.

Hiểu và sử dụng thành thạo `inspect` giúp bạn viết code thông minh hơn, linh hoạt hơn và dễ bảo trì hơn.