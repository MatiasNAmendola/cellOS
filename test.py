from proceso import Process
from scheduler import Scheduler

p1=Process('id1','nombre1',100,1)
p2=Process('id2','nombre2',200,2)
p3=Process('id3','nombre3',300,3)
p4=Process('id4','nombre4',400,4)

s=Scheduler()
s.schedule(p4)
s.schedule(p2)
s.schedule(p3)
s.schedule(p1)

s.printReadyList()

despachado=s.dequeReady()
print "elemento despachado:",despachado.getPriority()
s.printReadyList()