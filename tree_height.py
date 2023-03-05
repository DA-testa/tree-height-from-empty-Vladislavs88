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
  while(dala != -1):
    dala=koks[dala]
    dzilums=dzilums+1
  return dzilums  


  
#   def dzilums(i):
#     if parents[i] == -1:
#       koks[i] =1
    
#     if koks[i] !=0:
#       return koks[i]
 
    
#     else:
#       koks[i]=dzilums(parents[i])+1
#     return koks[i]
    

    
#   for i in range(n):
#     dzilums(i)
#   return int(max(koks))  
  
def main():
    teksts=input()
    
    if "I" in teksts:
        cipari=int(input())
        parents=list(map(int,input().split()))


      
    elif "F" in teksts:
        nosaukums=input()
        if "a" not in nosaukums:
            with open(str("test/" + nosaukums), mode="r") as fail:
                skaitit=int(fail.readline())
                parents=list(map(int,input().split()))
                
    else:
        print("Kluda")
    ptint(compute_height(skaitit,parents))
        

    

# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
main()
# print(numpy.array([1,2,3]))
