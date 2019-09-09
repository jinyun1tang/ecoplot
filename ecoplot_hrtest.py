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

varoi='ECO_CO2_FLUX'
nee=ecoutil.read_output_var('/Users/jinyuntang/work/github/ecoplot/eco_output/base_1011/',2001,2005,'hc',varoi)
varoi='SOIL_CO2_FLUX'
soilr=ecoutil.read_output_var('/Users/jinyuntang/work/github/ecoplot/eco_output/base_1011/',2001,2005,'hc',varoi)


varoi='ECO_CO2_FLUX'
nee1=ecoutil.read_output_var('/Users/jinyuntang/work/github/ecoplot/eco_output/0p1_1013/',2001,2005,'hc',varoi)
varoi='SOIL_CO2_FLUX'
soilr1=ecoutil.read_output_var('/Users/jinyuntang/work/github/ecoplot/eco_output/0p1_1013/',2001,2005,'hc',varoi)

doy=(range(0,len(nee)))

plt.subplot(211)
plt.plot(doy[600:720],nee[600:720])
plt.plot(doy[600:720],nee1[600:720])
plt.legend(['nee: a_base','b_x0.1'])
plt.subplot(212)
soilr[soilr<-20.]=float('NaN')
plt.plot(doy,soilr)
soilr1[soilr1<-20.]=float('NaN')
plt.plot(doy,soilr1)
plt.legend(['soil hr: a_base','b_x0.1'])
plt.xlabel('cumulative hours')
plt.show()
