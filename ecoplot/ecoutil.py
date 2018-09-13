

import numpy as np

class VarNotInFile(Exception):
    def __str__(self): return "VarNotInFile"


def get_output_file_name(fdir,year,otype):
    '''
    create output file name based on specified file directory, year and type
    supported otype:
    dc: daily carbon flux file
    dw: daily water varaibles
    hc: hourly carbon variables
    hh: hourly energy variables
    hn: hourly nitrogen variables
    hp: hourly phosphorus variables
    hw: hourly water variables
    '''
    ofile='%s/01010%4d%s'%(fdir,year,otype)
    return ofile


def read_output_file(ofilename):

    try:
        f=open(ofilename,'r')
        header = f.readline()
        header = header.strip()
        var_names = header.split()

        hourly_data=var_names[2]=='HOUR'

        nvar=len(var_names)
        if hourly_data:
            vshft=3
            print 'Hourly output variables'
        else:
            vshft=2
            print 'Daily output variables'

        for n in range(nvar):
            if n>= vshft:
                print '%d:%s\n'%(n-vshft+1,var_names[n])


        data=np.loadtxt(f)
        f.close()

        doy=data[:,0]

        return doy,data[:,vshft:nvar],var_names[vshft:]
    except IOError:
        print 'Open or read file %s failed\n'%ofilename


def extract_var(otype,varnames,data,varoi):
    '''
    Extract time series for the variable of interest given by varoi
    '''
    ts=[]
    try:
        j=0
        for var in varnames:
            if var == varoi:
                ts=data[:,j]
                break
            j=j+1
        if do_var_cdif(varoi,otype):
            ts[1:]=np.diff(ts)
    except:
        print "Variable does not exist on file"
        raise VarNotInFile()

    return ts

def do_var_cdif(varname,otype):

    if otype=='dc':
        yesno = (varname =='NBP')    \
            or (varname =='ECO_GPP') \
            or (varname =='ECO_RA')  \
            or (varname =='ECO_NPP') \
            or (varname =='ECO_RH')
    else:
        yesno=False
    return yesno



def read_output_var(fdir,year1,year2,otype,varoi):
    '''
    read multiyear data for a given variable
    '''

    for year in range(year1,year2+1):
        file=get_output_file_name(fdir,year,otype)
        doy,data,var_names=read_output_file(file)
        ts0=extract_var(otype,var_names,data,varoi)

        if year == year1:
            ts=ts0
        else:
            ts=np.append(ts,ts0)


    return ts
