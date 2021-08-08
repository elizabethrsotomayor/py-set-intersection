n = int(input())
m = input().split()

eng = set([int(i) for i in m])

b = int(input())
c = input().split()

fr = set([int(j) for j in c])

print(len(eng.intersection(fr)))
