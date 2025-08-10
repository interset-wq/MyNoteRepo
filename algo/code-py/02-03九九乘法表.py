"""九九乘法表"""

def mul_table() -> str:
    table = ''
    for i in range(1, 10):
        for j in range(1, i+1):
            table += f'{j}*{i}={i*j:>2}\t'
        table += '\n'
    return table.strip()

if __name__ == '__main__':
    table = mul_table()
    print(table)