from abc import ABC, abstractmethod

class Forma(ABC):
    def __init__(self, reng='Qara'):
        self.reng = reng

    def sahesi(self):
        pass

    def perimetri(self):
        pass

    def tesvir_et(self):
        return f"Bu, {self.reng} rengi forma."

class Duzbucaq(Forma):
    def __init__(self, en, uzunluq, reng='Qara'):
        super().__init__(reng)
        self.en = en 
        self.uzunluq = uzunluq


    def sahesi(self):
        return self.en * self.uzunluq
    
    def preimetri(self):
        return 2 * (self.en + self.uzunluq)
    
    def tesvir_et(self):
        return f"Bu, {self.reng} rengli duzbucaqli, eni {self.en}, uzunluq"
    
class Daire(Forma):
    def __init__(self, radius, reng='Qara'):
        super().__init__(reng)
        self.radius = radius


    def sahesi(self):
        return math.pi * self.radius ** 2
    
    def perimetri(self):
        return 2 * math.pi * self.radius
    
    def tesvir_et(self):
        return f"Bu, {self.reng} rengli daire, radiusu {self.radius}."
    
def forma_melumat_ver(forma):
    if not isinstance(forma, Forma):
        raise TypeError("Obyekt Forma tipinde deyil")
    print(forma.tesvir_et())
    print(f"Sahesi: {forma.sahesi()}")
    print(f"Perimetri: {Forma.perimetri()}")

# TEST 
try:
    d = Duzbucaq(5, 10, 'Qrmizi')
    a = Daire(7, 'Mavi')
    forma_melumat_ver(d)
    forma_melumat_ver(a)
    forma_melumat_ver("FormaDeyil") # Burada sehv verecek

except Exception as e:
    print(f"Xeta: {e}")