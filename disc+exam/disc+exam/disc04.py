#1.2
lamb = 'da'
def da(da):
    def lamb(lamb):
        nonlocal da
        def da(nk):
            da = nk + ['da']
            da.append(nk[0:2])
            return nk.pop()
    da(lamb)
    return da([[1], 2]) + 3
da(lambda da: da(lamb))

#1.3
def memory(n):
	def f(f):
		nonlocal n
		n=f(n)
		return n
	return f

#2.2
def add_this_many(x,el,lst):
	num=sum([i for i in lst if i==x])
	for i in range(sum):
		lst.append(el)
	return lst

#2.3
def reverse(lst):
	for i in range(len(lst)-1):
		lst.insert(i,lst[-1])
		lst.pop()
	return lst

#3.2
def group_by(s,fn):
	dic={}
	for i in s:
		if fn(i) not in dic:
			dic[fn(i)]=[i]
		else:
			dic[fn(i)].append(i)
	keys=[k for k in dic]
	keys.sort()
	for k in keys:
		return {k:dic[k]}

#3.3
def replace_all_deep(d,x,y):
	for key in d:
		if type(d[key])!=dict and d[key]==x:
			d[key]=y
		elif type(d[key])==dict:
			replace_all_deep(d[key],x,y)
			# 如果这里是 return replace 那么函数返回这里的返回值，并且前面的for不会继续。

########
#prep03#
########
# Tree ADT
def tree(label, branches=[]):
    """Construct a tree with the given label value and a list of branches."""
    for branch in branches:
        assert is_tree(branch), 'branches must be trees'
    return [label] + list(branches)

def label(tree):
    """Return the label value of a tree."""
    return tree[0]

def branches(tree):
    """Return the list of branches of the given tree."""
    return tree[1:]

def is_tree(tree):
    """Returns True if the given tree is a tree, and False otherwise."""
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True

def is_leaf(tree):
    """Returns True if the given tree's list of branches is empty, and False
    otherwise.
    """

#1 Tree Recursion with Trees
def sum_range(t):
	def helper(t):
		if is_leaf(t):
			return [label(t),label(t)]
		else:
			a=min([helper(i)[0] for i in branches(t)])
			b=max([helper(i)[1] for i in branches(t)])
			x=label(t)
			return [b+x,a+x]
	x,y=helper(t)
	return x-y

#2
def no_eleven(n):
	if n==0:
		return [[]]
	elif n==1:
		return [[6],[1]]
	else:
		a,b=no_eleven(n-1),no_eleven(n-2)
		return [[6]+s for s in a]+[[1,6]+s for s in b]

#3
def eval_with_add(t):
	if label(t)=='+':
		return sum()
	elif label(t)=='*':
		total=