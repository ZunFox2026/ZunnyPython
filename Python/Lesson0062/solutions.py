import asyncio
import aiohttp

# Bài tập 1: Kiểm tra trạng thái của nhiều URL
async def check_url_status(session, url):
    try:
        async with session.get(url) as response:
            return (url, response.status)
    except Exception as e:
        return (url, f"Lỗi: {e}")

async def check_multiple_urls(urls):
    async with aiohttp.ClientSession() as session:
        tasks = [check_url_status(session, url) for url in urls]
        results = await asyncio.gather(*tasks)
        return results

# Bài tập 2: Tạo async generator cho dãy Fibonacci
async def async_fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        await asyncio.sleep(0.05)  # Mô phỏng I/O
        yield a
        a, b = b, a + b

# Bài tập 3: Tải nội dung nhiều trang web song song
async def fetch_page_content(session, url):
    try:
        async with session.get(url) as response:
            text = await response.text()
            return (url, len(text))
    except Exception as e:
        return (url, f"Lỗi: {e}")

async def fetch_all_pages(urls):
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_page_content(session, url) for url in urls]
        results = await asyncio.gather(*tasks)
        for url, length in results:
            print(f"{url} - Độ dài nội dung: {length}")

# Bài tập 4: Đo thời gian thực thi bằng async context manager
class AsyncExecutionTimer:
    def __init__(self, task_name):
        self.task_name = task_name

    async def __aenter__(self):
        self.start_time = asyncio.get_event_loop().time()
        print(f"[Timer] Bắt đầu: {self.task_name}")
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        self.end_time = asyncio.get_event_loop().time()
        elapsed = self.end_time - self.start_time
        print(f"[Timer] {self.task_name} hoàn tất trong {elapsed:.2f} giây")

async def run_with_timer():
    async with AsyncExecutionTimer("Công việc mẫu"):
        await asyncio.sleep(1.5)

# Bài tập 5: Xử lý lỗi trong môi trường async
async def risky_task(task_id):
    # 50% khả năng lỗi
    if task_id % 2 == 0:
        await asyncio.sleep(1)
        return f"Task {task_id} thành công"
    else:
        await asyncio.sleep(1)
        raise Exception(f"Task {task_id} thất bại")

async def run_risky_tasks():
    tasks = [risky_task(i) for i in range(1, 6)]
    # Sử dụng return_exceptions=True để không dừng khi có lỗi
    results = await asyncio.gather(*tasks, return_exceptions=True)
    for result in results:
        if isinstance(result, Exception):
            print(f"[Lỗi] {result}")
        else:
            print(f"[Thành công] {result}")

# Hàm chạy tất cả bài tập để kiểm tra
async def run_all_solutions():
    print("=== Bài tập 1: Kiểm tra URL ===")
    urls = ['http://httpbin.org/status/200'] * 3
    results = await check_multiple_urls(urls)
    for r in results:
        print(r)

    print("\n=== Bài tập 2: Async Fibonacci ===")
    async for num in async_fibonacci(8):
        print(num, end=' ')
    print()

    print("\n=== Bài tập 3: Tải nhiều trang ===")
    test_urls = ['http://example.com'] * 3
    await fetch_all_pages(test_urls)

    print("\n=== Bài tập 4: Đo thời gian ===")
    await run_with_timer()

    print("\n=== Bài tập 5: Xử lý lỗi ===")
    await run_risky_tasks()

if __name__ == "__main__":
    asyncio.run(run_all_solutions())