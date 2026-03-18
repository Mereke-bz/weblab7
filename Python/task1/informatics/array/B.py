n = int(input())
a = list(map(int, input().split()))
result = [str(x) for x in a if x % 2 == 0]
print(' '.join(result))