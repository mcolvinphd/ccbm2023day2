N = 71
steps=0
while N != 1:
    print(N)
    steps += 1
    if N%2 == 0:
        N=N//2
    else:
        N = 3*N+1
print("steps=",steps)

