# Bài học Python số 73: Lập trình phản xạ (Reflection) và sử dụng `inspect` để phân tích mã nguồn

## Mục tiêu bài học
- Hiểu được khái niệm lập trình phản xạ (reflection) trong Python.
- Biết cách sử dụng module `inspect` để phân tích các đối tượng, hàm, lớp, và mã nguồn đang chạy.
- Ứng dụng `inspect` trong thực tế để ghi log, gỡ lỗi, xây dựng framework.
- Nâng cao khả năng tự động hóa và mở rộng chương trình thông qua việc đọc và phân tích mã nguồn.

## Lý thuyết chi tiết

### 1. Lập trình phản xạ (Reflection) là gì?
Lập trình phản xạ là khả năng của một chương trình có thể tự kiểm tra, phân tích và thay đổi cấu trúc hoặc hành vi của chính nó trong lúc chạy. Python hỗ trợ rất mạnh tính năng này, cho phép truy cập vào các thành phần như:
- Tên hàm, tham số
- Thuộc tính và phương thức của lớp
- Mã nguồn gốc của hàm
- Thông tin về stack gọi hàm

### 2. Module `inspect`
Module `inspect` trong Python cung cấp nhiều hàm hữu ích để thu thập thông tin về các đối tượng như hàm, lớp, module, stack frame.

Một số hàm quan trọng:
- `inspect.getmembers(obj)`: Lấy danh sách tất cả thành viên của một đối tượng.
- `inspect.isfunction(obj)`, `inspect.isclass(obj)`: Kiểm tra loại đối tượng.
- `inspect.getsource(obj)`: Lấy mã nguồn của đối tượng (nếu có).
- `inspect.signature(obj)`: Lấy thông tin về tham số của hàm.
- `inspect.stack()`: Lấy thông tin về các frame trong stack gọi hàm.

### 3. Ví dụ nhỏ minh họa
```python
import inspect

def hello(name: str, age: int = 20) -> str:
    return f"Xin chào {name}, {age} tuổi."

# Lấy chữ ký hàm
sig = inspect.signature(hello)
print(sig)  # (name: str, age: int = 20) -> str
```

## Ví dụ minh họa
Dưới đây là 3 ví dụ hoàn chỉnh minh họa cách sử dụng `inspect` trong thực tế.

### Ví dụ 1: In ra danh sách tất cả hàm trong một module
### Ví dụ 2: Tự động ghi log khi gọi hàm với tham số
### Ví dụ 3: Kiểm tra và in mã nguồn của các phương thức trong một lớp

## Bài tập thực hành
1. Viết hàm `print_class_info(cls)` in ra tất cả phương thức và thuộc tính của một lớp.
2. Viết decorator `@log_call` ghi lại tên hàm, tham số và giá trị trả về khi gọi hàm.
3. Viết hàm `find_functions_in_file(module, line_threshold)` tìm các hàm có số dòng mã nguồn lớn hơn ngưỡng.
4. Viết hàm `who_called_me()` in ra tên hàm đã gọi hàm hiện tại.
5. Viết hàm `validate_types(func)` kiểm tra kiểu tham số đầu vào theo annotation.

## Tổng kết
Module `inspect` là công cụ mạnh mẽ trong Python giúp lập trình viên có thể "nhìn vào" mã nguồn và cấu trúc chương trình khi đang chạy. Việc sử dụng phản xạ hợp lý giúp xây dựng các công cụ gỡ lỗi, framework, hệ thống plugin, hoặc kiểm tra tự động. Tuy nhiên, cần thận trọng vì lạm dụng `inspect` có thể làm giảm hiệu năng và khó bảo trì. Hãy dùng nó khi thực sự cần thiết và có kiểm soát.