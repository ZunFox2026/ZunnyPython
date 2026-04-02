# Tạo hình ảnh phản chiếu
## Giới thiệu
Trong thiết kế web, việc tạo hình ảnh phản chiếu là một kỹ thuật quan trọng để làm tăng sự thu hút và chuyên nghiệp cho trang web. Bài viết này sẽ hướng dẫn bạn cách tạo hình ảnh phản chiếu bằng CSS, một kỹ thuật cơ bản nhưng hiệu quả.

## Lý thuyết
Để tạo hình ảnh phản chiếu, bạn cần sử dụng thuộc tính `transform` trong CSS. Thuộc tính này cho phép bạn thực hiện các phép biến đổi trên phần tử, bao gồm cả việc lật hình ảnh. Ngoài ra, bạn cũng cần sử dụng thuộc tính `opacity` để điều chỉnh độ trong suốt của hình ảnh phản chiếu, giúp tạo hiệu ứng mờ ảo.

Ví dụ, để tạo hình ảnh phản chiếu, bạn có thể sử dụng đoạn code CSS sau:
```css
.reflect {
  transform: scaleY(-1);
  opacity: 0.5;
}
```
Trong đoạn code trên, `transform: scaleY(-1)` sẽ lật hình ảnh theo trục Y, tạo ra hiệu ứng phản chiếu. `opacity: 0.5` sẽ điều chỉnh độ trong suốt của hình ảnh phản chiếu, giúp tạo hiệu ứng mờ ảo.

## Ví dụ
Để minh họa cách tạo hình ảnh phản chiếu, hãy xem xét ví dụ sau:
```css
.box {
  width: 200px;
  height: 200px;
  background-image: url('image.jpg');
  background-size: cover;
}

.reflect {
  transform: scaleY(-1);
  opacity: 0.5;
  margin-top: 10px;
}
```
```html
<div class="box"></div>
<div class="box reflect"></div>
```
Trong ví dụ trên, chúng ta có hai phần tử `div` với class `box`. Phần tử đầu tiên sẽ hiển thị hình ảnh gốc, trong khi phần tử thứ hai sẽ hiển thị hình ảnh phản chiếu. Thuộc tính `transform` và `opacity` sẽ được áp dụng cho phần tử thứ hai để tạo hiệu ứng phản chiếu.

## Bài tập
Bài tập này yêu cầu bạn tạo một hình ảnh phản chiếu bằng CSS. Hãy thực hiện các bước sau:

* Tạo một phần tử `div` với class `box` và thêm một hình ảnh vào đó.
* Tạo một phần tử `div` khác với class `reflect` và thêm cùng một hình ảnh vào đó.
* Sử dụng thuộc tính `transform` và `opacity` để tạo hiệu ứng phản chiếu cho phần tử `div` với class `reflect`.
* Điều chỉnh giá trị của thuộc tính `opacity` để thay đổi độ trong suốt của hình ảnh phản chiếu.

Khi hoàn thành bài tập, bạn sẽ có một hình ảnh phản chiếu đẹp và chuyên nghiệp, giúp tăng sự thu hút cho trang web của mình.