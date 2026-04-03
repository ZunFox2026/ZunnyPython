# Bài học Python Nâng cao - Bài 46: Lập trình phản xạ (Reflection) và sử dụng `inspect` module

Trong bài học này, chúng ta sẽ tìm hiểu về **lập trình phản xạ (reflection)** trong Python và cách sử dụng module `inspect` — một công cụ mạnh mẽ giúp ta khám phá, phân tích và thao tác với mã nguồn trong thời gian thực. Đây là chủ đề nâng cao, rất hữu ích khi phát triển các framework, công cụ debug, hoặc hệ thống plugin.

## Mục tiêu bài học
- Hiểu khái niệm lập trình phản xạ (reflection) trong Python.
- Sử dụng được các hàm trong module `inspect` để lấy thông tin về đối tượng, hàm, lớp, và module.
- Ứng dụng `inspect` để xây dựng các công cụ phân tích mã nguồn, kiểm tra tham số hàm, hoặc ghi log thông minh.
- Biết cách sử dụng reflection một cách an toàn và hiệu quả.

## Lý thuyết chi tiết

### 1. Lập trình phản xạ (Reflection) là gì?
Lập trình phản xạ là khả năng của một chương trình trong việc tự khám phá và thao tác với cấu trúc của chính nó — như lớp, hàm, thuộc tính — trong lúc chạy. Python hỗ trợ reflection rất mạnh mẽ nhờ vào đặc điểm "mọi thứ đều là đối tượng".

Một số hàm built-in hỗ trợ reflection:
- `type(obj)`: lấy kiểu của đối tượng.
- `dir(obj)`: liệt kê các thuộc tính và phương thức của đối tượng.
- `hasattr(obj, attr)`: kiểm tra đối tượng có thuộc tính nào đó không.
- `getattr(obj, attr)`: lấy giá trị thuộc tính.
- `setattr(obj, attr, value)`: thiết lập giá trị thuộc tính.
- `callable(obj)`: kiểm tra đối tượng có thể gọi được không (hàm, phương thức...).

### 2. Module `inspect`
Module `inspect` cung cấp nhiều hàm tiện ích để lấy thông tin chi tiết về các đối tượng trong Python.

Một số hàm phổ biến:
- `inspect.getmembers(obj)`: trả về danh sách các thành viên (thuộc tính, phương thức) của đối tượng.
- `inspect.isfunction(obj)`, `inspect.ismethod(obj)`, `inspect.isclass(obj)`: kiểm tra loại đối tượng.
- `inspect.getsource(obj)`: lấy mã nguồn của đối tượng (nếu có).
- `inspect.signature(obj)`: lấy thông tin chữ ký hàm (tham số, kiểu, giá trị mặc định).

### 3. Ứng dụng thực tế
- Tự động ghi log tên hàm và tham số gọi.
- Xây dựng hệ thống plugin: tự động tìm và nạp các lớp con.
- Kiểm thử tự động: phân tích các hàm để kiểm tra tài liệu (docstring), tham số.
- Framework web hoặc ORM: ánh xạ các thuộc tính lớp thành cột cơ sở dữ liệu.

## Ví dụ minh họa
Xem file `main.py` để chạy các ví dụ.

## Bài tập thực hành
Xem file `exercises.py` và hoàn thành các bài tập. Gợi ý và lời giải có trong `solutions.py`.

## Tổng kết
Lập trình phản xạ và module `inspect` mở ra khả năng mạnh mẽ để viết mã linh hoạt, thông minh và tự động hóa. Tuy nhiên, cần sử dụng cẩn trọng vì có thể làm giảm hiệu năng và tính rõ ràng của mã nguồn. Khi sử dụng đúng cách, đây là công cụ không thể thiếu trong kho vũ khí của một lập trình viên Python chuyên nghiệp.
