
class bicicleteria():
    def crearBicicleta(self, nmero_de_serie, modelo, anio, precio):
        nmero_de_serie = input("Coloque la cadena alfanumerica de la bicicleta: ")
        modelo = input("Coloque modelo de la bicicleta: ")
        anio = int(input("Coloque año de la bicicleta: "))
        precio = int(input("Coloque precio de la bicicleta: "))
        self.nmero_de_serie = nmero_de_serie
        self.modelo = modelo
        self.anio = anio
        self.precio = precio
        

    def vender_bicicleta(self, bicicletas_vendidas, cantidaddebicicletasvendidas):
        bicicletas_vendidas = int(input("Coloque la cantidad de bicicletas vendidas"))
        cantidaddebicicletasvendidas = bicicletas_vendidas + cantidaddebicicletasvendidas
        self.bicicletas_vendidas = bicicletas_vendidas
        self.cantidadbicicletasvendidas = self.cantidadbicicletasvendidas
        if self.cantidadBicletas < bicicletas_vendidas:
            bicicletas_vendidas = int(input("La opcion no puede ser mayor a la cantidad de bicicletas en la bicicleteria, coloque de nuevo: "))
            self.cantidadBicletas = self.cantidadBicletas - bicicletas_vendidas
            print("La bicicleta fue vendida")
        elif self.cantidadBicletas > bicicletas_vendidas:
            self.cantidadBicletas = self.cantidadBicletas - bicicletas_vendidas
            print("La bicicleta fue vendida")
        bicicletas.pop(input("Coloque numero de serie, para eliminar el objeto: "))

    def cantidadDeVentas(self, cantidaddeventas):
        print(f"La cantidad de bicicletas vendidas es de: ", {self.cantidadbicicletasvendidas})
        cantidaddeventas = self.precio + cantidaddeventas
        self.cantidaddeventas = cantidaddeventas
        print(f"Se lleva un total acumulado de: ", {self.cantidaddeventas})

    def comprar_bicicleta(self, cantidad_bicicletas_compradas):
         cantidad_bicicletas_compradas = self.cantidadBicletas + cantidad_bicicletas_compradas
         print(f"La cantidad de bicicletas compradas es de: " ,{cantidad_bicicletas_compradas})

    def get_precio(self, variable):
        variable = input("Coloque numero de serie: ")
        if variable == self.nmero_de_serie:
            print(f"El precio es de", {self.precio})
        elif variable != self.nmero_de_serie:
            print("La bicicleta fue vendida o no esta dentro de los parametros.") 

    def set_precio(self, variable):
        variable = input("Coloque numero de serie de la bicicleta que desea cambiar el precio: ")
        if variable == self.nmero_de_serie:
            self.precio = int(input("Coloque nuevo precio: "))
        elif variable != self.nmero_de_serie:
            print("La bicicleta fue vendida o no esta dentro de los parametros.")

    def get_nmero_de_serie(self):
        print(f"Los numeros de serie son: ", {bicicletas.nmero_de_serie})                 





bicicletas = {}
bicicletas = bicicleteria()
opcion = 0

while opcion != 8:

    print("Las opciones son: ")
    print("1) crear bicicleta")
    print("2) Cantidad de ventas")
    print("3) Vender bicicleta")
    print("4) Comprar bicicleta")
    print("5) Ver precio de bicicleta")
    print("6) Cambiar precio de bicicleta")
    print("7) Ver los numeros de series de las bicicletas")
    print("8) Salir")
    opcion= int(input("Coloque opcion: "))
    if opcion == 1:
        bicicletas.crearBicicleta( nmero_de_serie=None, modelo=None, anio=None, precio=None)
    if opcion == 2:
        bicicletas.cantidadDeVentas()
    if opcion == 3:
        bicicletas.vender_bicicleta()
    if opcion == 4:
        bicicletas.crearBicicleta()
        bicicletas.comprar_bicicleta()
    if opcion == 5:
        bicicletas.get_precio()
    if opcion == 6:
        bicicletas.set_precio()
    if opcion == 7:
        bicicletas.get_nmero_de_serie()
    if opcion == 8:
        print("Ciclo finalizado") 



