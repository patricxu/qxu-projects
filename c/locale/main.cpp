#include <iostream>
#include <unistd.h>
#include <locale.h>

int main() {
	using namespace std;
	
	char* local = (char*)"zh_CN.utf16";
	char* oldLocal = NULL;
	oldLocal = setlocale(LC_ALL, local);
	cout << oldLocal << endl;


        const wchar_t *wcode = L"abc中文def";
        const char *code = "abc中文def";
	
	const char* p = "你若盛开蝴蝶自来!";

        wcout << wcode << endl;
        cout << code << endl;

        return 0;
}
