from random import choice
counter=0
while counter<100:
	print(counter)
	counter+=choice(range(10))

pop=100
while 1:
	pop=pop*1.1
	if pop>1000:
		break
print("Final pop=",pop)
