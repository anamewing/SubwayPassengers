from __future__ import division

def vectorplus(A,B,plus):
	'''plus=1 or -1'''
	if len(A)!=len(B): return
	return [A[i]+plus*B[i] for i in range(len(A))]

class environment:
	"""docstring for environment"""
	def __init__(self, bottomY,doorY,doorX,doorW,topY,carL,carR,coefficient,doorforce):
		self.bY=bottomY
		self.dY=doorY
		self.dX=doorX
		self.tY=topY
		self.dW=doorW
		self.cL=carL
		self.cR=carR
		self.a=[]
		self.doorforce=doorforce
		self.coefficient=coefficient
		
	def where(self,position):
		if position[1]>=self.bY:
			if position[1]<=self.dY:
				if (position[0]<=self.dX-self.dW/2.0)or(position[0]>=self.dX+self.dW/2.0):
					return 0
				else:
					return 1
			elif position[1]<=self.tY:
				if (position[0]>=self.dX-self.dW/2.0)and(position[0]<=self.dX+self.dW/2.0):
					return 2
				elif (position[0]>=self.cL)or(position[0]<=self.cR):
					return 3
			print position
			exit('!!!!!position not correct')

	def get_force(self,state):
		if state==0:
			return [ag for ag in self.a if ag.state<=1]
		elif state==1:
			return [ag for ag in self.a if ag.state<=2]
		elif state==2:
			return [ag for ag in self.a if ag.state>=1]
		elif state==3:
			return [ag for ag in self.a if ag.state>=2]

	def get_adjacent(self,position,radius):
		return [ag for ag in self.a if abs(ag.p[1]-position[1])<=radius]

	def boundary(self,nowP,deltaP,state):
		nextP=vectorplus(nowP,deltaP,1)
		Tan = lambda P: P[0]/(P[1]+1e-9)
		doorLP=[self.dX-self.dW/2.0,self.dY]
		doorRP=[self.dX+self.dW/2.0,self.dY]
		if state<=1:
			if nextP[1]<self.bY:
				nextP[1]=self.bY
			elif nextP[1]>self.dY:
				if not(Tan(vectorplus(doorLP,nowP,-1))<Tan(deltaP)and(Tan(vectorplus(doorRP,nowP,-1))>Tan(deltaP))):
					nextP[1]=self.dY
		if state>=2:
			if nextP[0]<self.cL:
				nextP[0]=self.cL
			elif nextP[0]>self.cR:
				nextP[0]=self.cR
			if nextP[1]>self.tY:
				nextP[1]=self.tY
			elif nextP[1]<self.dY:
				if not(Tan(vectorplus(doorRP,nowP,-1))<Tan(deltaP)and(Tan(vectorplus(doorLP,nowP,-1))>Tan(deltaP))):
					nextP[1]=self.dY
		return nextP

	def get_coefficient(self):
		return self.coefficient

	def get_doorforce(self):
		return self.doorforce
					





