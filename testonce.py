import agent
import environment
import random

def report(e):
	for ag in e.a:
		print str(ag.udid)+str(ag.p)+str(ag.state)+str(ag.bumped)
	print '------'



def testonce(bottomY,doorY,doorX,doorW,topY,carL,carR,coefficient,doorforce,radius,v,threshold):
	def analyze(e):
		return len([ag for ag in e.a if ag.p[1]>doorY])

	def notin(e):
		return [ag.p for ag in e.a if ag.state<=1]

	e=environment.environment(bottomY,doorY,doorX,doorW,topY,carL,carR,coefficient,doorforce)
	bumpTimes=0
	for k in range(20):
		a=agent.agent(radius,v,threshold,(carL+(carR-carL)*random.random()),0.4*(bottomY+(topY-bottomY)*random.random()),e,k)
	
	
	for i in xrange(2000):
		for ag in e.a:
			ag.move()
		for ag in e.a:
			ag.stateChange()
		bumpTimes+=len([ag for ag in e.a if ag.bumped])
		
	#print bumpTimes
	#print analyze(e)

	return [bumpTimes,analyze(e),notin(e)]