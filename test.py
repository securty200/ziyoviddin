n=int(input())
total=0
l=[]
for i in range(0,999):
    total = i%100

    if i + total == n:
        l.append(str(i))  
print(" ".join(l))