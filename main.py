a=int(input())
N1=0
N2=1
for i in range(2,a+1):
    N3=N1+N2
    print(N3)
    N1=N2
    N2=N3