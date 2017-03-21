#include<unistd.h>
extern "C" int DllTestCB(int (* callback)( char* ), char* str)
{
	if (callback != NULL)
	{
		int cnt = 1;
		while (cnt--)
		{
			callback(str);
			sleep(1);
		}
	}

	return 0;
}

