n = int(input())
num = []
for i in range(n):
    num.append(int(input()))
reverseNum = sorted(num,reverse=True)
print(reverseNum)