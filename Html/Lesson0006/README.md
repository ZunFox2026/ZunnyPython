# Tạo Form đăng nhập
## Giới thiệu
Trong phần này, chúng ta sẽ tìm hiểu cách tạo một form đăng nhập cơ bản bằng HTML và CSS. Form đăng nhập là một phần quan trọng của nhiều trang web, cho phép người dùng nhập thông tin của mình để truy cập vào hệ thống. Chúng ta sẽ học cách tạo ra một form đăng nhập với các trường nhập liệu như tên người dùng và mật khẩu, cũng như một nút đăng nhập.

## Lý thuyết
Để tạo một form đăng nhập, chúng ta cần sử dụng các thẻ HTML sau:
- `form`: Thẻ này dùng để định nghĩa một biểu mẫu.
- `input`: Thẻ này dùng để tạo ra các trường nhập liệu.
- `label`: Thẻ này dùng để tạo ra nhãn cho các trường nhập liệu.
- `button`: Thẻ này dùng để tạo ra một nút.

Ví dụ về HTML cơ bản cho một form đăng nhập:
```html
<form>
  <label for="username">Tên người dùng:</label>
  <input type="text" id="username" name="username"><br><br>
  <label for="password">Mật khẩu:</label>
  <input type="password" id="password" name="password"><br><br>
  <button type="submit">Đăng nhập</button>
</form>
```
Để làm cho form đăng nhập của chúng ta trở nên đẹp và hấp dẫn hơn, chúng ta có thể sử dụng CSS để tạo kiểu. Ví dụ, chúng ta có thể thêm màu nền, màu văn bản, và tạo kiểu cho các trường nhập liệu và nút.

Ví dụ về CSS:
```css
form {
  background-color: #f2f2f2;
  padding: 20px;
  border: 1px solid #ccc;
}

label {
  display: block;
  margin-bottom: 10px;
}

input[type="text"], input[type="password"] {
  width: 100%;
  height: 40px;
  margin-bottom: 20px;
  padding: 10px;
  border: 1px solid #ccc;
}

button[type="submit"] {
  width: 100%;
  height: 40px;
  background-color: #4CAF50;
  color: #fff;
  padding: 10px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

button[type="submit"]:hover {
  background-color: #3e8e41;
}
```
## Ví dụ
Khi chúng ta kết hợp HTML và CSS lại với nhau, chúng ta sẽ có một form đăng nhập như sau:
```html
<!DOCTYPE html>
<html>
<head>
  <title>Form đăng nhập</title>
  <style>
    form {
      background-color: #f2f2f2;
      padding: 20px;
      border: 1px solid #ccc;
    }

    label {
      display: block;
      margin-bottom: 10px;
    }

    input[type="text"], input[type="password"] {
      width: 100%;
      height: 40px;
      margin-bottom: 20px;
      padding: 10px;
      border: 1px solid #ccc;
    }

    button[type="submit"] {
      width: 100%;
      height: 40px;
      background-color: #4CAF50;
      color: #fff;
      padding: 10px;
      border: none;
      border-radius: 5px;
      cursor: pointer;
    }

    button[type="submit"]:hover {
      background-color: #3e8e41;
    }
  </style>
</head>
<body>
  <form>
    <label for="username">Tên người dùng:</label>
    <input type="text" id="username" name="username"><br><br>
    <label for="password">Mật khẩu:</label>
    <input type="password" id="password" name="password"><br><br>
    <button type="submit">Đăng nhập</button>
  </form>
</body>
</html>
```
## Bài tập
Bài tập cho bạn:
- Tạo một form đăng nhập với các trường nhập liệu tên người dùng và mật khẩu.
- Thêm một nút đăng nhập.
- Sử dụng CSS để tạo kiểu cho form đăng nhập của bạn.
- Thêm màu nền, màu văn bản, và tạo kiểu cho các trường nhập liệu và nút.
- Khi người dùng di chuột vào nút đăng nhập, màu nền của nút sẽ thay đổi.