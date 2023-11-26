import numpy as npg
from astropy.io import fits
import os
from astropy.time import Time


filt=input("\nREADHEADER.PY reads all the timestamps (KEY: 'UT') from one of the filters and puts them in a list in seconds from the first frames.\n\nWhat filter do you want to analyse (u,g,r,i,z)?")
os.system("ls *"+filt+"*o.fit >list_files")\



f=open("list_files","r+")

lines=f.readlines()

f.close()


f=open("log_times_"+filt+".txt","w+")
print()
print("writing to output to log_times_"+filt+".txt")
for i in range(0,len(lines)):
	hdul = fits.open(lines[i][:-1])
	#print(hdul[0].header['UT'])  
	times=hdul[0].header['UT']
	t = Time(times, format='iso', scale='utc')


	if i==0:
		start=t.mjd
	f.write(str(t.mjd-start)+"\n")
