n,k = map(int,input().split())

a = list(map(int,input().split()))
b = list(map(int,input().split()))

for _ in range(k):
    A_min_index = a.index(min(a))
    B_max_index = b.index(max(b))
    if a[A_min_index] >= b[B_max_index]:
        break
    a[A_min_index],b[B_max_index] = b[B_max_index],a[A_min_index] 

print(sum(a))