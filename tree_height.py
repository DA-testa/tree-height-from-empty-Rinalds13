# 221RDB152 Rinalds Ulmanis 7. grupa
# python3

import sys
import threading


def compute_height(n, parents):
    ch = [[] for _ in range(n)]
    r = None
    for i in range(n):
        parent = parents[i]
        if parent == -1:
            r = i
        else:
            ch[parent].append(i)
    stack = [(r, 0)]
    max_height = 0

    while stack:
        n, height = stack.pop()
        max_height = max(max_height, height)

        for c in ch[n]:
            stack.append((c, height + 1))
    return max_height


def main():
    ievades_veidas = input()

    if "I" in ievades_veidas:
        n = int(input())
        
        parents = list(map(int, input().split()))
        height = compute_height(n, parents)
        print(height + 1)
        
    elif "F" in ievades_veidas:
        nosaukums = input()
        
        with open("test/" + nosaukums, 'r') as fails:
            n = int(fails.readline())
            parents = list(map(int, fails.readline().split()))
            height = compute_height(n, parents)
            print(height + 1)
            
    else:
        print("error")
        exit()


sys.setrecursionlimit(10 ** 7)  # max depth of recursion
threading.stack_size(2 ** 27)  # new thread will get stack of such size
threading.Thread(target=main).start()
