from classes.element_class import Element
import numpy as np
import scipy as sp
import sys
sys.path.append('./PyTMM')
from PyTMM.refractiveIndex import RefractiveIndex

catalog = RefractiveIndex("./dbs/refractiveindex/database")
mat = catalog.getMaterial('main', 'Si', 'Aspnes')
# wavelength in nanometers
n1 = mat.getRefractiveIndex(500)
n2 = mat.getExtinctionCoefficient(500)

print(n1)
print(n2)

stdelem = {'mirror': '10D20ER.2', 'lens': 'LA1027-ML'}
a = Element()
print(a.kind)
