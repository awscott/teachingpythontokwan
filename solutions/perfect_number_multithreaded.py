import sys
import threading
from multiprocessing import Pool
import os
import argparse
import time

def make_threads_and_pool(function,num_threads = None,max_number = None):
	""" takes in a function object and the number of threads and max number to check
		will call a function that takes a list with [start_of_range,end_of_range] and join all results.
	"""
	chunk_size = int(max_number / num_threads)
	last = 0
	proc_args = []

	for i in range(1, num_threads +1): 
		low = last
		high = low + chunk_size
		if i == num_threads: #on the case that the chunck size truncated
			high = max_number
		last = high
		proc_args.append((low,high))
		print('process:',i,'has',low,'and',high)
		#makes a new process for each range of max number / 5 until max
	pool = Pool(processes=num_threads)
	list_perf = []

	for result in pool.map(function, proc_args):
		list_perf.extend(result)
	return list_perf

def find_perf_in_range(range_list):
	low, max_number = range_list #breaks up list of 2 and asignes them to vars

	#write code here
	#...
	perfect = []
	for num in range(low, max_number+1):
		if is_perfect(num):
			if num != 1:
				perfect.append(num) 
	return perfect



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
	parser = argparse.ArgumentParser(description='find perfect numbers below maximum')
	parser.add_argument('maximum', type=int,help='the highest value to check for perfect number under')
	parser.add_argument('-t',type=int,help='The amount of threads [default:5]',default=5)
	parser.add_argument('-T',help='output the amount of time elapsed during run',action='store_true')
	args = parser.parse_args()


	if args.T:
		time1 = time.time()
	perfects = make_threads_and_pool(find_perf_in_range,args.t,args.maximum)
	if args.T:
		time2 = time.time()
		print(perfects)
		print ('\nElapsed time %.3fs' % (time2-time1))
	else:
		print(perfects)
	print('done')
