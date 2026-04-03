import asyncio
import aiohttp
import random

# Bài tập 1: Tải danh sách URL bất đồng bộ
async def download_all_urls(urls):
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_single_url(session, url) for url in urls]
        results = await asyncio.gather(*tasks)
        return results

async def fetch_single_url(session, url):
    async with session.get(url) as response:
        content = await response.text()
        return len(content)

# Bài tập 2: Đếm số từ trong nhiều file
async def count_words_in_files(filenames):
    tasks = [count_words_in_one_file(filename) for filename in filenames]
    word_counts = await asyncio.gather(*tasks)
    return sum(word_counts)

async def count_words_in_one_file(filename):
    try:
        # Mô phỏng độ trễ I/O
        await asyncio.sleep(0.5)
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
            return len(content.split())
    except FileNotFoundError:
        print(f"Không tìm thấy file: {filename}")
        return 0

# Bài tập 3: Mô phỏng máy in chia sẻ
async def print_document(printer_id, document, queue):
    while True:
        # Lấy tài liệu từ hàng đợi
        doc = await queue.get()
        if doc is None:
            print(f"Máy in {printer_id} đã tắt.")
            break
        
        delay = random.uniform(1, 3)
        print(f"Máy in {printer_id} bắt đầu in: {doc} (thời gian: {delay:.1f}s)")
        await asyncio.sleep(delay)
        print(f"Máy in {printer_id} hoàn thành: {doc}")
        
        queue.task_done()

async def shared_printer_system(documents):
    queue = asyncio.Queue()
    
    # Thêm tất cả tài liệu vào hàng đợi
    for doc in documents:
        await queue.put(doc)
    
    # Tạo 2 máy in
    printers = [
        asyncio.create_task(print_document(1, None, queue)),
        asyncio.create_task(print_document(2, None, queue))
    ]
    
    # Chờ tất cả in xong
    await queue.join()
    
    # Dừng các máy in
    for _ in range(2):
        await queue.put(None)
    
    await asyncio.gather(*printers)
    print("Tất cả tài liệu đã được in xong.")

# Bài tập 4: Xử lý kết quả khi từng tác vụ hoàn thành
async def process_as_completed(tasks):
    # Sử dụng as_completed để xử lý ngay khi có kết quả
    for coro in asyncio.as_completed(tasks):
        result = await coro
        print(f"Một tác vụ đã hoàn thành với kết quả: {result}")
    
# Hàm hỗ trợ cho bài 4
async def sample_task(name, delay):
    await asyncio.sleep(delay)
    return f"{name} hoàn thành sau {delay}s"

# Bài tập 5: Máy chủ xử lý yêu cầu đơn giản
async def handle_request(request_id):
    processing_time = random.uniform(0.5, 2.0)
    await asyncio.sleep(processing_time)
    print(f"Yêu cầu #{request_id} đã được xử lý trong {processing_time:.2f}s")
    return processing_time

async def server_simulation(request_count):
    # Tạo danh sách các tác vụ xử lý yêu cầu
    tasks = [handle_request(i) for i in range(1, request_count + 1)]
    
    # Chạy đồng thời tất cả yêu cầu
    results = await asyncio.gather(*tasks)
    
    total_time = sum(results)
    print(f"Tổng thời gian xử lý tất cả yêu cầu: {total_time:.2f}s")
    print(f"Thời gian trung bình mỗi yêu cầu: {total_time / len(results):.2f}s")

# Hàm main để kiểm thử lời giải (tùy chọn)
async def main():
    # Test bài 1
    print("=== Bài tập 1: Tải URL ===")
    urls = ["https://httpbin.org/delay/1", "https://httpbin.org/json"]
    results = await download_all_urls(urls)
    print(f"Kết quả: {results}\n")
    
    # Test bài 2 (cần có file sample_1.txt, sample_2.txt...)
    print("=== Bài tập 2: Đếm từ trong file ===")
    files = [f"sample_{i}.txt" for i in range(1, 4)]
    total = await count_words_in_files(files)
    print(f"Tổng số từ: {total}\n")
    
    # Test bài 3
    print("=== Bài tập 3: Máy in chia sẻ ===")
    documents = [f"Tài liệu_{i}" for i in range(1, 6)]
    await shared_printer_system(documents)
    print()
    
    # Test bài 4
    print("=== Bài tập 4: Xử lý khi hoàn thành ===")
    tasks = [sample_task(f"Tác vụ {i}", random.uniform(1, 3)) for i in range(1, 4)]
    await process_as_completed(tasks)
    print()
    
    # Test bài 5
    print("=== Bài tập 5: Mô phỏng máy chủ ===")
    await server_simulation(5)

# Bỏ comment dòng dưới để chạy test
# asyncio.run(main())