
ls=[[]]


arr=[[1,2,3],[1,3,4],[6,7,9]]
row=len(arr)
coloumn=len(arr[0])
print("upper triangle")
for i  in range(0,row):
   for j in range(0,coloumn):
       if j >= i:
           print( arr[i][j] ,end="   ")
       else:
           print("* ",end="  ")
   print("\n")
   
   
   
print("lower triangle")
for i  in range(0,row):
   for j in range(0,coloumn):
       if j >= i:
            print("* ",end="  ")
       else:
           print( arr[i][j] ,end="   ")
   print("\n")
   
print("only print diagonal")
for i  in range(0,row):
   for j in range(0,coloumn):
       if j == i:
           print( arr[i][j] ,end="   ")
       else:
           print("* ",end="  ")
   print("\n")
   