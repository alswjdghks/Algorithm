x = int(input())

count= [0] * 30000
values = [2,3,5]
result = 0

for i in range(2,x+1):
    count[i] = count[i-1] + 1
    for j in values:
        if i % j == 0:
            count[i] = min(count[i],count[i//j]+1)
    print("i =",i, count[i])
print(count[x])