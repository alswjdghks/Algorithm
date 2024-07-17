n = int(input())
traveler_loc = [1,1]
plans = list(input().split())

for plan in plans:
    if plan == 'R' and traveler_loc[1] != n:
        traveler_loc[1] += 1
    elif plan == 'L'and traveler_loc[1] != 1:
        traveler_loc[1] -= 1
    elif plan == 'U' and traveler_loc[0] != 1:
        traveler_loc[0] -= 1
    elif plan == 'D' and traveler_loc[0] != n:
        traveler_loc[0] += 1
print(traveler_loc[0] , traveler_loc[1])