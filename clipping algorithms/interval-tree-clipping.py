'''
Application of trees in clipping:
When we have a set of lines parallel with the axis, we can use interval tree to optimize time.

Algorithm description:
- Project the segments on two axes
- Sort the intervals based on the first endpoint

'''

import SegmentTree
import pandas as pd


def build_tree(data):
	curr_tree = IntervalTree()
	for i in range(data.shape[0]):
		begin, end = data.iloc[i][0], data.iloc[i][1]
		iv = Interval(begin, end)
		curr_tree.add(interval)
	return curr_tree

def query(tree, begin, end):
	tree.search(begin, end)

#--- pseudocode
def report(tree, x_l):
	if (x_l - tree.left)*(x_l - tree.right) <= 0:
		if x_l in left:
			report(left, x_l)
		else:
			report(right, x_l)
#--- end pseudocode


def clipping(intervals):
	return

#--- main
if __name__ == "__main__":
	data = pd.DataFrame()
	# load points
	init_x, init_y = 0, 0
