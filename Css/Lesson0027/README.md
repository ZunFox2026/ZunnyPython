# Tìm hiểu về Media Queries
## Giới thiệu
Media Queries là một tính năng trong CSS cho phép bạn áp dụng các kiểu dáng khác nhau dựa trên các điều kiện cụ thể của thiết bị hoặc trình duyệt. Điều này giúp bạn tạo ra các trang web có khả năng thích ứng với nhiều loại thiết bị và kích thước màn hình khác nhau. Trong bài này, chúng ta sẽ tìm hiểu về Media Queries, cách chúng hoạt động và ví dụ về cách sử dụng chúng.

## Lý thuyết
Media Queries sử dụng cú pháp `@media` để xác định các điều kiện mà tại đó các kiểu dáng sẽ được áp dụng. Các điều kiện này có thể bao gồm chiều rộng màn hình, chiều cao màn hình, hướng màn hình (ngang hoặc dọc), và nhiều điều kiện khác. Ví dụ, bạn có thể sử dụng Media Queries để áp dụng một kiểu dáng khác cho các thiết bị di động khi chiều rộng màn hình nhỏ hơn 768 pixel:
```css
@media (max-width: 768px) {
  body {
    background-color: #f2f2f2;
  }
}
```
Trong ví dụ trên, khi chiều rộng màn hình nhỏ hơn hoặc bằng 768 pixel, nền của trang web sẽ được đổi thành màu xám.

## Ví dụ
Một ví dụ khác về việc sử dụng Media Queries là để tạo ra một menu điều hướng có thể thu gọn trên các thiết bị di động. Bạn có thể sử dụng Media Queries để ẩn menu khi chiều rộng màn hình nhỏ hơn 480 pixel và hiển thị một nút để người dùng có thể mở menu:
```css
@media (max-width: 480px) {
  .menu {
    display: none;
  }
  .menu-toggle {
    display: block;
  }
}
```
Khi chiều rộng màn hình lớn hơn 480 pixel, menu sẽ được hiển thị và nút menu toggle sẽ bị ẩn:
```css
@media (min-width: 481px) {
  .menu {
    display: block;
  }
  .menu-toggle {
    display: none;
  }
}
```
## Bài tập
Bài tập cho bạn là tạo một trang web đơn giản có thể thích ứng với các kích thước màn hình khác nhau. Hãy tạo một trang web có header, nội dung chính và footer. Sử dụng Media Queries để áp dụng các kiểu dáng khác nhau cho các phần tử này dựa trên chiều rộng màn hình. Ví dụ, bạn có thể làm cho header trở nên nhỏ hơn trên các thiết bị di động, hoặc ẩn sidebar khi chiều rộng màn hình nhỏ hơn 1024 pixel. Hãy thử nghiệm với các điều kiện và kiểu dáng khác nhau để tạo ra một trang web có khả năng thích ứng cao.