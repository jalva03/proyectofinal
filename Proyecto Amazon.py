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
def op():
    listaop = ["Microondas", "Televisiones", "Bocinas", "Aspiradoras", "Cafeteras", "Secadoras","Refrigeradores","Planchas","Hornos","Lavadoras"]
    print(listaop)
    producto = input("¿Que quieres comprar?: ")
    if producto == listaop[0]:
        listamarca1 = ["Teka" , "Whirlpool" , "Samsung" , "Balay" , "Bosch"]
        preciosmarca1 = [[2000,2200,1900,2300,2100]]
        print(listamarca1)
        productom = input("¿De que marca quieres tu producto?: ")
        if productom == listamarca1[0]:
            print(preciosmarca1[0])
        elif productom == listamarca1[1]:
            print(preciosmarca1[1])
        elif productom == listamarca1[2]:
            print(preciosmarca1[2])
        elif productom == listamarca1[3]:
            print(preciosmarca1[3])
        elif productom == listamarca1[4]:
            print(preciosmarca1[4])
    elif producto == listaop[1]:
        listamarca2 = ["LG", "Toshiba", "Samsung", "Sony", "Panasonic"]
        preciosmarca2 = [8000,8500,9000,9500,10000]
        print(listamarca2)
        productom = input("¿De que marca quieres tu producto?: ")
        if productom == listamarca2[0]:
            print(preciosmarca2[0])
        elif productom == listamarca2[1]:
            print(preciosmarca2[1])
        elif productom == listamarca2[2]:
            print(preciosmarca2[2])
        elif productom == listamarca2[3]:
            print(preciosmarca2[3])
        elif productom == listamarca2[4]:
            print(preciosmarca2[4])
    elif producto == listaop[2]:
        listamarca3 = ["Sony","Marsha", "Logitech", "KEF", "JBL"]
        preciosmarca3 = [1000,1300,1200,1350,1100]
        print(listamarca3)
        productom = input("¿De que marca quieres tu producto?: ")
        if productom == listamarca3[0]:
            print(preciosmarca3[0])
        elif productom == listamarca3[1]:
            print(preciosmarca3[1])
        elif productom == listamarca3[2]:
            print(preciosmarca3[2])
        elif productom == listamarca3[3]:
            print(preciosmarca3[3])
        elif productom == listamarca3[4]:
            print(preciosmarca3[4])
    elif producto == listaop[3]:
        listamarca4 = ["Philips","Shark","Bosch","Robot","Dyson"]
        preciosmarca4 = [700,650,500,550,750]
        print(listamarca4)
        productom = input("¿De que marca quieres tu producto?: ")
        if productom == listamarca4[0]:
            print(preciosmarca4[0])
        elif productom == listamarca4[1]:
            print(preciosmarca4[1])
        elif productom == listamarca4[2]:
            print(preciosmarca4[2])
        elif productom == listamarca4[3]:
            print(preciosmarca4[3])
        elif productom == listamarca4[4]:
            print(preciosmarca4[4])
    elif producto == listaop[4]:
        listamarca5 = ["Dolce Gusto", "Oster"," Nespresso", "Hamilton Beach", "Krups"]
        preciosmarca5 = [1000,800,900,850,950]
        print(listamarca5)
        productom = input("¿De que marca quieres tu producto?: ")
        if productom == listamarca5[0]:
            print(preciosmarca5[0])
        elif productom == listamarca5[1]:
            print(preciosmarca5[1])
        elif productom == listamarca5[2]:
            print(preciosmarca5[2])
        elif productom == listamarca5[3]:
            print(preciosmarca5[3])
        elif productom == listamarca5[4]:
            print(preciosmarca5[4])
    elif producto == listaop[5]:
        listamarca6 = ["LG", "Whirlpool" ,"Maytang", "Kenmore", "Speed Queen"]
        preciosmarca6 = [7900,8000,8200,7500,8500]
        print(listamarca6)
        productom = input("¿De que marca quieres tu producto?: ")
        if productom == listamarca6[0]:
            print(preciosmarca6[0])
        elif productom == listamarca6[1]:
            print(preciosmarca6[1])
        elif productom == listamarca6[2]:
            print(preciosmarca6[2])
        elif productom == listamarca6[3]:
            print(preciosmarca6[3])
        elif productom == listamarca6[4]:
            print(preciosmarca6[4])
    elif producto == listaop[6]:
        listamarca7 = ["Mabe", "Whirlpool", "Daewoo", "Frigidaire", "Samsung"]
        preciosmarca7 = [12000,11500,12800,11900,11200]
        print(listamarca7)
        productom = input("¿De que marca quieres tu producto?: ")
        if productom == listamarca7[0]:
            print(preciosmarca7[0])
        elif productom == listamarca7[1]:
            print(preciosmarca7[1])
        elif productom == listamarca7[2]:
            print(preciosmarca7[2])
        elif productom == listamarca7[3]:
            print(preciosmarca7[3])
        elif productom == listamarca7[4]:
            print(preciosmarca7[4])
    elif producto == listaop[7]:
        listamarca8 = ["Aigostar", "Philips", "Ufesa", "Rowenta", "Dcenta"]
        preciosmarca8 = [500,390,400,450,550]
        print(listamarca8)
        productom = input("¿De que marca quieres tu producto?: ")
        if productom == listamarca8[0]:
            print(preciosmarca8[0])
        elif productom == listamarca8[1]:
            print(preciosmarca8[1])
        elif productom == listamarca8[2]:
            print(preciosmarca8[2])
        elif productom == listamarca8[3]:
            print(preciosmarca8[3])
        elif productom == listamarca8[4]:
            print(preciosmarca8[4])
    elif producto == listaop[8]:
        listamarca9 = ["Miele", "Grundig", "Beko", "Cata", "Bosch"]
        preciosmarca9 = [11900,12200,13000,11500,12700]
        print(listamarca9)
        productom = input("¿De que marca quieres tu producto?: ")
        if productom == listamarca9[0]:
            print(preciosmarca9[0])
        elif productom == listamarca9[1]:
            print(preciosmarca9[1])
        elif productom == listamarca9[2]:
            print(preciosmarca9[2])
        elif productom == listamarca9[3]:
            print(preciosmarca9[3])
        elif productom == listamarca9[4]:
            print(preciosmarca9[4])
    elif producto == listaop[9]:
        listamarca10 = ["LG", "Maytag", "Kenmore", "Electrolux", "Samsung"]
        preciosmarca10 = [7000,6900,7300,7500,6700]
        print(listamarca10)
        productom = input("¿De que marca quieres tu producto?: ")
        if productom == listamarca10[0]:
            print(preciosmarca10[0])
        elif productom == listamarca10[1]:
            print(preciosmarca10[1])
        elif productom == listamarca10[2]:
            print(preciosmarca10[2])
        elif productom == listamarca10[3]:
            print(preciosmarca10[3])
        elif productom == listamarca10[4]:
            print(preciosmarca10[4])
    
    
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
        3)Agregar marca de un producto 
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
                    operacion = input("¿Quieres agregar o quitar productos del stock?: ")
                    if operacion == "agregar" or operacion == "Agregar":
                        Sstock()
                    elif operacion == "quitar" or operacion == "Quitar":
                        Rstock()
                if marcas == 2:
                    operacion = input("¿Quieres agregar o quitar productos del stock?: ")
                    if operacion == "agregar" or operacion == "Agregar":
                        Sstock()
                    elif operacion == "Quitar" or operacion == "quitar":
                        Rstock()
                if marcas == 3:
                    operacion = input("¿Quieres agregar o quitar productos del stock?: ")
                    if operacion == "agregar" or operacion == "Agregar":
                        Sstock()
                    elif operacion == "Quitar" or operacion == "quitar":
                        Rstock()
                if marcas == 4:
                    operacion = input("¿Quieres agregar o quitar productos del stock?: ")
                    if operacion == "Agregar" or operacion == "agregar":
                        Sstock()
                    elif operacion == "quitar" or operacion == "Quitar":
                        Rstock()
                if marcas == 5:
                    operacion = input("¿Quieres agregar o quitar productos del stock?: ")
                    if operacion == "agregar" or operacion == "Agregar":
                        Sstock()
                    elif operacion == "quitar" or operacion == "Quitar":
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
                    if operacion == "agregar" or operacion == "Agregar":
                        Sstock()
                    elif operacion == "Quitar" or operacion == "quitar":
                        Rstock()
                if marcas == 2:
                    operacion = input("¿Quieres agregar o quitar productos del stock?")
                    if operacion == "agregar" or operacion == "Agregar":
                        Sstock()
                    elif operacion == "Quitar" or operacion == "quitar":
                        Rstock()
                if marcas == 3:
                    operacion = input("¿Quieres agregar o quitar productos del stock?")
                    if operacion == "agregar" or operacion == "Agregar":
                        Sstock()
                    elif operacion == "Quitar" or operacion == "quitar":
                        Rstock()
                if marcas == 4:
                    operacion = input("¿Quieres agregar o quitar productos del stock?")
                    if operacion == "agregar" or operacion == "Agregar":
                        Sstock()
                    elif operacion == "quitar" or operacion == "Quitar":
                        Rstock()
                if marcas == 5:
                    operacion = input("¿Quieres agregar o quitar productos del stock?")
                    if operacion == "Agregar" or operacion == "agregar":
                        Sstock()
                    elif operacion == "quitar" or operacion == "Quitar":
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
                    if operacion == "agregar" or operacion == "Agregar":
                        Sstock()
                    elif operacion == "quitar" or operacion == "Quitar":
                        Rstock()
                if marcas == 2:
                    operacion = input("¿Quieres agregar o quitar productos del stock?")
                    if operacion == "Agregar" or operacion == "agregar":
                        Sstock()
                    elif operacion == "quitar" or operacion == "Quitar":
                        Rstock()
                if marcas == 3:
                    operacion = input("¿Quieres agregar o quitar productos del stock?")
                    if operacion == "agregar" or operacion == "Agregar":
                        Sstock()
                    elif operacion == "quitar" or operacion == "Quitar":
                        Rstock()
                if marcas == 4:
                    operacion = input("¿Quieres agregar o quitar productos del stock?")
                    if operacion == "Agregar" or operacion == "agregar":
                        Sstock()
                    elif operacion == "quitar" or operacion == "Quitar":
                        Rstock()
                if marcas == 5:
                    operacion = input("¿Quieres agregar o quitar productos del stock?")
                    if operacion == "Agregar" or operacion == "agregar":
                        Sstock()
                    elif operacion == "quitar" or operacion == "Quitar":
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
                    if operacion == "agregar" or operacion == "Agregar":
                        Sstock()
                    elif operacion == "quitar" or operacion == "Quitar":
                        Rstock()
                if marcas == 2:
                    operacion = input("¿Quieres agregar o quitar productos del stock?")
                    if operacion == "Agregar" or operacion == "agregar":
                        Sstock()
                    elif operacion == "quitar" or operacion == "Quitar":
                        Rstock()
                if marcas == 3:
                    operacion = input("¿Quieres agregar o quitar productos del stock?")
                    if operacion == "Agregar" or operacion == "agregar":
                        Sstock()
                    elif operacion == "quitar" or operacion == "Quitar":
                        Rstock()
                if marcas == 4:
                    operacion = input("¿Quieres agregar o quitar productos del stock?")
                    if operacion == "Agregar" or operacion == "agregar":
                        Sstock()
                    elif operacion == "quitar" or operacion == "Quitar":
                        Rstock()
                if marcas == 5:
                    operacion = input("¿Quieres agregar o quitar productos del stock?")
                    if operacion == "Agregar" or operacion == "agregar":
                        Sstock()
                    elif operacion == "quitar" or operacion == "Quitar":
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
                    if operacion == "Agregar" or operacion == "agregar":
                        Sstock()
                    elif operacion == "Quitar" or operacion == "quitar":
                        Rstock()
                if marcas == 2:
                    operacion = input("¿Quieres agregar o quitar productos del stock?")
                    if operacion == "agregar" or operacion == "Agregar":
                        Sstock()
                    elif operacion == "quitar" or operacion == "Quitar":
                        Rstock()
                if marcas == 3:
                    operacion = input("¿Quieres agregar o quitar productos del stock?")
                    if operacion == "agregar" or operacion == "Agregar":
                        Sstock()
                    elif operacion == "quitar" or operacion == "Quitar":
                        Rstock()
                if marcas == 4:
                    operacion = input("¿Quieres agregar o quitar productos del stock?")
                    if operacion == "agregar" or operacion == "Agregar":
                        Sstock()
                    elif operacion == "quitar" or operacion == "Quitar":
                        Rstock()
                if marcas == 5:
                    operacion = input("¿Quieres agregar o quitar productos del stock?")
                    if operacion == "Agregar" or operacion == "agregar":
                        Sstock()
                    elif operacion == "quitar" or operacion == "Quitar":
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
                    if operacion == "agregar" or operacion == "Agregar":
                        Sstock()
                    elif operacion == "quitar" or operacion == "Quitar":
                        Rstock()
                if marcas == 2:
                    operacion = input("¿Quieres agregar o quitar productos del stock?")
                    if operacion == "agregar" or operacion == "Agregar":
                        Sstock()
                    elif operacion == "quitar" or operacion == "Quitar":
                        Rstock()
                if marcas == 3:
                    operacion = input("¿Quieres agregar o quitar productos del stock?")
                    if operacion == "agregar" or operacion == "Agregar":
                        Sstock()
                    elif operacion == "quitar" or operacion == "Quitar":
                        Rstock()
                if marcas == 4:
                    operacion = input("¿Quieres agregar o quitar productos del stock?")
                    if operacion == "agregar" or operacion == "Agregar":
                        Sstock()
                    elif operacion == "quitar" or operacion == "Quitar":
                        Rstock()
                if marcas == 5:
                    operacion = input("¿Quieres agregar o quitar productos del stock?")
                    if operacion == "agregar" or operacion == "Agregar":
                        Sstock()
                    elif operacion == "quitar" or operacion == "Quitar":
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
                    if operacion == "Agregar" or operacion == "agregar":
                        Sstock()
                    elif operacion == "quitar" or operacion == "Quitar":
                        Rstock()
                if marcas == 2:
                    operacion = input("¿Quieres agregar o quitar productos del stock?")
                    if operacion == "agregar" or operacion == "Agregar":
                        Sstock()
                    elif operacion == "quitar" or operacion == "Quitar":
                        Rstock()
                if marcas == 3:
                    operacion = input("¿Quieres agregar o quitar productos del stock?")
                    if operacion == "Agregar" or operacion == "agregar":
                        Sstock()
                    elif operacion == "quitar" or operacion == "Quitar":
                        Rstock()
                if marcas == 4:
                    operacion = input("¿Quieres agregar o quitar productos del stock?")
                    if operacion == "agregar" or operacion == "Agregar":
                        Sstock()
                    elif operacion == "quitar" or operacion == "Quitar":
                        Rstock()
                if marcas == 5:
                    operacion = input("¿Quieres agregar o quitar productos del stock?")
                    if operacion == "agregar" or operacion == "Agregar":
                        Sstock()
                    elif operacion == "quitar" or operacion == "Quitar":
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
                    if operacion == "agregar" or operacion == "Agregar":
                        Sstock()
                    elif operacion == "quitar" or operacion == "Quitar":
                        Rstock()
                if marcas == 2:
                    operacion = input("¿Quieres agregar o quitar productos del stock?")
                    if operacion == "Agregar" or operacion == "agregar":
                        Sstock()
                    elif operacion == "quitar" or operacion == "Quitar":
                        Rstock()
                if marcas == 3:
                    operacion = input("¿Quieres agregar o quitar productos del stock?")
                    if operacion == "agregar" or operacion == "Agregar":
                        Sstock()
                    elif operacion == "quitar" or operacion == "Quitar":
                        Rstock()
                if marcas == 4:
                    operacion = input("¿Quieres agregar o quitar productos del stock?")
                    if operacion == "agregar" or operacion == "Agregar":
                        Sstock()
                    elif operacion == "quitar" or operacion == "Quitar":
                        Rstock()
                if marcas == 5:
                    operacion = input("¿Quieres agregar o quitar productos del stock?")
                    if operacion == "agregar" or operacion == "Agregar":
                        Sstock()
                    elif operacion == "quitar" or operacion == "Quitar":
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
                    if operacion == "Agregar" or operacion == "agregar":
                        Sstock()
                    elif operacion == "quitar" or operacion == "Quitar":
                        Rstock()
                if marcas == 2:
                    operacion = input("¿Quieres agregar o quitar productos del stock?")
                    if operacion == "Agregar" or operacion == "agregar":
                        Sstock()
                    elif operacion == "quitar" or operacion == "Quitar":
                        Rstock()
                if marcas == 3:
                    operacion = input("¿Quieres agregar o quitar productos del stock?")
                    if operacion == "Agregar" or operacion == "agregar":
                        Sstock()
                    elif operacion == "quitar" or operacion == "Quitar":
                        Rstock()
                if marcas == 4:
                    operacion = input("¿Quieres agregar o quitar productos del stock?")
                    if operacion == "Agregar" or operacion == "agregar":
                        Sstock()
                    elif operacion == "quitar" or operacion == "Quitar":
                        Rstock()
                if marcas == 5:
                    operacion = input("¿Quieres agregar o quitar productos del stock?")
                    if operacion == "Agregar" or operacion == "agregar":
                        Sstock()
                    elif operacion == "quitar" or operacion == "Quitar":
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
                    if operacion == "agregar" or operacion == "Agregar":
                        Sstock()
                    elif operacion == "quitar" or operacion == "Quitar":
                        Rstock()
                if marcas == 2:
                    operacion = input("¿Quieres agregar o quitar productos del stock?")
                    if operacion == "agregar" or operacion == "Agregar":
                        Sstock()
                    elif operacion == "quitar" or operacion == "Quitar":
                        Rstock()
                if marcas == 3:
                    operacion = input("¿Quieres agregar o quitar productos del stock?")
                    if operacion == "agregar" or operacion == "Agregar":
                        Sstock()
                    elif operacion == "quitar" or operacion == "Quitar":
                        Rstock()
                if marcas == 4:
                    operacion = input("¿Quieres agregar o quitar productos del stock?")
                    if operacion == "Agregar" or operacion == "agregar":
                        Sstock()
                    elif operacion == "quitar" or operacion == "Quitar":
                        Rstock()
                if marcas == 5:
                    operacion = input("¿Quieres agregar o quitar productos del stock?")
                    if operacion == "Agregar" or operacion == "Agregar":
                        Sstock()
                    elif operacion == "quitar" or operacion == "Quitar":
                        Rstock()
        if option == 2:
           ventas() 
        if option == 3:
            ejemplos = ["Microondas", "Televisiones", "Bocinas", "Aspiradoras", "Cafeteras","Secadoras", "Refrigeradores", "Planchas", "Hornos", "Lavadoras"]
            print("""*****MENÚ DE ELECTRODOMESTICOS*****
                  Selecciona el electrodomestico al cual quieres agregar una marca
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
                    *******************************""")
            electrodo = int(input("Ingrese el numero del electrodomestico el del cual quiere agregar una marca: "))
            if electrodo == 1:
                listam = ["Teka" , "Whirlpool" , "Samsung" , "Balay" , "Bosch"]
                listam.append(input("Ingrese la nueva marca: "))
                listamprecios = [2000,2200,1900,2300,2100]
                listamprecios.append(int(input("Ingrese el precio del objeto: ")))
                print(listam)
                print(listamprecios)
            if electrodo == 2:
                listat = ["LG", "Toshiba", "Samsung", "Sony", "Panasonic"]
                listatprecios = [8000,8500,9000,9500,10000]
                listat.append = input("Ingrese la nueva marca: ")
                listatprecios.append = int(input("Ingrese el precio del objeto: "))
                print(listat)
                print(listatprecios)
            if electrodo == 3:
                listab = ["Sony","Marsha", "Logitech", "KEF", "JBL"]
                listab.append(input("Ingrese la nueva marca: "))
                listabprecios =  [1000,1300,1200,1350,1100]
                listabprecios.append(int(input("Ingrese el precio del objeto: ")))
                print(listab)
                print(listabprecios)
            if electrodo == 4:
                listaA = ["Philips","Shark","Bosch","Robot","Dyson"]
                listaA.append(input("Ingrese la nueva marca: "))
                listaAprecios = [700,650,500,550,750]
                listaAprecios.append(int(input("Ingrese el precio del objeto: ")))
                print(listaA)
                print(listaAprecios)
            if electrodo == 5:
                listac = ["Dolce Gusto", "Oster"," Nespresso", "Hamilton Beach", "Krups"]
                listac.append(input("Ingrese la nueva marca: "))
                listacprecios = [1000,800,900,850,950] 
                listacprecios.append(int(input("Ingrese el precio del objeto: ")))
                print(listac)
                print(listacprecios)
            if electrodo == 6:
                listas =  ["LG", "Whirlpool" ,"Maytang", "Kenmore", "Speed Queen"]
                listas.append(input("Ingrese la nueva marca: "))
                listasprecios = [7900,8000,8200,7500,8500]
                listasprecios.append(int(input("Ingrese el precio del objeto: ")))
                print(listas)
                print(listasprecios)
            if electrodo == 7:
                listar = ["Mabe", "Whirlpool", "Daewoo", "Frigidaire", "Samsung"]
                listar.append(input("Ingrese la nueva marca: "))
                listarprecios = [12000,11500,12800,11900,11200]
                listarprecios.append(int(input("Ingrese el precio del objeto: ")))
                print(listar)
                print(listarprecios)
            if electrodo == 8:
                listaP = ["Aigostar", "Philips", "Ufesa", "Rowenta", "Dcenta"]
                listaP.append(input("Ingrese la nueva marca: "))
                listaPprecios = [500,390,400,450,550]
                listaPprecios.append(int(input("Ingrese el precio del objeto: ")))
                print(listaP)
                print(listaPprecios)
            if electrodo == 9:
                listah = ["Miele", "Grundig", "Beko", "Cata", "Bosch"]
                listah.append(input("Ingrese la nueva marca: "))
                listahprecios = [11900,12200,13000,11500,12700]
                listahprecios.append(int(input("Ingrese el precio del objeto: ")))
                print(listah)
                print(listahprecios)
            if electrodo == 10:
                listaL = ["LG", "Maytag", "Kenmore", "Electrolux", "Samsung"]
                listaL.append(input("Ingrese la nueva marca: "))
                listaLprecios = [7000,6900,7300,7500,6700]
                listaLprecios.append(int(input("Ingrese el precio del objeto: ")))
                print(listaL)
                print(listaLprecios)
                
                
                
                
                
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
                    respuesta = input("¿Quieres seguir comprando?: ")
                    if respuesta == "si" or respuesta == "Si":
                      op()
                            
                    elif respuesta == "no" or respuesta == "No":
                        print("Gracias por tu compra")
                        
            
                else:
                    descuento()
                    print("Y el precio de envio es de: ",pfenvio)
                    respuesta = input("¿Quieres seguir comprando?: ")
                    if respuesta == "si" or respuesta == "Si":
                      op()
                            
                    elif respuesta == "no" or respuesta == "No":
                        print("Gracias por tu compra")
            
            elif marca == 2:
                print(preciosmicro[1])
                Aprime = input("¿Cuenta con prime?: ")
                if Aprime == "Si" or Aprime == "si":
                    descuento()
                    prime()
                    respuesta = input("¿Quieres seguir comprando?: ")
                    if respuesta == "si" or respuesta == "Si":
                      op()
                            
                    elif respuesta == "no" or respuesta == "No":
                        print("Gracias por tu compra")
            
                else:
                    descuento()
                    print("Y el precio de envio es de: ",pfenvio)
                    respuesta = input("¿Quieres seguir comprando?: ")
                    if respuesta == "si" or respuesta == "Si":
                      op()
                            
                    elif respuesta == "no" or respuesta == "No":
                        print("Gracias por tu compra")
                        
            
            elif marca == 3:
                print(preciosmicro[2])
                Aprime = input("¿Cuenta con prime?: ")
                if Aprime == "Si" or Aprime == "si":
                    descuento()
                    prime()
                    respuesta = input("¿Quieres seguir comprando?: ")
                    if respuesta == "si" or respuesta == "Si":
                      op()
                            
                    elif respuesta == "no" or respuesta == "No":
                        print("Gracias por tu compra")
            
                else:
                    descuento()
                    print("Y el precio de envio es de: ",pfenvio)
                    respuesta = input("¿Quieres seguir comprando?: ")
                    if respuesta == "si" or respuesta == "Si":
                      op()
                            
                    elif respuesta == "no" or respuesta == "No":
                        print("Gracias por tu compra")
            
            elif marca == 4:
                print(preciosmicro[3])
                Aprime = input("¿Cuenta con prime?: ")
                if Aprime == "Si" or Aprime == "si":
                    descuento()
                    prime()
                    respuesta = input("¿Quieres seguir comprando?: ")
                    if respuesta == "si" or respuesta == "Si":
                      op()
                            
                    elif respuesta == "no" or respuesta == "No":
                        print("Gracias por tu compra")
                       
                    
                else:
                    descuento()
                    print("Y el precio de envio es de: ",pfenvio)
                    respuesta = input("¿Quieres seguir comprando?: ")
                    if respuesta == "si" or respuesta == "Si":
                      op()
                            
                    elif respuesta == "no" or respuesta == "No":
                        print("Gracias por tu compra")
            
            elif marca == 5:
                print(preciosmicro[4])
                Aprime = input("¿Cuenta con prime?: ")
                if Aprime == "Si" or Aprime == "si":
                    descuento()
                    prime()
                    respuesta = input("¿Quieres seguir comprando?: ")
                    if respuesta == "si" or respuesta == "Si":
                      op()
                            
                    elif respuesta == "no" or respuesta == "No":
                        print("Gracias por tu compra")
            
                else:
                    descuento()
                    print("Y el precio de envio es de: ",pfenvio)
                    respuesta = input("¿Quieres seguir comprando?: ")
                    if respuesta == "si" or respuesta == "Si":
                      op()
                            
                    elif respuesta == "no" or respuesta == "No":
                        print("Gracias por tu compra")
            
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
                    respuesta = input("¿Quieres seguir comprando?: ")
                    if respuesta == "si" or respuesta == "Si":
                      op()
                            
                    elif respuesta == "no" or respuesta == "No":
                        print("Gracias por tu compra")
                       
                else:
                    descuento()
                    print("Y el precio de envio es de: ",pfenvio)
                    respuesta = input("¿Quieres seguir comprando?: ")
                    if respuesta == "si" or respuesta == "Si":
                      op()
                            
                    elif respuesta == "no" or respuesta == "No":
                        print("Gracias por tu compra")
            
            elif marca == 2:
                print(preciostele[1])
                Aprime = input("¿Cuenta con prime?: ")
                if Aprime == "Si" or Aprime == "si":
                    descuento()
                    prime()
                    respuesta = input("¿Quieres seguir comprando?: ")
                    if respuesta == "si" or respuesta == "Si":
                      op()
                            
                    elif respuesta == "no" or respuesta == "No":
                        print("Gracias por tu compra")
            
                else:
                    descuento()
                    print("Y el precio de envio es de: ",pfenvio)
                    respuesta = input("¿Quieres seguir comprando?: ")
                    if respuesta == "si" or respuesta == "Si":
                      op()
                            
                    elif respuesta == "no" or respuesta == "No":
                        print("Gracias por tu compra")
            
            elif marca == 3:
                print(preciostele[2])
                Aprime = input("¿Cuenta con prime?: ")
                if Aprime == "Si" or Aprime == "si":
                    descuento()
                    prime()
                    respuesta = input("¿Quieres seguir comprando?: ")
                    if respuesta == "si" or respuesta == "Si":
                      op()
                            
                    elif respuesta == "no" or respuesta == "No":
                        print("Gracias por tu compra")
            
                else:
                    descuento()
                    print("Y el precio de envio es de: ",pfenvio)
                    respuesta = input("¿Quieres seguir comprando?: ")
                    if respuesta == "si" or respuesta == "Si":
                      op()
                            
                    elif respuesta == "no" or respuesta == "No":
                        print("Gracias por tu compra")
            
            elif marca == 4:
                print(preciostele[3])
                Aprime = input("¿Cuenta con prime?: ")
                if Aprime == "Si" or Aprime == "si":
                    descuento()
                    prime()
                    respuesta = input("¿Quieres seguir comprando?: ")
                    if respuesta == "si" or respuesta == "Si":
                      op()
                            
                    elif respuesta == "no" or respuesta == "No":
                        print("Gracias por tu compra")
            
                else:
                    descuento()
                    print("Y el precio de envio es de: ",pfenvio)
                    respuesta = input("¿Quieres seguir comprando?: ")
                    if respuesta == "si" or respuesta == "Si":
                      op()
                            
                    elif respuesta == "no" or respuesta == "No":
                        print("Gracias por tu compra")
            
            elif marca == 5:
                print(preciostele[4])
                Aprime = input("¿Cuenta con prime?: ")
                if Aprime == "Si" or Aprime == "si":
                    descuento()
                    prime()
                    respuesta = input("¿Quieres seguir comprando?: ")
                    if respuesta == "si" or respuesta == "Si":
                      op()
                            
                    elif respuesta == "no" or respuesta == "No":
                        print("Gracias por tu compra")
                       
            
                else:
                    descuento()
                    print("Y el precio de envio es de: ",pfenvio)
                    respuesta = input("¿Quieres seguir comprando?: ")
                    if respuesta == "si" or respuesta == "Si":
                      op()
                            
                    elif respuesta == "no" or respuesta == "No":
                        print("Gracias por tu compra")
            
    
    
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
                    respuesta = input("¿Quieres seguir comprando?: ")
                    if respuesta == "si" or respuesta == "Si":
                      op()
                            
                    elif respuesta == "no" or respuesta == "No":
                        print("Gracias por tu compra")
        
                else:
                    descuento()
                    print("Y el precio de envio es de: ",pfenvio)
                    respuesta = input("¿Quieres seguir comprando?: ")
                    if respuesta == "si" or respuesta == "Si":
                      op()
                            
                    elif respuesta == "no" or respuesta == "No":
                        print("Gracias por tu compra")
            
            elif marca == 2:
                print(preciosboci[1])
                Aprime = input("¿Cuenta con prime?: ")
                if Aprime == "Si" or Aprime == "si":
                    descuento()
                    prime()
                    respuesta = input("¿Quieres seguir comprando?: ")
                    if respuesta == "si" or respuesta == "Si":
                      op()
                            
                    elif respuesta == "no" or respuesta == "No":
                        print("Gracias por tu compra")
            
                else:
                    descuento()
                    print("Y el precio de envio es de: ",pfenvio)
                    respuesta = input("¿Quieres seguir comprando?: ")
                    if respuesta == "si" or respuesta == "Si":
                      op()
                            
                    elif respuesta == "no" or respuesta == "No":
                        print("Gracias por tu compra")
            
            elif marca == 3:
                print(preciosboci[2])
                Aprime = input("¿Cuenta con prime?: ")
                if Aprime == "Si" or Aprime == "si":
                    descuento()
                    prime()
                    respuesta = input("¿Quieres seguir comprando?: ")
                    if respuesta == "si" or respuesta == "Si":
                      op()
                            
                    elif respuesta == "no" or respuesta == "No":
                        print("Gracias por tu compra")
            
                else:
                    descuento()
                    print("Y el precio de envio es de: ",pfenvio)
                    respuesta = input("¿Quieres seguir comprando?: ")
                    if respuesta == "si" or respuesta == "Si":
                      op()
                            
                    elif respuesta == "no" or respuesta == "No":
                        print("Gracias por tu compra")
            
            elif marca == 4:
                print(preciosboci[3])
                Aprime = input("¿Cuenta con prime?: ")
                if Aprime == "Si" or Aprime == "si":
                    descuento()
                    prime()
                    respuesta = input("¿Quieres seguir comprando?: ")
                    if respuesta == "si" or respuesta == "Si":
                      op()
                            
                    elif respuesta == "no" or respuesta == "No":
                        print("Gracias por tu compra")
            
                else:
                    descuento()
                    print("Y el precio de envio es de: ",pfenvio)
                    respuesta = input("¿Quieres seguir comprando?: ")
                    if respuesta == "si" or respuesta == "Si":
                      op()
                            
                    elif respuesta == "no" or respuesta == "No":
                        print("Gracias por tu compra")
            
            elif marca == 5:
                print(preciosboci[4])
                Aprime = input("¿Cuenta con prime?: ")
                if Aprime == "Si" or Aprime == "si":
                    descuento()
                    prime()
                    respuesta = input("¿Quieres seguir comprando?: ")
                    if respuesta == "si" or respuesta == "Si":
                      op()
                            
                    elif respuesta == "no" or respuesta == "No":
                        print("Gracias por tu compra")
            
                else:
                    descuento()
                    print("Y el precio de envio es de: ",pfenvio)
                    respuesta = input("¿Quieres seguir comprando?: ")
                    if respuesta == "si" or respuesta == "Si":
                      op()
                            
                    elif respuesta == "no" or respuesta == "No":
                        print("Gracias por tu compra")
            

    
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
                    respuesta = input("¿Quieres seguir comprando?: ")
                    if respuesta == "si" or respuesta == "Si":
                      op()
                            
                    elif respuesta == "no" or respuesta == "No":
                        print("Gracias por tu compra")
            
                else:
                    descuento()
                    print("Y el precio de envio es de: ",pfenvio)
                    respuesta = input("¿Quieres seguir comprando?: ")
                    if respuesta == "si" or respuesta == "Si":
                      op()
                            
                    elif respuesta == "no" or respuesta == "No":
                        print("Gracias por tu compra")
            
            elif marca == 2:
                print(preciosaspi[1])
                Aprime = input("¿Cuenta con prime?: ")
                if Aprime == "Si" or Aprime == "si":
                    descuento()
                    prime()
                    respuesta = input("¿Quieres seguir comprando?: ")
                    if respuesta == "si" or respuesta == "Si":
                      op()
                            
                    elif respuesta == "no" or respuesta == "No":
                        print("Gracias por tu compra")
            
                else:
                    descuento()
                    print("Y el precio de envio es de: ",pfenvio)
                    respuesta = input("¿Quieres seguir comprando?: ")
                    if respuesta == "si" or respuesta == "Si":
                      op()
                            
                    elif respuesta == "no" or respuesta == "No":
                        print("Gracias por tu compra")
            
            elif marca == 3:
                print(preciosaspi[2])
                Aprime = input("¿Cuenta con prime?: ")
                if Aprime == "Si" or Aprime == "si":
                    descuento()
                    prime()
                    respuesta = input("¿Quieres seguir comprando?: ")
                    if respuesta == "si" or respuesta == "Si":
                      op()
                            
                    elif respuesta == "no" or respuesta == "No":
                        print("Gracias por tu compra")
            
                else:
                    descuento()
                    print("Y el precio de envio es de: ",pfenvio)
                    respuesta = input("¿Quieres seguir comprando?: ")
                    if respuesta == "si" or respuesta == "Si":
                      op()
                            
                    elif respuesta == "no" or respuesta == "No":
                        print("Gracias por tu compra")
            
            elif marca == 4:
                print(preciosaspi[3])
                Aprime = input("¿Cuenta con prime?: ")
                if Aprime == "Si" or Aprime == "si":
                    descuento()
                    prime()
                    respuesta = input("¿Quieres seguir comprando?: ")
                    if respuesta == "si" or respuesta == "Si":
                      op()
                            
                    elif respuesta == "no" or respuesta == "No":
                        print("Gracias por tu compra")
            
                else:
                    descuento()
                    print("Y el precio de envio es de: ",pfenvio)
                    respuesta = input("¿Quieres seguir comprando?: ")
                    if respuesta == "si" or respuesta == "Si":
                      op()
                            
                    elif respuesta == "no" or respuesta == "No":
                        print("Gracias por tu compra")
            
            elif marca == 5:
                print(preciosaspi[4])
                Aprime = input("¿Cuenta con prime?: ")
                if Aprime == "Si" or Aprime == "si":
                    descuento()
                    prime()
                    respuesta = input("¿Quieres seguir comprando?: ")
                    if respuesta == "si" or respuesta == "Si":
                      op()
                            
                    elif respuesta == "no" or respuesta == "No":
                        print("Gracias por tu compra")
            
                else:
                    descuento()
                    print("Y el precio de envio es de: ",pfenvio)
                    respuesta = input("¿Quieres seguir comprando?: ")
                    if respuesta == "si" or respuesta == "Si":
                      op()
                            
                    elif respuesta == "no" or respuesta == "No":
                        print("Gracias por tu compra")
            
    
    
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
                    respuesta = input("¿Quieres seguir comprando?: ")
                    if respuesta == "si" or respuesta == "Si":
                      op()
                            
                    elif respuesta == "no" or respuesta == "No":
                        print("Gracias por tu compra")
            
                else:
                    descuento()
                    print("Y el precio de envio es de: ",pfenvio)
                    respuesta = input("¿Quieres seguir comprando?: ")
                    if respuesta == "si" or respuesta == "Si":
                      op()
                            
                    elif respuesta == "no" or respuesta == "No":
                        print("Gracias por tu compra")
            
            elif marca == 2:
                print(precioscafe[1])
                Aprime = input("¿Cuenta con prime?: ")
                if Aprime == "Si" or Aprime == "si":
                    descuento()
                    prime()
                    respuesta = input("¿Quieres seguir comprando?: ")
                    if respuesta == "si" or respuesta == "Si":
                      op()
                            
                    elif respuesta == "no" or respuesta == "No":
                        print("Gracias por tu compra")
            
                else:
                    descuento()
                    print("Y el precio de envio es de: ",pfenvio)
                    respuesta = input("¿Quieres seguir comprando?: ")
                    if respuesta == "si" or respuesta == "Si":
                      op()
                            
                    elif respuesta == "no" or respuesta == "No":
                        print("Gracias por tu compra")
            
            elif marca == 3:
                print(precioscafe[2])
                Aprime = input("¿Cuenta con prime?: ")
                if Aprime == "Si" or Aprime == "si":
                    descuento()
                    prime()
                    respuesta = input("¿Quieres seguir comprando?: ")
                    if respuesta == "si" or respuesta == "Si":
                      op()
                            
                    elif respuesta == "no" or respuesta == "No":
                        print("Gracias por tu compra")
            
                else:
                    descuento()
                    print("Y el precio de envio es de: ",pfenvio)
                    respuesta = input("¿Quieres seguir comprando?: ")
                    if respuesta == "si" or respuesta == "Si":
                      op()
                            
                    elif respuesta == "no" or respuesta == "No":
                        print("Gracias por tu compra")
            
            elif marca == 4:
                print(precioscafe[3])
                Aprime = input("¿Cuenta con prime?: ")
                if Aprime == "Si" or Aprime == "si":
                    descuento()
                    prime()
                    respuesta = input("¿Quieres seguir comprando?: ")
                    if respuesta == "si" or respuesta == "Si":
                      op()
                            
                    elif respuesta == "no" or respuesta == "No":
                        print("Gracias por tu compra")
            
                else:
                    descuento()
                    print("Y el precio de envio es de: ",pfenvio)
                    respuesta = input("¿Quieres seguir comprando?: ")
                    if respuesta == "si" or respuesta == "Si":
                      op()
                            
                    elif respuesta == "no" or respuesta == "No":
                        print("Gracias por tu compra")
            
            elif marca == 5:
                print(precioscafe[4])
                Aprime = input("¿Cuenta con prime?: ")
                if Aprime == "Si" or Aprime == "si":
                    descuento()
                    prime()
                    respuesta = input("¿Quieres seguir comprando?: ")
                    if respuesta == "si" or respuesta == "Si":
                      op()
                            
                    elif respuesta == "no" or respuesta == "No":
                        print("Gracias por tu compra")
            
                else:
                    descuento()
                    print("Y el precio de envio es de: ",pfenvio)
                    respuesta = input("¿Quieres seguir comprando?: ")
                    if respuesta == "si" or respuesta == "Si":
                      op()
                            
                    elif respuesta == "no" or respuesta == "No":
                        print("Gracias por tu compra")
            
    
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
                    respuesta = input("¿Quieres seguir comprando?: ")
                    if respuesta == "si" or respuesta == "Si":
                      op()
                            
                    elif respuesta == "no" or respuesta == "No":
                        print("Gracias por tu compra")
            
                else:
                    descuento()
                    print("Y el precio de envio es de: ",pfenvio)
                    respuesta = input("¿Quieres seguir comprando?: ")
                    if respuesta == "si" or respuesta == "Si":
                      op()
                            
                    elif respuesta == "no" or respuesta == "No":
                        print("Gracias por tu compra")
            
            elif marca == 2:
                print(preciosseca[1])
                Aprime = input("¿Cuenta con prime?: ")
                if Aprime == "Si" or Aprime == "si":
                    descuento()
                    prime()
                    respuesta = input("¿Quieres seguir comprando?: ")
                    if respuesta == "si" or respuesta == "Si":
                      op()
                            
                    elif respuesta == "no" or respuesta == "No":
                        print("Gracias por tu compra")
            
                else:
                    descuento()
                    print("Y el precio de envio es de: ",pfenvio)
                    respuesta = input("¿Quieres seguir comprando?: ")
                    if respuesta == "si" or respuesta == "Si":
                      op()
                            
                    elif respuesta == "no" or respuesta == "No":
                        print("Gracias por tu compra")
            
            elif marca == 3:
                print(preciosseca[2])
                Aprime = input("¿Cuenta con prime?: ")
                if Aprime == "Si" or Aprime == "si":
                    descuento()
                    prime()
                    respuesta = input("¿Quieres seguir comprando?: ")
                    if respuesta == "si" or respuesta == "Si":
                      op()
                            
                    elif respuesta == "no" or respuesta == "No":
                        print("Gracias por tu compra")
            
                else:
                    descuento()
                    print("Y el precio de envio es de: ",pfenvio)
                    respuesta = input("¿Quieres seguir comprando?: ")
                    if respuesta == "si" or respuesta == "Si":
                      op()
                            
                    elif respuesta == "no" or respuesta == "No":
                        print("Gracias por tu compra")
            
            elif marca == 4:
                print(preciosseca[3])
                Aprime = input("¿Cuenta con prime?: ")
                if Aprime == "Si" or Aprime == "si":
                    descuento()
                    prime()
                    respuesta = input("¿Quieres seguir comprando?: ")
                    if respuesta == "si" or respuesta == "Si":
                      op()
                            
                    elif respuesta == "no" or respuesta == "No":
                        print("Gracias por tu compra")
            
                else:
                    descuento()
                    print("Y el precio de envio es de: ",pfenvio)
                    respuesta = input("¿Quieres seguir comprando?: ")
                    if respuesta == "si" or respuesta == "Si":
                      op()
                            
                    elif respuesta == "no" or respuesta == "No":
                        print("Gracias por tu compra")
            
            elif marca == 5:
                print(preciosseca[4])
                Aprime = input("¿Cuenta con prime?: ")
                if Aprime == "Si" or Aprime == "si":
                    descuento()
                    prime()
                    respuesta = input("¿Quieres seguir comprando?: ")
                    if respuesta == "si" or respuesta == "Si":
                      op()
                            
                    elif respuesta == "no" or respuesta == "No":
                        print("Gracias por tu compra")
            
                else:
                    descuento()
                    print("Y el precio de envio es de: ",pfenvio)
                    respuesta = input("¿Quieres seguir comprando?: ")
                    if respuesta == "si" or respuesta == "Si":
                      op()
                            
                    elif respuesta == "no" or respuesta == "No":
                        print("Gracias por tu compra")
            
   
    
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
                    respuesta = input("¿Quieres seguir comprando?: ")
                    if respuesta == "si" or respuesta == "Si":
                      op()
                            
                    elif respuesta == "no" or respuesta == "No":
                        print("Gracias por tu compra")
            
                else:
                    descuento()
                    print("Y el precio de envio es de: ",pfenvio)
                    respuesta = input("¿Quieres seguir comprando?: ")
                    if respuesta == "si" or respuesta == "Si":
                      op()
                            
                    elif respuesta == "no" or respuesta == "No":
                        print("Gracias por tu compra")
            
            elif marca == 2:
                print(preciosrefri[1])
                Aprime = input("¿Cuenta con prime?: ")
                if Aprime == "Si" or Aprime == "si":
                    descuento()
                    prime()
                    respuesta = input("¿Quieres seguir comprando?: ")
                    if respuesta == "si" or respuesta == "Si":
                      op()
                            
                    elif respuesta == "no" or respuesta == "No":
                        print("Gracias por tu compra")
            
                else:
                    descuento()
                    print("Y el precio de envio es de: ",pfenvio)
                    respuesta = input("¿Quieres seguir comprando?: ")
                    if respuesta == "si" or respuesta == "Si":
                      op()
                            
                    elif respuesta == "no" or respuesta == "No":
                        print("Gracias por tu compra")
            
            elif marca == 3:
                print(preciosrefri[2])
                Aprime = input("¿Cuenta con prime?: ")
                if Aprime == "Si" or Aprime == "si":
                    descuento()
                    prime()
                    respuesta = input("¿Quieres seguir comprando?: ")
                    if respuesta == "si" or respuesta == "Si":
                      op()
                            
                    elif respuesta == "no" or respuesta == "No":
                        print("Gracias por tu compra")
                    
            
                else:
                    descuento()
                    print("Y el precio de envio es de: ",pfenvio)
                    respuesta = input("¿Quieres seguir comprando?: ")
                    if respuesta == "si" or respuesta == "Si":
                      op()
                            
                    elif respuesta == "no" or respuesta == "No":
                        print("Gracias por tu compra")
            
            elif marca == 4:
                print(preciosrefri[3])
                Aprime = input("¿Cuenta con prime?: ")
                if Aprime == "Si" or Aprime == "si":
                    descuento()
                    prime()
                    respuesta = input("¿Quieres seguir comprando?: ")
                    if respuesta == "si" or respuesta == "Si":
                      op()
                            
                    elif respuesta == "no" or respuesta == "No":
                        print("Gracias por tu compra")
            
                else:
                    descuento()
                    print("Y el precio de envio es de: ",pfenvio)
                    respuesta = input("¿Quieres seguir comprando?: ")
                    if respuesta == "si" or respuesta == "Si":
                      op()
                            
                    elif respuesta == "no" or respuesta == "No":
                        print("Gracias por tu compra")
            
            elif marca == 5:
                print(preciosrefri[4])
                Aprime = input("¿Cuenta con prime?: ")
                if Aprime == "Si" or Aprime == "si":
                    descuento()
                    prime()
                    respuesta = input("¿Quieres seguir comprando?: ")
                    if respuesta == "si" or respuesta == "Si":
                      op()
                            
                    elif respuesta == "no" or respuesta == "No":
                        print("Gracias por tu compra")
            
                else:
                    descuento()
                    print("Y el precio de envio es de: ",pfenvio)
                    respuesta = input("¿Quieres seguir comprando?: ")
                    if respuesta == "si" or respuesta == "Si":
                      op()
                            
                    elif respuesta == "no" or respuesta == "No":
                        print("Gracias por tu compra")
            
    
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
                    respuesta = input("¿Quieres seguir comprando?: ")
                    if respuesta == "si" or respuesta == "Si":
                      op()
                            
                    elif respuesta == "no" or respuesta == "No":
                        print("Gracias por tu compra")
            
                else:
                    descuento()
                    print("Y el precio de envio es de: ",pfenvio)
                    respuesta = input("¿Quieres seguir comprando?: ")
                    if respuesta == "si" or respuesta == "Si":
                      op()
                            
                    elif respuesta == "no" or respuesta == "No":
                        print("Gracias por tu compra")
            
            elif marca == 2:
                print(preciospropa[1])
                Aprime = input("¿Cuenta con prime?: ")
                if Aprime == "Si" or Aprime == "si":
                    descuento()
                    prime()
                    respuesta = input("¿Quieres seguir comprando?: ")
                    if respuesta == "si" or respuesta == "Si":
                      op()
                            
                    elif respuesta == "no" or respuesta == "No":
                        print("Gracias por tu compra")
            
                else:
                    descuento()
                    print("Y el precio de envio es de: ",pfenvio)
                    respuesta = input("¿Quieres seguir comprando?: ")
                    if respuesta == "si" or respuesta == "Si":
                      op()
                            
                    elif respuesta == "no" or respuesta == "No":
                        print("Gracias por tu compra")
            
            elif marca == 3:
                print(preciospropa[2])
                Aprime = input("¿Cuenta con prime?: ")
                if Aprime == "Si" or Aprime == "si":
                    descuento()
                    prime()
                    respuesta = input("¿Quieres seguir comprando?: ")
                    if respuesta == "si" or respuesta == "Si":
                      op()
                            
                    elif respuesta == "no" or respuesta == "No":
                        print("Gracias por tu compra")
            
                else:
                    descuento()
                    print("Y el precio de envio es de: ",pfenvio)
                    respuesta = input("¿Quieres seguir comprando?: ")
                    if respuesta == "si" or respuesta == "Si":
                      op()
                            
                    elif respuesta == "no" or respuesta == "No":
                        print("Gracias por tu compra")
            
            elif marca == 4:
                print(preciospropa[3])
                Aprime = input("¿Cuenta con prime?: ")
                if Aprime == "Si" or Aprime == "si":
                    descuento()
                    prime()
                    respuesta = input("¿Quieres seguir comprando?: ")
                    if respuesta == "si" or respuesta == "Si":
                      op()
                            
                    elif respuesta == "no" or respuesta == "No":
                        print("Gracias por tu compra")
            
                else:
                    descuento()
                    print("Y el precio de envio es de: ",pfenvio)
                    respuesta = input("¿Quieres seguir comprando?: ")
                    if respuesta == "si" or respuesta == "Si":
                      op()
                            
                    elif respuesta == "no" or respuesta == "No":
                        print("Gracias por tu compra")
            
            elif marca == 5:
                print(preciospropa[4])
                Aprime = input("¿Cuenta con prime?: ")
                if Aprime == "Si" or Aprime == "si":
                    descuento()
                    prime()
                    respuesta = input("¿Quieres seguir comprando?: ")
                    if respuesta == "si" or respuesta == "Si":
                      op()
                            
                    elif respuesta == "no" or respuesta == "No":
                        print("Gracias por tu compra")
           
                else:
                    descuento()
                    print("Y el precio de envio es de: ",pfenvio)
                    respuesta = input("¿Quieres seguir comprando?: ")
                    if respuesta == "si" or respuesta == "Si":
                      op()
                            
                    elif respuesta == "no" or respuesta == "No":
                        print("Gracias por tu compra")
            
    
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
                    respuesta = input("¿Quieres seguir comprando?: ")
                    if respuesta == "si" or respuesta == "Si":
                      op()
                            
                    elif respuesta == "no" or respuesta == "No":
                        print("Gracias por tu compra")
            
                else:
                    descuento()
                    print("Y el precio de envio es de: ",pfenvio)
                    respuesta = input("¿Quieres seguir comprando?: ")
                    if respuesta == "si" or respuesta == "Si":
                      op()
                            
                    elif respuesta == "no" or respuesta == "No":
                        print("Gracias por tu compra")
            
            elif marca == 2:
                print(precioshorno[1])
                Aprime = input("¿Cuenta con prime?: ")
                if Aprime == "Si" or Aprime == "si":
                    descuento()
                    prime()
                    respuesta = input("¿Quieres seguir comprando?: ")
                    if respuesta == "si" or respuesta == "Si":
                      op()
                            
                    elif respuesta == "no" or respuesta == "No":
                        print("Gracias por tu compra")
            
                else:
                    descuento()
                    print("Y el precio de envio es de: ",pfenvio)
                    respuesta = input("¿Quieres seguir comprando?: ")
                    if respuesta == "si" or respuesta == "Si":
                      op()
                            
                    elif respuesta == "no" or respuesta == "No":
                        print("Gracias por tu compra")
            
            elif marca == 3:
                print(precioshorno[2])
                Aprime = input("¿Cuenta con prime?: ")
                if Aprime == "Si" or Aprime == "si":
                    descuento()
                    prime()
                    respuesta = input("¿Quieres seguir comprando?: ")
                    if respuesta == "si" or respuesta == "Si":
                      op()
                            
                    elif respuesta == "no" or respuesta == "No":
                        print("Gracias por tu compra")
            
                else:
                    descuento()
                    print("Y el precio de envio es de: ",pfenvio)
                    respuesta = input("¿Quieres seguir comprando?: ")
                    if respuesta == "si" or respuesta == "Si":
                      op()
                            
                    elif respuesta == "no" or respuesta == "No":
                        print("Gracias por tu compra")
            
            elif marca == 4:
                print(precioshorno[3])
                Aprime = input("¿Cuenta con prime?: ")
                if Aprime == "Si" or Aprime == "si":
                    descuento()
                    prime()
                    respuesta = input("¿Quieres seguir comprando?: ")
                    if respuesta == "si" or respuesta == "Si":
                      op()
                            
                    elif respuesta == "no" or respuesta == "No":
                        print("Gracias por tu compra")
            
                else:
                    descuento()
                    print("Y el precio de envio es de: ",pfenvio)
                    respuesta = input("¿Quieres seguir comprando?: ")
                    if respuesta == "si" or respuesta == "Si":
                      op()
                            
                    elif respuesta == "no" or respuesta == "No":
                        print("Gracias por tu compra")
            
            elif marca == 5:
                print(precioshorno[4])
                Aprime = input("¿Cuenta con prime?: ")
                if Aprime == "Si" or Aprime == "si":
                    descuento()
                    prime()
                    respuesta = input("¿Quieres seguir comprando?: ")
                    if respuesta == "si" or respuesta == "Si":
                      op()
                            
                    elif respuesta == "no" or respuesta == "No":
                        print("Gracias por tu compra")
            
                else:
                    descuento()
                    print("Y el precio de envio es de: ",pfenvio)
                    respuesta = input("¿Quieres seguir comprando?: ")
                    if respuesta == "si" or respuesta == "Si":
                      op()
                            
                    elif respuesta == "no" or respuesta == "No":
                        print("Gracias por tu compra")
            
   
    
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
                    respuesta = input("¿Quieres seguir comprando?: ")
                    if respuesta == "si" or respuesta == "Si":
                      op()
                            
                    elif respuesta == "no" or respuesta == "No":
                        print("Gracias por tu compra")
            
                else:
                    descuento()
                    print("Y el precio de envio es de: ",pfenvio)
                    respuesta = input("¿Quieres seguir comprando?: ")
                    if respuesta == "si" or respuesta == "Si":
                      op()
                            
                    elif respuesta == "no" or respuesta == "No":
                        print("Gracias por tu compra")
            
            elif marca == 2:
                print(precioslava[1])
                Aprime = input("¿Cuenta con prime?: ")
                if Aprime == "Si" or Aprime == "si":
                    descuento()
                    prime()
                    respuesta = input("¿Quieres seguir comprando?: ")
                    if respuesta == "si" or respuesta == "Si":
                      op()
                            
                    elif respuesta == "no" or respuesta == "No":
                        print("Gracias por tu compra")
            
                else:
                    descuento()
                    print("Y el precio de envio es de: ",pfenvio)
                    respuesta = input("¿Quieres seguir comprando?: ")
                    if respuesta == "si" or respuesta == "Si":
                      op()
                            
                    elif respuesta == "no" or respuesta == "No":
                        print("Gracias por tu compra")
            
            elif marca == 3:
                print(precioslava[2])
                Aprime = input("¿Cuenta con prime?: ")
                if Aprime == "Si" or Aprime == "si":
                    descuento()
                    prime()
                    respuesta = input("¿Quieres seguir comprando?: ")
                    if respuesta == "si" or respuesta == "Si":
                      op()
                            
                    elif respuesta == "no" or respuesta == "No":
                        print("Gracias por tu compra")
           
                else:
                    descuento()
                    print("Y el precio de envio es de: ",pfenvio)
                    respuesta = input("¿Quieres seguir comprando?: ")
                    if respuesta == "si" or respuesta == "Si":
                      op()
                            
                    elif respuesta == "no" or respuesta == "No":
                        print("Gracias por tu compra")
            
            elif marca == 4:
                print(precioslava[3])
                Aprime = input("¿Cuenta con prime?: ")
                if Aprime == "Si" or Aprime == "si":
                    descuento()
                    prime()
                    respuesta = input("¿Quieres seguir comprando?: ")
                    if respuesta == "si" or respuesta == "Si":
                      op()
                            
                    elif respuesta == "no" or respuesta == "No":
                        print("Gracias por tu compra")
            
                else:
                    descuento()
                    print("Y el precio de envio es de: ",pfenvio)
                    respuesta = input("¿Quieres seguir comprando?: ")
                    if respuesta == "si" or respuesta == "Si":
                      op()
                            
                    elif respuesta == "no" or respuesta == "No":
                        print("Gracias por tu compra")
            
            elif marca == 5:
                print(precioslava[4])
                Aprime = input("¿Cuenta con prime?: ")
                if Aprime == "Si" or Aprime == "si":
                    descuento()
                    prime()
                    respuesta = input("¿Quieres seguir comprando?: ")
                    if respuesta == "si" or respuesta == "Si":
                      op()
                            
                    elif respuesta == "no" or respuesta == "No":
                        print("Gracias por tu compra")
            
                else:
                    descuento()
                    print("Y el precio de envio es de: ",pfenvio)
                    respuesta = input("¿Quieres seguir comprando?: ")
                    if respuesta == "si" or respuesta == "Si":
                      op()
                            
                    elif respuesta == "no" or respuesta == "No":
                        print("Gracias por tu compra")
            

