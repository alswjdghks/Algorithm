n = int(input())
array = list(map(int,input().split()))

max_food = [0] * 100
max_food[0] = array[0]
max_food[1] = max(array[1],array[0])
for i in range(2,n):
    max_food[i] = max(max_food[i-1],max_food[i-2]+array[i])

print(max_food[n-1])