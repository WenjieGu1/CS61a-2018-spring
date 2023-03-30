"""3.1 Write a function that returns the largest number in a tree."""
def tree_max(t):
	"""Return the max of a tree."""
	if is_leaf(t):
		return label(t)
	else:
		return max([label(t)]+[tree_max(b) for b in branches(t)])

def height(t):
	"""Return the height of a tree"""
	if is_leaf(t):
		return 0
	else:
		return 1+max([height(b) for b in branches(t)])

def square_tree(t):
	"""Return a tree with the square of every element in t"""
	if is_leaf(t):
		label(t)**2
	else:
		return [label(t)**2]+[square_tree(b) for b in branches(t)]

def find_path(tree, x):
	"""
	>>> find_path(t, 5)
	[2, 7, 6, 5]
	>>> find_path(t, 10) # returns None
	"""
	if x==label(tree):
		return[x]
	for b in branches(tree):
		path=find_path(b,x)
		if path:
			return [label(tree)]+path

def prune(t, k):
	if k==0:
		return tree(label(t),[])
	if k>=height(t):
		return t
	else:
		return tree(label(t),[prune(b,k-1) for b in branches(t)])

###-------------------###
def tree(label, branches=[]):
	for branch in branches:
		assert is_tree(branch)
	return [label] + list(branches)

def label(tree):
	return tree[0]

def branches(tree):
	return tree[1:]

def is_leaf(tree):
	return not branches(tree)