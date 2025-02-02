from ant_colony import *

def distance(start, end):
	x_distance = abs(start[0] - end[0])
	y_distance = abs(start[1] - end[1])
	print(x_distance,y_distance)
	# //c = sqrt(a^2 + b^2)
	import math
	return math.sqrt(pow(x_distance, 2) + pow(y_distance, 2))

# //given some nodes, and some locations...
test_nodes = {0: (0, 7), 1: (3, 9), 2: (12, 4), 3: (14, 11), 4: (8, 11), 5: (15, 6), 6: (6, 15), 7: (15, 9), 8: (12, 10), 9: (10, 7)}

# //...and a function to get distance between nodes...

# //...we can make a colony of ants...
start=[(0), (12)]
end=[(24), (24)]
colony = ant_colony(test_nodes, distance(start,end))

# //...that will find the optimal solution with ACO
answer = colony.mainloop()