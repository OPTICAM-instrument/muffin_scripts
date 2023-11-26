import numpy as np


t,x=np.loadtxt("ds9_target.dat",unpack=True)
t,x2=np.loadtxt("ds9_bkg.dat",unpack=True)
t,x3=np.loadtxt("ds9_star1.dat",unpack=True)
t,x4=np.loadtxt("ds9_star2.dat",unpack=True)

f=open("test","w+")
for i in range(0,len(t)):
	f.write(str(t[i])+" "+str(x[i])+" "+str(x2[i])+" "+str(x3[i])+" "+str(x4[i])+"\n")
