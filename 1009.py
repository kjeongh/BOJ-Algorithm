case = int(input())
arr = []
for x in range(0, case):
    arr.append(input().split())
for y in range(len(arr)):
    com_num = int(arr[y][0])**int(arr[y][1])%10
    if com_num == 0: print("10")
    else: print(com_num)