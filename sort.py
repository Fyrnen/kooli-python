import random
import time
import sys

def bubblesort(sample):
    a = 0
    b = 1
    length = len(sample)

    for i in range(length):
        for j in range(length-1):
            if sample[a] > sample[b]:
                sample[a], sample[b] = sample[b], sample[a]

            a, b = a+1, b+1

        a = 0
        b = 1

    return sample

def insertionsort(sample):
    length = len(sample)

    for i in range(length-1):
        j = i + 1
        
        while sample[i] > sample[j]:
            sample[i], sample[j] = sample[j], sample[i]

            if i != 0:
                i, j = i-1, j-1

    return sample

def qs_partition(sample, start, end):
    length = len(sample)
    pivot = sample[end]
    index = start
    current = start

    while current < end:
        if sample[current] <= pivot:
            sample[current], sample[index] = sample[index], sample[current]
            index += 1

        current += 1

    sample[index], sample[end] = sample[end], sample[index]

    return index

def quicksort(sample, start, end):
    if start < end:
        index = qs_partition(sample, start, end)
        quicksort(sample, start, index-1)
        quicksort(sample, index+1, end)

    return sample

qs_numbers = []
in_numbers = []
bs_numbers = []
c_values = [1000, 2000, 5000, 10000, 20000, 50000, 100000, 200000, 500000, 1000000, 2000000, 5000000, 10000000]

for c in c_values:
    for i in range(c):
        n = random.randint(0, 5*c)
        qs_numbers.append(n)
        bs_numbers.append(n)
        in_numbers.append(n)

    print("List size:", c)
    
    qs_start_time = time.time()
    quickSortedNumbers = quicksort(qs_numbers, 0, len(qs_numbers)-1)
    qs_end_time = time.time()
    d_qs_time = qs_end_time - qs_start_time
    print("Quicksort runtime:", d_qs_time, "seconds")
    
    if d_qs_time > 60:
        sys.exit()
    
    in_start_time = time.time()
    insertionSortedNumbers = insertionsort(in_numbers)
    in_end_time = time.time()
    d_in_time = in_end_time - in_start_time
    print("Insertionsort runtime:", d_in_time, "seconds")

    if d_in_time > 60:
        sys.exit()
    '''
    bs_start_time = time.time()
    bubbleSortedNumbers = bubblesort(bs_numbers)
    bs_end_time = time.time()
    d_bs_time = bs_end_time - bs_start_time
    print("Bubblesort runtime:", d_bs_time, "seconds")

    if d_bs_time > 60:
        sys.exit()
    '''
    print("---")

    numbers = []
