from classesCust.element_class import Element
from classesCust.lgt_class import Lgt

# POLARIZATION MAYHEM

def main():
    a = Element()
    a.loadStandard('mirror')
    c = a.modelNum
    print(c)


if __name__ == '__main__':
    main()