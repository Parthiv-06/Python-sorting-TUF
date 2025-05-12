# # def merge(arr,left,mid,right):
# #     low=left
# #     high=mid+1
# #     temp=arr.copy()
# #     k=0

# #     while (low<=mid and high<=right):

# #         if temp[low]<=temp[high]:
               
# #                arr[k]=temp[low]
# #                low+=1
# #                k+=1
# #         else:
# #              arr[k]=temp[high]
# #              k+=1
# #              high+=1
# #     while(low<=mid):
# #         arr[k]=temp[low]
# #         k+=1
# #         low+=1
# #     while(high<=right):
# #          arr[k]=temp[high]
# #          k+=1
# #          high+=1
    
# # def merge_sort(arr,left,right):
# #      if left>=right:
# #           mid=(left+right)//2
# #           merge_sort(arr,left,mid)
# #           merge_sort(arr,mid+1,right)
# #           merge(arr,left,mid,right)
     
# # if __name__=="__main__":
# #      arr=[5,17,13,20,6,12]
# #      merge_sort(arr,0,5)
# #      for i in range(6):
# #           print(arr[i])


# def merge(arr,left,mid,right):
#     n1=mid-left+1
#     n2=right-mid
#     L=[0]*n1
#     R=[0]*n2
#     for i in range(n1):
#         L[i]=arr[left+i]
#     for i in range(n2):
#         R[i]=arr[mid+1+i]
#     low=0
#     high=0
#     k=0
#     while (low<=n1 and high<=n2):
#         if L[low]<=R[high]:
#             arr[k]=L[low]
#             low+=1
#             k+=1
#         else:
#             arr[k]=R[high]
#             k+=1
#             high+=1
#     while (low<=n1):
#         arr[k]=L[low]
#         low+=1
#         k+=1
#     while (high<=n2):
#         arr[k]=R[high]
#         high+=1
#         k+=1
# def merge_sort(arr,left,right):
#     if left<=right:
#         mid=(left+right)//2
#         merge_sort(arr,left,mid)
#         merge_sort(arr,mid+1,right)
#         merge(arr,left,mid,right)
# arr=[5,17,13,20,6,12]
# merge_sort(arr,0,5)
# for i in range(6):
#     print(arr[i])

def merge(arr,left,mid,right):
    n1=mid-left+1
    n2=right-mid
    L=[0]*n1
    R=[0]*n2
    for i in range(n1):
        L[i]=arr[left+i]
    for j in range(n2):
        R[j]=arr[mid+1+j]
    i=0
    j=0
    k=left
    while i<n1 and j<n2:
        if L[i]<R[j]:
            arr[k]=L[i]
            i+=1
            k+=1
        else:
            arr[k]=R[j]
            j+=1
            k+=1
    while i<n1:
        arr[k]=L[i]
        i+=1
        k+=1
    while j<n2:
        arr[k]=R[j]
        j+=1
        k+=1
def merge_sort(arr,left,right):
    if left<right:
        mid=(left+right)//2
        merge_sort(arr,left,mid)
        merge_sort(arr,mid+1,right)
        merge(arr,left,mid,right)
def printarray(arr):
    for i in arr:
        print(i,end=" ")
arr=[11,13,9,8,7,15]
merge_sort(arr,0,len(arr)-1)
printarray(arr)