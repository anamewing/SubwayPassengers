import math

def vectorplus(A,B,plus):
	'''plus=1 or -1'''
	if len(A)!=len(B): return
	return [A[i]+plus*B[i] for i in range(len(A))]

class environment:
	"""docstring for environment"""
	def __init__(self, bottomY,doorY,doorX,doorW,topY,carL,carR):
		super(environment, self).__init__()
		self.bY=bottomY
		self.dY=doorY
		self.dX=doorX
		self.tY=topY
		self.dW=doorW
		self.cL=carL
		self.cR=carR
		self.a=[]
		
	def where(self,position):
		if position[1]>=self.bY:
			if position[1]<=self.dY:
				if (position[0]<=self.dX-self.dW/2.0)||(position[0]>=self.dX+self.dW/2.0):
					return 0
				else:
					return 1
			else if position[1]<=self.tY:
				if (position[0]>=self.dX-self.dW/2.0)&&(position[0]<=self.dX+self.dW/2.0):
					return 2
				else if (position[0]<=self.cL)||(position[0]>=self.cR):
					return 3
			exit('position not correct')

	def get_force(self,state):
		if state==0:
			return [ag for ag in self.a if ag.state<=1]
		else if state==1:
			return [ag for ag in self.a if ag.state<=2]
		else if state==2:
			return [ag for ag in self.a if ag.state>=1]
		else if state==3:
			return [ag for ag in self.a if ag.state>=2]

	def getadjacent(self,position):


	def boundary(self,nowP,deltaP,state):
		nextP=vectorplus(nowp,deltaP,1)
		Tan = lambda P: P[0]/double(P[1])
		doorLP=[self.dX-self.dW/2.0,self.dY]
		doorRP=[self.dX+self.dW/2.0,self.dY]
		if state<=1:
			if nextP[1]<self.bY:
				nextP[1]=self.bY
			else if nextP[1]>self.dY:
				if !(Tan(vectorplus(doorLP,nowp,-1))<Tan(deltaP)&&Tan(vectorplus(doorRP,nowp,-1))>Tan(deltaP)):
					nextP[1]=self.dY
		if state>=2:
			if nextP[0]<self.cL:
				nextP[0]=self.cL
			else if nextP[0]>self.cR:
				nextP[0]=self.cR
			if nextP[1]>self.tY:
				nextP[1]=self.tY
			else if nextP[1]<self.dY:
				if !(Tan(vectorplus(doorRP,nowp,-1))<Tan(deltaP)&&Tan(vectorplus(doorLP,nowp,-1))>Tan(deltaP)):
					nextP[1]=self.dY
		return nextP
					





