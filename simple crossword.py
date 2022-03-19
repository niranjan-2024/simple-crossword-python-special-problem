# cook your dish here
#inputs
n,m =map(int,input().split())
l=[]
l2=[]
zzz=0
for _ in range(n):
    s=input()
    s1=list(s)
    s2=list(s)
    l.append(s1)
    l2.append(s2)

w=int(input())
d=dict()
for _ in range(w):
    x=input()
    y=len(x)
    d[y]=x

#problem solving
for  i in range(n) :
    ind=[]
    for j in  range(m):
        if(l[i][j]=='r' or l[i][j]=='b'):
            ind.append(j)
    if(len(ind)==2):
        le=ind[1]-ind[0]  +1
        z=0
        for k in range(ind[0],ind[1]+1):
            l2[i][k]=d[le][z]
            z+=1

for  i in range(m) :
    ind=[]
    for j in  range(n):
        
        if(l[j][i]=='c' or l[j][i]=='b'):
            ind.append(j)
        
        
    if(len(ind)==2):
        le=ind[1]-ind[0]  +1
        
        z=0
        for k in range(ind[0],ind[1]+1):
            var =l2[k][i]
            l2[k][i]=d[le][z]
            if(var!='.' and var !='c' and var!='b'):
                if(var!=l2[k][i]):
                    
                    zzz=1
                
           
            z+=1
#output
if(zzz==0):
    for p in  range(n):
        for q in range(m):
            print(l2[p][q],end="")
        print()
else:
    print("Invalid")
    
    
    
    
    
"""
test case 
input:

8 8
b.c..r##
.#r.r###
.#rr####
.#c#####
.#######
.#######
.#######
c#######
5
solution
sample
many
ash
no

output:

sample##
o#ash###
l#no####
u#y#####
t#######
i#######
o#######
n#######
"""
