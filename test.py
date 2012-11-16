import agent
import environment

def report(e):
	for ag in e.a:
		print ag.p

v=[30,30,10,10]

e=environment.environment(0,100,0,10,130,-30,30)

a=agent.agent(5,v,20,10,0,e)
b=agent.agent(5,v,20,-10,0,e)

report(e)