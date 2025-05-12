def bubble_sort(arr):
    n=len(arr)
    for i in range(n-1,0,-1):
        for j in range(i):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
        # print(arr)
    return arr

arr=[5,17,13,20,6,12]
print(bubble_sort(arr))