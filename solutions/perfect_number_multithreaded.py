import sys
import threading
from multiprocessing import Process
import os

def find_perf_in_range(low,max_number):
	

	#write code here
	#...
	perfect = []
	for num in range(low, max_number+1):
		if is_perfect(num):
			perfect.append(num) 
	print( perfect )



def is_perfect(number):
	""" 
	Desc: kwan will write code here that checks if the number passed into this function is a "perfect number"
		if so it will return True, otherwise it will return False
	Args: number (int): a number to determine if is perfect.
	Return: returns True or False 
	"""

	if number == 0:
		return False
	factors = get_factors(number)
	total = sum(factors)
	if total == number:
		return True
	return False

def get_factors(number):
	""" Desc: this function get all the factors of a number using given that if all half of the
		numbers factors are below the square root, and for each factor below the relevant 
		factor above the square root is the original number / low factor
		ie: sqrt(16) = 4
			all factors <= 4
			1,2,4
			all factor > 4
			8,16 #how ever we do not care about 16

			given the factor 1 we can determin another fact with 16/1 == 16
			given 2 we know 8 is a facotor because its 16 / 2 
			and finally 4 is the squre root of 16
			we only need to check 1,2,3 and 4 to find all factors 
			instead of checking 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15, and 16
		Args: number (int): the number to determine the facots of
		return: a list of factors for the number given

	"""
	factors = [1]
	sqrt = number ** 0.5
	for i in range (2,int(sqrt)+1):
		if number % i == 0:
			if i == sqrt:
				factors.append(i)
			else:
				factors.extend([i,int(number/i)])
	return factors

def sum_list(num_list):
	""" sums a list of numers, because i forbid kwan to use sum() """

	total = 0
	for i in num_list:
		total += i
	return total

if __name__ == '__main__':
	max_number = int(sys.argv[1])
	chunk_size = int(max_number / 5)
	last = 0
	procs = []
	num_threads = 5
	for i in range(1, num_threads +1): 
		low = last
		high = low + chunk_size
		if i == num_threads: #on the case that the chunck size truncated
			high = max_number
		last = high


		print('process:',i,'has',low,'and',high)
		#makes a new process for each range of max number / 5 until max
		proc = Process(target=find_perf_in_range, args=(low,high))
		procs.append(proc)
		proc.start()

	for proc in procs:
		proc.join() #end the process
	print('done')
