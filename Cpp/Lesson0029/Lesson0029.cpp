#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main() {
    // Tạo một tệp mới và ghi dữ liệu vào tệp
    ofstream tep("example.txt");
    if (tep.is_open()) {
        // Ghi dữ liệu vào tệp
        tep << "Xin chào, thế giới!" << endl;
        tep << "Đây là một ví dụ về làm việc với tệp." << endl;
        tep.close();
        cout << "Tệp đã được tạo và ghi dữ liệu thành công!" << endl;
    } else {
        cout << "Không thể mở tệp để ghi!" << endl;
    }

    // Đọc dữ liệu từ tệp
    ifstream doc("example.txt");
    if (doc.is_open()) {
        string dong;
        while (getline(doc, dong)) {
            cout << dong << endl;
        }
        doc.close();
        cout << "Đọc dữ liệu từ tệp thành công!" << endl;
    } else {
        cout << "Không thể mở tệp để đọc!" << endl;
    }

    return 0;
}