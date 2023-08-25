def insertionSort(items):

    for i in range(1,len(items)):
        key_item = items[i]
        j = i - 1
        while j>=0 and items[j] > key_item:       
            items[j+1] = items[j]
            j = j -1
        items[j+1] = key_item
      
    print(items)
    return items
    

it = [8, 6, 10, 5, 7, 2,2,8,9,12,15,16,20,88,45,96,102,44,1,9,-1]

expected = sorted(it)
resultado = insertionSort(it)



if expected == resultado:
    print("passed")



