# python3

import sys
import threading
import numpy


                
def compute_height(n, parents):
  lielums=0
  
  koks= numpy.array(parents)
  for i in range(n):
      lielums=max(next(koks,i), lielums)
  return lielums

def next(koks,i):
    dzilums=1
    dala=koks[i]
    while(dala != -1 ):
      dala=koks[dala]
      dzilums=dzilums+1
    return dzilums



  
def main():
    teksts=input()
    
    
    
    
    
    
    if "I" in teksts:
        
        cipari=int(input())
        vecaki=list(map(int, input().split()))

    elif "F" in teksts:
        nosaukums=input()
        if "a" and "A"  not in nosaukums:
          with open("test/" + nosaukums, 'r') as fail:
                cipari=int(fail.readline())
                vecaki=list(map(int,fail.readline().split()))
        else:
            print("kluda")
    else:
      print("kluda") 
    print(compute_height(cipari, vecaki))
            
 
        
    

# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
