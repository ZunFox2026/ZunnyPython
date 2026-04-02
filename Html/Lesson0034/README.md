# Tạo hiệu ứng bóng động cho hình ảnh
## Giới thiệu
Trong bài học này, chúng ta sẽ tìm hiểu cách tạo hiệu ứng bóng động cho hình ảnh bằng cách sử dụng HTML và CSS. Hiệu ứng bóng động giúp hình ảnh của bạn trở nên sinh động và thu hút hơn. Chúng ta sẽ sử dụng thuộc tính CSS như `box-shadow` và `animation` để tạo ra hiệu ứng này.

## Lý thuyết
Để tạo hiệu ứng bóng động cho hình ảnh, chúng ta cần sử dụng thuộc tính `box-shadow` để tạo bóng cho hình ảnh, và thuộc tính `animation` để tạo hiệu ứng động. Thuộc tính `box-shadow` cho phép chúng ta tạo bóng cho một phần tử HTML, với các giá trị như màu sắc, kích thước và vị trí của bóng. Thuộc tính `animation` cho phép chúng ta tạo hiệu ứng động cho một phần tử HTML, với các giá trị như thời gian, tốc độ và loại hiệu ứng.

Ví dụ, chúng ta có thể sử dụng CSS như sau:
```html
<img src="image.jpg" class="image">
```

```css
.image {
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);
  animation: bounce 2s infinite;
}

@keyframes bounce {
  0% {
    transform: scale(1);
  }
  50% {
    transform: scale(1.2);
  }
  100% {
    transform: scale(1);
  }
}
```
Trong ví dụ trên, chúng ta tạo bóng cho hình ảnh với màu sắc đen và kích thước 10px, và tạo hiệu ứng động với tên "bounce" và thời gian 2 giây. Hiệu ứng động này sẽ làm cho hình ảnh thay đổi kích thước từ 1 đến 1.2 và trở lại kích thước ban đầu.

## Ví dụ
Chúng ta có thể sử dụng HTML và CSS như sau:
```html
<img src="image.jpg" class="image">
```

```css
.image {
  width: 200px;
  height: 200px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);
  animation: rotate 4s infinite;
}

@keyframes rotate {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}
```
Trong ví dụ trên, chúng ta tạo bóng cho hình ảnh với màu sắc đen và kích thước 10px, và tạo hiệu ứng động với tên "rotate" và thời gian 4 giây. Hiệu ứng động này sẽ làm cho hình ảnh quay 360 độ.

## Bài tập
Bài tập của bạn là tạo hiệu ứng bóng động cho hình ảnh bằng cách sử dụng thuộc tính `box-shadow` và `animation`. Hãy thử tạo các hiệu ứng động khác nhau như dịch chuyển, thay đổi kích thước, quay, v.v. Hãy sử dụng các giá trị khác nhau cho thuộc tính `box-shadow` và `animation` để tạo ra các hiệu ứng động khác nhau.