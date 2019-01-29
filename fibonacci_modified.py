

def fib(N):
	if N == 2:
		return second
	elif N == 1:
		return first
	else:
		v = fib(N-1)**2 + fib(N-2)
		return v

if __name__ == '__main__':
	#line = raw_input().split()
	first = 0
	second = 1
	N = int(5)
	print(fib(N))

