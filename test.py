import agent
import environment
import random
import testonce

#import logging

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

radius=0.1
threshold=80

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

for i in range(20):

	result=(testonce.testonce(bottomY,doorY,doorX,doorW,topY,carL,carR,coefficient,doorforce,radius,v,threshold,agentCount))
	print [i,result]