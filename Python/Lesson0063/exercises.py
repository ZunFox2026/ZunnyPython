import asyncio
import aiohttp

# Bài tập 1: Viết hàm đếm ngược bất đồng bộ
def countdown(n):
    # TODO: In số từ n về 0, mỗi số cách nhau 0.5 giây
    pass

# Bài tập 2: Mô phỏng nấu ăn bất đồng bộ
def wash_vegetables():
    # TODO: Chờ 2 giây rồi in "Đã rửa rau"
    pass

def chop_onions():
    # TODO: Chờ 1 giây rồi in "Đã cắt hành"
    pass

def cook_soup():
    # TODO: Chờ 3 giây rồi in "Đã nấu xong súp"
    pass

async def cook_meal():
    # TODO: Chạy cả 3 tác vụ song song
    pass

# Bài tập 3: Tải và in độ dài nội dung 3 URL
async def fetch_and_print_length():
    # TODO: Tải 3 URL và in độ dài nội dung mỗi trang
    pass

# Bài tập 4: Đọc nhiều tệp bất đồng bộ
def read_file(filename):
    # TODO: Đọc tệp và trả về nội dung
    pass

async def read_files_async(filenames):
    # TODO: Đọc danh sách tệp song song
    pass

# Bài tập 5: Tải URL với timeout
async def fetch_with_timeout(url, timeout):
    # TODO: Tải URL, nếu quá timeout thì in "Timeout"
    pass