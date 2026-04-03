# Bài học Python nâng cao số 59: Lập trình phản xạ (Reflection) và sử dụng `inspect` module

## Mục tiêu bài học
- Hiểu được khái niệm lập trình phản xạ (reflection) trong Python.
- Sử dụng module `inspect` để truy xuất thông tin về các đối tượng, hàm, lớp, phương thức tại thời điểm chạy.
- Ứng dụng `inspect` để ghi log tự động, debug, xây dựng framework hoặc công cụ kiểm thử.
- Nâng cao khả năng phân tích và thao tác với mã nguồn một cách linh hoạt.

## Lý thuyết chi tiết

### 1. Lập trình phản xạ (Reflection) là gì?
Lập trình phản xạ là khả năng của một chương trình có thể kiểm tra, thay đổi cấu trúc hoặc hành vi của chính nó trong lúc chạy. Python hỗ trợ rất mạnh mẽ tính năng này.

Trong Python, bạn có thể:
- Kiểm tra kiểu dữ liệu bằng `type()` hoặc `isinstance()`.
- Lấy tên hàm, module, lớp bằng thuộc tính `__name__`.
- Kiểm tra các thuộc tính và phương thức bằng `dir()`.
- Gọi hàm động bằng `getattr()`, `setattr()`.

Tuy nhiên, để đi sâu hơn, Python cung cấp module `inspect` — một công cụ mạnh mẽ để phản xạ mã nguồn.

### 2. Module `inspect`
Module `inspect` cho phép truy xuất thông tin chi tiết về các đối tượng như:
- Hàm: tên, tham số, giá trị mặc định, dòng mã nguồn.
- Lớp: phương thức, thuộc tính, phân cấp kế thừa.
- Frame: ngữ cảnh thực thi, biến cục bộ, tên hàm đang gọi.

#### Một số hàm quan trọng:
- `inspect.getmembers(obj)`: Trả về danh sách các thành viên (thuộc tính, phương thức) của đối tượng.
- `inspect.isfunction(obj)`, `inspect.isclass(obj)`: Kiểm tra loại đối tượng.
- `inspect.signature(func)`: Lấy chữ ký hàm (tham số, kiểu, mặc định).
- `inspect.getsource(obj)`: Lấy mã nguồn của đối tượng.
- `inspect.stack()`: Lấy danh sách các frame gọi hàm (gọi ngược).

### 3. Ứng dụng thực tế
- Tạo decorator ghi log tự động tên hàm và tham số.
- Xây dựng framework web hoặc API tự động phát hiện route.
- Viết công cụ kiểm thử tự động phát hiện các hàm cần test.
- Gỡ lỗi (debug) nâng cao bằng cách in ra ngữ cảnh gọi hàm.

## Ví dụ minh họa

### Ví dụ 1: In thông tin chi tiết về một hàm
Sử dụng `inspect.signature` để phân tích tham số của hàm.

### Ví dụ 2: Ghi log tự động tên hàm và tham số sử dụng decorator
Tạo decorator thông minh dùng `inspect` để ghi log chi tiết.

### Ví dụ 3: Phân tích lớp và phương thức tại thời gian chạy
In ra tất cả các phương thức của một lớp, bao gồm tham số và mã nguồn (nếu có).

## Bài tập thực hành
1. Viết hàm `print_caller_info()` in ra tên hàm gọi nó và dòng lệnh gọi.
2. Viết decorator `@log_calls` ghi log khi một hàm được gọi, bao gồm tham số đầu vào.
3. Viết hàm `explore_module(module)` in ra tất cả hàm và lớp trong một module, cùng tham số của từng hàm.
4. Viết hàm `find_functions_with_kwargs(module)` tìm tất cả hàm trong module có tham số từ khóa (**kwargs).
5. Viết decorator `@validate_types` kiểm tra kiểu tham số đầu vào của hàm sử dụng `inspect`.

## Tổng kết
Lập trình phản xạ và module `inspect` là những công cụ mạnh mẽ trong tay lập trình viên Python nâng cao. Chúng giúp bạn viết mã linh hoạt, thông minh và có thể tự động hóa nhiều tác vụ như ghi log, kiểm thử, hoặc xây dựng các framework. Việc hiểu rõ `inspect` sẽ mở ra cánh cửa để bạn đọc và thao tác với mã nguồn một cách chủ động hơn bao giờ hết.

> **Lưu ý**: Dùng `inspect` một cách cẩn trọng, vì nó có thể làm giảm hiệu năng và tăng độ phức tạp. Chỉ dùng khi thực sự cần thiết như trong công cụ phát triển, framework hoặc debug.
