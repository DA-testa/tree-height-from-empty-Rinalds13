# python3

import sys
import threading


def compute_height(n, parents):
    # Write this function
    max_height = [0] * n
    # Your code here
    for i in range(n):
        j = i
        while j != -1:
            if max_height[j] != 0:
                break
            j = parents[j]

        if j == -1:
            max_height[i] = 1
        else:
            max_height[i] = max_height[j] + 1

    return max(max_height)


def main():
    # implement input form keyboard and from files
    nosaukums = input()
    if 'a' in nosaukums:
        print("Nepareizs nosaukums.")
        return
    try:
        with open(nosaukums) as file:
            n = int(file.readlines())
            parents = list(map(int, file.readlines().split()))
    except:
        return
    
    # let user input file name to use, don't allow file names with letter a
    # account for github input inprecision
    
    # input number of elements
    # input values in one variable, separate with space, split these values in an array
    # call the function and output it's result
    height = compute_height(n, parents)
    print(height)

# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
