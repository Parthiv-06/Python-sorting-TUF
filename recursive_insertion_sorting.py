def recursive_insertion_sorting(arr,n,i):
    if i==n:
        return arr
    j=i
    while j>0 and arr[j]<arr[j-1]:
        arr[j],arr[j-1]=arr[j-1],arr[j]
        j-=1
    recursive_insertion_sorting(arr,n,i+1)
arr=[5,17,13,20,6,12]
recursive_insertion_sorting(arr,6,0)
print(arr)