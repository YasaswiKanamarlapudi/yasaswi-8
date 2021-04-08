slab=list(map(int,input().split()))
per=list(map(int,input().split()))
p=[x/100 for x in per]
rebate=int(input())
tax=list(map(int,input().split()))
N=len(slab)
mt=[0]
m=0
sal=[]
for i in range(N-1):
    m=m+(slab[i+1]-slab[i])*p[i]
    mt.append(m)
for i in tax:
    if(i>mt[-1]):
        t=i-mt[-1]
        a=t/p[-1]
        s=a+rebate+slab[-1]
        sal.append(s)
    else:
        for j in range(N-1):
            if(i>mt[j] and i<=mt[j+1]):
                t=i-mt[j]
                a=t/p[j]
                s=a+rebate+slab[j]
                sal.append(s)
print(int(sum(sal)))  

    
    
    

    
