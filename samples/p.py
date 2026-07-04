  #prime numbers upto n numbers
n = int(input())
for j in range(2, n):
    for i in range(2, j):
        if j % i == 0:
            break
    else:
        print(j)