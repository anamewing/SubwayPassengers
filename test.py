import agent
import environment
import random
import testonce

bumpTimes=0

agentCount=20

bottomY=0
doorY=30
doorX=0
doorW=1
topY=35
carL=-5
carR=5
coefficient=200*0.9**2
doorforce=1500

radius=0.02
threshold=100

velocity=0.04


def report(e):
	for ag in e.a:
		print str(ag.udid)+str(ag.p)+str(ag.state)+str(ag.bumped)
	print '------'

def analyze(e):
	return len([ag for ag in e.a if ag.p[1]>doorY])


#v=[30,30,5,5]
v=[velocity,velocity,velocity/4,velocity/4,velocity/8]
result=[];

for threshold in [80]:

	result=(testonce.testonce(bottomY,doorY,doorX,doorW,topY,carL,carR,coefficient,doorforce,radius,v,threshold,agentCount))
	print [threshold,result]