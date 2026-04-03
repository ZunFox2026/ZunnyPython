import asyncio
import aiofiles

# --- Bài tập 1 ---
async def fetch_data(name, delay):
    """
    Mô phỏng việc tải dữ liệu từ máy chủ
    """
    print(f"[Tải] Bắt đầu: {name} (sẽ mất {delay}s)")
    await asyncio.sleep(delay)
    print(f"[Tải] Hoàn thành: {name}")
    return f"{name}: dữ liệu hoàn chỉnh"

async def exercise_1():
    # Chạy 3 tác vụ đồng thời
    results = await asyncio.gather(
        fetch_data("Người dùng", 2),
        fetch_data("Sản phẩm", 1.5),
        fetch_data("Đơn hàng", 2.5)
    )
    print("Kết quả nhận được:")
    for res in results:
        print(res)

# --- Bài tập 2 ---
async def read_file_async(filename):
    """
    Đọc file bất đồng bộ
    """
    try:
        async with aiofiles.open(filename, 'r', encoding='utf-8') as f:
            content = await f.read()
            print(f"[Đọc] {filename} có {len(content)} ký tự")
            return content
    except Exception as e:
        print(f"[Lỗi] {filename}: {e}")
        return None

async def exercise_2():
    # Tạo file mẫu
    await aiofiles.open("doc1.txt", 'w', encoding='utf-8').write("Nội dung tài liệu 1\nDòng mới\n")
    await aiofiles.open("doc2.txt", 'w', encoding='utf-8').write("Tài liệu 2: ABC xyz\n")

    # Đọc bất đồng bộ
    results = await asyncio.gather(
        read_file_async("doc1.txt"),
        read_file_async("doc2.txt")
    )
    print("Đã đọc xong tất cả.")

# --- Bài tập 3 ---
async def printer_task(queue):
    """
    Nhiệm vụ in: lấy tài liệu từ queue và xử lý
    """
    while True:
        doc = await queue.get()
        if doc is None:
            break
        print(f"🖨️  Đang in: '{doc}' (2s)...")
        await asyncio.sleep(2)
        print(f"✅ Đã in xong: '{doc}'")
        queue.task_done()

async def user_submit(queue, user_name, doc_name):
    """
    Người dùng gửi tài liệu in
    """
    print(f"📤 {user_name} gửi: '{doc_name}'")
    await queue.put(doc_name)

async def exercise_3():
    queue = asyncio.Queue()

    # Tạo tác vụ in
    printer = asyncio.create_task(printer_task(queue))

    # Người dùng gửi
    await user_submit(queue, "Minh", "CV.pdf")
    await user_submit(queue, "Hoa", "Thư xin việc.docx")
    await user_submit(queue, "Dung", "Báo cáo tháng.xlsx")

    # Đợi in xong tất cả
    await queue.join()

    # Dừng printer
    await queue.put(None)
    await printer

# --- Bài tập 4 ---
async def print_numbers(task_id):
    """
    In số từ 1 đến 3 với độ trễ
    """
    for i in range(1, 4):
        print(f"[Task {task_id}] {i}")
        await asyncio.sleep(0.5)

async def exercise_4():
    # Chạy 5 task song song
    await asyncio.gather(*[print_numbers(i) for i in range(1, 6)])

# --- Bài tập 5 ---
async def slow_task():
    """
    Tác vụ chậm
    """
    await asyncio.sleep(3)
    return "Tác vụ hoàn thành!"

async def timeout_example():
    """
    Chạy tác vụ với giới hạn thời gian
    """
    try:
        result = await asyncio.wait_for(slow_task(), timeout=2.0)
        print(result)
    except asyncio.TimeoutError:
        print("❌ Lỗi: Thời gian thực thi quá lâu (timeout = 2s)")

# Chạy tất cả bài tập
async def main():
    print("=== Bài tập 1 ===")
    await exercise_1()
    
    print("\n=== Bài tập 2 ===")
    await exercise_2()
    
    print("\n=== Bài tập 3 ===")
    await exercise_3()
    
    print("\n=== Bài tập 4 ===")
    await exercise_4()
    
    print("\n=== Bài tập 5 ===")
    await timeout_example()

if __name__ == "__main__":
    asyncio.run(main())