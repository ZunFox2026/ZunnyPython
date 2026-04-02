# Tạo hình nền động
## Giới thiệu
Tạo hình nền động là một kỹ thuật được sử dụng trong thiết kế web để tạo ra các hiệu ứng hình ảnh động thú vị trên trang web. Với sự hỗ trợ của CSS, bạn có thể dễ dàng tạo ra các hình nền động mà không cần phải sử dụng đến JavaScript. Trong bài viết này, chúng ta sẽ tìm hiểu về cách tạo hình nền động bằng CSS.

## Lý thuyết
Để tạo hình nền động, bạn cần sử dụng đến thuộc tính `background` trong CSS. Thuộc tính này cho phép bạn thiết lập màu sắc, hình ảnh, và các hiệu ứng khác cho hình nền của một phần tử. Để tạo hiệu ứng động, bạn có thể sử dụng đến các thuộc tính như `background-position`, `background-size`, và `animation`.

Ví dụ, để tạo một hình nền động với hiệu ứng di chuyển, bạn có thể sử dụng code CSS sau:
```css
.element {
  background-image: url('image.jpg');
  background-position: 0% 0%;
  background-size: 100% 100%;
  animation: move 10s infinite;
}

@keyframes move {
  0% {
    background-position: 0% 0%;
  }
  100% {
    background-position: 100% 100%;
  }
}
```
Trong ví dụ trên, chúng ta sử dụng thuộc tính `animation` để tạo hiệu ứng động cho hình nền. Thuộc tính `@keyframes` được sử dụng để định nghĩa các khung hình của hiệu ứng động.

## Ví dụ
Dưới đây là một ví dụ cụ thể về cách tạo hình nền động bằng CSS:
```css
.container {
  width: 100%;
  height: 100vh;
  background-image: linear-gradient(to right, #f00, #0f0, #00f);
  background-size: 400% 400%;
  animation: move 10s infinite;
}

@keyframes move {
  0% {
    background-position: 0% 0%;
  }
  100% {
    background-position: 100% 100%;
  }
}
```
Trong ví dụ trên, chúng ta tạo một hình nền động với hiệu ứng di chuyển của một gradient màu. Thuộc tính `background-size` được sử dụng để thiết lập kích thước của hình nền, và thuộc tính `animation` được sử dụng để tạo hiệu ứng động.

## Bài tập
Để luyện tập kỹ năng tạo hình nền động, bạn có thể thực hiện các bài tập sau:
- Tạo một hình nền động với hiệu ứng di chuyển của một hình ảnh.
- Tạo một hình nền động với hiệu ứng thay đổi màu sắc.
- Tạo một hình nền động với hiệu ứng kết hợp giữa di chuyển và thay đổi màu sắc.
Với các bài tập trên, bạn sẽ có thể cải thiện kỹ năng tạo hình nền động và áp dụng vào các dự án thực tế.