def partition(arr,low,high):
    pivot=arr[low]
    i=low
    j=high
    while i<j:
        while pivot>arr[i] and i<=high:
            i+=1
        while pivot<arr[j] and j>=low:
            j-=1
        if i<j:
            arr[i],arr[j]=arr[j],arr[i]
    return i

def quick_sort(arr,low,high):
    if low<high:
        pi=partition(arr,low,high)
        quick_sort(arr,low,pi-1)
        quick_sort(arr,pi+1,high)

arr=[5,17,13,20,6,12]
quick_sort(arr,0,5)
print(arr)
