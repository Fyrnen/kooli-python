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

def insertionsort(sample):
    length = len(sample)

    for i in range(length-1):
        j = i + 1
        
        while sample[i] > sample[j]:
            sample[i], sample[j] = sample[j], sample[i]

            if i != 0:
                i, j = i-1, j-1

    return sample

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
