n,m = map(int,input().split())
card = [[0] * m for _ in range(n)]

for i in range(n):
    card[i] = list(map(int,input().split()))

maxValue = min(card[0])
for i in range(1,n):
    if min(card[i]) > maxValue:
        maxValue = min(card[i])    
print(maxValue)


#for i in range(n):
#   data = list(map(int, input().split()))
#   min_value = min(data)
#   result = max(result,min_value)

#print(result)
