import random
import time
import sys
from sort import *

qs_numbers, in_numbers, bs_numbers = [], [], []
qs_run, in_run, bs_run = True, True, True
qs_counter, in_counter, bs_counter = 0, 0, 0
c_values = [1000, 2000, 5000, 10000, 20000, 50000, 100000, 200000, 500000, 1000000, 2000000, 5000000, 10000000]

for c in c_values:
    for i in range(c):
        n = random.randint(0, 5*c)
        qs_numbers.append(n)
        bs_numbers.append(n)
        in_numbers.append(n)

    print("List size:", c)
    
    if qs_run:
        qs_start_time = time.time()
        quickSortedNumbers = quicksort(qs_numbers, 0, len(qs_numbers)-1)
        qs_end_time = time.time()
        d_qs_time = qs_end_time - qs_start_time
        print("Quicksort runtime:", d_qs_time, "seconds")
        qs_counter += 1
        
        if d_qs_time > 60:
            qs_run = False
    
    if in_run:
        in_start_time = time.time()
        insertionSortedNumbers = insertionsort(in_numbers)
        in_end_time = time.time()
        d_in_time = in_end_time - in_start_time
        print("Insertion sort runtime:", d_in_time, "seconds")
        in_counter += 1

        if d_in_time > 60:
            in_run = False
    
    if bs_run:
        bs_start_time = time.time()
        bubbleSortedNumbers = bubblesort(bs_numbers)
        bs_end_time = time.time()
        d_bs_time = bs_end_time - bs_start_time
        print("Bubble sort runtime:", d_bs_time, "seconds")
        bs_counter += 1

        if d_bs_time > 60:
            bs_run = False
        
    print("---")

    numbers = []
    
    if not any([qs_run, bs_run, in_run]):
        print("Quicksort:", qs_counter, "cycles.")
        print("Insertion sort:", in_counter, "cycles.")
        print("Bubble sort:", bs_counter, "cycles.")
        sys.exit()
