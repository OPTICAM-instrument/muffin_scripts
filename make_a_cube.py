import numpy as np
from astropy.io import fits
import os
from astropy.time import Time


filt=input("What filter do you want to analyse (u,g,r,i,z)?")
os.system("ls *"+filt+"*o.fit >list_files")



f=open("list_files","r+")

lines=f.readlines()

f.close()
print("opening and reading files....")
hdul = fits.open(lines[0][:-1])

img_list = [hdul[0].data]

for i in range(1,len(lines)):

	hdul = fits.open(lines[i][:-1])

	img_list.append(hdul[0].data)

img_array=np.array(img_list)

print("writing cube to mycube.fits")
fits.writeto('mycube.fits', img_array)
