

#Creamos una clase bicicleteria, la cual va a tener sus atributos y metodos
class bicicleteria:
    #Aqui igualamos todo a 0 para que el conteo empiece desde ese y no empiece con otro numero al azar
    bicicletas = 0
    bicicletas = bicicletas + 1
    cantidad_de_ventas = int
    
    def vender_bicicleta():
        cantidad_vendida = cantidad_vendida + 1
        #Subimos la cantidad de de bicicletas vendidas

    def comprar_bicicleta():
        cantidad_comprada = cantidad_comprada + 1
        #Desde aqui subimos la cantidad de bicicletas compradas

    def gananciasDeclaradas(self):
        declarar_ganancias = input(float("Ingrese ganancias de las ventas: "))
        self.declarar_ganancias = declarar_ganancias
        print(f"Total ganado es de: ", {self.declarar_ganancias})
        #Desde aqui podemos declarar las ganancias que se tiene con la venta de una bicicleta
        

#Instanciamos el clase Bicicleta con sus atributos y metodos
class Bicicleta:
    def cargarbici(self) -> None:
        #Con este metodo cargamos una bicicleta nueva y la instanciamos
        nmero_de_serie =str(input("Numero de serie: "))
        modelo =str(input("Modelo: "))
        anio = int(input("Año: "))
        precio = float(input("Precio: "))
        self.nmero_de_serie = nmero_de_serie
        self.modelo = modelo
        self.anio = anio
        self.precio = precio

    def set_precio(self, bici):
        #Con este metodo podemos modificar el precio de la bicicleta a llamar
        variable = str(input("Ingrese numero de serie de la bicicleta: "))
        if variable == self.nmero_de_serie:
            precio = float(input("Ingrese el nuevo precio de la bicicleta: "))
            self.precio = precio
        elif variable != self.nmero_de_serie:
            print("Error, el numero de serie no existe")    

    def get_precio(self):
        #Con este metodo obenemos el el precio de la bicicleta
        #La igualamos a una variable vacia para poder llamar esa bicicleta y que no llame otra
        variable = str(input("Ingrese numero de serie de la bicicleta: "))
        if variable == self.nmero_de_serie:
           print("El precio de la bicicleta es de: ", self.precio)
        elif variable != self.nmero_de_serie:
            print("Error, el numero de serie no existe") 
    def get_nmero_de_serie(self):
        #Aqui llamamos los numeros de serie de las bicicletas
        print(self.nmero_de_serie)
bici = {}
bici = Bicicleta()
bicicleteria1 = bicicleteria()
opcion = 0

#Un pequeño menu interactivo para poder entrar en los diferentes metodos y poder salir y entrar
while opcion != 8:
    print("Opcion 1 crear una bicicleta")
    print("Opcion 2 cambiar el precio de una bicicleta")
    print("Opcion 3 ver el precio de una bicicleta")
    print("Opcion 4 ver el numeros de serie de una bicicleta")
    print("Opcion 5 ver cantidad de bicicletas compradas")
    print("Opcion 6 ver cantidad de bicicletas vendidas")
    opcion = int(input("Ingrese la opcion que desea: "))
    if opcion == 1:
        bici.cargarbici()
        bicicleteria1()
        bicicleteria1.comprar_bicicleta()
    if opcion == 2:
        bici.set_precio()
    if opcion == 3:
        bici.get_precio()
    if opcion == 4:
        bici.get_nmero_de_serie()
    if opcion == 5:
        print(bicicleteria1.comprar_bicicleta())
    if opcion == 6:
        print(bicicleteria1.vender_bicicleta()) 
    if opcion == 8:
        break
