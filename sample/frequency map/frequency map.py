# using frequency method
'''arr=[2,4,5,6,7,2,3,4,5,6]
freq=dict()
for i in range(len(arr)):
      if arr[i] in freq:
          freq[arr[i]]+=1  #if already there the key will just increment by 1
      else:
          freq[arr[i]]=1   #if key not in there or the val is entering first time the key will be 1 
print(freq)'''

arr=[2,4,5,6,7,2,3,4,5,6]
hash={}
for i in  range(len(arr)):
    hash[arr[i]]=hash.get(arr[i],0)+1 
print(hash)
#in here hash.get(arr[i],0)+1 
# checks that is this value is already in this dict 
# if not it assume its key as 0 and add with 1 to set key 
# as 1 with repect to that value..else there is number in dict 
# it the 1 will add with the key which is returned