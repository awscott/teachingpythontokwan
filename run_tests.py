import unittest
import os
import sys
import subprocess
import time
from decimal import Decimal
import signal
from lessons import *
class TestEvenOdd(unittest.TestCase):
	pass

class TestPerfectNumber(unittest.TestCase):
	def test_is_number_perfect(self):
		p_numbers = [6, 28, 496, 8128]
		for perf in p_numbers:
			self.assertTrue(is_perfect(perf))
		for i in range(0,1000):
			if i in p_numbers:
				continue
			self.assertFalse(is_perfect(i))

if __name__ == '__main__':
	sys.argv.append('-v')
	unittest.main(exit=False)
	sys.argv.remove('-v')