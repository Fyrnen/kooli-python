#Comparison of different sorting methods in python

The methods currently implemented are bubble sort, insertion sort and quicksort.
The program runs all the sorting algorithms over a shared list and measures the time spent to do so.
As a "safeguard" to prevent the algorithms from working too long, it stops whenever a function takes over 1 minute to complete its sorting.
The script increases the size of the list every cycle starting from 1,000 and going up to 1,000,000 integers.
To generate said lists, the script uses python's in-built random.randint() function.
