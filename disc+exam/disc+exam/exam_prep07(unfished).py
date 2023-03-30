"""1. Linky Paths Implement linky_paths which takes in a Tree t and modifies
 each label to be the path from that node to the root"""
 def linky_paths(t):
	"""
	>>> t = Tree(1, [Tree(2)])
	>>> linky_paths(t)
	>>> t
	Tree(Link(1), [Tree(Link(2, Link(1))]
	"""
	def helper(t, path_so_far):
		t.label=Link(t.label, path_so_far)
		for branche in t.branches:
			helper(branche,t.label)
	helper(t,Link.empty)

"""2. Find File Path Implement find_file_path which takes in a Tree t and a string
file_str and returns the full path of a file that we search for if the file exists. 
If the file does not exist, then return None.(my solution is a bit different from 
the giving skeleton)"""
def find_file_path(t, file_str):
	"""
	>>> t = Tree('data', [Tree('comm', [Tree('dummy.py')]),
	Tree('ecc',
	[Tree('hello.py'), Tree('file.py')]), Tree('file2.py')])
	>>> find_file_path(t, 'file2.py')
	'/data/file2.py'
	>>> find_file_path(t, 'dummy.py')
	'/data/comm/dummy.py'
	>>> find_file_path(t, 'hello.py')
	'/data/ecc/hello.py'
	>>> find_file_path(t, 'file.py')
	'/data/ecc/file.py'
	"""
	def helper(t, file_str, path_so_far):
		if t.label == file_str:
			return path_so_far
		elif t.is_leaf():
			return None
		for branche in t.branches:
			path_so_far=path_so_far+'/'+string(branche.label)
			return helper(branche, file_str, path_so_far)
	return helper(t, file_str, string(t.label))

"""1. Convert to String Implement convert_to_string which takes in a Linked List
link and coverts the Linked List to a file path"""
def convert_to_string(link):
	"""
	>>> link = Link(data, Link(file2.py))
	>>> convert_to_string(link)
	'/data/file2.py'
	"""
	result=''
	while link != Link.empty:
		result+='/{0}'.format(link.first)
		link=link.rest
	return result

"""2.All Paths Linked Implement all_paths_linked which takes in a Tree t and returns
 a list of all paths from root to leaf in a tree with one catch – each path is 
 represented as a linked list."""
def all_paths_linked(t):
	"""
	>>> t1 = Tree(1, [Tree(2), Tree(3)])
	>>> t2 = Tree(1, [Tree(2), Tree(3, [Tree(4), Tree(5)])
	])
	>>> all_paths(t1)
	[Link(1, Link(2)), Link(1, Link(3))]
	>>> all_paths(t2)
	[Link(1, Link(2)), Link(1, Link(3, Link(4))), Link(1,
	Link(3, Link(5)))]
	"""
	if is_leaf(t):
		return Link(t.label)
	result=[]
	for branche in t.branches:
		result=result + [Link(t.label, x), for x in all_paths_linked(branche)]
	return result

"""3. Find File Path 2 Implement find_file_path which takes in a Tree t and a string
file_str and returns the full path of a file that we search for if the file exists. If the
file does not exist, then return None.
"""
def find_file_path2(t, file_str):
	"""
	>>> t = Tree('data', [Tree('comm', [Tree('dummy.py')]),
	Tree('ecc',
	[Tree('hello.py'), Tree('file.py')]), Tree('file2.py')])
	>>> find_file_path2(t, 'file2.py')
	'/data/file2.py'
	>>> find_file_path2(t, 'dummy.py')
	'/data/comm/dummy.py'
	>>> find_file_path2(t, 'hello.py')
	'/data/ecc/hello.py'
	>>> find_file_path2(t, 'file.py')
	'/data/ecc/file.py'
	"""
#---------------------------
class Link:
	"""A linked list with a first element and the rest."""
	empty = ()
	def __init__(self, first, rest=empty):
		assert rest is Link.empty or isinstance(rest, Link)
		self.first = first
		self.rest = rest
	def __getitem__(self, i):
		if i == 0:
			return self.first
		else:
			return self.rest[i-1]
	def __len__(self):
		return 1 + len(self.rest)
	def __repr__(self):
		"""Return a string that would evaluate to link."""
		if self.rest is Link.empty:
			rest = ''
		else:
			rest = ', ' + repr(self.rest)
		return 'Link({0}{1})'.format(self.first, rest)
	def __add__(self, t):
		"""Return a new link that combines with two links."""
		if self is Link.empty:
			return t
		else:
			return Link(self.first, self.rest+t)

class Tree:
    def __init__(self, label, branches=[]):
    for c in branches:
        assert isinstance(c, Tree)
    self.label = label
    self.branches = list(branches)

    def __repr__(self):
    if self.branches:
        branches_str = ', ' + repr(self.branches)
    else:
        branches_str = ''
    return 'Tree({0}{1})'.format(self.label, branches_str)

    def is_leaf(self):
    return not self.branches

    def __eq__(self, other):
    return type(other) is type(self) and self.label == other.label \
           and self.branches == other.branches

    def __str__(self):
    def print_tree(t, indent=0):
        tree_str = '  ' * indent + str(t.label) + "\n"
        for b in t.branches:
            tree_str += print_tree(b, indent + 1)
        return tree_str
    return print_tree(self).rstrip()