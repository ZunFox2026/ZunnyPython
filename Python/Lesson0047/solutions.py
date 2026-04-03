import asyncio
import time
import random

# Bài tập 1: Viết hàm tải xuống bất đồng bộ
async def tai_xuong(url):
    print(f"Đang tải xuống từ {url}...")
    await asyncio.sleep(1)  # Mô phỏng thời gian tải
    print(f"Tải xong: {url}")
    return f"File từ {url}"

# Bài tập 2: Tải 5 URL song song
async def tai_nhieu():
    urls = [f"https://example.com/file{i}.pdf" for i in range(1, 6)]
    print("=== Bài tập 2: Tải 5 file song song ===")
    start = time.time()
    
    # Chạy tất cả cùng lúc
    ket_qua = await asyncio.gather(*[tai_xuong(url) for url in urls])
    
    end = time.time()
    print(f"Tất cả tải xong trong {end - start:.2f} giây")
    return ket_qua

# Bài tập 3: Chạy 3 task với thời gian khác nhau
async def mot_giay():
    print("Task 1 giây bắt đầu")
    await asyncio.sleep(1)
    print("Task 1 giây xong")
    return "1s"

async def hai_giay():
    print("Task 2 giây bắt đầu")
    await asyncio.sleep(2)
    print("Task 2 giây xong")
    return "2s"

async def in_bat_dau():
    print("Bắt đầu!")
    return "Start"

async def chay_3_task():
    print("\n=== Bài tập 3: Chạy 3 task song song ===")
    start = time.time()
    
    # Tạo và chạy song song
    ket_qua = await asyncio.gather(mot_giay(), hai_giay(), in_bat_dau())
    
    end = time.time()
    print(f"Tổng thời gian thực thi: {end - start:.2f} giây")
    print("Kết quả:", ket_qua)

# Bài tập 4: Hàm chạy danh sách coroutine
async def thuc_hien_song_song(danh_sach_ham):
    """
    Chạy song song danh sách các coroutine
    """
    print("\n=== Bài tập 4: Chạy danh sách coroutine ===")
    start = time.time()
    ket_qua = await asyncio.gather(*danh_sach_ham)
    end = time.time()
    print(f"Hoàn thành trong {end - start:.2f} giây")
    return ket_qua

# Bài tập 5: Xử lý lỗi trong coroutine
async def co_the_loi(id):
    print(f"Coroutine {id} đang chạy...")
    await asyncio.sleep(0.5)
    if random.choice([True, False]):
        raise ValueError(f"Lỗi ngẫu nhiên ở task {id}")
    return f"Thành công: {id}"

async def chay_voi_xu_ly_loi():
    print("\n=== Bài tập 5: Xử lý lỗi trong coroutine ===")
    tasks = [co_the_loi(i) for i in range(5)]
    
    # Dùng return_exceptions=True để không bị crash
    ket_qua = await asyncio.gather(*tasks, return_exceptions=True)
    
    for i, kq in enumerate(ket_qua):
        if isinstance(kq, Exception):
            print(f"Task {i}: LỖI - {kq}")
        else:
            print(f"Task {i}: {kq}")

# Hàm chính để chạy tất cả bài tập
async def main():
    await tai_nhieu()
    await chay_3_task()
    
    # Bài tập 4: Dùng thử hàm thuc_hien_song_song
    danh_sach = [mot_giay(), hai_giay(), in_bat_dau()]
    await thuc_hien_song_song(danh_sach)
    
    await chay_voi_xu_ly_loi()

if __name__ == "__main__":
    asyncio.run(main())