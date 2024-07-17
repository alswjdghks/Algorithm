n = int(input())
students = []
for i in range(n):
    name,score = input().split()
    score = int(score)
    students.append((name,score))

result = sorted(students,key = lambda student: student[1])
for student in result:
    print(student[0], end = " ") 
