import sys
def get_sum(values):
	all_zeros = True
	for i in values:
		if i >= 0:
			all_zeros= False
	if all_zeros:
		return max(values)
	s = 0
	for i in values:
		if i > 0:
			s += i
	return s
def get_max_sum(values):
	_sum = 0
	_sum_after_neg = 0
	_neg_flag = False
	all_zeros = True
	for i in values:
		if i >= 0:
			all_zeros= False
	if all_zeros:
		return max(values)
	for i in range(len(values)):
		#print values[i]
		if values[i] >= 0 and _neg_flag == False:
				_sum += values[i]
		elif _neg_flag == True:
			_sum_after_neg += values[i]
			if _sum_after_neg >= 0:
				_neg_flag = False
				_sum += _sum_after_neg
				if values[i] > _sum:
					_sum = values[i]
		elif values[i] < 0 :# first negative value occurs
			_neg_flag = True
			_sum_after_neg = values[i]

			# if the sum between the negative and current index is positive
			# then add the sum with the actual sum
			

	return _sum



f = open('input.txt', 'r+')                             
sys.stdin = f   
T = int(raw_input())
for i in range(T):
	N = int(raw_input())
	values = raw_input().split()
	values = [ int(value) for value in values]
	#print values
	print get_max_sum(values), get_sum(values)
