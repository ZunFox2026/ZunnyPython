# Làm quen với thư viện Pygame
## Giới thiệu
Thư viện Pygame là một thư viện Python được sử dụng để tạo ra các trò chơi và ứng dụng đồ họa. Pygame cung cấp một cách đơn giản và dễ dàng để tạo ra các chương trình đồ họa, bao gồm cả việc tạo ra các cửa sổ, vẽ đồ họa, xử lý sự kiện và phát âm thanh. Pygame được thiết kế để dễ dàng sử dụng, ngay cả đối với những người mới bắt đầu với lập trình Python.

## Lý thuyết
Để bắt đầu sử dụng Pygame, bạn cần phải cài đặt nó vào môi trường Python của mình. Bạn có thể làm điều này bằng cách chạy lệnh `pip install pygame` trong terminal. Sau khi cài đặt, bạn có thể nhập thư viện Pygame vào chương trình của mình bằng cách sử dụng lệnh `import pygame`.

Pygame cung cấp một số chức năng chính, bao gồm:
- Tạo cửa sổ: Pygame cho phép bạn tạo ra các cửa sổ với kích thước và tiêu đề tùy chỉnh.
- Vẽ đồ họa: Pygame cung cấp các chức năng để vẽ các hình dạng cơ bản, chẳng hạn như điểm, đường thẳng, hình chữ nhật và hình tròn.
- Xử lý sự kiện: Pygame cho phép bạn xử lý các sự kiện, chẳng hạn như nhấn phím, di chuyển chuột và đóng cửa sổ.
- Phát âm thanh: Pygame cung cấp các chức năng để phát âm thanh và nhạc.

Ví dụ, để tạo ra một cửa sổ với kích thước 640x480 và tiêu đề "Làm quen với Pygame", bạn có thể sử dụng code sau:
```python
import pygame
pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Làm quen với Pygame")
```

## Ví dụ
Dưới đây là một ví dụ đơn giản về việc sử dụng Pygame để tạo ra một chương trình đồ họa. Chương trình này sẽ tạo ra một cửa sổ với kích thước 640x480 và vẽ một hình chữ nhật màu đỏ tại vị trí (100, 100).
```python
import pygame
pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Làm quen với Pygame")
screen.fill((255, 255, 255))
pygame.draw.rect(screen, (255, 0, 0), (100, 100, 200, 200))
pygame.display.flip()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
```

## Bài tập
Bài tập này yêu cầu bạn tạo ra một chương trình đồ họa đơn giản sử dụng Pygame. Chương trình sẽ tạo ra một cửa sổ với kích thước 640x480 và vẽ một hình tròn màu xanh tại vị trí (320, 240). Ngoài ra, chương trình sẽ xử lý sự kiện đóng cửa sổ và thoát chương trình khi người dùng nhấn nút đóng.
- Bước 1: Tạo một cửa sổ với kích thước 640x480 và tiêu đề "Làm quen với Pygame".
- Bước 2: Vẽ một hình tròn màu xanh tại vị trí (320, 240).
- Bước 3: Xử lý sự kiện đóng cửa sổ và thoát chương trình khi người dùng nhấn nút đóng.
- Bước 4: Chạy chương trình và kiểm tra kết quả.