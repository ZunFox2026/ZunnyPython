# Khởi tạo Pygame
import pygame
import sys

# Khởi tạo các mô-đun của Pygame
pygame.init()

# Thiết lập chiều rộng và chiều cao của cửa sổ
chieu_rong = 800
chieu_cao = 600

# Tạo cửa sổ với chiều rộng và chiều cao đã thiết lập
cua_so = pygame.display.set_mode((chieu_rong, chieu_cao))

# Thiết lập tiêu đề của cửa sổ
pygame.display.set_caption("Làm quen với thư viện Pygame")

# Thiết lập màu sắc (đỏ, xanh lá, xanh da trời)
mau_do = (255, 0, 0)
mau_xanh_la = (0, 255, 0)
mau_xanh_da_troi = (0, 0, 255)

# Vòng lặp chính của trò chơi
while True:
    for su_kien in pygame.event.get():
        if su_kien.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Vẽ hình chữ nhật màu đỏ
    pygame.draw.rect(cua_so, mau_do, (100, 100, 200, 200))

    # Vẽ hình tròn màu xanh lá
    pygame.draw.circle(cua_so, mau_xanh_la, (400, 300), 100)

    # Vẽ hình tam giác màu xanh da trời
    pygame.draw.polygon(cua_so, mau_xanh_da_troi, ((600, 200), (700, 400), (500, 400)))

    # Cập nhật cửa sổ
    pygame.display.update()

    # Điều chỉnh tốc độ khung hình
    pygame.time.Clock().tick(60)