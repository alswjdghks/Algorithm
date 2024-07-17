n = int(input())
k = list(map(int,input().split()))

food = [0] * (n+1)

even_food = [ k[i] for i in range(n) if i%2 == 0 ]
odd_food = [ k[i] for i in range(n) if i%2 == 1 ]

print(max(sum(even_food),sum(odd_food)))
