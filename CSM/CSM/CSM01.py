"""#### Recursion ###"""
def is_sorted(n):
	if (n//10)%10 >= n%10:
		return is_sorted(n//10)
	elif n//10 == 0:
		return True
	else:
		return False


def mario_number(level):
	if level//10%10==1 and level//100%10==1:
		return mario_number(level//100)+mario_number(level//10)
	elif level//100%10==1:
		return mario_number(level//100)
	elif level//10%10==1:
		return mario_number(level//10)
	elif level//10==0:
		return 1
	else:
		return 0


def make_change(n):
	if n==0:
		return 0
	elif n>=4:
		return min(make_change(n-1)+1,make_change(n-3)+1,make_change(n-4)+1)
	elif n>=3:
		return min(make_change(n-1)+1,make_change(n-3)+1)
	else:
		return min(make_change(n-1)+1,make_change(n-1)+1)


"""### Data Abstraction ###"""
"""
def elephant(name, age, can_fly):
	return [name,age,can_fly]

def elephant_name(e):
	return e[0]

def elephant_age(e):
	return e[1]

def elephant_can_fly(e):
	return e[2]
"""


def elephant(name, age, can_fly):
"""
>>> chris = elephant("Chris Martin", 38, False)
>>> elephant_name(chris)
"Chris Martin"
>>> elephant_age(chris)
38
>>> elephant_can_fly(chris)
False
"""
	def select(command):
		return {"name":name,"age":age,"can_fly":can_fly}
	return select

def elephant_name(e):
return e("name")

def elephant_age(e):
return e("age")

def elephant_can_fly(e):
return e("can_fly")