# Tạo hiệu ứng loading
## Giới thiệu
Trong thiết kế web, hiệu ứng loading là một phần quan trọng giúp cải thiện trải nghiệm người dùng. Khi một trang web hoặc ứng dụng đang tải dữ liệu, một hiệu ứng loading sẽ giúp người dùng biết rằng trang web đang hoạt động và chờ đợi. Trong bài này, chúng ta sẽ tìm hiểu cách tạo hiệu ứng loading cơ bản bằng HTML và CSS.

## Lý thuyết
Để tạo hiệu ứng loading, chúng ta có thể sử dụng CSS để tạo các hình dạng và animation. Một trong những cách phổ biến nhất là sử dụng CSS Keyframes để tạo animation. Chúng ta cũng có thể sử dụng các thuộc tính như `opacity`, `transform` và `animation` để tạo hiệu ứng loading.

Ví dụ, chúng ta có thể tạo một hình tròn quay bằng cách sử dụng CSS như sau:
```html
<div class="loading"></div>
```

```css
.loading {
  width: 50px;
  height: 50px;
  border: 5px solid #ccc;
  border-top: 5px solid #333;
  border-radius: 50%;
  animation: spin 1s linear infinite;
}

@keyframes spin {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}
```
## Ví dụ
Chúng ta có thể tạo một hiệu ứng loading đơn giản bằng cách sử dụng HTML và CSS. Ví dụ, chúng ta có thể tạo một trang web với một nút "Tải dữ liệu" và khi người dùng click vào nút, một hiệu ứng loading sẽ xuất hiện.

```html
<button class="btn">Tải dữ liệu</button>
<div class="loading" style="display: none;"></div>
```

```css
.loading {
  width: 50px;
  height: 50px;
  border: 5px solid #ccc;
  border-top: 5px solid #333;
  border-radius: 50%;
  animation: spin 1s linear infinite;
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}

@keyframes spin {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}
```

Khi người dùng click vào nút, chúng ta có thể sử dụng JavaScript để hiển thị hiệu ứng loading.

```javascript
document.querySelector('.btn').addEventListener('click', function() {
  document.querySelector('.loading').style.display = 'block';
  // Code tải dữ liệu ở đây
  setTimeout(function() {
    document.querySelector('.loading').style.display = 'none';
  }, 2000);
});
```

## Bài tập
Bài tập cho bạn là tạo một hiệu ứng loading với các hình dạng khác nhau, như hình vuông, hình tam giác, hình tròn với các màu sắc khác nhau. Bạn cũng có thể thêm các hiệu ứng chuyển động khác nhau, như zoom, fade, slide. Hãy thử nghiệm và tạo ra các hiệu ứng loading độc đáo và thú vị.