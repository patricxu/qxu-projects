#include <regex>
#include <iostream>
#include <stdio.h>
#include <string>

using namespace std;

int main(int argc,char** argv)
{
	//match for 20170229
	//notmatch for 20170230
	regex pattern("^[0-9]{4}(((0[13578]|(10|12))(0[1-9]|[1-2][0-9]|3[0-1]))|(02(0[1-9]|[1-2][0-9]))|((0[469]|11)(0[1-9]|[1-2][0-9]|30)))$", regex_constants::extended);
    printf("input strings:\n");
    string buf;

    while(cin>>buf)
    {
        printf("*******\n%s\n********\n",buf.c_str());

        if(buf == "quit")
        {
            printf("quit just now!\n");
            break;
        }

        match_results<string::const_iterator> result;
        printf("run compare now!  '%s'\n", buf.c_str());
        bool valid = regex_match(buf,result,pattern);
        printf("compare over now!  '%s'\n", buf.c_str());

        if(!valid)
            printf("no match!\n");
        else
            printf("ok\n");
    }

    return 0 ;
}