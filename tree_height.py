# python3
# Vladislavs Sidorkins 221RDB070

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
            
 
        
 
sys.setrecursionlimit(10**7)  
threading.stack_size(2**27)   
threading.Thread(target=main).start()
