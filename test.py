import agent
import environment

def report(e):
	for ag in e.a:
		print str(ag.udid)+str(ag.p)+str(ag.state)+str(ag.bumped)
	print '------'

v=[30,30,10,10]

e=environment.environment(0,100,0,10,130,-30,30,100,1000)

a=agent.agent(0.2,v,10,10,20,e,1)
b=agent.agent(0.2,v,10,-10,0,e,2)
c=agent.agent(0.2,v,10,50,20,e,3)
report(e)

for i in xrange(1,100):
	for ag in e.a:
		ag.move()


	report(e)
