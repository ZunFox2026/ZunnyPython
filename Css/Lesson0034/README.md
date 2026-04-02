# Tìm hiểu về Media Query
## Giới thiệu
Media Query là một tính năng trong CSS cho phép chúng ta áp dụng các phong cách khác nhau dựa trên các điều kiện cụ thể của thiết bị hoặc môi trường mà trang web được hiển thị. Điều này giúp chúng ta tạo ra các trang web đáp ứng (responsive) và có thể thích nghi với nhiều loại thiết bị và kích thước màn hình khác nhau. Trong bài này, chúng ta sẽ tìm hiểu về Media Query và cách sử dụng nó trong thiết kế web.

## Lý thuyết
Media Query được sử dụng để xác định các điều kiện mà phong cách sẽ được áp dụng. Các điều kiện này có thể bao gồm kích thước màn hình, định hướng thiết bị (nằm ngang hoặc đứng), độ phân giải, v.v. Cú pháp cơ bản của Media Query là `@media` followed by một điều kiện và một khối code CSS sẽ được áp dụng khi điều kiện đó được đáp ứng. Ví dụ:
```css
@media (max-width: 768px) {
  body {
    background-color: #f2f2f2;
  }
}
```
Trong ví dụ trên, khi chiều rộng màn hình nhỏ hơn hoặc bằng 768px, nền của trang web sẽ được đổi sang màu #f2f2f2.

## Ví dụ
Chúng ta có thể sử dụng Media Query để tạo ra các phong cách khác nhau cho các thiết bị di động và máy tính bảng. Ví dụ, chúng ta có thể tạo ra một menu di động chỉ khi chiều rộng màn hình nhỏ hơn 480px:
```css
@media (max-width: 480px) {
  .menu {
    display: block;
  }
}
```
Hoặc, chúng ta có thể sử dụng Media Query để thay đổi kích thước phông chữ và khoảng cách giữa các dòng khi chiều rộng màn hình lớn hơn 1024px:
```css
@media (min-width: 1024px) {
  body {
    font-size: 18px;
    line-height: 1.5;
  }
}
```
## Bài tập
Bài tập này yêu cầu bạn tạo ra một trang web đơn giản có thể thích nghi với các thiết bị di động và máy tính bảng. Sử dụng Media Query để áp dụng các phong cách khác nhau dựa trên kích thước màn hình. Các yêu cầu cụ thể bao gồm:
- Khi chiều rộng màn hình nhỏ hơn 480px, nền của trang web sẽ được đổi sang màu #f2f2f2 và menu sẽ được hiển thị dưới dạng menu di động.
- Khi chiều rộng màn hình lớn hơn 1024px, kích thước phông chữ sẽ được tăng lên 18px và khoảng cách giữa các dòng sẽ được tăng lên 1.5.
Hãy thử nghiệm với các điều kiện và phong cách khác nhau để tạo ra một trang web đáp ứng và đẹp mắt.