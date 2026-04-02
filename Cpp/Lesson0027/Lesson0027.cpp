#include <iostream>
#include <fstream> // thư viện để làm việc với tệp

using namespace std;

int main() {
    // Tạo một tệp mới và ghi dữ liệu vào tệp
    ofstream tepGhi("example.txt"); // tạo tệp và mở để ghi
    if (tepGhi.is_open()) {
        // ghi dữ liệu vào tệp
        tepGhi << "Xin chào, thế giới!" << endl;
        tepGhi.close(); // đóng tệp
        cout << "Ghi dữ liệu vào tệp thành công." << endl;
    } else {
        cout << "Không thể mở tệp để ghi." << endl;
    }

    // Đọc dữ liệu từ tệp
    ifstream tepDoc("example.txt"); // tạo tệp và mở để đọc
    if (tepDoc.is_open()) {
        char kyTu;
        while (tepDoc.get(kyTu)) {
            // đọc dữ liệu từ tệp
            cout << kyTu;
        }
        tepDoc.close(); // đóng tệp
        cout << "\nĐọc dữ liệu từ tệp thành công." << endl;
    } else {
        cout << "Không thể mở tệp để đọc." << endl;
    }

    return 0;
}