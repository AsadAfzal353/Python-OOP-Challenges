
class DNABase:

    valid_names = { 'a': 'adenine', 'adenine': 'adenine',
                    'c': 'cytosine', 'cytosine': 'cytosine',
                    'g': 'guanine', 'guanine' : 'guanine',
                    't': 'thymine', 'thymine': 'thymine'
                  }
    
    def __init__(self, nucleotide):
        self.base = nucleotide
        self.set_base(self.base)

    def __repr__(self):
        return f"{type(self).__name__}(nucleotide='{self._base}')"

    def get_base(self):
        return self._base
    
    def set_base(self, name):
        if name.lower() not in self.valid_names.keys():
            raise ValueError(f"{name} is not a recognized DNA nucleotide")
        else:
            self._base = self.valid_names[name.lower()]

    base = property(fget=get_base, fset=set_base)


if __name__ == "__main__":

    b1 = DNABase('A')
    b1 # DNABase(nucleotide='adenine')

    b1.base # 'adenine'

    b1.nucleotide #AttributeError: 'DNABase' object has no attribute 'nucleotide'

    b1.base = 'c'
    b1 # DNABase(nucleotide='cytosine')

    b1.base = "Aoli" # ValueError: Aoli is not a recognized DNA nucleotide
    b1

    DNABase("aol") # ValueError: aol is not a recognized DNA nucleotide

    b1.base = "thYMIne"
    b1 # DNABase(nucleotide='thymine')

    b1.__dict__