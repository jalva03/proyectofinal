#%% Funciones
def prime():
    tarifa = 20
    penvio = tarifa - tarifa
    print("El precio de envio es de: ", penvio)
        
def descuento():
    dia = input("¿Que dia de la semana es hoy?: ")
    precio = int(input("Ingrese el precio del producto de la lista de precios: "))
    if dia == "Sabado" or dia == "Domingo" or dia == "sabado" or dia == "domingo" or dia == "sábado" or dia == "Sábado":
        descuento = precio - (precio*.10)
        print("El producto con el 10% de descuento tiene un valor de: ", descuento)
    else:
        print("No hay descuento")
        
pfenvio = 20

def Sstock():
    stock = 10
    n = int(input("Ingrese la cantidad de productos a agregar en el stock: "))
    suma = stock + n
    print("El stock cuenta ahora con ", suma, " productos")
def Rstock():
    stock = 10
    n = int(input("Ingrese la cantidad de productos a remover en el stock: "))
    resta = stock - n
    print("El stock cuenta ahora con ", resta, " productos")    
    
def ventas():
    Cmicroondas = int(input("Ingrese la cantidad de microondas vendidos: "))
    Ctelevisiones = int(input("Ingrese la cantidad de televisiones vendidos: "))
    Cbocinas = int(input("Ingrese la cantidad de bocinas vendidos: "))
    Caspiradoras = int(input("Ingrese la cantidad de aspiradoras vendidos: "))
    Ccafeteras = int(input("Ingrese la cantidad de cafeteras vendidos: "))
    Csecadoras = int(input("Ingrese la cantidad de secadoras vendidos: "))
    Crefrigeradores = int(input("Ingrese la cantidad de refrigeradores vendidos: "))
    Cplanchas = int(input("Ingrese la cantidad de plachas vendidos: "))
    Chornos = int(input("Ingrese la cantidad de hornos vendidos: "))
    Clavadoras = int(input("Ingrese la cantidad de lavadoras vendidos: "))
    Pmicro = 2000
    Ptelevisiones = 7000
    Pbocinas = 500
    Paspiradoras = 700
    Pcafeteras = 600
    Psecadoras = 4000
    Prefri = 8000
    Pplachas =  800
    Phorno = 3500
    Plavadoras = 4500
    tmicro = Cmicroondas * Pmicro
    ttelevision = Ctelevisiones * Ptelevisiones
    tbocinas = Cbocinas * Pbocinas
    taspi = Caspiradoras * Paspiradoras
    tcafe = Ccafeteras * Pcafeteras
    tseca = Csecadoras * Psecadoras
    trefri = Crefrigeradores * Prefri
    tplacha = Cplanchas * Pplachas
    thorno = Chornos * Phorno
    tlava = Clavadoras * Plavadoras
    suma = tmicro + ttelevision +tbocinas + taspi + tcafe + tseca + trefri + tplacha + thorno + tlava
    print("Las ventas por mes que obtuviste fueron de: ", suma, " pesos")
#%%
# Dias de descuentos: Sábado y Domingo
# Contraseña de Admin: 12345
# Contraseña de Cliente: 54321
usuario = ["Admin","Cliente"]
print("""******MENÚ DE BIENVENIDA DE AMAZON*****
¿Es usted un admin o un cliente?
1)Admin
2)Cliente
***********************************************""")

who = int(input("Ingrese la opcion elegida: "))
if who == 1:
    contraseña = int(input("Ingrese la contraseña Admin: "))
    if contraseña == 12345:
        print("Bienvenido Amdin")
        print("""*****MENÚ DE OPCIONES DE ADMIN*****
        1)Stock
        2)Ventas del mes
        *****************************************""")
        option = int(input("Ingrese la opcion del menu: "))
        if option == 1:
            electros = ["Microondas", "Televisiones", "Bocinas", "Aspiradoras", "Cafeteras","Secadoras", "Refrigeradores", "Planchas", "Hornos", "Lavadoras"]
            print("""MENÚ DE STOCK DE LOS ELECTRODOMESTICOS CLASIFICADOS***
            1)Microondas
            2)Televisiones
            3)Bocinas
            4)Aspiradoras
            5)Cafeteras
            6)Secadoras
            7)Refrigeradores
            8)Planchas de ropa
            9)Hornos de gas
            10)Lavadoras
            **************************************************************""")
            electro = int(input("Ingrese el numero del electrodomestico del cual quiere revisar el stock: "))
            if electro == 1:
                print(f'''*****MENU DE MARCAS DE {str(electros[electro -1]).upper()}*******
                1)Teka
                2)Whirlpool  
                3)Samsung
                4)Balay
                5)Bosch
                *********''')
                marcas = int(input("Ingrese el numero de la marca de microondas: "))
                if marcas == 1:
                    operacion = input("¿Quieres agregar o quitar productos del stock?")
                    if operacion == "sumar" or operacion == "Sumar":
                        Sstock()
                    elif operacion == "restar" or operacion == "Restar":
                        Rstock()
                if marcas == 2:
                    operacion = input("¿Quieres agregar o quitar productos del stock?")
                    if operacion == "sumar" or operacion == "Sumar":
                        Sstock()
                    elif operacion == "restar" or operacion == "Restar":
                        Rstock()
                if marcas == 3:
                    operacion = input("¿Quieres agregar o quitar productos del stock?")
                    if operacion == "sumar" or operacion == "Sumar":
                        Sstock()
                    elif operacion == "restar" or operacion == "Restar":
                        Rstock()
                if marcas == 4:
                    operacion = input("¿Quieres agregar o quitar productos del stock?")
                    if operacion == "sumar" or operacion == "Sumar":
                        Sstock()
                    elif operacion == "restar" or operacion == "Restar":
                        Rstock()
                if marcas == 5:
                    operacion = input("¿Quieres agregar o quitar productos del stock?")
                    if operacion == "sumar" or operacion == "Sumar":
                        Sstock()
                    elif operacion == "restar" or operacion == "Restar":
                        Rstock()
            if electro == 2:
                print(f'''*****MENU DE MARCAS DE {str(electros[electro -1]).upper()}*******
                1) 1)LG
                2)Toshiba
                3)Samsung
                4)Sony
                5)Panasonic
                *********''')
                marcas = int(input("Ingrese el numero de la marca de televisones: "))
                if marcas == 1:
                    operacion = input("¿Quieres agregar o quitar productos del stock?")
                    if operacion == "sumar" or operacion == "Sumar":
                        Sstock()
                    elif operacion == "restar" or operacion == "Restar":
                        Rstock()
                if marcas == 2:
                    operacion = input("¿Quieres agregar o quitar productos del stock?")
                    if operacion == "sumar" or operacion == "Sumar":
                        Sstock()
                    elif operacion == "restar" or operacion == "Restar":
                        Rstock()
                if marcas == 3:
                    operacion = input("¿Quieres agregar o quitar productos del stock?")
                    if operacion == "sumar" or operacion == "Sumar":
                        Sstock()
                    elif operacion == "restar" or operacion == "Restar":
                        Rstock()
                if marcas == 4:
                    operacion = input("¿Quieres agregar o quitar productos del stock?")
                    if operacion == "sumar" or operacion == "Sumar":
                        Sstock()
                    elif operacion == "restar" or operacion == "Restar":
                        Rstock()
                if marcas == 5:
                    operacion = input("¿Quieres agregar o quitar productos del stock?")
                    if operacion == "sumar" or operacion == "Sumar":
                        Sstock()
                    elif operacion == "restar" or operacion == "Restar":
                        Rstock()
                        
            if electro == 3:
                print(f'''*****MENU DE MARCAS DE {str(electros[electro -1]).upper()}*******
                1) 1)Sony
                2)Marshall
                3)Logitech
                4)KEF
                5)JBL
                *********''')
                marcas = int(input("Ingrese el numero de la marca de bocinas: "))
                if marcas == 1:
                    operacion = input("¿Quieres agregar o quitar productos del stock?")
                    if operacion == "sumar" or operacion == "Sumar":
                        Sstock()
                    elif operacion == "restar" or operacion == "Restar":
                        Rstock()
                if marcas == 2:
                    operacion = input("¿Quieres agregar o quitar productos del stock?")
                    if operacion == "sumar" or operacion == "Sumar":
                        Sstock()
                    elif operacion == "restar" or operacion == "Restar":
                        Rstock()
                if marcas == 3:
                    operacion = input("¿Quieres agregar o quitar productos del stock?")
                    if operacion == "sumar" or operacion == "Sumar":
                        Sstock()
                    elif operacion == "restar" or operacion == "Restar":
                        Rstock()
                if marcas == 4:
                    operacion = input("¿Quieres agregar o quitar productos del stock?")
                    if operacion == "sumar" or operacion == "Sumar":
                        Sstock()
                    elif operacion == "restar" or operacion == "Restar":
                        Rstock()
                if marcas == 5:
                    operacion = input("¿Quieres agregar o quitar productos del stock?")
                    if operacion == "sumar" or operacion == "Sumar":
                        Sstock()
                    elif operacion == "restar" or operacion == "Restar":
                        Rstock()
            if electro == 4:
                print(f'''*****MENU DE MARCAS DE {str(electros[electro -1]).upper()}*******
                1)Philips
                2)Shark
                3)Bosch
                4)Robot
                5)Dyson
                   *********''')
                marcas = int(input("Ingrese el numero de la marca de aspiradoras: "))
                if marcas == 1:
                    operacion = input("¿Quieres agregar o quitar productos del stock?")
                    if operacion == "sumar" or operacion == "Sumar":
                        Sstock()
                    elif operacion == "restar" or operacion == "Restar":
                        Rstock()
                if marcas == 2:
                    operacion = input("¿Quieres agregar o quitar productos del stock?")
                    if operacion == "sumar" or operacion == "Sumar":
                        Sstock()
                    elif operacion == "restar" or operacion == "Restar":
                        Rstock()
                if marcas == 3:
                    operacion = input("¿Quieres agregar o quitar productos del stock?")
                    if operacion == "sumar" or operacion == "Sumar":
                        Sstock()
                    elif operacion == "restar" or operacion == "Restar":
                        Rstock()
                if marcas == 4:
                    operacion = input("¿Quieres agregar o quitar productos del stock?")
                    if operacion == "sumar" or operacion == "Sumar":
                        Sstock()
                    elif operacion == "restar" or operacion == "Restar":
                        Rstock()
                if marcas == 5:
                    operacion = input("¿Quieres agregar o quitar productos del stock?")
                    if operacion == "sumar" or operacion == "Sumar":
                        Sstock()
                    elif operacion == "restar" or operacion == "Restar":
                        Rstock()
            if electro == 5:
                print(f'''*****MENU DE MARCAS DE {str(electros[electro -1]).upper()}*******
                1)Dolce Gusto
                2)Oster
                3)Nespresso
                4)Hamilton Beach
                5)Krups
                *********''')
                marcas = int(input("Ingrese el numero de la marca de cafeteras: "))
                if marcas == 1:
                    operacion = input("¿Quieres agregar o quitar productos del stock?")
                    if operacion == "sumar" or operacion == "Sumar":
                        Sstock()
                    elif operacion == "restar" or operacion == "Restar":
                        Rstock()
                if marcas == 2:
                    operacion = input("¿Quieres agregar o quitar productos del stock?")
                    if operacion == "sumar" or operacion == "Sumar":
                        Sstock()
                    elif operacion == "restar" or operacion == "Restar":
                        Rstock()
                if marcas == 3:
                    operacion = input("¿Quieres agregar o quitar productos del stock?")
                    if operacion == "sumar" or operacion == "Sumar":
                        Sstock()
                    elif operacion == "restar" or operacion == "Restar":
                        Rstock()
                if marcas == 4:
                    operacion = input("¿Quieres agregar o quitar productos del stock?")
                    if operacion == "sumar" or operacion == "Sumar":
                        Sstock()
                    elif operacion == "restar" or operacion == "Restar":
                        Rstock()
                if marcas == 5:
                    operacion = input("¿Quieres agregar o quitar productos del stock?")
                    if operacion == "sumar" or operacion == "Sumar":
                        Sstock()
                    elif operacion == "restar" or operacion == "Restar":
                        Rstock()
            if electro == 6:
                print(f'''*****MENU DE MARCAS DE {str(electros[electro -1]).upper()}*******
                1)LG
                2)Whirlpool
                3)Maytang
                4)Kenmore
                5)Speed Queen
                *********''')
                marcas = int(input("Ingrese el numero de la marca de secadoras: "))
                if marcas == 1:
                    operacion = input("¿Quieres agregar o quitar productos del stock?")
                    if operacion == "sumar" or operacion == "Sumar":
                        Sstock()
                    elif operacion == "restar" or operacion == "Restar":
                        Rstock()
                if marcas == 2:
                    operacion = input("¿Quieres agregar o quitar productos del stock?")
                    if operacion == "sumar" or operacion == "Sumar":
                        Sstock()
                    elif operacion == "restar" or operacion == "Restar":
                        Rstock()
                if marcas == 3:
                    operacion = input("¿Quieres agregar o quitar productos del stock?")
                    if operacion == "sumar" or operacion == "Sumar":
                        Sstock()
                    elif operacion == "restar" or operacion == "Restar":
                        Rstock()
                if marcas == 4:
                    operacion = input("¿Quieres agregar o quitar productos del stock?")
                    if operacion == "sumar" or operacion == "Sumar":
                        Sstock()
                    elif operacion == "restar" or operacion == "Restar":
                        Rstock()
                if marcas == 5:
                    operacion = input("¿Quieres agregar o quitar productos del stock?")
                    if operacion == "sumar" or operacion == "Sumar":
                        Sstock()
                    elif operacion == "restar" or operacion == "Restar":
                        Rstock()
            if electro == 7:
                print(f'''*****MENU DE MARCAS DE {str(electros[electro -1]).upper()}*******
                1)Mabe
                2)Whirlpool
                3)Daewoo
                4)Frigidaire
                5)Samsung
                *********''')
                marcas = int(input("Ingrese el numero de la marca de refrigeradores: "))
                if marcas == 1:
                    operacion = input("¿Quieres agregar o quitar productos del stock?")
                    if operacion == "sumar" or operacion == "Sumar":
                        Sstock()
                    elif operacion == "restar" or operacion == "Restar":
                        Rstock()
                if marcas == 2:
                    operacion = input("¿Quieres agregar o quitar productos del stock?")
                    if operacion == "sumar" or operacion == "Sumar":
                        Sstock()
                    elif operacion == "restar" or operacion == "Restar":
                        Rstock()
                if marcas == 3:
                    operacion = input("¿Quieres agregar o quitar productos del stock?")
                    if operacion == "sumar" or operacion == "Sumar":
                        Sstock()
                    elif operacion == "restar" or operacion == "Restar":
                        Rstock()
                if marcas == 4:
                    operacion = input("¿Quieres agregar o quitar productos del stock?")
                    if operacion == "sumar" or operacion == "Sumar":
                        Sstock()
                    elif operacion == "restar" or operacion == "Restar":
                        Rstock()
                if marcas == 5:
                    operacion = input("¿Quieres agregar o quitar productos del stock?")
                    if operacion == "sumar" or operacion == "Sumar":
                        Sstock()
                    elif operacion == "restar" or operacion == "Restar":
                        Rstock()
            
            if electro == 8:
                print(f'''*****MENU DE MARCAS DE {str(electros[electro -1]).upper()}*******
                1)Aigostar
                2)Philips
                3)Ufesa
                4)Rowenta  
                5)Dcenta
                *********''')
                marcas = int(input("Ingrese el numero de la marca de planchas de ropa: "))
                if marcas == 1:
                    operacion = input("¿Quieres agregar o quitar productos del stock?")
                    if operacion == "sumar" or operacion == "Sumar":
                        Sstock()
                    elif operacion == "restar" or operacion == "Restar":
                        Rstock()
                if marcas == 2:
                    operacion = input("¿Quieres agregar o quitar productos del stock?")
                    if operacion == "sumar" or operacion == "Sumar":
                        Sstock()
                    elif operacion == "restar" or operacion == "Restar":
                        Rstock()
                if marcas == 3:
                    operacion = input("¿Quieres agregar o quitar productos del stock?")
                    if operacion == "sumar" or operacion == "Sumar":
                        Sstock()
                    elif operacion == "restar" or operacion == "Restar":
                        Rstock()
                if marcas == 4:
                    operacion = input("¿Quieres agregar o quitar productos del stock?")
                    if operacion == "sumar" or operacion == "Sumar":
                        Sstock()
                    elif operacion == "restar" or operacion == "Restar":
                        Rstock()
                if marcas == 5:
                    operacion = input("¿Quieres agregar o quitar productos del stock?")
                    if operacion == "sumar" or operacion == "Sumar":
                        Sstock()
                    elif operacion == "restar" or operacion == "Restar":
                        Rstock()
            if electro == 9:
                print(f'''*****MENU DE MARCAS DE {str(electros[electro -1]).upper()}*******
                1)Miele
                2)Grundig
                3)Beko
                4)Cata
                5)Bosch
                *********''')
                marcas = int(input("Ingrese el numero de la marca de hornos de gas: "))
                if marcas == 1:
                    operacion = input("¿Quieres agregar o quitar productos del stock?")
                    if operacion == "sumar" or operacion == "Sumar":
                        Sstock()
                    elif operacion == "restar" or operacion == "Restar":
                        Rstock()
            if electro == 10:
                print(f'''*****MENU DE MARCAS DE {str(electros[electro -1]).upper()}*******
                1)LG
                2)Maytag
                3)Kenmore
                4)Electrolux
                5)Samsung
                *********''')
                marcas = int(input("Ingrese el numero de la marca de lavadoras: "))
                if marcas == 1:
                    operacion = input("¿Quieres agregar o quitar productos del stock?")
                    if operacion == "sumar" or operacion == "Sumar":
                        Sstock()
                    elif operacion == "restar" or operacion == "Restar":
                        Rstock()
                if marcas == 2:
                    operacion = input("¿Quieres agregar o quitar productos del stock?")
                    if operacion == "sumar" or operacion == "Sumar":
                        Sstock()
                    elif operacion == "restar" or operacion == "Restar":
                        Rstock()
                if marcas == 3:
                    operacion = input("¿Quieres agregar o quitar productos del stock?")
                    if operacion == "sumar" or operacion == "Sumar":
                        Sstock()
                    elif operacion == "restar" or operacion == "Restar":
                        Rstock()
                if marcas == 4:
                    operacion = input("¿Quieres agregar o quitar productos del stock?")
                    if operacion == "sumar" or operacion == "Sumar":
                        Sstock()
                    elif operacion == "restar" or operacion == "Restar":
                        Rstock()
                if marcas == 5:
                    operacion = input("¿Quieres agregar o quitar productos del stock?")
                    if operacion == "sumar" or operacion == "Sumar":
                        Sstock()
                    elif operacion == "restar" or operacion == "Restar":
                        Rstock()
        if option == 2:
           ventas() 


elif who == 2:
    contraseña = int(input("Ingrese la contraseña de Cliente: "))
    if contraseña == 54321:
        print("Bienvenido CLiente")
        opciones = ["Microondas", "Televisiones", "Bocinas", "Aspiradoras", "Cafeteras","Secadoras", "Refrigeradores", "Planchas", "Hornos", "Lavadoras"]
        print("""******MENÚ DE ELECTRODOMÉSTICOS*****
        1)Microondas
        2)Televisiones
        3)Bocinas
        4)Aspiradoras
        5)Cafeteras
        6)Secadoras  
        7)Refrigeradores
        8)Planchas de ropa
        9)Hornos de gas
        10)Lavadoras
        *******************************************""")

        opcion = int(input("Ingrese el numero del electrodomestico el cual quiere comprar: "))
        if opcion == 1:
            print(f'''*****MENU DE MARCAS DE {str(opciones[opcion -1]).upper()}*******
            1)Teka
            2)Whirlpool  
            3)Samsung
            4)Balay
            5)Bosch
            *********''')
            marca = int(input("Ingrese el numero de la marca de microondas: "))
            #Los precios estan ordenados de acuerdo al orden de aparicion de cada marca
            preciosmicro = [2000,2200,1900,2300,2100]
            if marca == 1:
                print(preciosmicro[0])
                Aprime = input("¿Cuenta con prime?: ")
                if Aprime == "Si" or Aprime == "si":
                    descuento()
                    prime()
            
                else:
                    descuento()
                    print("Y el precio de envio es de: ",pfenvio)
            
            elif marca == 2:
                print(preciosmicro[1])
                Aprime = input("¿Cuenta con prime?: ")
                if Aprime == "Si" or Aprime == "si":
                    descuento()
                    prime()
            
                else:
                    descuento()
                    print("Y el precio de envio es de: ",pfenvio)
            
            elif marca == 3:
                print(preciosmicro[2])
                Aprime = input("¿Cuenta con prime?: ")
                if Aprime == "Si" or Aprime == "si":
                    descuento()
                    prime()
            
                else:
                    descuento()
                    print("Y el precio de envio es de: ",pfenvio)
            
            elif marca == 4:
                print(preciosmicro[3])
                Aprime = input("¿Cuenta con prime?: ")
                if Aprime == "Si" or Aprime == "si":
                    descuento()
                    prime()
                else:
                    descuento()
                    print("Y el precio de envio es de: ",pfenvio)
            
            elif marca == 5:
                print(preciosmicro[4])
                Aprime = input("¿Cuenta con prime?: ")
                if Aprime == "Si" or Aprime == "si":
                    descuento()
                    prime()
            
                else:
                    descuento()
                    print("Y el precio de envio es de: ",pfenvio)
            
        elif opcion == 2:
            print(f'''*****MENU DE MARCAS DE {str(opciones[opcion -1]).upper()}*******
            1)LG
            2)Toshiba
            3)Samsung
            4)Sony
            5)Panasonic
            ******''')
            marca = int(input("Ingrese el numero de la marca de televisiones: "))
            #Los precios estan ordenados de acuerdo al orden de aparicion de cada marca
            preciostele = [8000,8500,9000,9500,10000]
            if marca == 1:
                print(preciostele[0])
                Aprime = input("¿Cuenta con prime?: ")
                if Aprime == "Si" or Aprime == "si":
                    descuento()
                    prime()
                else:
                    descuento()
                    print("Y el precio de envio es de: ",pfenvio)
            
            elif marca == 2:
                print(preciostele[1])
                Aprime = input("¿Cuenta con prime?: ")
                if Aprime == "Si" or Aprime == "si":
                    descuento()
                    prime()
            
                else:
                    descuento()
                    print("Y el precio de envio es de: ",pfenvio)
            
            elif marca == 3:
                print(preciostele[2])
                Aprime = input("¿Cuenta con prime?: ")
                if Aprime == "Si" or Aprime == "si":
                    descuento()
                    prime()
            
                else:
                    descuento()
                    print("Y el precio de envio es de: ",pfenvio)
            
            elif marca == 4:
                print(preciostele[3])
                Aprime = input("¿Cuenta con prime?: ")
                if Aprime == "Si" or Aprime == "si":
                    descuento()
                    prime()
            
                else:
                    descuento()
                    print("Y el precio de envio es de: ",pfenvio)
            
            elif marca == 5:
                print(preciostele[4])
                Aprime = input("¿Cuenta con prime?: ")
                if Aprime == "Si" or Aprime == "si":
                    descuento()
                    prime()
            
                else:
                    descuento()
                    print("Y el precio de envio es de: ",pfenvio)
            
    
    
        elif opcion == 3:
            print(f'''*****MENU DE MARCAS DE {str(opciones[opcion -1]).upper()}*******
            1)Sony
            2)Marshall
            3)Logitech
            4)KEF
            5)JBL
            ******''')
            marca = int(input("Ingrese el numero de la marca de bocinas: "))
            #Los precios estan ordenados de acuerdo al orden de aparicion de cada marca
            preciosboci = [1000,1300,1200,1350,1100]
            if marca == 1:
                print(preciosboci[0])
                Aprime = input("¿Cuenta con prime?: ")
                if Aprime == "Si" or Aprime == "si":
                    descuento()
                    prime()
        
                else:
                    descuento()
                    print("Y el precio de envio es de: ",pfenvio)
            
            elif marca == 2:
                print(preciosboci[1])
                Aprime = input("¿Cuenta con prime?: ")
                if Aprime == "Si" or Aprime == "si":
                    descuento()
                    prime()
            
                else:
                    descuento()
                    print("Y el precio de envio es de: ",pfenvio)
            
            elif marca == 3:
                print(preciosboci[2])
                Aprime = input("¿Cuenta con prime?: ")
                if Aprime == "Si" or Aprime == "si":
                    descuento()
                    prime()
            
                else:
                    descuento()
                    print("Y el precio de envio es de: ",pfenvio)
            
            elif marca == 4:
                print(preciosboci[3])
                Aprime = input("¿Cuenta con prime?: ")
                if Aprime == "Si" or Aprime == "si":
                    descuento()
                    prime()
            
                else:
                    descuento()
                    print("Y el precio de envio es de: ",pfenvio)
            
            elif marca == 5:
                print(preciosboci[4])
                Aprime = input("¿Cuenta con prime?: ")
                if Aprime == "Si" or Aprime == "si":
                    descuento()
                    prime()
            
                else:
                    descuento()
                    print("Y el precio de envio es de: ",pfenvio)
            

    
        elif opcion == 4:
            print(f'''*****MENU DE MARCAS DE {str(opciones[opcion -1]).upper()}*******
            1)Philips
            2)Shark
            3)Bosch
            4)Robot
            5)Dyson
            ******''') 
            marca = int(input("Ingrese el numero de la marca de aspiradoras: "))
            #Los precios estan ordenados de acuerdo al orden de aparicion de cada marca
            preciosaspi = [700,650,500,550,750]
            if marca == 1:
                print(preciosaspi[0])
                Aprime = input("¿Cuenta con prime?: ")
                if Aprime == "Si" or Aprime == "si":
                    descuento()
                    prime()
            
                else:
                    descuento()
                    print("Y el precio de envio es de: ",pfenvio)
            
            elif marca == 2:
                print(preciosaspi[1])
                Aprime = input("¿Cuenta con prime?: ")
                if Aprime == "Si" or Aprime == "si":
                    descuento()
                    prime()
            
                else:
                    descuento()
                    print("Y el precio de envio es de: ",pfenvio)
            
            elif marca == 3:
                print(preciosaspi[2])
                Aprime = input("¿Cuenta con prime?: ")
                if Aprime == "Si" or Aprime == "si":
                    descuento()
                    prime()
            
                else:
                    descuento()
                    print("Y el precio de envio es de: ",pfenvio)
            
            elif marca == 4:
                print(preciosaspi[3])
                Aprime = input("¿Cuenta con prime?: ")
                if Aprime == "Si" or Aprime == "si":
                    descuento()
                    prime()
            
                else:
                    descuento()
                    print("Y el precio de envio es de: ",pfenvio)
            
            elif marca == 5:
                print(preciosaspi[4])
                Aprime = input("¿Cuenta con prime?: ")
                if Aprime == "Si" or Aprime == "si":
                    descuento()
                    prime()
            
                else:
                    descuento()
                    print("Y el precio de envio es de: ",pfenvio)
            
    
    
        elif opcion == 5:
            print(f'''*****MENU DE MARCAS DE {str(opciones[opcion -1]).upper()}*******
            1)Dolce Gusto
            2)Oster
            3)Nespresso
            4)Hamilton Beach
            5)Krups
            ******''')
            marca = int(input("Ingrese el numero de la marca de cafeteras: "))
            #Los precios estan ordenados de acuerdo al orden de aparicion de cada marca
            precioscafe = [1000,800,900,850,950]
            if marca == 1:
                print(precioscafe[0])
                Aprime = input("¿Cuenta con prime?: ")
                if Aprime == "Si" or Aprime == "si":
                    descuento()
                    prime()
            
                else:
                    descuento()
                    print("Y el precio de envio es de: ",pfenvio)
            
            elif marca == 2:
                print(precioscafe[1])
                Aprime = input("¿Cuenta con prime?: ")
                if Aprime == "Si" or Aprime == "si":
                    descuento()
                    prime()
            
                else:
                    descuento()
                    print("Y el precio de envio es de: ",pfenvio)
            
            elif marca == 3:
                print(precioscafe[2])
                Aprime = input("¿Cuenta con prime?: ")
                if Aprime == "Si" or Aprime == "si":
                    descuento()
                    prime()
            
                else:
                    descuento()
                    print("Y el precio de envio es de: ",pfenvio)
            
            elif marca == 4:
                print(precioscafe[3])
                Aprime = input("¿Cuenta con prime?: ")
                if Aprime == "Si" or Aprime == "si":
                    descuento()
                    prime()
            
                else:
                    descuento()
                    print("Y el precio de envio es de: ",pfenvio)
            
            elif marca == 5:
                print(precioscafe[4])
                Aprime = input("¿Cuenta con prime?: ")
                if Aprime == "Si" or Aprime == "si":
                    descuento()
                    prime()
            
                else:
                    descuento()
                    print("Y el precio de envio es de: ",pfenvio)
            
    
        elif opcion == 6:
            print(f'''*****MENU DE MARCAS DE {str(opciones[opcion -1]).upper()}*******
            1)LG
            2)Whirlpool
            3)Maytang
            4)Kenmore
            5)Speed Queen
            ******''')
            marca = int(input("Ingrese el numero de la marca de secadoras: "))
            #Los precios estan ordenados de acuerdo al orden de aparicion de cada marca
            preciosseca = [7900,8000,8200,7500,8500]
            if marca == 1:
                print(preciosseca[0])
                Aprime = input("¿Cuenta con prime?: ")
                if Aprime == "Si" or Aprime == "si":
                    descuento()
                    prime()
            
                else:
                    descuento()
                    print("Y el precio de envio es de: ",pfenvio)
            
            elif marca == 2:
                print(preciosseca[1])
                Aprime = input("¿Cuenta con prime?: ")
                if Aprime == "Si" or Aprime == "si":
                    descuento()
                    prime()
            
                else:
                    descuento()
                    print("Y el precio de envio es de: ",pfenvio)
            
            elif marca == 3:
                print(preciosseca[2])
                Aprime = input("¿Cuenta con prime?: ")
                if Aprime == "Si" or Aprime == "si":
                    descuento()
                    prime()
            
                else:
                    descuento()
                    print("Y el precio de envio es de: ",pfenvio)
            
            elif marca == 4:
                print(preciosseca[3])
                Aprime = input("¿Cuenta con prime?: ")
                if Aprime == "Si" or Aprime == "si":
                    descuento()
                    prime()
            
                else:
                    descuento()
                    print("Y el precio de envio es de: ",pfenvio)
            
            elif marca == 5:
                print(preciosseca[4])
                Aprime = input("¿Cuenta con prime?: ")
                if Aprime == "Si" or Aprime == "si":
                    descuento()
                    prime()
            
                else:
                    descuento()
                    print("Y el precio de envio es de: ",pfenvio)
            
   
    
        elif opcion == 7:
            print(f'''*****MENU DE MARCAS DE {str(opciones[opcion -1]).upper()}*******
            1)Mabe
            2)Whirlpool
            3)Daewoo
            4)Frigidaire
            5)Samsung
            ******''')
            marca = int(input("Ingrese el numero de la marca de refrigeradores: "))
            #Los precios estan ordenados de acuerdo al orden de aparicion de cada marca
            preciosrefri=[12000,11500,12800,11900,11200]
            if marca == 1:
                print(preciosrefri[0])
                Aprime = input("¿Cuenta con prime?: ")
                if Aprime == "Si" or Aprime == "si":
                    descuento()
                    prime()
            
                else:
                    descuento()
                    print("Y el precio de envio es de: ",pfenvio)
            
            elif marca == 2:
                print(preciosrefri[1])
                Aprime = input("¿Cuenta con prime?: ")
                if Aprime == "Si" or Aprime == "si":
                    descuento()
                    prime()
            
                else:
                    descuento()
                    print("Y el precio de envio es de: ",pfenvio)
            
            elif marca == 3:
                print(preciosrefri[2])
                Aprime = input("¿Cuenta con prime?: ")
                if Aprime == "Si" or Aprime == "si":
                    descuento()
                    prime()
            
                else:
                    descuento()
                    print("Y el precio de envio es de: ",pfenvio)
            
            elif marca == 4:
                print(preciosrefri[3])
                Aprime = input("¿Cuenta con prime?: ")
                if Aprime == "Si" or Aprime == "si":
                    descuento()
                    prime()
            
                else:
                    descuento()
                    print("Y el precio de envio es de: ",pfenvio)
            
            elif marca == 5:
                print(preciosrefri[4])
                Aprime = input("¿Cuenta con prime?: ")
                if Aprime == "Si" or Aprime == "si":
                    descuento()
                    prime()
            
                else:
                    descuento()
                    print("Y el precio de envio es de: ",pfenvio)
            
    
        elif opcion == 8:
            print(f'''*****MENU DE MARCAS DE {str(opciones[opcion -1]).upper()}*******
            1)Aigostar
            2)Philips
            3)Ufesa
            4)Rowenta  
            5)Dcenta
            ******''')
            marca = int(input("Ingrese el numero de la marca de planchas de ropa: "))
            #Los precios estan ordenados de acuerdo al orden de aparicion de cada marca
            preciospropa = [500,390,400,450,550]
            if marca == 1:
                print(preciospropa[0])
                Aprime = input("¿Cuenta con prime?: ")
                if Aprime == "Si" or Aprime == "si":
                    descuento()
                    prime()
            
                else:
                    descuento()
                    print("Y el precio de envio es de: ",pfenvio)
            
            elif marca == 2:
                print(preciospropa[1])
                Aprime = input("¿Cuenta con prime?: ")
                if Aprime == "Si" or Aprime == "si":
                    descuento()
                    prime()
            
                else:
                    descuento()
                    print("Y el precio de envio es de: ",pfenvio)
            
            elif marca == 3:
                print(preciospropa[2])
                Aprime = input("¿Cuenta con prime?: ")
                if Aprime == "Si" or Aprime == "si":
                    descuento()
                    prime()
            
                else:
                    descuento()
                    print("Y el precio de envio es de: ",pfenvio)
            
            elif marca == 4:
                print(preciospropa[3])
                Aprime = input("¿Cuenta con prime?: ")
                if Aprime == "Si" or Aprime == "si":
                    descuento()
                    prime()
            
                else:
                    descuento()
                    print("Y el precio de envio es de: ",pfenvio)
            
            elif marca == 5:
                print(preciospropa[4])
                Aprime = input("¿Cuenta con prime?: ")
                if Aprime == "Si" or Aprime == "si":
                    descuento()
                    prime()
           
                else:
                    descuento()
                    print("Y el precio de envio es de: ",pfenvio)
            
    
        elif opcion == 9:
            print(f'''*****MENU DE MARCAS DE {str(opciones[opcion -1]).upper()}*******
            1)Miele
            2)Grundig
            3)Beko
            4)Cata
            5)Bosch
            ******''')
            marca = int(input("Ingrese el numero de la marca de hornos de gas: "))
            #Los precios estan ordenados de acuerdo al orden de aparicion de cada marca
            precioshorno = [11900,12200,13000,11500,12700]
            if marca == 1:
                print(precioshorno[0])
                Aprime = input("¿Cuenta con prime?: ")
                if Aprime == "Si" or Aprime == "si":
                    descuento()
                    prime()
            
                else:
                    descuento()
                    print("Y el precio de envio es de: ",pfenvio)
            
            elif marca == 2:
                print(precioshorno[1])
                Aprime = input("¿Cuenta con prime?: ")
                if Aprime == "Si" or Aprime == "si":
                    descuento()
                    prime()
            
                else:
                    descuento()
                    print("Y el precio de envio es de: ",pfenvio)
            
            elif marca == 3:
                print(precioshorno[2])
                Aprime = input("¿Cuenta con prime?: ")
                if Aprime == "Si" or Aprime == "si":
                    descuento()
                    prime()
            
                else:
                    descuento()
                    print("Y el precio de envio es de: ",pfenvio)
            
            elif marca == 4:
                print(precioshorno[3])
                Aprime = input("¿Cuenta con prime?: ")
                if Aprime == "Si" or Aprime == "si":
                    descuento()
                    prime()
            
                else:
                    descuento()
                    print("Y el precio de envio es de: ",pfenvio)
            
            elif marca == 5:
                print(precioshorno[4])
                Aprime = input("¿Cuenta con prime?: ")
                if Aprime == "Si" or Aprime == "si":
                    descuento()
                    prime()
            
                else:
                    descuento()
                    print("Y el precio de envio es de: ",pfenvio)
            
   
    
        elif opcion == 10:
            print(f'''*****MENU DE MARCAS DE {str(opciones[opcion -1]).upper()}*******
            1)LG
            2)Maytag
            3)Kenmore
            4)Electrolux
            5)Samsung
            ******''')
            marca = int(input("Ingrese el numero de la marca de lavadoras: "))
            #Los precios estan ordenados de acuerdo al orden de aparicion de cada marca
            precioslava = [7000,6900,7300,7500,6700]
            if marca == 1:
                print(precioslava[0])
                Aprime = input("¿Cuenta con prime?: ")
                if Aprime == "Si" or Aprime == "si":
                    descuento()
                    prime()
            
                else:
                    descuento()
                    print("Y el precio de envio es de: ",pfenvio)
            
            elif marca == 2:
                print(precioslava[1])
                Aprime = input("¿Cuenta con prime?: ")
                if Aprime == "Si" or Aprime == "si":
                    descuento()
                    prime()
            
                else:
                    descuento()
                    print("Y el precio de envio es de: ",pfenvio)
            
            elif marca == 3:
                print(precioslava[2])
                Aprime = input("¿Cuenta con prime?: ")
                if Aprime == "Si" or Aprime == "si":
                    descuento()
                    prime()
           
                else:
                    descuento()
                    print("Y el precio de envio es de: ",pfenvio)
            
            elif marca == 4:
                print(precioslava[3])
                Aprime = input("¿Cuenta con prime?: ")
                if Aprime == "Si" or Aprime == "si":
                    descuento()
                    prime()
            
                else:
                    descuento()
                    print("Y el precio de envio es de: ",pfenvio)
            
            elif marca == 5:
                print(precioslava[4])
                Aprime = input("¿Cuenta con prime?: ")
                if Aprime == "Si" or Aprime == "si":
                    descuento()
                    prime()
            
                else:
                    descuento()
                    print("Y el precio de envio es de: ",pfenvio)
            