# Bài học Python số 91: Xử lý đồng thời với Asyncio (Nâng cao)

## Mục tiêu bài học
- Hiểu rõ mô hình xử lý bất đồng bộ (asynchronous) trong Python.
- Nắm vững cách sử dụng `asyncio` để viết chương trình xử lý nhiều tác vụ đồng thời mà không cần đa luồng.
- Biết cách sử dụng `async`, `await`, `Task`, `gather`, và `as_completed` để tối ưu hiệu suất.
- Ứng dụng `asyncio` vào các tình huống thực tế như tải dữ liệu từ API, xử lý tệp tin, hoặc xử lý yêu cầu mạng.

## Lý thuyết chi tiết

Python cung cấp thư viện `asyncio` để hỗ trợ lập trình bất đồng bộ. Khác với đa luồng hay đa tiến trình, lập trình bất đồng bộ cho phép chương trình thực hiện nhiều nhiệm vụ mà không bị chặn bởi các thao tác I/O (như đọc ghi file, gọi API, truy cập mạng).

### Các khái niệm chính

- **`async def`**: Định nghĩa một hàm bất đồng bộ. Hàm này trả về một *coroutine object*.
- **`await`**: Dừng thực thi hàm bất đồng bộ tại điểm đó cho đến khi coroutine được `await` hoàn thành.
- **Event Loop**: Vòng lặp sự kiện quản lý và thực thi các coroutine.
- **`asyncio.create_task()`**: Bọc một coroutine thành Task để chạy đồng thời.
- **`asyncio.gather()`**: Chạy nhiều coroutine song song và chờ tất cả hoàn thành.
- **`asyncio.as_completed()`**: Trả về các coroutine theo thứ tự hoàn thành (không cần đợi tất cả).

### Ví dụ đơn giản

```python
import asyncio

async def say_hello(name, delay):
    await asyncio.sleep(delay)
    print(f'Xin chào, {name}! (sau {delay}s)')

# Chạy đồng thời
async def main():
    await asyncio.gather(
        say_hello('An', 2),
        say_hello('Bình', 1)
    )

# Bắt đầu vòng lặp sự kiện
asyncio.run(main())
```

## Ví dụ minh họa

### Ví dụ 1: Tải dữ liệu từ nhiều API đồng thời
Giả sử bạn cần lấy dữ liệu từ 3 API thời tiết khác nhau. Thay vì gọi tuần tự (tốn thời gian), bạn có thể dùng `asyncio` để gọi song song.

### Ví dụ 2: Xử lý nhiều tệp tin bất đồng bộ
Đọc nhiều tệp tin lớn cùng lúc mà không chặn luồng chính.

### Ví dụ 3: Xử lý yêu cầu mạng nhanh với `aiohttp`
Sử dụng `aiohttp` để gửi yêu cầu HTTP bất đồng bộ.

## Bài tập thực hành
1. Viết hàm `fetch_url(url)` để lấy nội dung từ một URL sử dụng `aiohttp`.
2. Viết hàm bất đồng bộ `read_files_async(file_list)` để đọc nội dung các tệp tin đồng thời.
3. Tạo một máy chủ đơn giản mô phỏng xử lý yêu cầu bất đồng bộ.
4. Dùng `as_completed` để in kết quả ngay khi một tác vụ hoàn thành.
5. Cải thiện hiệu suất bằng cách giới hạn số lượng tác vụ chạy song song.

## Tổng kết
`asyncio` là công cụ mạnh mẽ giúp tối ưu hiệu suất trong các ứng dụng I/O-bound như web scraping, API, xử lý tệp tin, và mạng. Khi sử dụng đúng cách, nó giúp chương trình nhanh hơn đáng kể so với cách tiếp cận tuần tự. Tuy nhiên, cần tránh dùng cho các tác vụ CPU-heavy.

> ⚠️ Lưu ý: Để chạy các ví dụ sử dụng `aiohttp`, bạn cần cài đặt: `pip install aiohttp`