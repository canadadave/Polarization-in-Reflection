class Element():
    def __init__(self):
        # name of element (e.g. 'First focussing lens') [string]
        self.desc = 'unnamed'
        # type of element (e.g. 'mirror','lens') [string]
        self.kind = 'unspecified'
        # model number [string]
        self.modelNum = 'unspecified'
        # properties of element [dict]
        self.props = {}
        # position on table (plane of table/ xz-plane) [list]
        self.pos = [0, 0]
        # angle with z-axis in rad [double]
        self.gamma = 0

    def rotate(self,angle=0):
        self.gamma = self.gamma+angle

    def resetPos(self):
        self.pos = [0, 0]

    def loadProps(self, wavelength=500):
        import sys
        sys.path.append('./PyTMM')
        from PyTMM.refractiveIndex import RefractiveIndex

        # Refractive index
        catalog = RefractiveIndex("./dbs/refractiveindex/database")
        mat = catalog.getMaterial('main', 'Si', 'Aspnes')
        # wavelength in nanometers
        eta = mat.getRefractiveIndex(wavelength)
        kappa = mat.getExtinctionCoefficient(wavelength)

        self.props = {'eta': eta, 'kappa': kappa}

    def loadStandard(self, kindin=None):
        # Unfinished

        # Fill element-object with standard values from reference library
        stdelem = {'mirror': '10D20ER.2',
                   'lens': "LA1027-ML"}

        if kindin is not None:
            self.kind = kindin
        if self.kind == 'unspecified':
            return
        else:
            self.modelNum = stdelem[self.kind]

        self.loadProps