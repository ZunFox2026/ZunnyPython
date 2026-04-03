# Bài học Python số 99 - Cấp độ Nâng cao

## Chủ đề: **Coroutine và Async/Await trong Python**

Trong bài học này, chúng ta sẽ tìm hiểu về **coroutine** và cơ chế **async/await** — một trong những tính năng mạnh mẽ nhất của Python để xử lý đồng thời (concurrency) mà không cần đa luồng. Đây là chủ đề nâng cao, phù hợp với các lập trình viên muốn tối ưu hiệu suất ứng dụng, đặc biệt khi làm việc với I/O như mạng, file, database.

### 🎯 Mục tiêu bài học
- Hiểu được khái niệm coroutine và sự khác biệt giữa hàm bình thường và hàm bất đồng bộ.
- Sử dụng được `async` và `await` để viết code bất đồng bộ.
- Áp dụng `asyncio` để thực thi nhiều tác vụ đồng thời một cách hiệu quả.
- Nhận biết được khi nào nên và không nên dùng async/await.

### 📚 Lý thuyết chi tiết

#### 1. Coroutine là gì?
Coroutine là một hàm có thể tạm dừng và tiếp tục thực thi. Khác với hàm bình thường chạy từ đầu đến cuối, coroutine có thể `yield` hoặc `await` để nhường quyền điều khiển cho các tác vụ khác.

Trong Python, ta định nghĩa một coroutine bằng từ khóa `async def`:
```python
async def my_coroutine():
    print("Bắt đầu")
    await asyncio.sleep(1)  # Tạm dừng 1 giây
    print("Kết thúc")
```

#### 2. async và await
- `async`: Dùng để khai báo một hàm là coroutine.
- `await`: Dùng để đợi một coroutine hoàn thành. Chỉ có thể dùng trong hàm `async`.

#### 3. Event Loop
`asyncio` sử dụng một **event loop** để quản lý và chạy các coroutine. Nó cho phép nhiều tác vụ chạy "đồng thời" bằng cách luân phiên thực thi khi có tác vụ nào đó bị block (ví dụ: chờ I/O).

#### 4. Khi nào nên dùng?
- Khi làm việc với mạng: HTTP request, WebSocket, API.
- Đọc/ghi file lớn.
- Truy vấn database (với driver hỗ trợ async).
- Không nên dùng cho tác vụ CPU-intensive (nên dùng multiprocessing).

### 🧪 Ví dụ minh họa
Xem nội dung trong `main.py` để chạy các ví dụ thực tế về:
- Tải trang web song song.
- Mô phỏng xử lý nhiều yêu cầu I/O cùng lúc.

### 📝 Bài tập thực hành
Thực hiện các bài tập trong `exercises.py`, sau đó kiểm tra lời giải tại `solutions.py`.

### 🔚 Tổng kết
Async/await là công cụ mạnh mẽ giúp tăng hiệu suất ứng dụng Python khi xử lý I/O-bound. Hiểu rõ cách hoạt động của event loop và coroutine sẽ giúp bạn viết code nhanh hơn, tiết kiệm tài nguyên. Tuy nhiên, cần tránh lạm dụng với các tác vụ xử lý CPU nặng.

> ⚠️ Lưu ý: Chỉ dùng `await` bên trong hàm `async`. Dùng `asyncio.run()` để chạy coroutine ở mức cao nhất.
