# Làm việc với tệp
## Giới thiệu
Làm việc với tệp là một phần quan trọng trong lập trình, cho phép chúng ta lưu trữ và đọc dữ liệu từ tệp. Trong C++, chúng ta có thể sử dụng các lớp và hàm trong thư viện chuẩn để thực hiện các thao tác này. Bài viết này sẽ giới thiệu về cách làm việc với tệp trong C++.

## Lý thuyết
Để làm việc với tệp trong C++, chúng ta cần sử dụng các lớp `ifstream` (để đọc tệp), `ofstream` (để ghi tệp) và `fstream` (để đọc và ghi tệp). Các lớp này được định nghĩa trong tệp tiêu đề `fstream`.

Chúng ta có thể mở một tệp bằng cách tạo một đối tượng của lớp tương ứng và truyền tên tệp vào hàm constructor. Ví dụ:
```cpp
#include <fstream>

int main() {
    std::ifstream file("example.txt");
    // ...
}
```
Sau khi mở tệp, chúng ta có thể sử dụng các hàm như `read()`, `write()`, `getline()` để đọc và ghi dữ liệu vào tệp.

## Ví dụ
Dưới đây là một ví dụ về cách đọc và ghi dữ liệu vào tệp:
```cpp
#include <fstream>
#include <iostream>
#include <string>

int main() {
    // Tạo một tệp mới và ghi dữ liệu vào tệp
    std::ofstream fileOut("example.txt");
    if (fileOut.is_open()) {
        fileOut << "Xin chào, thế giới!" << std::endl;
        fileOut.close();
    }

    // Đọc dữ liệu từ tệp
    std::ifstream fileIn("example.txt");
    if (fileIn.is_open()) {
        std::string line;
        while (std::getline(fileIn, line)) {
            std::cout << line << std::endl;
        }
        fileIn.close();
    }

    return 0;
}
```
Trong ví dụ trên, chúng ta tạo một tệp mới có tên "example.txt" và ghi câu "Xin chào, thế giới!" vào tệp. Sau đó, chúng ta đọc dữ liệu từ tệp và in ra màn hình.

## Bài tập
Bài tập này yêu cầu bạn viết một chương trình C++ để thực hiện các thao tác sau:

* Tạo một tệp mới có tên "test.txt"
* Ghi 5 dòng dữ liệu vào tệp
* Đọc dữ liệu từ tệp và in ra màn hình
* Thêm 2 dòng dữ liệu mới vào tệp
* Đọc lại dữ liệu từ tệp và in ra màn hình

Bạn có thể sử dụng các lớp và hàm trong thư viện chuẩn C++ để thực hiện các thao tác này. Chúc bạn thành công!