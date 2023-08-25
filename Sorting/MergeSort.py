arr = [8, 6, 10, 5, 7, 2,-1]

def merge_sort(arr):
    if len(arr) > 1:
        mid_point = len(arr)//2
        left_arr = arr[:mid_point]
        right_arr = arr[mid_point:]

        merge_sort(left_arr)
        merge_sort(right_arr)

        x = y = k = 0

        while x < len(left_arr) and y < len(right_arr):
            if (left_arr[x] > right_arr[y]):
                arr[k] = right_arr[y]
                y+=1
                       
            else:
                arr[k] = left_arr[x]
                x+=1
                
            k+=1

        while x < len(left_arr):
            arr[k] = left_arr[x]
            x+=1
            k+=1
        while y < len(right_arr):
            arr[k] = right_arr[y]
            y+=1
            k+=1

        


        print("LEFT: ",left_arr)
        print("RIGHT: ",right_arr)
        print("array K: ",arr)


         
print(arr)
merge_sort(arr)