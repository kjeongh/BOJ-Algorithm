import sys
input = sys.stdin.readline
T = int(input())
ans = []
for _ in range(T):
    a,b = map(int,input().split())
    aa = a%10
    
    #경우의 수 1가지
    if aa == 0: print(10)
    elif aa in [1,5,6]: print(aa)
    
    elif aa in [4,9]: #경우의 수 2가지
        bb = b%2
        if bb == 0:
            print(aa*aa%10)
        else: print(aa)
    else: #경우의 수 4가지
        bb = b%4
        if bb == 0: print(aa**bb%10)
        #ans.append(aa**(bb%4)%10)


#안해썅