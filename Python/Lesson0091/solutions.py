import asyncio
import aiohttp

# Bài tập 1: Viết hàm fetch_url để lấy nội dung từ URL
async def fetch_url(url):
    # Tạo session để gửi yêu cầu
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            # Trả về nội dung văn bản
            return await response.text()

# Bài tập 2: Đọc nhiều tệp tin bất đồng bộ
async def read_files_async(file_list):
    # Hàm đọc tệp đồng bộ
    def read_sync(filename):
        with open(filename, 'r', encoding='utf-8') as f:
            return f.read()
    # Dùng asyncio.to_thread để không chặn event loop
    tasks = [asyncio.to_thread(read_sync, f) for f in file_list]
    # Chờ tất cả hoàn thành
    return await asyncio.gather(*tasks)

# Bài tập 3: Tạo máy chủ mô phỏng xử lý yêu cầu
async def handle_request(request_id, delay):
    print(f'Yêu cầu {request_id} bắt đầu, chờ {delay}s...')
    await asyncio.sleep(delay)
    print(f'Yêu cầu {request_id} hoàn thành!')
    return f'Kết quả_{request_id}'

async def process_requests(requests):
    # Tạo danh sách các coroutine
    tasks = [handle_request(req_id, delay) for req_id, delay in requests]
    # Chạy song song và chờ kết quả
    results = await asyncio.gather(*tasks)
    return results

# Bài tập 4: In kết quả khi hoàn thành (dùng as_completed)
async def task_with_result(name, delay):
    await asyncio.sleep(delay)
    return f'{name} hoàn thành sau {delay}s'

async def run_in_order_of_completion():
    tasks = [
        task_with_result('T1', 2),
        task_with_result('T2', 1),
        task_with_result('T3', 3)
    ]
    # Duyệt theo thứ tự hoàn thành
    for coro in asyncio.as_completed(tasks):
        result = await coro
        print(f'Kết quả: {result}')

# Bài tập 5: Giới hạn số lượng tác vụ chạy song song
async def limited_concurrent_tasks(tasks, limit):
    # Sử dụng semaphore để giới hạn số lượng tác vụ chạy đồng thời
    semaphore = asyncio.Semaphore(limit)
    
    async def run_with_limit(task):
        async with semaphore:
            return await task
    
    # Bọc các task với semaphore
    limited_tasks = [run_with_limit(task) for task in tasks]
    # Chạy tất cả
    return await asyncio.gather(*limited_tasks)

# Hàm kiểm thử các bài tập (không cần gọi trong exercises.py)
async def test_solutions():
    print('=== Kiểm thử Bài tập 1 (fetch_url) ===')
    content = await fetch_url('https://httpbin.org/json')
    print(f'Đã lấy dữ liệu từ API: {len(content)} ký tự\n')
    
    print('=== Kiểm thử Bài tập 2 (read_files_async) ===')
    # Tạo file mẫu
    sample_files = ['test1.txt', 'test2.txt']
    for i, f in enumerate(sample_files):
        with open(f, 'w') as fp:
            fp.write(f'Nội dung file {i+1}\n' * 50)
    contents = await read_files_async(sample_files)
    print(f'Đã đọc {len(contents)} file\n')
    
    print('=== Kiểm thử Bài tập 3 (process_requests) ===')
    requests = [('R1', 1), ('R2', 2), ('R3', 1.5)]
    results = await process_requests(requests)
    print('Kết quả:', results, '\n')
    
    print('=== Kiểm thử Bài tập 4 (as_completed) ===')
    await run_in_order_of_completion()
    
    print('\n=== Kiểm thử Bài tập 5 (giới hạn đồng thời) ===')
    # Tạo nhiều task mô phỏng
    long_tasks = [asyncio.sleep(1, result=f'T{i}') for i in range(5)]
    start = asyncio.get_event_loop().time()
    results = await limited_concurrent_tasks(long_tasks, limit=2)
    duration = asyncio.get_event_loop().time() - start
    print(f'Kết quả giới hạn: {results}')
    print(f'Thời gian thực hiện: {duration:.2f}s (nếu không giới hạn sẽ nhanh hơn, nhưng ở đây mô phỏng giới hạn tài nguyên)')

# Gỡ bỏ dòng comment dưới để kiểm thử
# asyncio.run(test_solutions())