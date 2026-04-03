# Bài học Python số 96: Xử lý đồng thời với asyncio - Lập trình bất đồng bộ nâng cao

## Mục tiêu bài học
- Hiểu được khái niệm và lợi ích của lập trình bất đồng bộ trong Python.
- Nắm vững cách sử dụng `async` và `await` để viết code bất đồng bộ.
- Biết cách sử dụng `asyncio` để quản lý nhiều tác vụ đồng thời.
- Áp dụng được kiến thức vào các tình huống thực tế như xử lý yêu cầu mạng, đọc file, hoặc xử lý tác vụ I/O tốn thời gian.

## Lý thuyết chi tiết

Lập trình bất đồng bộ (asynchronous programming) giúp chương trình thực hiện nhiều tác vụ cùng lúc mà không bị chặn bởi các thao tác chậm như đọc file, gửi HTTP request, hoặc chờ phản hồi từ cơ sở dữ liệu.

### 1. Khái niệm cơ bản
- `async def`: Định nghĩa một hàm bất đồng bộ.
- `await`: Dùng để đợi một coroutine hoàn tất. Chỉ dùng được bên trong hàm `async`.
- `asyncio`: Thư viện chuẩn của Python dùng để chạy và quản lý các coroutine.

### 2. Ví dụ đơn giản
```python
import asyncio

async def say_hello():
    print("Đang bắt đầu...")
    await asyncio.sleep(1)  # Giả lập tác vụ tốn thời gian
    print("Xin chào sau 1 giây!")

async def main():
    await say_hello()

# Chạy chương trình
asyncio.run(main())
```

### 3. Chạy nhiều tác vụ song song
Dùng `asyncio.gather()` để chạy nhiều coroutine đồng thời.

```python
await asyncio.gather(task1(), task2(), task3())
```

## Ví dụ minh họa

### Ví dụ 1: Tải nhiều trang web đồng thời
Sử dụng `aiohttp` để gửi yêu cầu HTTP bất đồng bộ.

### Ví dụ 2: Đọc nhiều file cùng lúc
Mô phỏng việc đọc file lớn mà không làm chậm chương trình.

### Ví dụ 3: Xử lý hàng đợi tác vụ bất đồng bộ
Tạo một hệ thống xử lý tác vụ theo hàng đợi với nhiều worker.

## Bài tập thực hành
1. Viết một coroutine tải nội dung từ danh sách URL.
2. Tạo một hàm bất đồng bộ đếm số từ trong nhiều file văn bản.
3. Viết chương trình mô phỏng máy in chia sẻ với nhiều người dùng.
4. Dùng `asyncio.as_completed()` để xử lý kết quả khi từng tác vụ hoàn thành.
5. Tạo một máy chủ đơn giản mô phỏng xử lý yêu cầu bất đồng bộ.

## Tổng kết
Bài học này giúp bạn làm chủ lập trình bất đồng bộ trong Python bằng `asyncio`. Đây là kỹ năng quan trọng khi phát triển ứng dụng hiệu năng cao, đặc biệt trong các hệ thống web, API, hoặc xử lý dữ liệu lớn. Lập trình bất đồng bộ giúp tối ưu tài nguyên và giảm thời gian chờ, từ đó cải thiện trải nghiệm người dùng.
