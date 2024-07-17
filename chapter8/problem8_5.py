n,m = map(int,input().split())

count = [10001] * 10001
count[0] = 0
coin_value = []

for i in range(n):
    coin_value.append(int(input()))

for i in range(min(coin_value),m+1):
    min_count = count[i]
    for coin in coin_value:
        if count[i-coin] != 10001:
            if count[i - coin] + 1 < min_count:
                min_count = count[i-coin] + 1
    count[i] = min_count

if count[n] == 10001:
    print(-1)
else:
    print(count[n])
