arr=[[1,1,1],[1,0,1],[1,1,1]]
row=len(arr)
col=len(arr[0])
r=[0]*row
c=[0]*col
for i in range(0,row):
   for j in range(0,col):
       if arr[i][j]==0:
           r[i]=-1
           c[j]=-1
for i in range(0,row):
       for j in range(0,col):
        if r[i]==-1 or c[j]==-1:
           arr[i][j]=0
print(arr)
            
           
           
         
       
            
