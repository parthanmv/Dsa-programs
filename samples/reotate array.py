num=[2,3,4,5,6,7]
num[:]= [num[-1]]+num[0:len(num)-1]
print(num)