import ecoutil
import numpy as np


import matplotlib.pyplot as plt

#file=ecoutil.get_output_file_name('/Users/jinyuntang/work/ecoplot/ecosims/base/',1996,'hh')

#doy,data,var_names=ecoutil.read_output_file(file)

#varoi='AIR_TEMP'
#ts=ecoutil.extract_var(var_names,data,varoi)

#import matplotlib.pyplot as plt
#plt.plot(doy,ts)
#plt.title(varoi)
#plt.show()



varoi='ECO_GPP'
gpp1=ecoutil.read_output_var('/Users/jinyuntang/work/ecoplot/ecosims/base/',1996,2003,'dc',varoi)
varoi='ECO_NPP'
npp1=ecoutil.read_output_var('/Users/jinyuntang/work/ecoplot/ecosims/base/',1996,2003,'dc',varoi)
varoi='ECO_RH'
rh1=ecoutil.read_output_var('/Users/jinyuntang/work/ecoplot/ecosims/base/',1996,2003,'dc',varoi)

varoi='ECO_GPP'
gpp2=ecoutil.read_output_var('/Users/jinyuntang/work/ecoplot/ecosims/0po2/',1996,2003,'dc',varoi)
varoi='ECO_NPP'
npp2=ecoutil.read_output_var('/Users/jinyuntang/work/ecoplot/ecosims/0po2/',1996,2003,'dc',varoi)
varoi='ECO_RH'
rh2=ecoutil.read_output_var('/Users/jinyuntang/work/ecoplot/ecosims/0po2/',1996,2003,'dc',varoi)


doy=range(0,len(npp1))
plt.subplot(311)
plt.plot(doy,gpp1-gpp2)
plt.subplot(312)
plt.plot(doy,npp1-npp2)
plt.subplot(313)
plt.plot(doy,rh1-rh2)
plt.show()
