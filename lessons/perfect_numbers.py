import sys


def main(max_number):

	print(max_number)
	#write code here
	#...
	perfect = []
	if is_perfect(max_number):
		perfect.append(max_number) #this is how you add things to a list. with list.append(), there is also remove() and pop() and so on...
	print(perfect) #delete all this and write your code, google if you need to



def is_perfect(number):
	""" 
	Desc: kwan will write code here that checks if the number passed into this function is a "perfect number"
		if so it will return True, otherwise it will return False
	Args: number (int): a number to determine if is perfect.
	Return: returns True or False 
	"""
	return True #code here, obviously return true is not always gonna work


## relevant info about numbers
# x / y is x divided by y
# x % y is the remander of the division of x and y
# 6 % 4 is 2 because 1 four fits in then no more 4s can go in there with out busting, but 2 can be added now to get 6
# 10 % 3 is 1 cause 3 + 3 +3 is 9 and thats one away from 10
# 8 % 4 is 0 cause there is no remainder

if __name__ == '__main__':
	max_number = int(sys.argv[1])# python perf.py 10000
	main(max_number) #should print 6 496 8128
