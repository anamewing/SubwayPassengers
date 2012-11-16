import agent
import environment

def report(e):
	for ag in e.a:
		print ag.p

v=[30,30,10,10]

e=environment.environment(0,100,0,10,130,-30,30,100)

a=agent.agent(5,v,20,10,20,e)
b=agent.agent(5,v,20,-10,0,e)

report(e)

a.move()
b.move()
report(e)