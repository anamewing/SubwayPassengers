from __future__ import division
import math
import random


def comp_norm (x,y) : return math.sqrt( x**2 + y**2 )

class agent():
	def __init__(self, radius , velocity, threshold,x,y,environ,udid):
		self.state = 0 # 0 = outside1, 1 = outside2, 2 = inside 1, 3 = inside 2
		self.bumped=False;
		self.r = radius
		self.v = velocity # list, length=length(state)
		self.t = threshold
		self.f = [0.0,0.0] # force
		self.p = [x,y]
		self.e = environ
		self.udid = udid
		self.e.a.append(self)

	def distance(self,agent):
		return  math.sqrt(comp_norm(self.p[0]-agent.p[0],self.p[1]-agent.p[1]))

	def stateChange(self):
		self.state = self.e.where(self.p) # where method return 0,1,2,3
		adjacent = self.e.get_adjacent(self.p,self.r) # get_adjacent method return a list of agent
		for a in adjacent:
			if self.udid == a.udid : continue
			if self.distance(a) < 2*self.r:
				if (self.state-1.5)*(a.state-1.5)>0:
					self.bumped = True

	def force(self,agent):
		if self.udid == agent.udid : return
		d=self.distance(agent)
		if d==0:
			self.p[0]+=1e-8*random.random()
			self.p[1]+=1e-8*random.random()
			d=self.distance(agent)
		norm = self.e.get_coefficient() / d**2
		self.f[0] += ( (self.p[0]-agent.p[0])/d ) * norm 
		self.f[1] += ( (self.p[1]-agent.p[1])/d ) * norm

	def move(self) :
		self.f=[0.0,0.0]
		if self.bumped : 
			self.bumped = False
			return
		map( self.force, self.e.get_force(self.state) ) 
		#print [ag.p for ag in self.e.get_force(self.state)]
		self.doorforce()
		fnorm = comp_norm(self.f[0],self.f[1])
		#print fnorm
		#print self.f
		if fnorm > self.t :
			deltaX = (self.f[0]/fnorm)*self.v[self.state]
			deltaY = (self.f[1]/fnorm)*self.v[self.state]
		else :
			deltaX = (self.f[0]/self.t)*self.v[self.state]
			deltaY = (self.f[1]/self.t)*self.v[self.state]
		self.p = self.e.boundary( self.p, (deltaX,deltaY),self.state )
		#self.stateChange()

	def doorforce(self):
		#if self.state>=2:return
		dF=self.e.get_doorforce()
		dx=self.p[0]-self.e.dX
		dy=self.p[1]-(self.e.dY+self.e.tY)/2.0
		doorDistance=comp_norm(dx,dy)
		self.f[0]-=(dx)/doorDistance * dF
		self.f[1]-=(dy)/doorDistance * dF
















