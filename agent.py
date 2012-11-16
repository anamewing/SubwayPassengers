import math


def comp_norm (x,y) : return math.sqrt( x**2 + y**2 )

class agent():
	def __init__(self, radius , velocity, threshold,x,y,environ):
		self.state = 0 # 0 = outside1, 1 = outside2, 2 = inside 1, 3 = inside 2
		self.bumped=False;
		self.r = radius
		self.v = velocity # list, length=length(state)
		self.t = threshold
		self.f = [0.0,0.0] # force
		self.p = [x,y]
		self.e = environ
		self.e.a.append(self)

	def distance(self,agent):
		return  comp_norm(self.p[0]-agent.p[0],self.p[1]-agent.p[1])

	def stateChange(self):
		self.state = self.e.where(self.p) # where method return 0,1,2,3
		adjacent = self.e.get_adjacent(self.p,self.r) # get_adjacent method return a list of agent
		for a in adjacent:
			if self.distance(a) < 2*self.r:
				self.bumped = True

	def force(self,agent):
		d=distance(self,agent)
		if d ==0 : return
		norm = self.e.get_coefficient() / d
		self.f[0] += ( (self.p[0]-agent.p[0])/d ) * norm # in fact as d^-2
		self.f[1] += ( (self.p[1]-agent.p[1])/d ) * norm
		#TODO force by door

	def move(self) :
		if self.bumped : return
		map( force, self.e.get_force(self.state) ) 
		fnorm = comp_norm(self.f[0],self.f[1])
		if fnorm > self.t :
			deltaX = (f[0]/fnorm) * self.v[self.state]
			deltaY = (f[1]/fnorm) * self.v[self.state]
		else :
			deltaX = (f[0]/self.t) * self.v[self.state]
			deltaY = (f[1]/self.t) * self.v[self.state]
		self.p = self.e.boundary( self.p, (deltaX,deltaY),self.state )













