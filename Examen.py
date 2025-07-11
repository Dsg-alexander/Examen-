#DIEGO ALEXANDER SANTIBAÑEZ GODOY

#Examen: Ejercicio de tienda especializada en venta de notebooks

#Diccionarios iniciales.


#productos = {modelo: [marca, pantalla, RAM, disco, GB de DD, procesador, video], ...]
productos = {'8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
'2175HD': ['Acer', 14, '4GB', 'SSD', '512GB', 'Intel Core i7', 'Nvidia GTX1050'],
'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i5', 'Nvidia RTX2080Ti'],
'fgdxFHD': ['HP', 15.6, '12GB', 'DD', '1T', 'Intel Core i5', 'integrada'],
'GF75HD': ['Asus', 15.6, '12GB', 'DD', '1T', 'Intel Core i3', 'Nvidia GTX1050'],
'123FHD': ['Acer', 14, '6GB', 'DD', '1T', 'AMD Ryzen 7', 'integrada'],
'342FHD': ['Acer', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 5', 'Nvidia GTX1050'],
'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 5', 'Nvidia GTX1050'],
}


#stock = {modelo: [precio, stock], ...]
stock = {'8475HD': [387990,10], '2175HD': [327990,4], 'JjfFHD': [424990,1],
'fgdxFHD': [664990,21], '123FHD': [290890,32], '342FHD': [444990,7],
'GF75HD': [749990,2], 'UWU131HD': [349990,1], 'FS1230HD': [249990,0],
}

#Funcion para stock por tipo de marca.
def stock_marca(marca):
    total = 0;
    for dato1,dato2 in productos.items():
        if(dato2[1].lower() == tipo_marca.lower):
            total += stock[dato1][1]



#Funcion para buscar por precios.
def buscar_por_precio(precio_min,precio_max):
    resultados = []
    for codigo,datos in productos.items():
        precio = datos[1]
        if(precio >= precio_min and precio <= precio_max) and (stock[codigo][1]>0):
            resultados.append(codigo + '--' + datos[1])
    if resultados:
        resultados.sort();
        print("Productos encontrados", resultados)
    else:
        print("No hay productos en ese rango de precio")


#Funcion para ordenar y actualizar stock
def ordenar_stock(codigo, nuevo_stock):
    if(codigo in stock):
        stock[codigo[1]] = nuevo_stock
        return True
    return False



#aqui procedemos a mostrarle el menu como programa principal al cliente para que decida la opcion deseada.
while True:
    print("*** MENU PRINCIPAL ***")
    print("1. Stock marca.")
    print("2. Busqueda por precio.")
    print("3. Listado de productos.")
    print("4. Salir.")

    try:
        opc = int(input("Bienvenido a PyBooks, ingrese la opcion deseada: "))
        

        #Con esta opcion el usuario consultara por la marca del producto la cual se le imprimira el stock en pantalla.
        if (opc == 1):
            tipo_marca = input("Ingrese la marca que desea consultar: ")
            stock_marca(stock)
            
            total = 0;
            for stock,tipo_marca in productos.items():
                if(tipo_marca[1].lower() == tipo_marca.lower):
                    total += stock[stock][1]
            
            
            
            
          
        #Esta opcion nos permite hacer una busqueda por el precio del producto.    
        elif (opc == 2):
            precio_min = float(input("Ingrese el precio minimo: "))
            precio_max = float(input("Ingrese el precio maximo: "))


            resultados = []
            for codigo,datos in productos.items():
                precio = datos[1]
                if(precio >= precio_min and precio <= precio_max) and (stock[codigo][1]>0):
                    resultados.append(codigo + '--' + datos[1])
            if resultados:
                resultados.sort();
                print("Productos encontrados", resultados)
            else:
                print("No hay productos en ese rango de precio")



        #Esta opcion nos imprime en pantalla el listado de forma ordenada.
        elif(opc == 3):
            print("***Listado de notebooks ordenados*** ")
            ordenar_productos = ()
            productos.sort() = ordenar_productos
            print(ordenar_productos)

            
            
        

        #Esta opcion nos permitira dar la finalizacion al codigo.
        elif(opc == 4):
            print("Programa finalizado. ")
            break

        else:
            print("Debe selecionar una opcion valida!!")





    except ValueError:
        print("Solo pueden ingresarse valores numericos para ingresar la opcion")
