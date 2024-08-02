"""upon creating a graph up to node 100, discovered that any path from the root to the target cell went down by
 exponents of 2 such that you could use the difference converted to binary to reconstruct the path from the root
  to the target"""


def find(bigboy, goal):
	diff = bigboy - goal
	diffl = reversed(bin(diff)[2:])
	n = 1
	value = bigboy
	for i in diffl:
		if i == '1':
			bigboy -= n
			value += bigboy
		n *= 2
	return value
