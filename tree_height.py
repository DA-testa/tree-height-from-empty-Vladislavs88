# python3

import sys
import threading
# import numpy


                
def compute_height(n, parents):
    kids= []
    for i in range(n):
        if parents[i]==-1:
            root=i
        else:
            children[parents].append(i)
 def compute_dzilums(mezgls):
    if not kids[mezgls]:
        return 1
    max_height = 0
    for berns in kids[mezgls]:
        dzilums=compute_dzilums(berns)
        max_height=max(max_height,dzilums)
    return max_height +1
return compute_dzilums(root)
    
#     if node not in children:
#         return height
#     else:
#         childr_heights=[]
#         for childr in kids[mezgls]:
#             childr_heights.append(compute_height(childr,height+1))
       


def main():
    teksts=input()
    
    if "I" in teksts:
        cipari=int(input())
        parents=list(map(int,input().split()))
        viss=compute_height(n, parents)
        print(viss)       
    elif "F" in teksts:
        nosaukums=input()
        if "a" not in nosaukums:
            with open("test/" + nosaukums, "r") as fail:
                skaitit=int(fail.readline().split()))
                viss=compute_height(n, parents)
                print(viss)
    else:
        print("Kluda")
        

    

# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
main()
# print(numpy.array([1,2,3]))
