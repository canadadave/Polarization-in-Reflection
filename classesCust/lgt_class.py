import array as arr
from numpy import sqrt


class Lgt():

    def __init__(self):
        # intensity
        self.int = 100
        # light frequency
        self.nu = 400e12      #[Hz]
        # spectral bandwidth
        self.delta_nu = 0     #[Hz]
        # wavevector in xz-plane
        self.k = arr.array('d', [0, 0, 0])
        # polarization vector in xy-plane
        self.v = arr.array('d', [0, 1])
        # coherence length
        self.s_c = 1e12       #[m]
        # beam waist
        self.w0 = 1           #[mm]

    def normVector(self,vec):
        # Normalizes any array-type structure
        magn = 0
        for idx in vec:
            magn = magn+vec[idx]**2
        norm = sqrt(magn)
        for idx in vec:
            vec[idx] = 1/norm*vec[idx]
        return vec

    def normV(self):
        # norm = sqrt(self.v[0]**2+self.v[1]**2)
        # self.v[0]=1/norm*self.v[0]
        # self.v[1]=1/norm*self.v[1]
        self.v = self.normVector(self.v)