import asyncio
import aiohttp
import time

# Ví dụ 1: Coroutine đơn giản với await
async def say_after(delay, message):
    """In một thông điệp sau một khoảng thời gian (giả lập công việc I/O)"""
    await asyncio.sleep(delay)  # Giả lập chờ I/O
    print(message)

async def example_1():
    print("=== Ví dụ 1: Chạy tuần tự vs song song ===")
    
    # Chạy tuần tự
    print("Chạy tuần tự...")
    start = time.time()
    await say_after(1, "Hello")
    await say_after(2, "World")
    print(f"Thời gian tuần tự: {time.time() - start:.2f}s")
    
    # Chạy song song
    print("Chạy song song...")
    start = time.time()
    await asyncio.gather(
        say_after(1, "Hello"),
        say_after(2, "World")
    )
    print(f"Thời gian song song: {time.time() - start:.2f}s")

# Ví dụ 2: Tải nội dung nhiều URL đồng thời
async def fetch_url(session, url):
    """Tải một URL và trả về độ dài nội dung"""
    async with session.get(url) as response:
        content = await response.text()
        print(f"{url}: {len(content)} ký tự")
        return len(content)

async def example_2():
    print("\n=== Ví dụ 2: Tải nhiều trang web song song ===")
    urls = [
        "https://httpbin.org/delay/1",
        "https://httpbin.org/delay/2",
        "https://httpbin.org/json"
    ]
    
    start = time.time()
    async with aiohttp.ClientSession() as session:
        # Chạy tất cả các tác vụ đồng thời
        results = await asyncio.gather(
            *[fetch_url(session, url) for url in urls]
        )
    print(f"Tổng ký tự nhận được: {sum(results)}")
    print(f"Thời gian tải: {time.time() - start:.2f}s")

# Ví dụ 3: Mô phỏng xử lý yêu cầu API
async def handle_request(request_id):
    """Mô phỏng xử lý một yêu cầu API tốn thời gian I/O"""
    print(f"Bắt đầu xử lý yêu cầu {request_id}")
    await asyncio.sleep(1.5)  # Giả lập thời gian xử lý
    print(f"Hoàn thành yêu cầu {request_id}")
    return f"Kết quả_{request_id}"

async def example_3():
    print("\n=== Ví dụ 3: Xử lý 5 yêu cầu API song song ===")
    start = time.time()
    
    # Tạo danh sách các coroutine
    tasks = [handle_request(i) for i in range(1, 6)]
    
    # Chạy song song và lấy kết quả
    results = await asyncio.gather(*tasks)
    print(f"Tất cả kết quả: {results}")
    print(f"Tổng thời gian xử lý: {time.time() - start:.2f}s")

# Hàm chính
async def main():
    await example_1()
    await example_2()
    await example_3()

# Chạy chương trình
if __name__ == "__main__":
    asyncio.run(main())