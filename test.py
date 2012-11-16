import agent
import environment

def report(e):
	for ag in e.a:
		print str(ag.udid)+str(ag.p)+str(ag.state)+str(ag.bumped)
	print '------'

v=[30,30,10,10]

e=environment.environment(0,100,0,10,130,-30,30,100,10000)

a=agent.agent(0.2,v,10,10,20,e,1)
b=agent.agent(0.2,v,10,-10,0,e,2)
c=agent.agent(0.2,v,10,50,20,e,3)
d=agent.agent(0.2,v,10,0,20,e,4)
ee=agent.agent(0.2,v,10,10,40,e,5)
report(e)

for i in xrange(1,200):
	for ag in e.a:
		ag.move()
	print i
	report(e)
