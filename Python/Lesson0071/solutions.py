import asyncio
import aiohttp

# Bài tập 1: Tải danh sách URL và in độ dài nội dung
async def download_and_print_length(urls):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in urls:
            # Tạo task cho mỗi URL
            task = fetch_single_url(session, url)
            tasks.append(task)
        # Chạy song song
        await asyncio.gather(*tasks)

async def fetch_single_url(session, url):
    try:
        async with session.get(url) as response:
            content = await response.text()
            print(f"{url} - Độ dài: {len(content)} ký tự")
    except Exception as e:
        print(f"Lỗi khi tải {url}: {e}")

# Bài tập 2: Chạy 5 tác vụ chậm song song
async def slow_counter(name, count):
    for i in range(1, count + 1):
        print(f"{name}: {i}")
        await asyncio.sleep(0.5)  # Chờ 0.5 giây

async def run_parallel_counters():
    tasks = []
    for i in range(5):
        task = slow_counter(f"Bộ đếm {i+1}", 3)
        tasks.append(task)
    await asyncio.gather(*tasks)

# Bài tập 3: In số chẵn và lẻ song song
async def print_even_numbers():
    for i in range(2, 11, 2):
        print(f"Chẵn: {i}")
        await asyncio.sleep(0.5)

async def print_odd_numbers():
    for i in range(1, 10, 2):
        print(f"Lẻ: {i}")
        await asyncio.sleep(0.5)

async def run_even_odd_parallel():
    # Chạy song song cả hai
    await asyncio.gather(
        print_even_numbers(),
        print_odd_numbers()
    )

# Bài tập 4: Máy khách kết nối đến máy chủ
async def client_connect_to_server():
    try:
        # Kết nối đến máy chủ
        reader, writer = await asyncio.open_connection('127.0.0.1', 8888)
        
        # Gửi dữ liệu
        message = "Xin chao"
        writer.write(message.encode())
        await writer.drain()  # Đảm bảo dữ liệu được gửi

        # Nhận phản hồi
        data = await reader.read(100)
        print(f"Phản hồi từ máy chủ: {data.decode()}")

        # Đóng kết nối
        writer.close()
        await writer.wait_closed()
    except ConnectionRefusedError:
        print("Không thể kết nối đến máy chủ. Vui lòng chạy máy chủ trước.")
    except Exception as e:
        print(f"Lỗi kết nối: {e}")

# Bài tập 5: Xử lý lỗi trong hàm async
async def risky_task(url):
    timeout = aiohttp.ClientTimeout(total=10)  # Đặt timeout
    try:
        async with aiohttp.ClientSession(timeout=timeout) as session:
            async with session.get(url) as response:
                if response.status == 200:
                    content = await response.text()
                    print(f"Tải thành công {url}, độ dài: {len(content)}")
                else:
                    print(f"Lỗi HTTP {response.status} khi truy cập {url}")
    except aiohttp.ClientConnectorError:
        print(f"Không thể kết nối đến {url} (lỗi mạng)")
    except aiohttp.ClientResponseError as e:
        print(f"Lỗi phản hồi HTTP: {e}")
    except asyncio.TimeoutError:
        print(f"Yêu cầu đến {url} bị timeout")
    except Exception as e:
        print(f"Lỗi không xác định khi truy cập {url}: {e}")