n = int(input())
a = list(map(int, input().split()))
print(' '.join(str(a[i]) for i in range(0, n, 2)))