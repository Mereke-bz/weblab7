n = int(input())
result = []
p = 1
while p <= n:
    result.append(str(p))
    p = p* 2

print(' '.join(result))