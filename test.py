import agent
import environment
import random

def report(e):
	for ag in e.a:
		print str(ag.udid)+str(ag.p)+str(ag.state)+str(ag.bumped)
	print '------'

v=[30,30,5,5]

e=environment.environment(0,100,0,10,130,-30,30,100,2000)

for k in range(1,20):
	a=agent.agent(0.2,v,10,-30+60*random.random(),40*random.random(),e,k)


report(e)

for i in xrange(1,200):
	for ag in e.a:
		ag.move()
	for ag in e.a:
		ag.stateChange()
	print i
	report(e)
