k = int(input())
per=[0]*(k*2+1)
per[k+1]=1
for i in range(k+2, k*2+1):
    per[i]= per[i-1]+per[i-2]
for i in range(k, -1, -1):
    per[i]=per[i+2]-per[i+1]
print(per)
