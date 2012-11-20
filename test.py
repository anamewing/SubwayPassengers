import agent
import environment
import random

bumpTimes=0

bottomY=0
doorY=30
doorX=0
doorW=1
topY=35
carL=-5
carR=5
coefficient=200
doorforce=2000

radius=0.02
threshold=100


def report(e):
	for ag in e.a:
		print str(ag.udid)+str(ag.p)+str(ag.state)+str(ag.bumped)
	print '------'

def analyze(e):
	return len([ag for ag in e.a if ag.p[1]>doorY])


#v=[30,30,5,5]
v=[0.04,0.04,0.04,0.04]



e=environment.environment(bottomY,doorY,doorX,doorW,topY,carL,carR,coefficient,doorforce)

for k in range(20):
	a=agent.agent(radius,v,threshold,(carL+(carR-carL)*random.random()),0.4*(bottomY+(topY-bottomY)*random.random()),e,k)


report(e)

for i in xrange(2000):
	for ag in e.a:
		ag.move()
	for ag in e.a:
		ag.stateChange()
	bumpTimes+=len([ag for ag in e.a if ag.bumped])
	print i
	if i%10==0:report(e)
print bumpTimes