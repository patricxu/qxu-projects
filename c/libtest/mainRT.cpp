#include <dlfcn.h>
#include <stdio.h>

int main()
{
    void* handle = dlopen("libpkg.so", RTLD_LAZY);
    if(!handle)
    {
        printf("failed to load libpkg.so\n");
        return -1;
    }

    char* error = NULL;
    typedef void (*PKG_FUNC)();
    PKG_FUNC pPkg_func = (PKG_FUNC)dlsym(handle, "pkg_func");
    if((error = dlerror()) != NULL)
    {
        printf("failed to load symbol pkg_func %s\n", error);
        return -1;
    }
    pPkg_func();

    return 0;

}
