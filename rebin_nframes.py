import numpy as np
import os


os.system("ls *dat")
os.system("ls *qdp")

fname=  input("file?")
t,x=np.loadtxt(fname,unpack=True)


tnew=np.zeros(int((len(t)/2.+1)))
xnew=np.zeros(int((len(t)/2.+1)))
enew=np.zeros(int((len(t)/2.+1)))


pref=  input("prefix?")
k=0
print(t[1]-t[0])
N=int(  input("N?"))
f=open(pref+'_reb'+str(N)+'_new.dat','w+')
for i in range(0,len(t)-1):
	if (i+1)%N==0:
		xm=np.mean(x[i-(N-1):i])
		tm=np.mean(t[i-(N-1):i])		
		#em=(np.sum(e[i-(N-1):i]**2)/(N**2))**0.5
		f.write(str(tm)+' '+str(xm)+"\n")#+' '+str(em )+'\n')



