# Tạo hình nền động
## Giới thiệu
Bài này sẽ hướng dẫn cách tạo hình nền động bằng CSS. Hình nền động là một yếu tố quan trọng trong thiết kế web, giúp trang web trở nên sinh động và thu hút hơn. Với CSS, chúng ta có thể tạo ra nhiều hiệu ứng hình nền động khác nhau, từ đơn giản đến phức tạp.

## Lý thuyết
Để tạo hình nền động, chúng ta cần sử dụng thuộc tính `background` trong CSS. Thuộc tính này cho phép chúng ta đặt hình nền cho một phần tử HTML. Ngoài ra, chúng ta cũng cần sử dụng thuộc tính `animation` để tạo ra hiệu ứng động. Ví dụ, chúng ta có thể tạo ra một hình nền động bằng cách sử dụng thuộc tính `background-image` và `animation` như sau:
```css
body {
  background-image: linear-gradient(to right, #f00, #0f0, #00f);
  background-size: 100% 100%;
  animation: dynamicBackground 10s ease infinite;
}

@keyframes dynamicBackground {
  0% {
    background-position: 0% 0%;
  }
  100% {
    background-position: 100% 100%;
  }
}
```
Trong ví dụ trên, chúng ta tạo ra một hình nền động bằng cách sử dụng thuộc tính `background-image` để đặt một hình nền gradient, và thuộc tính `animation` để tạo ra hiệu ứng động. Thuộc tính `@keyframes` được sử dụng để định nghĩa các khung hình của hiệu ứng động.

## Ví dụ
Dưới đây là một ví dụ khác về tạo hình nền động bằng CSS:
```css
body {
  background-image: url('background.jpg');
  background-size: cover;
  animation: dynamicBackground 5s ease infinite;
}

@keyframes dynamicBackground {
  0% {
    transform: scale(1);
  }
  100% {
    transform: scale(1.2);
  }
}
```
Trong ví dụ này, chúng ta tạo ra một hình nền động bằng cách sử dụng thuộc tính `background-image` để đặt một hình nền, và thuộc tính `animation` để tạo ra hiệu ứng động. Thuộc tính `@keyframes` được sử dụng để định nghĩa các khung hình của hiệu ứng động, trong đó hình nền được phóng to và thu nhỏ liên tục.

## Bài tập
Bài tập của bạn là tạo ra một hình nền động bằng CSS. Hãy sử dụng thuộc tính `background` và `animation` để tạo ra một hiệu ứng hình nền động. Bạn có thể sử dụng các thuộc tính khác như `background-image`, `background-size`, `transform` để tạo ra hiệu ứng động. Sau khi hoàn thành, hãy chia sẻ kết quả của bạn với mọi người. Một số ý tưởng cho bài tập của bạn:
* Tạo ra một hình nền động bằng cách sử dụng hình ảnh hoặc màu sắc.
* Sử dụng thuộc tính `@keyframes` để định nghĩa các khung hình của hiệu ứng động.
* Thử nghiệm với các thuộc tính khác như `transition`, `transform` để tạo ra hiệu ứng động.