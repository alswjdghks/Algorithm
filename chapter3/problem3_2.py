# N,M,K�� �������� �����Ͽ� �Է¹ޱ�
N,M,K = map(int,input().split())  # 5 8 3
# N���� ���� �������� �����Ͽ� �Է¹ޱ�
numbers = list(map(int,input().split())) # 2 4 5 4 6

numbers.sort() # �Է¹��� �� ����
total,count = 0,0
for i in range(M):
    if count >= K:
        count = 0
        total += numbers[-2] 
        continue
    total += numbers[-1]
    count += 1
print(total)

#���� ū ���� �������� Ƚ�� ���

# fisrt = numbers[-1]
#second = numbers[-2]
#count = int(M / (K+1) ) * K
#count += M % (K+1)

#result = 0
#result += count*fisrt // ���� ū �� ���ϱ�
#result += (M - count) * second  // �� ��°�� ū �� ���ϱ�
#print(result)

