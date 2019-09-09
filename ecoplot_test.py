import numpy as np


import matplotlib.pyplot as plt

#file=ecoutil.get_output_file_name('/Users/jinyuntang/work/ecoplot/eco_output/base/',1996,'hh')

#doy,data,var_names=ecoutil.read_output_file(file)

#varoi='AIR_TEMP'
#ts=ecoutil.extract_var(var_names,data,varoi)

#import matplotlib.pyplot as plt
#plt.plot(doy,ts)
#plt.title(varoi)
#plt.show()

from ecoplot import ecoutil

varoi='ECO_GPP'
gpp1=ecoutil.read_output_var('/Users/jinyuntang/work/github/ecoplot/eco_output/base_1011/',2001,2005,'dc',varoi)
varoi='ECO_NPP'
npp1=ecoutil.read_output_var('/Users/jinyuntang/work/github/ecoplot/eco_output/base_1011/',2001,2005,'dc',varoi)
varoi='ECO_RA'
rh1=ecoutil.read_output_var('/Users/jinyuntang/work/github/ecoplot/eco_output/base_1011/',2001,2005,'dc',varoi)
varoi='ECO_LAI'
lai1=ecoutil.read_output_var('/Users/jinyuntang/work/github/ecoplot/eco_output/base_1011/',2001,2005,'dc',varoi)

varoi='ECO_GPP'
gpp3=ecoutil.read_output_var('/Users/jinyuntang/work/github/ecoplot/eco_output/base_new/',2001,2005,'dc',varoi)
varoi='ECO_NPP'
npp3=ecoutil.read_output_var('/Users/jinyuntang/work/github/ecoplot/eco_output/base_new/',2001,2005,'dc',varoi)
varoi='ECO_RA'
rh3=ecoutil.read_output_var('/Users/jinyuntang/work/github/ecoplot/eco_output/base_new/',2001,2005,'dc',varoi)
varoi='ECO_LAI'
lai3=ecoutil.read_output_var('/Users/jinyuntang/work/github/ecoplot/eco_output/base_new/',2001,2005,'dc',varoi)


varoi='ECO_GPP'
gpp2=ecoutil.read_output_var('/Users/jinyuntang/work/github/ecoplot/eco_output/0p5_1011/',2001,2005,'dc',varoi)
varoi='ECO_NPP'
npp2=ecoutil.read_output_var('/Users/jinyuntang/work/github/ecoplot/eco_output/0p5_1011/',2001,2005,'dc',varoi)
varoi='ECO_RA'
rh2=ecoutil.read_output_var('/Users/jinyuntang/work/github/ecoplot/eco_output/0p5_1011/',2001,2005,'dc',varoi)
varoi='ECO_LAI'
lai2=ecoutil.read_output_var('/Users/jinyuntang/work/github/ecoplot/eco_output/0p5_1011/',2001,2005,'dc',varoi)


varoi='ECO_GPP'
gpp4=ecoutil.read_output_var('/Users/jinyuntang/work/github/ecoplot/eco_output/0p2_1011/',2001,2005,'dc',varoi)
varoi='ECO_NPP'
npp4=ecoutil.read_output_var('/Users/jinyuntang/work/github/ecoplot/eco_output/0p2_1011/',2001,2005,'dc',varoi)
varoi='ECO_RA'
rh4=ecoutil.read_output_var('/Users/jinyuntang/work/github/ecoplot/eco_output/0p2_1011/',2001,2005,'dc',varoi)
varoi='ECO_LAI'
lai4=ecoutil.read_output_var('/Users/jinyuntang/work/github/ecoplot/eco_output/0p2_1011/',2001,2005,'dc',varoi)

varoi='ECO_GPP'
gpp5=ecoutil.read_output_var('/Users/jinyuntang/work/github/ecoplot/eco_output/0p1_1013/',2001,2005,'dc',varoi)
varoi='ECO_NPP'
npp5=ecoutil.read_output_var('/Users/jinyuntang/work/github/ecoplot/eco_output/0p1_1013/',2001,2005,'dc',varoi)
varoi='ECO_RA'
rh5=ecoutil.read_output_var('/Users/jinyuntang/work/github/ecoplot/eco_output/0p1_1013/',2001,2005,'dc',varoi)
varoi='ECO_LAI'
lai5=ecoutil.read_output_var('/Users/jinyuntang/work/github/ecoplot/eco_output/0p1_1013/',2001,2005,'dc',varoi)

doy=range(0,len(npp1))
plt.subplot(411)
plt.plot(doy,gpp1)
plt.plot(doy,gpp2)
plt.plot(doy,gpp4)
plt.plot(doy,gpp5)
plt.legend(['ECO_GPP: a','b','c','d'])
plt.subplot(412)
plt.plot(doy,rh1)
plt.plot(doy,rh2)
plt.plot(doy,rh4)
plt.plot(doy,rh5)
plt.legend(['rh: a','b','c','d'])
plt.subplot(413)
xu1,=plt.plot(doy,lai1)
xu2,=plt.plot(doy,lai2)
xu2,=plt.plot(doy,lai4)
xu3,=plt.plot(doy,lai5)
plt.legend(['lai: a','b','c','d'])

plt.show()
