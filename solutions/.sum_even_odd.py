import sys
# given a number return the sum of all the even numbers
# the only point is to use your previously created methods in python and use them here


def sum_even(number):
	""" 
	sum up all the the even numbers between 0 and number inclusive
	return the result when you are finished
	"""
	total = 0
	for i in range(0,number+1):
		if even(i):
			total += i
	return total
	
def sum_odd(number):
	""" 
	sum up all the the odd numbers between 0 and number inclusive
	return the result when you are finished
	"""
	total = 0
	for i in range (0,number+1):
		if odd(i):
			total += i
	return total

def even(x):
	""" 
	this function should return True if the given number (x) is even otherwise False
	"""
	return int(x) % 2 == 0

def odd(x):
	"""should return True if number is odd, else False """
	return not int(x) % 2 == 0


if __name__ == '__main__':
	print(sum_even(sys.argv[1]))