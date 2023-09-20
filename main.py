from logica.DibujoCuadrado import DibujoCuadrado

if __name__ == "__main__":
    dimension = int(input("Escribe la dimensión N >= 2 del cuadrado a dibujar: "))

    dibujoCuadrado = DibujoCuadrado(dimension)
    
    dibujoCuadrado.dibujarPrimeraLinea()
    dibujoCuadrado.dibujarLaterales()
    dibujoCuadrado.dibujarLineaAbajo()

    