# BOJ 4358 생태학
# https://www.acmicpc.net/problem/4358

from sys import stdin
from collections import defaultdict

treeType = defaultdict(int)
count = 0

while True:
    tree = stdin.readline().strip()
    if tree == '': break
    treeType[tree] += 1
    count += 1

for tree, cnt in sorted(treeType.items(), key=lambda x:x[0]):
    print('%s %.4f'%(tree, cnt/count*100))