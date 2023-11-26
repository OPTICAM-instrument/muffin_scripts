import numpy as np
from astropy.io import fits
import os
from astropy.time import Time

#asking filter
filt=input("What filter do you want to analyse (u,g,r,i,z)?")
os.system("ls *"+filt+"*o.fit >list_files")\


#open list of files 
f=open("list_files","r+")
lines=f.readlines()
f.close()


#loop to read UT and write them in log_time_xx_sec.txt
f=open("log_times_"+filt+"_sec.txt","w+")
print()

print("reading UT and writing to output to log_times_"+filt+".txt....")
for i in range(0,len(lines)):
	hdul = fits.open(lines[i][:-1])
	#print(hdul[0].header['UT'])  
	times=hdul[0].header['UT']
	t = Time(times, format='iso', scale='utc')


	if i==0:
		start=t.mjd
		t_arr=[t.mjd]
	if i>0: 
		t_arr.append(t.mjd)
	f.write(str((t.mjd-start)*86400)+"\n")


#t=np.loadtxt("log_times_"+filt+"_sec.txt",unpack=True)
#print("AVERAGE TIME RESOLUTION: "+str(np.mean(np.diff(t)*86400))+" s")

print()
print("writing to time resolution of each bin to list_dt_"+filt+".txt....")
f=open("list_dt_"+filt+"_sec.txt","w+")
for i in range(0,len(t_arr)-1):

#	f.write(str(t[i])+" "+str(np.diff(t)[i]*86400)+" "+str(np.diff(t_arr)[i]*86400)+"\n")
	f.write(str(np.diff(t_arr)[i]*86400)+"\n")
f.close()

print("*************************************")
print()
print()
print()
print("                 DONE! READY TO CHECK THE TIMING OF YOUR DATASET")
print()

print()
print("                 THE AVERAGE TIME RESOLUTION IS: "+str(np.mean(np.diff(t_arr)*86400))+" s")
print()

print("*************************************")
print()

print()

print("FURTER CHECKS:")

print("		FOLLOW SEQUENCE A) TO PLOT VALUE OF THE TIME STAMP VS THE NUMBER OF FRAMES\n\n		FOLLOW SEQUENCE B) TO PLOT THE TIME RESOLUTION VS THE NUMBER OF FRAMES")
print()

print()
print("*************************************")


print()

print()
print("SEQUENCE A) TIME STAMP VS THE NUMBER OF FRAMES\n\ngnuplot\nset xlabel '# of Frames' \n set ylabel 'Time from first frame (s)'\npl 'log_times_"+filt+"_sec.txt' ti ''\n\n*************************************\n\nSEQUENCE B) TIME RESOLUTION VS THE NUMBER OF FRAMES\n\ngnuplot\nset xlabel '#  of Frames' \nset ylabel '{/Symbol D}t (s)'\npl 'list_dt_"+filt+"_sec.txt' ti ''\n\n ")

#N.B. The time is calculated in seconds from the time of the first stamp *N.B. The time is calculated in seconds 
