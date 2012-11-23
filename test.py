from __future__ import division
import agent
import environment
import random
import testonce

#import logging

bumpTimes=0

agentCount=20

TryTimes=10

bottomY=0
doorY=30
doorX=0
doorW=1
topY=35
carL=-5
carR=5
coefficient=200*0.9**2
doorforce=coefficient/(0.25**2)

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
result=[]

f1=open('result.txt','w')
f2=open('recordall.txt','w')
writefile=lambda fh,s:fh.write(str(s)+'\n')

for threshold in [80]:
	for coefficient in [i*20 for i in range(1,16)]:
		for doorforce in [coefficient*(i) for i in [1,2,4,6,8]]:
			recordall=[]
			for i in range(TryTimes):
				result=(testonce.testonce(bottomY,doorY,doorX,doorW,topY,carL,carR,coefficient,doorforce,radius,v,threshold,agentCount))
				record=[threshold,coefficient,doorforce,i,result]
				recordall.append(result)
				writefile(f1,record)
				f1.flush()
				print record
			ave=[sum([re[0] for re in recordall])/TryTimes,sum([re[1] for re in recordall])/TryTimes]
			writefile(f2,[threshold,coefficient,doorforce,ave])
			f2.flush()


f1.close()
f2.close()
