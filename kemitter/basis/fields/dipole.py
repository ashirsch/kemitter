import numpy as np
from numba import jit, prange


@jit("complex128[:,:,:](complex128[:,:],complex128[:,:],complex128[:,:],complex128[:,:],"
     "complex128[:,:,:],complex128[:,:,:],float64,float64)",
     parallel=True, nopython=True)
def _ypol_edx(ux, uy, uz2s, uz3, Tpxy, Tsz, n2o, n3):
    edx = np.zeros_like(Tsz)
    for uxi in prange(edx.shape[0]):
        for uyi in prange(edx.shape[1]):
            B = (np.sqrt(np.abs(n3 / uz3[uxi, uyi]) / 3.0) * (uz3[uxi, uyi] / (ux[uxi, uyi] ** 2 + uy[uxi, uyi] ** 2)))
            for w in prange(edx.shape[2]):
                edx[uxi,uyi,w] = B * ((ux[uxi,uyi] * uy[uxi,uyi] / n2o * Tpxy[uxi, uyi, w]) -
                                      (ux[uxi,uyi] * uy[uxi,uyi] / uz2s[uxi, uyi] * Tsz[uxi, uyi, w]))
    return edx


@jit("complex128[:,:,:](complex128[:,:],complex128[:,:],complex128[:,:],complex128[:,:],"
     "complex128[:,:,:],complex128[:,:,:],float64,float64)",
     parallel=True, nopython=True)
def _ypol_edy(ux, uy, uz2s, uz3, Tpxy, Tsz, n2o, n3):
    edy = np.zeros_like(Tsz)
    for uxi in prange(edy.shape[0]):
        for uyi in prange(edy.shape[1]):
            B = (np.sqrt(np.abs(n3 / uz3[uxi, uyi]) / 3.0) * (uz3[uxi, uyi] / (ux[uxi, uyi] ** 2 + uy[uxi, uyi] ** 2)))
            for w in prange(edy.shape[2]):
                edy[uxi,uyi,w] = B * ((uy[uxi,uyi]**2 / n2o * Tpxy[uxi, uyi, w]) +
                                      (ux[uxi,uyi]**2 / uz2s[uxi,uyi] * Tsz[uxi, uyi, w]))
    return edy


@jit("complex128[:,:,:](complex128[:,:],complex128[:,:],complex128[:,:],complex128[:,:],"
     "complex128[:,:,:],float64,float64)",
     parallel=True, nopython=True)
def _ypol_edz(ux, uy, uz2s, uz3, Tpz, n2o, n3):
    edz = np.zeros_like(Tpz)
    for uxi in prange(edz.shape[0]):
        for uyi in prange(edz.shape[1]):
            B = (np.sqrt(np.abs(n3 / uz3[uxi, uyi]) / 3.0) * (uz3[uxi, uyi] / (ux[uxi, uyi] ** 2 + uy[uxi, uyi] ** 2)))
            Bz = B * (uy[uxi,uyi]*(ux[uxi,uyi]**2+uy[uxi,uyi]**2) / (n2o*uz2s[uxi,uyi]))
            for w in prange(edz.shape[2]):
                edz[uxi,uyi,w] = Bz * Tpz[uxi, uyi, w]
    return edz


@jit("complex128[:,:,:](complex128[:,:],complex128[:,:],complex128[:,:],complex128[:,:],"
     "complex128[:,:,:],complex128[:,:,:],float64,float64)",
     parallel=True, nopython=True)
def _ypol_mdx(ux, uy, uz2p, uz3, Tsxy, Tpz, n2o, n3):
    mdx = np.zeros_like(Tpz)
    for uxi in prange(mdx.shape[0]):
        for uyi in prange(mdx.shape[1]):
            B = (np.sqrt(np.abs(n3 / uz3[uxi, uyi]) / 3.0) * (uz3[uxi, uyi] / (ux[uxi, uyi] ** 2 + uy[uxi, uyi] ** 2)))
            for w in prange(mdx.shape[2]):
                mdx[uxi, uyi, w] = -B * ((uy[uxi, uyi] ** 2 / uz2p[uxi,uyi] * Tpz[uxi, uyi, w]) +
                                        (ux[uxi, uyi] ** 2 / n2o * Tsxy[uxi, uyi, w]))
    return mdx


@jit("complex128[:,:,:](complex128[:,:],complex128[:,:],complex128[:,:],complex128[:,:],"
     "complex128[:,:,:],complex128[:,:,:],float64,float64)",
     parallel=True, nopython=True)
def _ypol_mdy(ux, uy, uz2p, uz3, Tsxy, Tpz, n2o, n3):
    mdy = np.zeros_like(Tpz)
    for uxi in prange(mdy.shape[0]):
        for uyi in prange(mdy.shape[1]):
            B = (np.sqrt(np.abs(n3 / uz3[uxi, uyi]) / 3.0) * (uz3[uxi, uyi] / (ux[uxi, uyi] ** 2 + uy[uxi, uyi] ** 2)))
            for w in prange(mdy.shape[2]):
                mdy[uxi,uyi,w] = -B * ((ux[uxi,uyi] * uy[uxi,uyi] / n2o * Tsxy[uxi, uyi, w]) -
                                      (ux[uxi,uyi] * uy[uxi,uyi] / uz2p[uxi, uyi] * Tpz[uxi, uyi, w]))
    return mdy


@jit("complex128[:,:,:](complex128[:,:],complex128[:,:],complex128[:,:],complex128[:,:],"
     "complex128[:,:,:],float64,float64)",
     parallel=True, nopython=True)
def _ypol_mdz(ux, uy, uz2s, uz3, Tsz, n2o, n3):
    mdz = np.zeros_like(Tsz)
    for uxi in prange(mdz.shape[0]):
        for uyi in prange(mdz.shape[1]):
            B = (np.sqrt(np.abs(n3 / uz3[uxi, uyi]) / 3.0) * (uz3[uxi, uyi] / (ux[uxi, uyi] ** 2 + uy[uxi, uyi] ** 2)))
            Bz = B * (ux[uxi,uyi]*(ux[uxi,uyi]**2+uy[uxi,uyi]**2) / (n2o*uz2s[uxi,uyi]))
            for w in prange(mdz.shape[2]):
                mdz[uxi,uyi,w] = -Bz * Tsz[uxi, uyi, w]
    return mdz
