#!/bin/bash
rm -rf get_last_c1.fit get_last_c2.fit get_last_c3.fit

ds9_cam1=$(ssh opticamc1@10.0.0.1 "find /images/opticamc1/$1/ -type f -exec ls -t1 {} + | head -1" )
ds9_cam2=$(ssh opticamc2@10.0.0.2 "find /images/opticamc2/$1/ -type f -exec ls -t1 {} + | head -1" )
ds9_cam3=$(ssh opticamc3@10.0.0.3 "find /images/opticamc3/$1/ -type f -exec ls -t1 {} + | head -1" )


scp opticamc1@10.0.0.1:$ds9_cam1 get_last_c1.fit
scp opticamc2@10.0.0.2:$ds9_cam2 get_last_c2.fit
scp opticamc3@10.0.0.3:$ds9_cam3 get_last_c3.fit

#ds9 -tile yes -tile grid -tile column get_last_c1.fit -cmap Heat -zscale  get_last_c2.fit -cmap Heat -zscale get_last_c3.fit -cmap Heat -zscale &

#display get_last_c1.fit 1
#display get_last_c1.fit 2
#display get_last_c1.fit 3
(echo 'display get_last_c1.fit 1'; echo -e '\n') | tr -d '\n' ; echo -e '\r' 
(echo 'display get_last_c2.fit 2'; echo -e '\n') | tr -d '\n' ; echo -e '\r'
(echo 'display get_last_c3.fit 3'; echo -e '\n') | tr -d '\n' ; echo -e '\r'


