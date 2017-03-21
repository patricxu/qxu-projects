all: main

libadd:
	g++ -g -shared -fPIC add/add.*  -o libadd.so
    
libsub:
	g++ -g -shared -fPIC sub/sub.* -o libsub.so
  
libcalc: libadd libsub
	g++ -g -shared -fPIC calc/calc.*  -Iadd -Isub -L. -ladd -lsub -o libcalc.so

libpkg: libcalc
	g++ -g -shared -fPIC pkg/pkg.* -Icalc -L. -lcalc -o libpkg.so

libpkgRT: libcalc
	g++ -g -shared -fPIC pkg/pkg.* -Icalc -L. -lcalc -o libpkg.so    

#libpkg.so未与libcalc.so链接，虽然编译可以通过但是实际运行时会有如下错误
#./mainRTCrash.out: symbol lookup error: ./libpkg.so: undefined symbol: _Z4funcii
libpkgRTCrash: libcalc
	g++ -g -shared -fPIC pkg/pkg.* -Icalc -o libpkg.so 
    
main: libpkg
	g++ -g main.cpp -Ipkg -L. -lpkg -o main.out
    
mainRT: libpkgRT
	g++ -g mainRT.cpp -ldl -o mainRT.out
    
mainRTCrash: libpkgRTCrash
	g++ -g mainRT.cpp -ldl -o mainRTCrash.out
    
clean:
	rm -f *.so *.o *.out