# Tạo Form đăng nhập
## Giới thiệu
Trong bài học này, chúng ta sẽ tìm hiểu cách tạo một Form đăng nhập cơ bản sử dụng HTML và CSS. Form đăng nhập là một phần quan trọng của hầu hết các trang web, cho phép người dùng nhập thông tin để truy cập vào hệ thống. Chúng ta sẽ học cách tạo các phần tử form, sử dụng các thuộc tính và样式 CSS để tạo ra một giao diện đăng nhập đẹp và thân thiện với người dùng.

## Lý thuyết
Để tạo một Form đăng nhập, chúng ta cần sử dụng các phần tử HTML sau:
- `form`: Đây là phần tử chính của form, chứa tất cả các phần tử khác.
- `input`: Đây là phần tử nhập liệu, cho phép người dùng nhập thông tin.
- `label`: Đây là phần tử nhãn, dùng để mô tả các phần tử nhập liệu.
- `button`: Đây là phần tử nút, dùng để提交 form.

Chúng ta cũng cần sử dụng các thuộc tính HTML sau:
- `type`: Xác định loại nhập liệu, ví dụ `text`, `password`, `submit`.
- `name`: Xác định tên của phần tử nhập liệu.
- `id`: Xác định id của phần tử nhập liệu.

Ví dụ:
```html
<form>
  <label for="username">Tên đăng nhập:</label>
  <input type="text" id="username" name="username"><br><br>
  <label for="password">Mật khẩu:</label>
  <input type="password" id="password" name="password"><br><br>
  <button type="submit">Đăng nhập</button>
</form>
```
Chúng ta cũng có thể sử dụng CSS để tạo样式 cho form, ví dụ:
```css
form {
  width: 300px;
  margin: 50px auto;
  padding: 20px;
  border: 1px solid #ccc;
  border-radius: 10px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

label {
  display: block;
  margin-bottom: 10px;
}

input {
  width: 100%;
  height: 30px;
  margin-bottom: 20px;
  padding: 10px;
  border: 1px solid #ccc;
}

button {
  width: 100%;
  height: 30px;
  background-color: #4CAF50;
  color: #fff;
  padding: 10px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

button:hover {
  background-color: #3e8e41;
}
```
## Ví dụ
Chúng ta có thể tạo một Form đăng nhập cơ bản như sau:
```html
<form>
  <label for="username">Tên đăng nhập:</label>
  <input type="text" id="username" name="username"><br><br>
  <label for="password">Mật khẩu:</label>
  <input type="password" id="password" name="password"><br><br>
  <button type="submit">Đăng nhập</button>
</form>
```
Và thêm CSS để tạo样式:
```css
form {
  width: 300px;
  margin: 50px auto;
  padding: 20px;
  border: 1px solid #ccc;
  border-radius: 10px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

label {
  display: block;
  margin-bottom: 10px;
}

input {
  width: 100%;
  height: 30px;
  margin-bottom: 20px;
  padding: 10px;
  border: 1px solid #ccc;
}

button {
  width: 100%;
  height: 30px;
  background-color: #4CAF50;
  color: #fff;
  padding: 10px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

button:hover {
  background-color: #3e8e41;
}
```
## Bài tập
Bài tập: Tạo một Form đăng nhập cơ bản sử dụng HTML và CSS. Thêm các phần tử nhập liệu cho tên đăng nhập và mật khẩu, và một nút đăng nhập. Sử dụng CSS để tạo样式 cho form và các phần tử nhập liệu.