class DibujoCuadrado():
    def __init__ (self, dimension):
        self.dimension = dimension

    def dibujarPrimeraLinea (self):
        for i in range (self.dimension + 1):
            print('* ', end = '') # * + un espacio

        print()

    def dibujarLaterales (self):
        j = 1
        while j <= self.dimension - 2: 
            for k in range(self.dimension):
                if k == 0 :
                    print('* ', end = '') # * + un espacio
                elif k == self.dimension - 1:
                    print('  *', end = '')  # Dos espacios + *
                else:
                    print('  ', end = '') # Dos espacios
            # Fin del if:
            print()
            j += 1

    def dibujarLineaAbajo (self):
        i = 0
        while i < self.dimension + 1:
            print('* ', end = '') # * + un espacio
            i += 1
        