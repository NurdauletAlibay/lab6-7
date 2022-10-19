n = int(input())
dict = {}
for i in range(n):
    f, s = map(str, input().split())
    dict[f] = s
    dict[s] = f
s = str(input())
print(dict[s])