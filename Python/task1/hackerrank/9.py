import sys
from collections import defaultdict

def solve():
    input_data = sys.stdin.read().split()
    idx = 0
    
    n, m = int(input_data[idx]), int(input_data[idx+1])
    idx += 2
    
    
    positions = defaultdict(list)
    for i in range(n):
        word = input_data[idx]
        idx += 1
        positions[word].append(i + 1)  
    
    
    results = []
    for _ in range(m):
        word = input_data[idx]
        idx += 1
        if word in positions:
            results.append(' '.join(map(str, positions[word])))
        else:
            results.append('-1')
    
    print('\n'.join(results))

solve()