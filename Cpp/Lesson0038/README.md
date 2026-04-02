# Làm việc với tệp
## Giới thiệu
Làm việc với tệp là một phần quan trọng trong lập trình, cho phép chúng ta lưu trữ và đọc dữ liệu từ các tệp tin. Trong C++, chúng ta có thể sử dụng các hàm và lớp để thực hiện các操作 này. Bài viết này sẽ giới thiệu về cách làm việc với tệp trong C++.

## Lý thuyết
Trong C++, chúng ta có thể sử dụng lớp `fstream` để làm việc với tệp. Lớp `fstream` cung cấp các hàm để mở, đọc và ghi tệp. Để mở một tệp, chúng ta sử dụng hàm `open()` và truyền vào đường dẫn đến tệp. Nếu tệp không tồn tại, chúng ta có thể tạo một tệp mới bằng cách sử dụng hàm `open()` với tham số `ios::out`.

Ví dụ:
```cpp
#include <fstream>

int main() {
    std::ofstream file("example.txt");
    if (file.is_open()) {
        file << "Xin chào, thế giới!";
        file.close();
    }
    return 0;
}
```
Trong ví dụ trên, chúng ta mở một tệp mới có tên "example.txt" và ghi vào đó dòng chữ "Xin chào, thế giới!".

## Ví dụ
Để đọc dữ liệu từ một tệp, chúng ta có thể sử dụng hàm `>>` hoặc `getline()`. Ví dụ:
```cpp
#include <fstream>
#include <string>

int main() {
    std::ifstream file("example.txt");
    if (file.is_open()) {
        std::string line;
        while (std::getline(file, line)) {
            std::cout << line << std::endl;
        }
        file.close();
    }
    return 0;
}
```
Trong ví dụ trên, chúng ta mở tệp "example.txt" và đọc từng dòng dữ liệu từ tệp, sau đó in ra màn hình.

## Bài tập
Bài tập: Tạo một chương trình C++ để lưu trữ và đọc dữ liệu từ một tệp. Chương trình nên có các chức năng sau:
- Tạo một tệp mới và ghi vào đó một dòng chữ.
- Đọc dữ liệu từ tệp và in ra màn hình.
- Thêm một dòng chữ mới vào tệp.
- Đọc lại dữ liệu từ tệp và in ra màn hình.

Lời giải:
```cpp
#include <fstream>
#include <string>

int main() {
    // Tạo tệp mới và ghi vào đó một dòng chữ
    std::ofstream file("example.txt");
    if (file.is_open()) {
        file << "Xin chào, thế giới!";
        file.close();
    }

    // Đọc dữ liệu từ tệp và in ra màn hình
    std::ifstream file2("example.txt");
    if (file2.is_open()) {
        std::string line;
        while (std::getline(file2, line)) {
            std::cout << line << std::endl;
        }
        file2.close();
    }

    // Thêm một dòng chữ mới vào tệp
    std::ofstream file3("example.txt", std::ios::app);
    if (file3.is_open()) {
        file3 << "\nTạm biệt, thế giới!";
        file3.close();
    }

    // Đọc lại dữ liệu từ tệp và in ra màn hình
    std::ifstream file4("example.txt");
    if (file4.is_open()) {
        std::string line;
        while (std::getline(file4, line)) {
            std::cout << line << std::endl;
        }
        file4.close();
    }
    return 0;
}
```
Chúc bạn thành công trong việc làm việc với tệp trong C++!