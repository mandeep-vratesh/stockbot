import multiprocessing
from multiprocessing import Pool, TimeoutError

print(multiprocessing.cpu_count())

def f(x):
	print(x)

if __name__ == '__main__':
        p = Pool(multiprocessing.cpu_count())
        p.map(f, [1,2,3])

