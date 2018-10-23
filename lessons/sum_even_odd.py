import sys
# given a number return the sum of all the even numbers
# the only point is to use your previously created methods in python and use them here


def sum_even(number):
	""" 
	sum up all the the even numbers between 0 and number inclusive
	return the result when you are finished
	"""

def sum_odd(number):
	""" 
	sum up all the the odd numbers between 0 and number inclusive
	return the result when you are finished
	"""

def even(x):
	""" copy paste of nicks test code"""
	if int(sys.argv[1])%2 == 0:
		print("This shit's even")
	else:
		print('probs odd')




if __name__ == '__main__':
	print(sum_even(sys.argv[1]))