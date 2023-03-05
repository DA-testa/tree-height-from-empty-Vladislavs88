# python3

import sys
import threading
import numpy

    n=int(input())
    parents=list(map(int,input().split()))
children= {}
    for i in range(n):
        if parents[i]==-1:
            root=i
        else:
            if parents[i] not in children;
            children[parents[i]]=[i]
            else:
                children[parents[i]].append(i)
                
def compute_height(n, parents):
    max_height = 0
    if node not in children:
        return height
    else:
        childr_heights=[]
        for childr in children[node]:
            childr_heights.append(compute_height(childr,height+1))
        
            
    
    # Write this function
  
    # Your code here
    return max_height
height=compute_height(root,0)
print(height)


def main():
    # implement input form keyboard and from files
    
    # let user input file name to use, don't allow file names with letter a
    # account for github input inprecision
    
    # input number of elements
    # input values in one variable, separate with space, split these values in an array
    # call the function and output it's result
    pass

# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
main()
# print(numpy.array([1,2,3]))
