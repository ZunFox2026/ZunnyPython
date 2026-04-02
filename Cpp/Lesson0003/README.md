# Làm việc với tệp
## Giới thiệu
Làm việc với tệp là một phần quan trọng trong lập trình, đặc biệt là khi bạn cần lưu trữ hoặc đọc dữ liệu từ bên ngoài chương trình. Trong C++, có nhiều cách để làm việc với tệp, bao gồm cả việc sử dụng các hàm và lớp riêng biệt cho mục đích này. Bài viết này sẽ hướng dẫn bạn cách làm việc với tệp trong C++.

## Lý thuyết
Trong C++, có hai loại tệp chính: tệp văn bản (text file) và tệp nhị phân (binary file). Tệp văn bản chứa dữ liệu dưới dạng văn bản, trong khi tệp nhị phân chứa dữ liệu dưới dạng nhị phân. Để làm việc với tệp, bạn cần sử dụng các hàm và lớp như `fstream`, `ifstream`, `ofstream`. 

- `fstream` là lớp cơ bản cho việc làm việc với tệp, cho phép bạn đọc và ghi dữ liệu vào tệp.
- `ifstream` là lớp con của `fstream`, cho phép bạn đọc dữ liệu từ tệp.
- `ofstream` là lớp con của `fstream`, cho phép bạn ghi dữ liệu vào tệp.

Ví dụ về khai báo và sử dụng các lớp này:
```cpp
#include <fstream>
#include <iostream>

int main() {
    // Mở tệp để đọc
    std::ifstream inputFile("input.txt");
    
    // Đọc dữ liệu từ tệp
    std::string line;
    while (std::getline(inputFile, line)) {
        std::cout << line << std::endl;
    }
    
    // Đóng tệp
    inputFile.close();
    
    return 0;
}
```

## Ví dụ
Dưới đây là ví dụ cụ thể về cách làm việc với tệp trong C++:
```cpp
#include <fstream>
#include <iostream>

int main() {
    // Mở tệp để ghi
    std::ofstream outputFile("output.txt");
    
    // Ghi dữ liệu vào tệp
    outputFile << "Xin chào, thế giới!" << std::endl;
    
    // Đóng tệp
    outputFile.close();
    
    // Mở tệp để đọc
    std::ifstream inputFile("output.txt");
    
    // Đọc dữ liệu từ tệp
    std::string line;
    while (std::getline(inputFile, line)) {
        std::cout << line << std::endl;
    }
    
    // Đóng tệp
    inputFile.close();
    
    return 0;
}
```
Trong ví dụ này, chúng ta mở tệp `output.txt` để ghi dữ liệu vào, sau đó đóng tệp. Tiếp theo, chúng ta mở tệp `output.txt` lại để đọc dữ liệu từ tệp và hiển thị ra màn hình.

## Bài tập
Bài tập cho bạn:
- Tạo một chương trình C++ để ghi dữ liệu vào tệp `data.txt`.
- Chương trình sẽ yêu cầu người dùng nhập tên, tuổi và địa chỉ.
- Sau khi người dùng nhập xong, chương trình sẽ ghi thông tin này vào tệp `data.txt`.
- Cuối cùng, chương trình sẽ đọc dữ liệu từ tệp `data.txt` và hiển thị ra màn hình.

Hãy thử thực hành và giải quyết bài tập này để rèn luyện kỹ năng làm việc với tệp trong C++!