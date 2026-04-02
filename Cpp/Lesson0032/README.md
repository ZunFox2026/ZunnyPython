# Xử lý tệp
## Giới thiệu
Xử lý tệp là một phần quan trọng trong lập trình, cho phép bạn lưu trữ và đọc dữ liệu từ các tệp trên đĩa cứng. Trong C++, bạn có thể sử dụng các hàm và lớp để thực hiện các hoạt động này. Bài viết này sẽ giới thiệu về cách xử lý tệp trong C++.

## Lý thuyết
Để xử lý tệp trong C++, bạn cần bao gồm hàm `fstream` trong chương trình của mình. Hàm này cung cấp các lớp `ifstream`, `ofstream` và `fstream` để đọc, ghi và đọc/ghi tệp tương ứng.

*   `ifstream`: Lớp này được sử dụng để đọc tệp. Bạn có thể tạo một đối tượng `ifstream` và sử dụng nó để đọc dữ liệu từ tệp.
*   `ofstream`: Lớp này được sử dụng để ghi tệp. Bạn có thể tạo một đối tượng `ofstream` và sử dụng nó để ghi dữ liệu vào tệp.
*   `fstream`: Lớp này được sử dụng để đọc và ghi tệp. Bạn có thể tạo một đối tượng `fstream` và sử dụng nó để đọc và ghi dữ liệu vào tệp.

Ví dụ về cách sử dụng `ifstream` để đọc tệp:
```cpp
#include <fstream>
#include <iostream>
using namespace std;

int main() {
    ifstream file("test.txt");
    if (file.is_open()) {
        string line;
        while (getline(file, line)) {
            cout << line << endl;
        }
        file.close();
    } else {
        cout << "Không thể mở tệp";
    }
    return 0;
}
```

## Ví dụ
Dưới đây là một ví dụ về cách sử dụng `ofstream` để ghi tệp:
```cpp
#include <fstream>
#include <iostream>
using namespace std;

int main() {
    ofstream file("test.txt");
    if (file.is_open()) {
        file << "Xin chào, thế giới!";
        file.close();
    } else {
        cout << "Không thể mở tệp";
    }
    return 0;
}
```

## Bài tập
Bài tập 1: Viết một chương trình C++ để đọc tên và tuổi của người dùng, sau đó ghi thông tin này vào một tệp có tên "thongtin.txt".

Bài tập 2: Viết một chương trình C++ để đọc thông tin từ tệp "thongtin.txt" và hiển thị ra màn hình.

Bài tập 3: Viết một chương trình C++ để đọc danh sách các số từ tệp "danh sach so.txt", sau đó tính và hiển thị tổng của các số này.

Hy vọng những thông tin trên sẽ giúp bạn hiểu rõ hơn về cách xử lý tệp trong C++. Chúc bạn thành công trong việc lập trình!