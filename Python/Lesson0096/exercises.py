import asyncio

# Bài tập 1: Tải danh sách URL bất đồng bộ
# Viết hàm `download_all_urls(urls)` sử dụng aiohttp để tải tất cả URL trong danh sách
# Trả về danh sách độ dài nội dung của từng URL
async def download_all_urls(urls):
    # TODO: Viết code tại đây
    pass

# Bài tập 2: Đếm số từ trong nhiều file
# Viết hàm `count_words_in_files(filenames)` để đếm tổng số từ trong các file
# Sử dụng asyncio để đọc bất đồng bộ
async def count_words_in_files(filenames):
    # TODO: Viết code tại đây
    pass

# Bài tập 3: Mô phỏng máy in chia sẻ
# Viết một hệ thống in ấn với 1 hàng đợi và 2 máy in (worker)
# Mỗi tác vụ in mất 1-3 giây ngẫu nhiên
async def print_document(printer_id, document, queue):
    # TODO: Xử lý in tài liệu
    pass

async def shared_printer_system(documents):
    # TODO: Tạo hàng đợi và khởi động worker
    pass

# Bài tập 4: Xử lý kết quả khi từng tác vụ hoàn thành
# Viết hàm `process_as_completed(tasks)` sử dụng asyncio.as_completed()
# để xử lý kết quả ngay khi từng coroutine hoàn thành
async def process_as_completed(tasks):
    # TODO: Xử lý từng kết quả khi sẵn sàng
    pass

# Bài tập 5: Máy chủ xử lý yêu cầu đơn giản
# Viết một coroutine mô phỏng máy chủ xử lý yêu cầu
# Mỗi yêu cầu mất 0.5-2 giây để xử lý
async def handle_request(request_id):
    # TODO: Xử lý yêu cầu và in ra thông báo
    pass

async def server_simulation(request_count):
    # TODO: Tạo và chạy đồng thời các yêu cầu
    pass