import random

diccionario = ['casa','cascada', 'fuente', 'tienda']
escenario = \
            '''   
        ~~~~~~~~~|~
                |
        0123456 J    
        ~~~~~~~~~~~   
        '''

simbolos = '><(((º>'


def iniciar_juego(diccionario):
            palabra = random.choice(diccionario).lower()
            tablero = ['_']*len(palabra)
            return tablero, palabra, []


def mostrar(errores):
            escena = escenario
            for i in range (0, len(simbolos)):
                simbolo = simbolos[i] if i < errores else ' '
                escena = escena.replace(str(i), simbolo)
            print(escena)


def mostrar_tablero(tablero, letras_erroneas) :
            for casilla in tablero:
                print(casilla, end=' ')
            print()
            print()

            if len(letras_erroneas)> 0:
                print('letras erroneas: ', *letras_erroneas)
                print()


def pedir_letra(tablero, letras_erroneas):
            valida = False
            while not valida:
                letra = input("Introduce una letra: " ).lower()
                valida = 'a' <= letra <= 'z' and len(letra) == 1
                if not valida :
                    print("Error, no se introdujo o se coloco mal la letra")
                else:
                    valida = letra not in tablero + letras_erroneas
                    if not valida:
                        print("Leta repetida, proba con otra")
            
            return letra

def procesar_letra(letra, palabra, tablero, letras_erroneas):
            if letra in palabra:
                print('Has acertado una letra.')
                actualizar_tablero(letra, palabra, tablero)
            else:
                print('Has fallado.')
                letras_erroneas.append(letra)

def actualizar_tablero(letra, palabra, tablero):
            for indice, letra_palabra in enumerate(palabra):
                if letra == letra_palabra:
                    tablero[indice] = letra 

def comprobar_palabra(tablero):
            return '_' not in tablero

def jugar_al_ahorcado(diccionario):

            tablero, palabra, letras_erroneas = iniciar_juego(diccionario)

            while len(letras_erroneas) < len(simbolos):
                mostrar(len(letras_erroneas))
                mostrar_tablero(tablero, letras_erroneas)
                letra = pedir_letra(tablero, letras_erroneas)
                procesar_letra(letra, palabra, tablero, letras_erroneas)
                if comprobar_palabra(tablero):
                    print("Bien lo has logrado")
                    break
            else:
                    print(f"Lastima, perdiste, la palabra adivinar era ",{palabra})
                    mostrar(len(letras_erroneas))

            mostrar_tablero(tablero, letras_erroneas)    


if __name__ == '__main__':
            diccionario = ['casa', 'pescado', 'juego', 'calabaza']

            while True:
                jugar_al_ahorcado(diccionario)