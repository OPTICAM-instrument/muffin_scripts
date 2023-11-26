import numpy as np
from astropy.io import fits
import os
from astropy.time import Time
filt=input("\nREAD_DITS.PY reads all the timestamps (KEY: 'UT') that have been extracted with READHEADER and evaulates the average time resolution. Furthermore it saves into file the time resolution for each time stamp in sec.\n\nWhat filter do you want to analyse (u,g,r,i,z)?")
t=np.loadtxt("log_times_"+filt+".txt",unpack=True)
print(np.mean(np.diff(t)*86400))


f=open("list_dt_"+filt+"_sec","w+")
for i in range(0,len(t)-1):

	f.write(str(t[i])+" "+str(np.diff(t)[i]*86400)+"\n")
f.close()
