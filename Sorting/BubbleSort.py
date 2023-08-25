arr = [8, 6, 10, 5, 7, 2,-1]

def bubble_sort(arr):
    for x in range(0,len(arr)-1):
        for idx, y in enumerate(range(len(arr)-1-x,0,-1)):
            if (arr[idx] > arr[idx + 1]):
                arr[idx], arr[idx+1] = arr[idx+1], arr[idx]
    return arr


print(bubble_sort(arr))
