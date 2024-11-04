# Linear Search or Sequential Search
# Brute Force Method (simple but slow)

my_list = [8, 5, 0, 3, 9, 7]
ITEM = 7

#function that searches for an item in the list
#if you find an item return true, if you make it through
#the entire structure without finding one return false
def search(item, listy):
    for element in listy:
        if element == item:
            return True
    return False


#brute force search that is very slow
#linear search increases with the size of the array/list 
#time complexity of On
print(search(ITEM, my_list))

ITEM_INDEX = my_list.index(ITEM)