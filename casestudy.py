'''
n=5
for i in range(n+1,0,-1):
    for j in range(i):
        print("*",end="")
    print()
'''
'''
n=5
for i in range(n+1):
    for j in range(2*(n-i)+1):
        print("*",end=" ")
    print()
'''
'''
n=5
for i in range(n):
    for j in range(i):
        print(" ",end="")
    for k in range(2*n-2*i-1):
        print("*",end="")
    print()
'''
'''
n=5
for i in range(n+1):
    for j in range(n-i):
        print(" ",end="")
    for k in range(i):
        print("*",end="")
    print()
'''
'''
n=5
for i in range(n-1):
    for j in range(n-1-i):
        print(" ",end="")
    for k in range(i*2+1):
        print("*",end="")
    print()
for i in range(n-1,-1,-1):
    for j in range(n-i-1):
        print(" ",end="")
    for k in range(i*2+1):
        print("*",end="")
    print()
 '''
'''
n=5
for i in range(n-1,-1,-1):
    for j in range(n-i-1):
        print(" ",end="")
    for k in range(i*2+1):
        print("*",end="")
    print()
for i in range(1,n):
    for j in range(n-1-i):
        print(" ",end="")
    for k in range(i*2+1):
        print("*",end="")
    print()

'''
'''
#hollow diamond
==========
   *
  * *
 *   *
*     *
 *   *
  * *
   *

n=4
for i in range(n-1):
    for j in range(n-i-1):
        print(" ",end="")
    for j in range(i*2+1):
        if j==0 or j==i*2 or i==n-1:
            print("*",end="")
        else:
            print(" ",end="")
    print()
for i in range(n-1,-1,-1):
    for j in range(n-i-1):
        print(" ",end="")
    for j in range(i*2+1):
        if j==0 or j==i*2:
            print("*",end="")
        else:
            print(" ",end="")
    print()

'''
'''
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5 

n=5
for i in range(n):
    for j in range(1,i+2):
        print(j,end=" ")
    print()
'''
'''
   *
  * *
 *   *
*******

n=5
for i in range(n+1):              # i goes from 0 to 4
    for j in range(n-i-1):        # spaces before stars
        print(" ", end="")
    for j in range(i*2+1):        # stars and spaces
        if j==0 or j==i*2 or i==n-1:  # first, last star or bottom row
            print("*", end="")
        else:
            print(" ", end="")
    print()

'''
'''
==========
*******
 *   *
  * *
   *

n=4
for i in range(n-1,-1,-1):
    for j in range(n-i-1):
        print(" ",end="")
    for j in range(i*2+1):
        if j==0 or j==i*2 or i==n-1:
            print("*",end="")
        else:
            print(" ",end="")
    print()
'''
'''
===== RESTART: C:/Users/Abhilash/OneDrive/Desktop/Pythod IDLE/casestudy.py =====
    1
   21
  321
 4321
54321

n=5
for i in range(n):
    for j in range(n-i-1):
        print(" ",end="")
    for k in range(i+1,0,-1):
        print(k,end="")
    print()
'''
'''
===== RESTART: C:/Users/Abhilash/OneDrive/Desktop/Pythod IDLE/casestudy.py =====
    1
   212
  32123
 4321234
543212345



n=5
for i in range(n):
    for j in range(n-i-1):
        print(" ",end="")
    for k in range(i+1,0,-1):
        print(k,end="")
    for m in range(2,i+2):
        print(m,end="")
    print()
 '''
n=5
for i in range(n):
    for j in range(i):
        print(" ",end="")
    for k in range(2*n-2*i-1):
        print("*",end="")
    print()













