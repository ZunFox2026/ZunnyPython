import asyncio
import time

# Bài tập 1: Viết hàm tải xuống bất đồng bộ
# Viết hàm `tai_xuong(url)` mô phỏng tải một file từ URL
# In ra đang tải, chờ 1 giây, rồi in hoàn thành
# async def tai_xuong(url):
#     pass

# Bài tập 2: Tải 5 URL song song
# Dùng asyncio.gather để tải 5 URL cùng lúc
# async def tai_nhieu():
#     urls = [f"https://example.com/file{i}.pdf" for i in range(1, 6)]
#     # Gọi tai_xuong cho từng URL song song
#     pass

# Bài tập 3: Chạy 3 task với thời gian khác nhau
# Tạo 3 coroutine: mot_giay(), hai_giay(), in_bat_dau()
# Chạy song song và đo tổng thời gian
# async def mot_giay():
#     pass
# async def hai_giay():
#     pass
# async def in_bat_dau():
#     pass
# async def chay_3_task():
#     pass

# Bài tập 4: Hàm chạy danh sách coroutine
# Viết hàm `thuc_hien_song_song(danh_sach_ham)` nhận danh sách các coroutine
# và chạy chúng song song bằng gather
# async def thuc_hien_song_song(danh_sach_ham):
#     pass

# Bài tập 5: Xử lý lỗi trong coroutine
# Viết hàm `co_the_loi(id)` có 50% khả năng ném lỗi
# Dùng try/except để xử lý, đảm bảo chương trình không crash
# async def co_the_loi(id):
#     pass
# async def chay_voi_xu_ly_loi():
#     tasks = [co_the_loi(i) for i in range(5)]
#     # Dùng gather với return_exceptions=True
#     pass