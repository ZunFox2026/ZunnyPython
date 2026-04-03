import asyncio
import aiohttp
import time

# Ví dụ 1: Tải nhiều trang web đồng thời
async def fetch_url(session, url):
    print(f"Đang tải: {url}")
    async with session.get(url) as response:
        content = await response.text()
        print(f"Đã tải xong {url}, độ dài nội dung: {len(content)}")
        return len(content)

async def fetch_multiple_urls():
    urls = [
        "https://httpbin.org/delay/1",
        "https://httpbin.org/delay/2",
        "https://httpbin.org/json"
    ]
    async with aiohttp.ClientSession() as session:
        # Chạy đồng thời tất cả các yêu cầu
        results = await asyncio.gather(
            *[fetch_url(session, url) for url in urls]
        )
        print(f"Tổng độ dài nội dung: {sum(results)}")

# Ví dụ 2: Đọc nhiều file cùng lúc
async def read_file(filename):
    # Mô phỏng việc đọc file chậm
    await asyncio.sleep(1)
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
            word_count = len(content.split())
            print(f"{filename}: {word_count} từ")
            return word_count
    except FileNotFoundError:
        print(f"Không tìm thấy file: {filename}")
        return 0

async def read_multiple_files():
    filenames = [f"sample_{i}.txt" for i in range(1, 4)]
    # Tạo file mẫu nếu chưa có
    for i, name in enumerate(filenames, 1):
        with open(name, 'w', encoding='utf-8') as f:
            f.write(f"Đây là nội dung mẫu cho file số {i}. " * 50)
    
    # Đọc bất đồng bộ
    results = await asyncio.gather(*[read_file(f) for f in filenames])
    print(f"Tổng số từ trong tất cả file: {sum(results)}")

# Ví dụ 3: Xử lý hàng đợi tác vụ bất đồng bộ
async def worker(worker_id, queue):
    while True:
        # Lấy tác vụ từ hàng đợi
        task = await queue.get()
        if task is None:
            print(f"Worker {worker_id} ngừng hoạt động.")
            break
        
        print(f"Worker {worker_id} đang xử lý: {task}")
        await asyncio.sleep(2)  # Giả lập xử lý lâu
        print(f"Worker {worker_id} hoàn thành: {task}")
        
        # Đánh dấu tác vụ đã xong
        queue.task_done()

async def task_queue_demo():
    # Tạo hàng đợi
    queue = asyncio.Queue()

    # Thêm các tác vụ vào hàng đợi
    tasks = [f"Tác vụ {i}" for i in range(1, 6)]
    for task in tasks:
        await queue.put(task)
    
    # Tạo 3 worker
    workers = [asyncio.create_task(worker(i, queue)) for i in range(1, 4)]
    
    # Chờ tất cả tác vụ hoàn thành
    await queue.join()
    
    # Gửi tín hiệu dừng
    for _ in workers:
        await queue.put(None)
    
    # Chờ các worker kết thúc
    await asyncio.gather(*workers)
    print("Tất cả tác vụ đã được xử lý xong.")

# Chạy tất cả ví dụ
async def main():
    print("=== Ví dụ 1: Tải nhiều URL đồng thời ===")
    start = time.time()
    await fetch_multiple_urls()
    print(f"Thời gian thực hiện: {time.time() - start:.2f}s\n")

    print("=== Ví dụ 2: Đọc nhiều file đồng thời ===")
    start = time.time()
    await read_multiple_files()
    print(f"Thời gian thực hiện: {time.time() - start:.2f}s\n")

    print("=== Ví dụ 3: Xử lý hàng đợi bất đồng bộ ===")
    start = time.time()
    await task_queue_demo()
    print(f"Thời gian thực hiện: {time.time() - start:.2f}s")

if __name__ == "__main__":
    asyncio.run(main())