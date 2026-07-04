'''total=1
n=int(input())
def  fact(i,total):
            if i > n:
                return fact
            total=total*i
            return fact(i+1,total=total+1)    
print("",fact(1,total))
'''
'''arr=[2,4,5,6,7,2,3,4,5,6]
hash={}
for i in range(len(arr)):
            if arr[i] in hash:
                hash[arr[i]]+=1
            else:
                hash[arr[i]]=1
print(hash[])'''
'''arr=[1,1]
i=0
if arr[i]<arr[i+1]:
        print(i)
else:
        print(i+1)
'''
nums=[0,3,7,2,5,8,4,6,0,1]
count=0
nums = sorted(set(nums))
n=len(nums)  
max_count=0
for i in range(1,n):
          if nums[i]-nums[i-1]==1:
              count+=1
              max_count=max(max_count,count)
          else:
              count=0
max_count+=1
print(max_count)
