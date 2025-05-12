def recursive_bubble_sort(arr,n):
    if n<0:
        return arr
    for j in range(n):
        if arr[j]>arr[j+1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]
    recursive_bubble_sort(arr,n-1)
arr=[5,17,13,20,6,12]
recursive_bubble_sort(arr,len(arr)-1)
print(arr)
    