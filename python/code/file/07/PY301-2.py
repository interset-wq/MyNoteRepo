'''
输入文件 ： candidate0.txt
输出文件 ： candidate.txt
'''

candidates = []
with open('candidate0.txt') as fi:
    for line in fi.readlines():
        parts = line.strip('\n').split()
        name = ' '.join(parts[:2])
        if all(int(part)>=60 for part in parts[2:-1]):
            candidates.append(name)
txt = '\n'.join(candidates)
with open('candidate.txt', 'w') as fo:
    fo.write(txt)
