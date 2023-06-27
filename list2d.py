from random import choice
list2d=[[choice((0,1)) for x in range(8)] for y in range(8)]
for x in range(8):
	print(list2d[x])