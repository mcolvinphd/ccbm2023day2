from random import choice
import matplotlib.pyplot as plt
npart=300
sides=[]
avetimes=[]
steps = [(1,0),(-1,0),(0,1),(0,-1)]
for side in range(21,102,10):   #Loop over different size boxes
    grid=[[0 for x in range(side)] for y in range(side)]
    time=0
    for ipart in range(npart):
        # Start particle at center
        x,y = side//2,side//2
        counter=0
        # perform the random walk until particle departs
        while 1:
            counter+=1
            grid[x][y]=0   #Remove particle from current spot
            # Randomly move particle
            sx,sy = choice(steps)
            x += sx
            y += sy
            if x<0 or y<0 or x==side or y==side:
                time+=counter
                break
            grid[x][y]=1   #Put particle in new location
    avetime=time/npart
    sides.append(side**2)
    avetimes.append(avetime)
    print("side=%3d <t>=%7.2f  <t>/r2=%5.2f"%(side,avetime, avetime/(side**2)))
plt.plot(sides,avetimes)
plt.xlabel("Side length squared")
plt.ylabel("Ave escape time")
plt.show()

