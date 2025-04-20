def selection_sort(arr):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[j] < arr[i]:
                arr[i], arr[j] = arr[j], arr[i]  
    return arr

print(selection_sort([5, 3, 8, 4, 2]))
