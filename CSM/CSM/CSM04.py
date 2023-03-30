#1
class Baller:
	all_players = []
	def __init__(self, name, has_ball = False):
		self.name = name
		self.has_ball = has_ball
		Baller.all_players.append(self)
	def pass_ball(self, other_player):
		if self.has_ball:
			self.has_ball = False
			other_player.has_ball = True
			return True
		else:
			return False
class BallHog(Baller):
	def pass_ball(self, other_player):
		return False
#2
class TeamBaller(Baller):
	def pass_ball(self,other_player):
		if Baller.pass_ball(self,other_player):
			print('Yay!')
			return True
		else:
			print('I don\'t have the ball')
			return False
#3
class PingPongTracker:
	'''
>>> tracker1 = PingPongTracker()
>>> tracker2 = PingPongTracker()
>>> tracker1.next()
1
>>> tracker1.next()
2
>>> tracker2.next()
1
'''
	def __init__(self):
		self.current = 0
		self.index = 1
		self.add = True
	def next(self):
		if self.index%7==0 or has_seven(self.index):
			self.add= not self.add
		if self.add:
			self.current+=1
		else:
			self.current-=1
		self.index+=1
		return self.current
def has_seven(d):
	while d > 0:
		if d%10==7:
			return True
		else:
			d=d//10
	return False

#4
class Bird:
	def __init__(self, call):
		self.call = call
		self.can_fly = True
	def fly(self):
		if self.can_fly:
			return "Don't stop me now!"
		else:
			return "Ground control to Major Tom..."
	def speak(self):
		print(self.call)

class Chicken(Bird):
	def speak(self, other):
		Bird.speak(self)
		other.speak()

class Penguin(Bird):
	can_fly = False
	def speak(self):
		call = "Ice to meet you"
		print(call)

def live(long):
	def prosper(spock, live):
		nonlocal long
		if len(long) == 1:
			return spock+1
		long[1] = live(long[0])
		long = long[1:]
		prosper(long[0], abs)
		return spock[0]+1
	prosper(long, lambda trek: trek-3)