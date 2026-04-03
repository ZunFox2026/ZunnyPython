# Bài học Python số 68: Lập trình phản xạ (Reflection) và sử dụng `inspect` module

## Mục tiêu bài học
- Hiểu được khái niệm lập trình phản xạ (reflection) trong Python.
- Biết cách sử dụng module `inspect` để truy vấn thông tin về các đối tượng, hàm, lớp, và stack.
- Áp dụng phản xạ để xây dựng các công cụ gỡ lỗi, kiểm thử tự động, hoặc framework linh hoạt.
- Nâng cao kỹ năng lập trình Python ở cấp độ cao thông qua ví dụ thực tế.

## Lý thuyết chi tiết

### 1. Lập trình phản xạ là gì?
Lập trình phản xạ (Reflection) là khả năng của một chương trình trong việc kiểm tra, thay đổi cấu trúc, hành vi của chính nó trong lúc chạy (runtime). Python hỗ trợ phản xạ rất mạnh mẽ nhờ vào bản chất "everything is an object".

### 2. Module `inspect`
Module `inspect` cung cấp các hàm hữu ích để thu thập thông tin về các đối tượng Python như: hàm, lớp, phương thức, module, stack frame, v.v.

Một số hàm phổ biến:

- `inspect.getmembers(obj)`: Trả về danh sách các thành viên (thuộc tính, phương thức) của đối tượng.
- `inspect.isfunction(obj)`, `inspect.isclass(obj)`: Kiểm tra loại đối tượng.
- `inspect.getsource(obj)`: Lấy mã nguồn của đối tượng (nếu có).
- `inspect.signature(obj)`: Lấy thông tin về tham số của hàm.
- `inspect.stack()`: Lấy thông tin về các frame trong stack gọi hàm.

### 3. Ứng dụng thực tế
- Ghi log tự động tên hàm đang chạy.
- Tạo framework kiểm thử tự động phát hiện các hàm test.
- Xây dựng decorator thông minh.
- Debug tự động in tham số đầu vào của hàm.

## Ví dụ minh họa

Dưới đây là 3 ví dụ minh họa cách sử dụng `inspect` để:
1. In tên và tham số của hàm đang gọi.
2. Liệt kê tất cả các hàm trong một module.
3. Tự động phát hiện và chạy các hàm test.

## Bài tập thực hành

1. Viết hàm in ra tên các tham số và giá trị của chúng trong hàm đang gọi.
2. Viết hàm kiểm tra và in ra tất cả các lớp trong một module.
3. Tạo một decorator ghi log tên hàm và thời gian thực thi.
4. Viết hàm liệt kê tất cả các phương thức public của một lớp.
5. Tự động tìm và in tên các hàm bắt đầu bằng 'test_' trong module hiện tại.

## Tổng kết

Lập trình phản xạ và module `inspect` là công cụ mạnh mẽ giúp Python trở thành ngôn ngữ linh hoạt, phù hợp để xây dựng các framework, công cụ kiểm thử, debug tự động. Việc hiểu và sử dụng thành thạo `inspect` sẽ mở rộng khả năng của lập trình viên trong việc phân tích và thao tác với mã nguồn ở cấp độ runtime.

Tuy nhiên, cần sử dụng phản xạ một cách cẩn trọng vì nó có thể làm giảm hiệu năng và làm mã nguồn khó đọc hơn nếu lạm dụng.

Bài học này đã trang bị cho bạn kiến thức nâng cao để khai thác sức mạnh ẩn sâu trong Python.
