import asyncio
import aiohttp

# Bài tập 1: Viết hàm đếm ngược bất đồng bộ
async def countdown(n):
    for i in range(n, -1, -1):
        print(i)
        await asyncio.sleep(0.5)  # Chờ 0.5 giây

# Bài tập 2: Mô phỏng nấu ăn bất đồng bộ
async def wash_vegetables():
    await asyncio.sleep(2)
    print("Đã rửa rau")

async def chop_onions():
    await asyncio.sleep(1)
    print("Đã cắt hành")

async def cook_soup():
    await asyncio.sleep(3)
    print("Đã nấu xong súp")

async def cook_meal():
    # Chạy song song 3 tác vụ
    await asyncio.gather(
        wash_vegetables(),
        chop_onions(),
        cook_soup()
    )

# Bài tập 3: Tải và in độ dài nội dung 3 URL
async def fetch_and_print_length():
    urls = [
        "http://httpbin.org/html",
        "http://httpbin.org/json",
        "http://httpbin.org/uuid"
    ]
    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in urls:
            async def fetch_one(url):
                async with session.get(url) as response:
                    text = await response.text()
                    print(f"{url}: {len(text)} ký tự")
            tasks.append(fetch_one(url))
        await asyncio.gather(*tasks)

# Bài tập 4: Đọc nhiều tệp bất đồng bộ
async def read_file(filename):
    loop = asyncio.get_event_loop()
    try:
        # Đọc tệp trong executor để không chặn event loop
        content = await loop.run_in_executor(None, lambda: open(filename, 'r').read())
        print(f"Đọc {filename}: {len(content)} ký tự")
        return content
    except FileNotFoundError:
        print(f"Không tìm thấy: {filename}")
        return None

async def read_files_async(filenames):
    await asyncio.gather(*[read_file(f) for f in filenames])

# Bài tập 5: Tải URL với timeout
async def fetch_with_timeout(url, timeout):
    async with aiohttp.ClientSession() as session:
        try:
            async with asyncio.timeout(timeout):  # Sử dụng asyncio.timeout (từ Python 3.11+)
                async with session.get(url) as response:
                    text = await response.text()
                    print(f"Tải thành công {url}, độ dài: {len(text)}")
        except TimeoutError:
            print(f"Timeout khi tải {url}")

# Hàm main để kiểm tra bài tập
async def main():
    print("=== Bài 1: Đếm ngược ===")
    await countdown(3)

    print("\n=== Bài 2: Nấu ăn ===")
    await cook_meal()

    print("\n=== Bài 3: Tải URL ===")
    await fetch_and_print_length()

    print("\n=== Bài 4: Đọc tệp ===")
    # Tạo tệp mẫu
    for i in range(1, 4):
        with open(f"test_file{i}.txt", "w") as f:
            f.write(f"Nội dung tệp {i} " * 50)
    await read_files_async(["test_file1.txt", "test_file2.txt", "test_file3.txt"])

    print("\n=== Bài 5: Tải với timeout ===")
    await fetch_with_timeout("http://httpbin.org/delay/2", 3)  # Thành công
    await fetch_with_timeout("http://httpbin.org/delay/5", 3)  # Timeout

if __name__ == "__main__":
    asyncio.run(main())