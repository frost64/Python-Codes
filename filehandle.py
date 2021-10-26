import os
name='filehandle.txt'
direct='Desktop'
sunny=os.path.join(direct,name)
with open(sunny,'r') as f:
    q=[]
    for line in f:
        w=line.strip()
        q.append(w.split('\n'))
    for i in q[0]:
        v0= i[3:4]
    for j in q[1]:
        a= j[2:5]
    for k in q[2]:
        dt= k[3:6]
    for l in q[3]:
        interval= range(int(l[10:11]),int(l[12:13]))
print ('v0=',v0,'a=',a,'dt=',dt,'interval=',interval)