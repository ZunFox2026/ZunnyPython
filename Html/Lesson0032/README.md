# Tạo hiệu ứng loading
## Giới thiệu
Hiệu ứng loading là một phần quan trọng trong thiết kế web, giúp người dùng biết rằng trang web đang tải nội dung. Trong bài này, chúng ta sẽ tìm hiểu cách tạo hiệu ứng loading bằng HTML và CSS.

## Lý thuyết
Để tạo hiệu ứng loading, chúng ta cần sử dụng các kỹ thuật sau:
- Sử dụng HTML để tạo cấu trúc của hiệu ứng loading.
- Sử dụng CSS để tạo kiểu và hiệu ứng cho hiệu ứng loading.
- Sử dụng thuộc tính `animation` trong CSS để tạo hiệu ứng chuyển động.
Ví dụ về cấu trúc HTML và CSS cơ bản cho hiệu ứng loading:
```html
<div class="loading">
  <div class="loading-bar"></div>
</div>
```
```css
.loading {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}

.loading-bar {
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
Trong ví dụ trên, chúng ta sử dụng một div có lớp `loading` để chứa hiệu ứng loading, và một div có lớp `loading-bar` để tạo hình tròn chuyển động.

## Ví dụ
Dưới đây là ví dụ về cách tạo hiệu ứng loading bằng HTML và CSS:
```html
<div class="loading">
  <div class="loading-bar"></div>
</div>
```
```css
.loading {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}

.loading-bar {
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
Kết quả sẽ là một hình tròn chuyển động tại vị trí trung tâm của trang web.

## Bài tập
Bài tập cho bạn:
- Tạo một hiệu ứng loading với hình dạng khác, chẳng hạn như hình vuông hoặc hình chữ nhật.
- Thử thay đổi màu sắc và kích thước của hiệu ứng loading.
- Tạo một hiệu ứng loading với nhiều hình dạng khác nhau, chẳng hạn như hình tròn, hình vuông và hình chữ nhật.