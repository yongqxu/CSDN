
def binary_search(data, start, end, value):
    if start >= end:
        return -1
    mid = start + (end - start >> 1)
    #print('start={}, end={}, mid={}'.format(start, end, mid))
    if data[mid] == value:
        return mid
    elif data[mid] < value:
        return binary_search(data, mid + 1, end, value)
    else:
        return binary_search(data, start, mid - 1, value)

data = [2, 3, 1, 4, 5, 6, 6, 9, 10, -1]
data.sort()
print('search {}'.format(data))
print('found 5 at: ', binary_search(data, 0, len(data), 5))
print('found -1 at: ', binary_search(data, 0, len(data), -1))
print('found 11 at: ', binary_search(data, 0, len(data), 11))