import math

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
		
	def where(position):
		if position[1]>=bottomY:
			if position[1]<=doorY:
				if (position[0]<=self.dX-self.dW/2)||(position[0]>=self.dX+self.dW/2):
					return 0
				else:
					return 1
			else if position[1]<=topY:
				if (position[0]>=self.dX-self.dW/2)&&(position[0]<=self.dX+self.dW/2):
					return 2
				else if (position[0]<=self.cL)||(position[0]>=self.cR):
					return 3
			exit('position not correct')

	def get_force(state):

	def getadjacent(position):

	def boundary(nowP,deltaP):
