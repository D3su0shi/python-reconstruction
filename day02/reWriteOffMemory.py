numList = [1, 3, 5, 7, 9]

def binary_search(list, item):
    low = 0
    high = len(list) - 1


    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]

        if guess == item :
            return mid
        if guess > item :
            high = mid - 1
        else :
            low = mid + 1

    return None

position = binary_search(numList, 9)
print(position)

'''
    found some logic errors in the way the book was doing the binary search
    the mid was set to low + high and comapring guess with mid instead of the item
    so after fixing that i see the current way to write the code for it
'''