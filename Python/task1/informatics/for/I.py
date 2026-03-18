import math

a = int(input())
sum = 0
i = 1

while(i <= math.sqrt(a)):
    if(a % i == 0):
        sum += 1
        if(i != a / i):
            sum += 1
    i += 1

print(sum)