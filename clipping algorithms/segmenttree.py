import numpy as np
import math

class node:
	def __init__(self, begin, end, v):
		self.begin = begin
		self.end = end
		self.left = None
		self.right = None
		self.value = v
		self.list = []	# to store the segments

class segmenttree(object):
	def __init__(self):

		return

	def insert(self, v, begin, end):
		if int(v) in [begin:end]:
			v.list.append((begin, end))
		else:
			if (v.left.begin <= end) or (v.left.end >= begin):
				insert(v.left, begin, end)
			else:
				insert(v.right, begin, end)

	def query(self, v, q_x):
		if (v.left != None) or (v.right != None):
			if q_x in [v.left.begin:v.left.end]:
				query(v.left, q_x)
			else:
				query(v.right, q_x)

	def traverse(self, v):
		return