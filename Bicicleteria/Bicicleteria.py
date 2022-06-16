





class bicicleteria():
    def __init__(self) -> None:
        bicicletas = {}
        self.bicicletas = bicicletas [Bicicleta]
        ganancias = float(0,0)
        cantidad_de_ventas = int(0)
        self.ganancias = ganancias
        self.cantidad_de_ventas = cantidad_de_ventas
        

    def vender_bicicleta(self, Bicicleta):
        venta_bici = self.cantidad_de_ventas + 1
        self.cantidad_de_ventas = venta_bici
        gananciastotal = self.ganancias + self.bicicletas(bici.precio)

        print(venta_bici)

    def comprar_bicicleta(self, Bicicleta):
        compra_bici = compra_bici + 1
        
        




class Bicicleta():
    def __init__(self) -> None:
        nmero_de_serie =str(input("Numero de serie: "))
        modelo =str(input("Modelo: "))
        anio = int(input("Año: "))
        precio = float(input("Precio: "))
        self.nmero_de_serie = nmero_de_serie
        self.modelo = modelo
        self.anio = anio
        self.precio = precio

    def set_precio(self):
        variable = str(input("Ingrese numero de serie de la bicicleta: "))
        if variable == self.nmero_de_serie:
            precio = float(input("Ingrese el nuevo precio de la bicicleta: "))
            self.precio = precio
        elif variable != self.nmero_de_serie:
            print("Error, el numero de serie no existe")    

    def get_precio(self):
        variable = str(input("Ingrese numero de serie de la bicicleta: "))
        if variable == self.nmero_de_serie:
           print("El precio de la bicicleta es de: ", self.precio)
        elif variable != self.nmero_de_serie:
            print("Error, el numero de serie no existe") 
    def get_nmero_de_serie(self):
        print(self.nmero_de_serie)


bici = Bicicleta()
bici.get_precio()
bici.get_nmero_de_serie()
bici.set_precio()
bici.get_precio()
bicicleteria1 = bicicleteria()
print(bicicleteria1)
