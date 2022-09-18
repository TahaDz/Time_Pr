import os


if __name__ == '__main__':
	
	a = list(range(1000,17000,255))
	i = 0
	n_data = 2000
	for index,ni in enumerate(a):
		for nj in a[index:]:
					if i < n_data:
						os.system("gcc Cfiles/gesummv.c -lOpenCL -lm -o Cfiles/gesummv.c -w -fcompare-debug-second")
						os.system("./Cfiles/gesummv 1 0 "+ str(ni)+" "+ str(nj))
						i += 1

	print(i)




	






