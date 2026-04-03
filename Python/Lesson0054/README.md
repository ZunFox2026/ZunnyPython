# Bài học Python Nâng cao - Bài 54: Lập trình phản xạ (Reflection) trong Python

## Mục tiêu bài học
- Hiểu được khái niệm và ứng dụng của lập trình phản xạ (reflection) trong Python.
- Biết cách sử dụng các hàm `getattr`, `setattr`, `hasattr`, `delattr`, và `inspect` để thao tác với đối tượng và lớp một cách động.
- Áp dụng phản xạ để xây dựng các công cụ linh hoạt như serializer, factory, hoặc framework xử lý plugin.

## Lý thuyết chi tiết

### 1. Phản xạ là gì?
**Phản xạ (Reflection)** là khả năng của một chương trình trong việc tự quan sát và thay đổi cấu trúc, hành vi của chính nó trong lúc chạy. Trong Python, điều này đặc biệt mạnh mẽ nhờ vào bản chất động của ngôn ngữ.

Python cho phép:
- Kiểm tra thuộc tính và phương thức của đối tượng/lớp.
- Truy cập, thêm, sửa, xóa thuộc tính một cách động.
- Kiểm tra stack, gọi hàm, phân tích mã nguồn...

### 2. Các hàm phản xạ cơ bản

- `hasattr(obj, name)`: Kiểm tra đối tượng có thuộc tính nào không.
- `getattr(obj, name, default)`: Lấy giá trị thuộc tính.
- `setattr(obj, name, value)`: Gán giá trị cho thuộc tính.
- `delattr(obj, name)`: Xóa thuộc tính.

### 3. Module `inspect`
Module `inspect` giúp kiểm tra chi tiết về các đối tượng như:
- Hàm, phương thức, lớp, module.
- Tham số, tên, dòng mã, stack frame...

Một số hàm hữu ích:
- `inspect.getmembers(obj)`: Lấy danh sách các thành viên.
- `inspect.isfunction(obj)`, `inspect.ismethod(obj)`
- `inspect.signature(func)`: Lấy thông tin tham số hàm.

### 4. Ứng dụng thực tế
- Xây dựng serializer/deserializer tự động.
- Framework web hoặc ORM tự động ánh xạ.
- Plugin system: tự động phát hiện và nạp module.
- Ghi log hành vi động.

## Ví dụ minh họa

Dưới đây là 3 ví dụ thực tế minh họa cách dùng phản xạ:

### Ví dụ 1: Serializer đối tượng tự động
Chuyển đối tượng Python thành từ điển (dictionary) bằng cách duyệt thuộc tính.

### Ví dụ 2: Gọi phương thức theo tên (plugin pattern)
Tự động gọi phương thức dựa trên chuỗi tên, hữu ích cho CLI hoặc menu.

### Ví dụ 3: Kiểm tra và ghi log tham số hàm
Sử dụng `inspect.signature` để ghi log tham số đầu vào của một hàm.

## Bài tập thực hành
1. Viết hàm `safe_getattr` an toàn hơn `getattr`.
2. Viết hàm list_methods trả về tên các phương thức công khai của một đối tượng.
3. Tạo một plugin manager đơn giản.
4. Viết hàm kiểm tra một lớp có kế thừa từ một lớp khác không.
5. Viết hàm dump_object_info in ra chi tiết về một đối tượng.

## Tổng kết
Lập trình phản xạ là công cụ mạnh mẽ giúp Python trở nên rất linh hoạt. Khi sử dụng đúng cách, nó giúp viết code tái sử dụng cao, giảm lặp lại và tăng khả năng mở rộng. Tuy nhiên, cần cẩn trọng vì code phản xạ có thể khó đọc và debug nếu lạm dụng. Hãy dùng khi thật sự cần thiết và có kiểm thử đầy đủ.