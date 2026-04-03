# Bài học 71: Xử lý bất đồng bộ với asyncio và async/await trong Python (Cấp độ nâng cao)

## Mục tiêu bài học
- Hiểu khái niệm về lập trình bất đồng bộ (asynchronous programming) và tại sao nó quan trọng.
- Nắm vững cách sử dụng `async`, `await`, và module `asyncio` trong Python.
- Biết cách viết các hàm bất đồng bộ để xử lý I/O hiệu quả hơn (như mạng, file, API...).
- Áp dụng `asyncio` vào các tình huống thực tế như tải nhiều trang web cùng lúc.
- Phân biệt được giữa lập trình đồng bộ và bất đồng bộ.

## Lý thuyết chi tiết

### 1. Lập trình bất đồng bộ là gì?

Lập trình bất đồng bộ cho phép chương trình thực hiện nhiều tác vụ cùng lúc mà không bị chặn (non-blocking). Điều này đặc biệt hữu ích khi làm việc với các hoạt động tốn thời gian như:
- Gọi API
- Đọc/ghi file
- Truy cập cơ sở dữ liệu
- Gửi yêu cầu mạng

Trong khi lập trình đồng bộ, mỗi tác vụ phải hoàn thành mới đến tác vụ tiếp theo, thì lập trình bất đồng bộ cho phép chương trình "chờ" một tác vụ (như tải trang) mà vẫn có thể làm việc khác.

### 2. Các khái niệm cơ bản

- **`async def`**: Định nghĩa một hàm bất đồng bộ. Hàm này trả về một *coroutine object*, không thực thi ngay.
- **`await`**: Dùng để chờ một coroutine hoàn thành. Chỉ dùng được bên trong hàm `async`.
- **`asyncio`**: Module chuẩn của Python để xử lý các hoạt động bất đồng bộ.
- **Event loop**: Vòng lặp sự kiện, là trái tim của `asyncio`. Nó quản lý và phân bổ thời gian thực thi cho các coroutine.

### 3. Ví dụ đơn giản

```python
import asyncio

async def say_hello():
    print("Bắt đầu...")
    await asyncio.sleep(1)  # Giả lập tác vụ chậm (như gọi API)
    print("Xin chào!")

# Cách chạy
asyncio.run(say_hello())
```

## Ví dụ minh họa

### Ví dụ 1: Tải nhiều trang web song song

Sử dụng `aiohttp` để gửi nhiều yêu cầu HTTP cùng lúc, tiết kiệm thời gian.

### Ví dụ 2: Xử lý nhiều tác vụ I/O

Mô phỏng việc đọc nhiều file lớn hoặc xử lý nhiều kết nối mạng.

### Ví dụ 3: Tạo máy chủ đơn giản với asyncio

Sử dụng `asyncio.start_server` để tạo máy chủ TCP xử lý nhiều client đồng thời.

## Bài tập thực hành

1. Viết hàm bất đồng bộ tải nội dung từ danh sách URL và in độ dài mỗi trang.
2. Tạo một hàm mô phỏng việc xử lý 5 tác vụ chậm (dùng `asyncio.sleep`) chạy song song.
3. Viết chương trình in số chẵn và số lẻ từ 1 đến 10, mỗi số cách nhau 0.5 giây, nhưng chạy song song.
4. Tạo một máy khách đơn giản kết nối đến máy chủ và nhận dữ liệu.
5. Xử lý lỗi trong môi trường bất đồng bộ bằng `try/except` trong hàm `async`.

## Hướng dẫn cài đặt thư viện phụ trợ

Một số ví dụ cần `aiohttp`:

```bash
pip install aiohttp
```

## Tổng kết

Bài học này giới thiệu cách sử dụng `asyncio` để viết chương trình Python hiệu quả hơn khi làm việc với các tác vụ I/O. Lập trình bất đồng bộ giúp tối ưu thời gian chờ, đặc biệt khi xử lý nhiều yêu cầu cùng lúc. Tuy nhiên, cần lưu ý:

- Chỉ dùng `await` trong hàm `async`.
- Tránh các tác vụ tính toán nặng trong coroutine vì chúng có thể làm chậm event loop.
- Sử dụng `asyncio.gather()` để chạy nhiều coroutine song song.
- Luôn xử lý lỗi trong môi trường bất đồng bộ.

Thành thạo `async/await` mở ra cánh cửa để xây dựng các ứng dụng hiệu suất cao như web crawler, API server, trò chơi mạng, v.v.