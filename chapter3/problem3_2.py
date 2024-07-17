# N,M,K를 공백으로 구분하여 입력받기
N,M,K = map(int,input().split())  # 5 8 3
# N개의 수를 공백으로 구분하여 입력받기
numbers = list(map(int,input().split())) # 2 4 5 4 6

numbers.sort() # 입력받은 수 정렬
total,count = 0,0
for i in range(M):
    if count >= K:
        count = 0
        total += numbers[-2] 
        continue
    total += numbers[-1]
    count += 1
print(total)

#가장 큰 수가 더해지는 횟수 계산

# fisrt = numbers[-1]
#second = numbers[-2]
#count = int(M / (K+1) ) * K
#count += M % (K+1)

#result = 0
#result += count*fisrt // 가장 큰 수 더하기
#result += (M - count) * second  // 두 번째로 큰 수 더하기
#print(result)

