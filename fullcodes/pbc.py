from random import choice
side=4
x=0
for i in range(30):
    x += choice((-1,1))
    if x < 0: x=side-1
    if x==side: x=0
    print(x)