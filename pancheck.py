import numpy as np 
import matplotlib.pyplot as plt
import pandas as pd
from astropy.coordinates import SkyCoord
import astropy.coordinates as coord
import astropy.units as u
PAN=pd.read_csv("Pantheon+SH0ES.dat",sep=" ")
JLA=pd.read_csv("jla_lcparams.txt",sep=" ")


#rd1=SkyCoord(JLA['ra'], JLA['dec'], unit=u.deg)
rd2=SkyCoord(PAN['RA'], PAN['DEC'], unit=u.deg)
#gal1 = rd1.galactic
gal2 = rd2.galactic
ind1=np.array([])
ind2=np.array([])

#jx=JLA['x1']
px=PAN['x1']

#jz=JLA['zhel']
pz=PAN['zHEL']

#JLAmjd=JLA['tmax']
PANmjd=PAN['PKMJD']
set1=PAN['IDSURVEY']
print('#,PAN[name]1,PAN[name]2,PAN[zcmb]1,PAN[zCMB]2,MJDPAN1,MJDPAN2')
s1=np.array([])
s2=np.array([])
ar=[]
for i in range (len(PAN['RA'])):
    for j in range (i,len(PAN['RA'])):
         if i!=j and j not in ind2:
             if  coord.angular_separation(gal2[i].l,gal2[i].b,gal2[j].l,gal2[j].b)<0.1*u.deg and abs(PANmjd[i]-PANmjd[j])<5.1 and set1[i]!=set1[j]: #put set1[i]==set1[j] for same surveys
                ind1=np.append(ind1,i)
                ind2=np.append(ind2,j)
                ar.append([i,j])
                print(i,PAN['CID'][i],PAN['CID'][j],PAN['zCMB'][i],PAN['zCMB'][j],PAN['PKMJD'][j],PAN['PKMJD'][j])
                
np.save("countssib",ind1)    
np.save("counts2sib",ind2)               
np.save("finalsib",ar)

