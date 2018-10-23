import os
import sys
currDir = os.getcwd()
sys.path.append(os.path.abspath(currDir) + "/lessons")
from perfect_numbers import is_perfect, find_all_perfect
from sum_even_odd import sum_even, sum_odd, even, odd

