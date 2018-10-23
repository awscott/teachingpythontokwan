import sys


def main(max_number):
	
	print(max_number)
	#write code here
	#...
	perfect = []
	for num in range(0, max_number+1):
		if is_perfect(num):
			perfect.append(num) 

	print(perfect[1:]) 



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
	total = 0
	for i in num_list:
		total += i
	return total
## random things about numbers
# x / y is x divided by y
# x % y is the remander of the division of x and y
# 6 % 4 is 2 because 1 four fits in then no more 4s can go in there with out busting, but 2 can be added now to get 6
# 10 % 3 is 1 cause 3 + 3 + 3 is 9 and thats one away from 10
# 8 % 4 is 0 cause there is no remainder


if __name__ == '__main__':
	max_number = int(sys.argv[1])
	main(max_number)
