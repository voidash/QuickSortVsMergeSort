import math

def mergesort(arr: list) -> list:
    left_pos = 0 
    right_pos = len(arr)
    if len(arr)  <= 1:
         return arr
    partition_position = (left_pos + right_pos)// 2
    left = mergesort(arr[0:partition_position])
    right = mergesort(arr[partition_position:right_pos])
    return merge(left, right)

def merge(left: list, right: list) -> list:
    merged_list = []
    # left finger and right finger denotes left and right array position 
    left_finger = 0 
    right_finger = 0
    if type(left[0]) is not str:
        left.append(math.inf)
        right.append(math.inf)
    else:
        left.append("zzzz")
        right.append("zzzz")
    while left_finger < len(left) - 1 or right_finger < len(right) - 1:
        if left[left_finger] <= right[right_finger]:
            merged_list.append(left[left_finger])
            left_finger+=1 
        elif right[right_finger] < left[left_finger]:
            merged_list.append(right[right_finger])
            right_finger+=1 
    return merged_list

        
# unsorted = [14,1,633,223,12,1223,132423423,23423234231332,34]
# print(mergesort(unsorted))






