from timing import Timer
from mergesort import mergesort
from quicksort import quicksort
from listgenerator import ListDescendingIntegerGenerator, ListFloatGenerator, ListIntegerGenerator, ListStringGenerator, ListDescendingIntegerGenerator
from chartgen import generate_chart


number_of_elements = []
time_taken = []


def quicksort_generate_string_chart(filename,max, interval):
# for 10000 
    for i in range(0,max,interval):
        timer = Timer()
        unsorted_list = ListStringGenerator(i,50)
        timer.start()
        quicksort(unsorted_list,0,len(unsorted_list)-1)
        elapsed_time = timer.stop()
        number_of_elements.append(i)
        time_taken.append(elapsed_time)
    generate_chart(filename, number_of_elements,time_taken, "number of elements", "time taken (seconds)")
def mergesort_generate_string_chart(filename,max, interval):
# for 10000 
    for i in range(0,max,interval):
        timer = Timer()
        unsorted_list = ListStringGenerator(i,50)
        timer.start()
        sorted = mergesort(unsorted_list)
        elapsed_time = timer.stop()
        number_of_elements.append(i)
        time_taken.append(elapsed_time)
    generate_chart(filename, number_of_elements,time_taken, "number of elements", "time taken (seconds)")

def quicksort_generate_chart(filename,max, interval, descending=False):
# for 10000 
    for i in range(0,max,interval):
        timer = Timer()
        unsorted_list = []
        if not descending:
            unsorted_list = ListIntegerGenerator(i,0,1000)
        else:
            unsorted_list = ListDescendingIntegerGenerator(i,0,1000)
        
        timer.start()
        quicksort(unsorted_list,0,len(unsorted_list)-1)
        elapsed_time = timer.stop()
        number_of_elements.append(i)
        time_taken.append(elapsed_time)
    generate_chart(filename, number_of_elements,time_taken, "number of elements", "time taken (seconds)")

def mergesort_generate_chart(filename,max, interval, descending=False):
# for 10000 
    for i in range(0,max,interval):
        timer = Timer()
        if not descending:
            unsorted_list = ListIntegerGenerator(i,0,1000)
        else:
            unsorted_list = ListDescendingIntegerGenerator(i,0,1000)
        timer.start()
        sorted = mergesort(unsorted_list)
        elapsed_time = timer.stop()
        number_of_elements.append(i)
        time_taken.append(elapsed_time)
    generate_chart(filename, number_of_elements,time_taken, "number of elements", "time taken (seconds)")

# mergesort_generate_chart("mergesort_random_100000.png", 100000, 10000)
# mergesort_generate_chart("mergesort_random_1000000_descending.png", 1000000, 100000,descending=True)
# mergesort_generate_chart("mergesort_random_100000_descending.png", 100000, 10000,descending=True)
# quicksort_generate_chart("quicksort_random_100000_descending.png", 10000, 100,descending=False)
# quicksort_generate_chart("quicksort_random_1000000000_descending.png", 10000, 1000,descending=True)
mergesort_generate_string_chart("mergesort_string_10000.png", 10000,1000)
# quicksort_generate_string_chart("quicksort_string_10000.png", 10000,1000)







