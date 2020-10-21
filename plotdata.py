import matplotlib.pyplot as plt
import numpy as np
from scipy import optimize
from scipy.interpolate import interpn

"""
Plotting data

"""

#------------------------------------------------------------------------
def plotspec(spec1,spec2,spec3,spec4,n1=10,n2=15,n3=4,n4=10,lab1='NGC4258',lab2='NGC4639',lab3='Early type',lab4='Late type',fs=15,xmin=3500,xmax=9200,ymin=0,ymax=16):
    
    plt.plot(spec1[0,:],spec1[1,:]*n1/max(spec1[1,:]),label=lab1)
    plt.plot(spec2[0,:],spec2[1,:]*n2/max(spec2[1,:]),label=lab2)
    plt.plot(spec3[0,:],spec3[1,:]*n3/max(spec3[1,:]),label=lab3)
    plt.plot(spec4[0,:],spec4[1,:]*n4/max(spec4[1,:]),label=lab4)
    plt.xlabel("Wavelength (Angstrom)",size=20)
    plt.ylabel('Normalised flux',size=20)
    plt.xlim(xmin,xmax)
    plt.ylim(ymin,ymax)
    plt.legend(fontsize=fs)

#------------------------------------------------------------------------
def HubbleDiagram(D,z,m='o',col='r',line='none'):
    
    plt.xlabel("Distance (Mpc)",size=20)
    plt.ylabel("Recession Velocity (km/s)",size=20)
    plt.plot(D,z,marker=m,c=col,ls=line,ms=10)
    
#------------------------------------------------------------------------
def linfit(xdata, ydata, norm = 0, pinit=[70.0]):

    # Define function for calculating a power law
    linear = lambda p, x: norm + (p[0] * x)
    linfit = lambda p, x, y: y-linear(p,x)

    # Fit data with function defined above
    out = optimize.leastsq(linfit,pinit,args=(xdata,ydata), full_output=1)

    # Determine best-fit parameters and associated errors
    index = out[0]
    covar = out[1]
    indexErr = np.sqrt( covar[0][0] )
    
    return index[0],indexErr*100
