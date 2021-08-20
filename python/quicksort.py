from timing import Timer
def quicksort(arr: list, left : int , right : int):
    if(left >= right): return
    pivot = partition(arr, left, right)
    quicksort(arr, left, pivot-1)
    quicksort(arr,pivot, right)

def swap(arr,pos1,pos2):
    swap_variable = arr[pos1]
    arr[pos1] = arr[pos2]
    arr[pos2] = swap_variable

def partition(arr:list, left: int, right: int) -> int:
    #set compareposition position to end of the array always
    compare = right
    pivot_pos = left

    for t in range(left,right):
        if(arr[t] <= arr[compare]):
            swap(arr,t,pivot_pos)
            pivot_pos += 1
        
    swap(arr,pivot_pos,compare)
    return pivot_pos


# timer = Timer()

# unsorted = [56,12,13,1,89,4,356,72]
# timer.start()
# quicksort(unsorted, 0 , len(unsorted)-1)
# elapsed = timer.stop()
# print(elapsed)
# print(unsorted)

    


