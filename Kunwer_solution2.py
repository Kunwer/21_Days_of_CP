T=int(input())
first=''
second=''
list=[]
for i in range(T):
    n=int(input())
    b=str(n)
    c=int(b[::-1])
    for d in range(2,n):
        if n%d==0:
            first='no'
            break
        else:
            first='yes'
            
    for e in range(2,c):
        if c%e==0:
            second='no'
            break
        else:
            second='yes'
    if first=='yes'and second=='yes':
        list.append('yes')
    else:
        list.append('no')
for z in range(T):
    print(list[z])
