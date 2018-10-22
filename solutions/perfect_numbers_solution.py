import sys
#basic perfect numbers solution
def main(max_number):
	
	print(max_number)
	#write code here
	#...
	perfect = []
	for num in range(0, max_number+1):
		if is_perfect(num):
			perfect.append(num) 
	print(perfect) 


def is_perfect(number):
	""" 
	Desc: kwan will write code here that checks if the number passed into this function is a "perfect number"
		if so it will return True, otherwise it will return False
	Args: number (int): a number to determine if is perfect.
	Return: returns True or False 
	"""
	factors = []
	if number == 0:
		return False
	for integer in range(1,number):
		if number % integer == 0:
			factors.append(integer)
	
	total = sum_list(factors)
	if total == number:
		return True #code here, obviously return true is not always gonna work
	return False

def sum_list(num_list):
	total = 0
	for i in num_list:
		total += i
	return total


if __name__ == '__main__':
	max_number = int(sys.argv[1])
	main(max_number)
