# 221RDB152 Rinalds Ulmanis 7. grupa 
# python3

import sys
import threading

def lasa_input():
    
    # kāds būs ievades veids
    ievades_veids = input("Ievades veids:")
    while ievades_veids not in ["I", "F"]:
        # ja nav ne I ne F
        ievades_veids = input("Nepareizs input type")

    # ja ievades veids ir I
    if ievades_veids == "I":
        n = int(input())
        parents = list(map(int, input().split()))
    # citādāk jāievada faila nosaukums
    else:
        nosaukums = input()
        # nevar saturēt burtu a
        while "a" in nosaukums:
            nosaukums = input("Nepareizs nosaukums")
        # meiģina atvērt failu
        try:
            with open("test/" + nosaukums, "r") as fails:
                n = int(fails.readline())
                parents = list(map(int, fails.readline().split()))
        # ja nesanāk nolasīt failu
        except:
            print("error faila lasīšanā")
            return lasa_input()

    return n, parents

# apreiķina augstumu
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
            stack.append((c, height+1))
    return max_height

def main():
    n, parents = lasa_input()
    height = compute_height(n, parents)
    print(height + 1)

sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
