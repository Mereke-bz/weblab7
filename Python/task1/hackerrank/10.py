import sys

def solve():
    data = sys.stdin.read().split('\n')
    idx = 0
    t = 1  
    
    while idx < len(data):
        line = data[idx].strip()
        if not line:
            idx += 1
            continue
        
        n = int(line)
        idx += 1
        
        
        headers = data[idx].strip().split()
        idx += 1
        marks_col = headers.index('MARKS')
        
        total = 0
        for _ in range(n):
            row = data[idx].strip().split()
            idx += 1
            total += int(row[marks_col])
        
        avg = total / n
        print(f"{avg:.2f}")

solve()