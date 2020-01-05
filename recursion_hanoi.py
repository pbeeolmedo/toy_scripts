## HANOI PROBLEM:
# |A| - |B| - |C|
# Move n disks stacked on top of each other from A -> C with hanoi rules
# From: computerphile youtube video on recursion
def move(f,t):
    # f = from 'position'
    # t = to 'position'
    print(f"Move disk from {f} to {t}.")

def hanoi(n,f,h,t):
    ## moves n disks from position "f" to position "t" using position "h" as intermediate
    # n = number of disks
    # f = from 'position'
    # h = helper 'position'
    # t = to 'position'

    if n == 0: #dont want negative 'n' in recursion
        pass
    else:
        hanoi(n-1,f,t,h) # move n-1 disks from "f" to the helper position "h"
        move(f,t) # move the remaining disk from "f" to the final "t"
        hanoi(n-1,h,f,t) # move the n-1 disks stuck in "h" through to "t" using the empty "f" as intermediate


hanoi(8,"A","B","C")