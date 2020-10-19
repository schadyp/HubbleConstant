#!/usr/bin/env python

"""
Reading in and manipulating ascii files

"""

# Load in module needed to read in ascii files
import numpy as np
import pandas as pd

#------------------------------------------------------------------------
def readspec(infile):
    
    # Read in first spectrum
    df = pd.read_csv('Spectra/%s' % infile,sep=' ')

    wave = df['Wavelength_Angs'].values
    flux = df['Flux(erg/s/cm2/A)'].values
    specdata = np.array([wave,flux])

    return specdata

#------------------------------------------------------------------------
def readLC(infile):
    
    # Read in first spectrum
    df = pd.read_csv('Cepheids/Lightcurves/%s' % infile,sep=' ')

    mjd = df['MJD'].values
    mag = df['Vmag'].values
    mag_err = df['mag_err'].values

    return mjd-2452978,mag

#------------------------------------------------------------------------
def readdata(infile):
    
    # Read in first spectrum
    df = pd.read_csv('Expansion/%s' % infile)

    Do = df["Distance o (Mpc)"].values
    Dz = df["Distance z (Mpc)"].values
    vel_LG = df["Velocity LG (km/s)"].values
    vel_virgo = df["Velocity Virgo (km/s)"].values

    return Do,vel_virgo
