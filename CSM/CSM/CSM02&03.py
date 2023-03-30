#######
#CSM02#
def is_prime(num):
    assert type(num) is int, "num is not an integer: %r" % num
    assert num > 1, "num is not greater than one: %r" % num
    for n in range(2,num):
        if num%n == 0:
            return False
        if num%n > 1:
            return True
    return True

def all_primes(nums):
	return [i for i in nums if is_prime(i)]

def  list_of_lists(lst):
	new=[]
	for i in range(len(lst)):
		new.append([0]+lst[:i])
	return new

def sum_of_nodes(t):
	sum=0
	if is_leaf(t):
		return label(t)
	for i in branches(t):
		sum+=sum_of_nodes(i)
	return sum+label(t)

# Tree ADT
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

#######
#CSM03#
#3
def accumulate(lst):
    l=list(lst)
    for i in range(len(lst)):
        if isinstance(l[i],list):
            inside=accumulate(lst[i])
            l[i]=inside
        else:
            lst[i]=sum(l[:i+1])
    return lst[i]
"""
发现一个问题，l是lst的复制体，但是l和lst的嵌套列表却是同一个。
影响：以[3, 7, [2, 5, 6], 9]为例。
本来line53可以写成l[i]=sum(l[i])（i=2时），由于l[2]和lst[2]都是
[2,7,13]则不符合l[2]==13的预期
"""
#2
def has_seven(k): # Use this function for your answer below
    if k % 10 == 7:
        return True
    elif k < 10:
        return False
    else:
        return has_seven(k // 10)
def make_pingpong_tracker():
    index,current,add=1,0,True
    def pingpong_tracker():
        nonlocal index,current,add
        if add:
            current+=1
        else:
            current-=1
        if has_seven(index) or index%7==0:
            add=not add
        index+=1
        return current
    return pingpong_tracker