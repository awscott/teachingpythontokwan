# written by nick kwan
# sum all numbers below n
import sys
# from pudb import set_trace; set_trace()
# x = int(sys.argv[2])


# list = sys.argv
# some_value = x-1


# y = some_value
# from pudb import set_trace; set_trace()
def sumbelow(x):
	total = 0
	for y in range(0,x):
		total = total + y
		# y = y - 1
	return total

def factz(x):
	total = 1
	for y in range(1,x):
		total = total * y
		# y = y - 1
	return total

def even(x):

	if int(sys.argv[1])%2 == 0:
		print("This shit's even")
	else:
		print('probs odd')

if sys.argv[2] == "factoral":
	print("factoral = ", factz(int(sys.argv[1])))

if sys.argv[2] == "sumbelow":
	print("sum below three = ", sumbelow(int(sys.argv[1])))

even(int(sys.argv[1]))


