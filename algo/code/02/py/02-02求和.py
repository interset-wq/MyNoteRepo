"""求和 计算不大于n的项的总和
1 + 4 + 10 + ... 
后一项 = (前一项 + 1) * 2
"""

def get_sum(n: int) -> int:
    sum = 0
    i = 1
    while i <= n:
        sum += i
        i += 1
        i *= 2
    return sum

if __name__ == '__main__':
    n = 5
    print(get_sum(n)) # 5