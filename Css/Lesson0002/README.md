# Tìm hiểu về Media Query
## Giới thiệu
Media Query là một tính năng trong CSS cho phép bạn áp dụng các样式 khác nhau tùy thuộc vào các điều kiện nhất định của thiết bị hoặc trình duyệt. Điều này giúp cho trang web của bạn có thể thích ứng với các kích thước màn hình khác nhau, từ điện thoại di động đến máy tính bảng và máy tính để bàn. Trong bài này, chúng ta sẽ tìm hiểu về cơ bản của Media Query và cách sử dụng nó để tạo ra các trang web đáp ứng.

## Lý thuyết
Media Query sử dụng cú pháp `@media` để xác định các điều kiện mà樣式 sẽ được áp dụng. Các điều kiện này có thể bao gồm chiều rộng và chiều cao của màn hình, độ phân giải, hướng của thiết bị (đứng hoặc nằm), v.v. Ví dụ, bạn có thể sử dụng Media Query để thay đổi kích thước phông chữ hoặc chiều rộng của một phần tử khi trang web được xem trên một thiết bị di động. Ví dụ CSS:
```css
@media (max-width: 768px) {
  body {
    font-size: 16px;
  }
}
```
Điều này có nghĩa là khi chiều rộng của màn hình nhỏ hơn hoặc bằng 768px, kích thước phông chữ của phần tử `body` sẽ được đặt thành 16px.

## Ví dụ
Để minh họa rõ hơn về cách sử dụng Media Query, hãy xem xét một ví dụ khác. Giả sử bạn muốn tạo một trang web có thanh điều hướng nằm ngang trên máy tính để bàn nhưng chuyển thành thanh điều hướng dọc trên điện thoại di động. Bạn có thể sử dụng Media Query như sau:
```css
@media (min-width: 769px) {
  nav {
    flex-direction: row;
  }
}

@media (max-width: 768px) {
  nav {
    flex-direction: column;
  }
}
```
Trong ví dụ này, khi chiều rộng của màn hình lớn hơn hoặc bằng 769px, thanh điều hướng sẽ được sắp xếp theo hàng ngang (`flex-direction: row`). Ngược lại, khi chiều rộng nhỏ hơn hoặc bằng 768px, thanh điều hướng sẽ được sắp xếp theo cột dọc (`flex-direction: column`).

## Bài tập
Để thực hành sử dụng Media Query, bạn có thể thử tạo một trang web đơn giản với các phần tử như tiêu đề, ảnh và đoạn văn. Sau đó, sử dụng Media Query để thay đổi cách hiển thị của các phần tử này tùy thuộc vào kích thước màn hình. Ví dụ, bạn có thể thay đổi kích thước của tiêu đề, ẩn hoặc hiện các phần tử nhất định, hoặc thay đổi bố cục của trang web. Điều này sẽ giúp bạn hiểu rõ hơn về cách Media Query hoạt động và cách bạn có thể sử dụng nó để tạo ra các trang web đáp ứng và thân thiện với người dùng.