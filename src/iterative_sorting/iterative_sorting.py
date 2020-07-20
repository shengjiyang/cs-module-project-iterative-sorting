def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # (hint, can do in 3 loc)
        for j in range(cur_index + 1, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j

        arr[smallest_index], arr[cur_index] = arr[cur_index], arr[smallest_index]

    return arr


def bubble_sort(arr):
    # i = cur_index, j = next_index
    for i in range(len(arr) - 1):
        # limits range to only two values at a time
        for j in range(len(arr) - i - 1):
            # compare cur_index and next_index values
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr

'''
STRETCH: implement the Counting Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''
def counting_sort(arr, maximum=None):
    if len(arr) == 0:
        return arr

    if maximum == None:
        maximum = max(arr)

    if any(n < 0 for n in arr) == True:
        return "Error, negative numbers not allowed in Count Sort"

    counts = []
    for i in range(0, maximum + 1):
        counts.append(arr.count(i))

    for j in range(1, len(counts)):
        counts[j] = counts[j] + counts[j - 1]

    counts = counts[:-1]
    counts.insert(0, 0)

    return counts


if __name__ == "__main__":
    print(counting_sort([1, 5, 8, 4, 2, 9, 6, 0, 3, 7]))