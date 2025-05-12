def insertion_sorting(arr):
    n=len(arr)
    for i in range(n):
        j=i
        while j>0 and arr[j-1]>arr[j]:
            arr[j-1],arr[j]=arr[j],arr[j-1]
            j-=1
        print(arr)
    return arr
arr=[5,17,13,20,6,12]
print(insertion_sorting(arr))