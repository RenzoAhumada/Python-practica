
#Se crea la clase triangulo la cual tendra un constructor para pasar los datos de los lados y asi poder utilizarlos mas adelante
class triangulo():
    def __init__(self, lado1, lado2, lado3):
            lado1 = int(input("Coloque lado 1 "))
            lado2 = int(input("Coloque lado 2 "))
            lado3 = int(input("Coloque lado 3 "))
            
            print("Se esta creando su triangulo")

            self.lado1 = lado1
            self.lado2 = lado2
            self.lado3 = lado3
    def mostrarLados(self):
        print(f"Los lados son: Lado 1", {self.lado1}, "Lado 2 ", {self.lado2} , "Lado 3 ", {self.lado3} )
    def ladoMayor(self):

        #En este pequeño bucle se verificara cual es el lado mayor, el cual se representa con una variable, la cual verifica segun si el lado es mayor al anterior este tomara su lugar
                ladomayor = self.lado1         
                if ladomayor < self.lado2:
                    ladomayor = self.lado2                  
                elif ladomayor < self.lado3:
                    ladomayor = self.lado3
                

                print(f"El lado mayor es {ladomayor}")                      
    def mostrarTipo(self):

        #Aqui se verifica la cantidad de lados iguales.
        if self.lado1 == self.lado2 & self.lado1 == self.lado3:
            print("El triangulo es un de tipo equilatero")
        elif self.lado1 == self.lado2 & self.lado1 != self.lado3:
            print("El triangulo es de tipo isoceles")
        elif self.lado2 == self.lado3 & self.lado1 != self.lado2:
             print("El triangulo es de tipo isoceles")
        else:
            print("El triangulo es de tipo escaleno")            
