#option 1, sorted function built off timsort
#built from merge sort/ insertion sort
#time complexity: n log n 
def find_second_smallest(my_list):
    if len(my_list) < 2:
        return None
    sorted_list = sorted(my_list)
    return sorted_list[1]

#custom alg to find 2nd smallest item
#time complexity is On b/c you only iterate through once
def find_second_smallest_v2(my_list):
    if len(my_list) < 2:
        return None
    smallest = float('inf')
    second_smallest = float('inf')

    for num in my_list:
        if num < smallest:
            second_smallest = smallest
            smallest = num
        elif num < second_smallest:
            second_smallest = num
    return second_smallest

print(find_second_smallest_v2([5, 8, 3, 2, 6]))
