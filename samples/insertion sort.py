key=0
arr=[5,4,3]
for i in range(0,len(arr)):
   if arr[i-1]>arr[i]:
     key=arr[i]
     j=i-1
     while j >= 0 and arr[j] > key:
         arr[j+1]=arr[j]
         j-=1
     arr[j+1]=key
print(arr)
                         