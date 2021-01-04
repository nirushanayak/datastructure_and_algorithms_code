import sys

def mergeKLists(lists):
    a = [0]*len(lists)
    result = list()
    for i in range(len(lists)):
        a[i] = lists[i].pop(0) if len(lists[i])>0 else sys.maxsize
    min = findMin(a)
    while a[min] != sys.maxsize:
        result.append(a[min])
        a[min] = lists[min].pop(0) if len(lists[min]) else sys.maxsize
        min = findMin(a)
    print(result)
    return result


def findMin(arr):
    min = 0
    for i in range(1, len(arr)):
        if arr[i] < arr[min]:
            min = i
    return min

lists = [[1,4,5],[1,3,4],[2,6]]
mergeKLists([[2],[4],[1],[3,5]])
