import unittest
import os
import sys
import subprocess
import time
from decimal import Decimal
import signal
from lessons import *
odds = [3,5,7,9,11]
evens = [2,4,6,8,10]

class TestEvenOdd(unittest.TestCase):
	def test_even(self):
		for i in odds:
			self.assertTrue(odd(i))
		for i in evens:
			self.assertFalse(odd(i))

	def test_odd(self):
		for i in evens:
			self.assertTrue(even(i))
		for i in odds:
			self.assertFalse(even(i))
	def test_sum_even(self):
		self.assertTrue(6 == sum_even(5) )
		self.assertTrue(650 == sum_even(50) )
	def test_sum_odd(self):
		self.assertFalse(9 == sum_odd(5) )
		self.assertFalse(625 == sum_odd(50) )

class TestPerfectNumber(unittest.TestCase):
	def test_is_number_perfect(self):
		p_numbers = [6, 28, 496, 8128]
		for perf in p_numbers:
			self.assertTrue(is_perfect(perf))
		for i in range(0,1000):
			if i in p_numbers:
				continue
			self.assertFalse(is_perfect(i))
	def test_all_perfect(self):
		p_numbers = [6, 28, 496, 8128]
		kwan_perf = find_all_perfect(10000)
		self.assertEqual(p_numbers,kwan_perf)

if __name__ == '__main__':
	sys.argv.append('-v')
	unittest.main(exit=False)
	sys.argv.remove('-v')