def selection_sort(arr):
    n=len(arr)
    for i in range(n):
        mini=i
        for j in range(i+1,n):
            if arr[j]<arr[mini]:
                mini=j
        arr[i],arr[mini]=arr[mini],arr[i]
        # print(arr)
    return arr
arr=[5,17,13,20,6,12]
print(selection_sort(arr))