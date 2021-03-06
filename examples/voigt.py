import pyspeckit
import numpy as np
from pyspeckit.spectrum.models import voigtfitter

# technically, the voigt fitter works as a singlefitter (i.e., you can fit the
# background level and the peak simultaneously) 
# in practice, however, you need to fit the background independently except for
# gaussians.  I don't know why this is.

xarr = pyspeckit.spectrum.units.SpectroscopicAxis(np.linspace(-100,100,500),unit='km/s',refX=1e9,refX_units='Hz')
VF = voigtfitter.voigt_fitter()

sp1 = pyspeckit.Spectrum(xarr=xarr, data=VF.voigt(xarr,1,0,2.5,2.5) + np.random.randn(xarr.shape[0])/20., error=np.ones(xarr.shape[0])/20.)
sp1.plotter()
sp1.specfit(fittype='gaussian',composite_fit_color='b',clear=False,annotate=False)
sp1.specfit(fittype='lorentzian',composite_fit_color='g',clear=False,annotate=False)
sp1.specfit(fittype='voigt',composite_fit_color='r',clear=False,annotate=True)
sp1.baseline.annotate()

sp2 = pyspeckit.Spectrum(xarr=xarr, data=VF.voigt(xarr,1,0,2.5,5.0) + np.random.randn(xarr.shape[0])/20., error=np.ones(xarr.shape[0])/20.)
sp2.plotter()
sp2.specfit(fittype='gaussian',composite_fit_color='b',clear=False,annotate=False)
sp2.specfit(fittype='lorentzian',composite_fit_color='g',clear=False,annotate=False)
sp2.specfit(fittype='voigt',composite_fit_color='r',clear=False,annotate=True)
sp2.baseline.annotate()

sp3 = pyspeckit.Spectrum(xarr=xarr, data=VF.voigt(xarr,1,0,2.5,5.0) + np.random.randn(xarr.shape[0])/50., error=np.ones(xarr.shape[0])/50.)
sp3.plotter()
sp3.specfit(fittype='gaussian',composite_fit_color='b',clear=False,annotate=False)
sp3.specfit(fittype='lorentzian',composite_fit_color='g',clear=False,annotate=False)
sp3.specfit(fittype='voigt',composite_fit_color='r',clear=False,annotate=True)
sp3.baseline.annotate()
