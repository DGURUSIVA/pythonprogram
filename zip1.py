a=[1,2,3]
b=[4,5,6]
c=[7,8,9]
out=[]
for i,j,k in zip(a,b,c):
    out=out+[i]+[j]+[k]
    print(out)
