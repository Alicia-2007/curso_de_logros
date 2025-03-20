
# Online Python - IDE, Editor, Compiler, Interpreter
# Actividad Hogar
# Menu de compras
def visualizar_menu(): #define esta variable
    print(f"Visualiza las opciones del menu:") #imprime este texto en pantalla
    opciones = [   #abre lista
        "1. Ingresar un nuevo item",
        "2. Quitar un item",
        "3. Mostrar todos los productos en el carrito",
        "4. Totalizar presupuesto",
        "5. Salir"
         ]
    print("Menú:") 
    for opcion in opciones:
        print(opcion)
def diccionario_carrito(): #diccionario carrito
    carrito = {}  # Diccionario para almacenar los productos con su monto y cantidad
    while True:
        visualizar_menu()
        opcion = input("Seleccione una opción: ")
        opciones = {
            "1": ingresar_producto,
            "2": quitar_producto,    
            "3": mostrar_carrito,
            "4": totalizar_presupuesto
        }
        if opcion in opciones:
            opciones[opcion](carrito)
        elif opcion == "5":
            print("Espero le haya gustado su compra!")
            break
        else:
            print("Respuesta no reconocida. Vuelva a ingresar una opcion.")
#ingresar los numeros, sean montos, cantidades, whatever
def ingresar_numero(mensaje): #para asi no tener que declarar esta vaina cada vez que pida un numero, y para que el usuario no salga con que su cafe costo "dinero" en vez de dar un numero
    print(f"ingrese un numero:")
    while True:
       valor = input(mensaje) 
       if valor.replace(".", "", 1).isdigit():  # Permite números enteros y decimales, no estoy segura de como funciona, pero lo vi en youtube, y el isdigit es para verificar que sean numeros y no haya letras
        return float(valor) if "." in valor else int(valor) #if it is a decimal "." it will read float #return es para poder reutulizar el dato 
       print("Es necesario que sea un numero.")
#para ingresar el item
def ingresar_producto(carrito): #carrito es el diccionario
    print(f"Ingresar un nuevo item")
    item = input("Ingrese el nombre del item: ").strip().title().upper()#para que no distinga mayusculas, espacios o asi
    cantidad = ingresar_numero("Ingrese la cantidad: ")
    monto = ingresar_numero("Ingrese el monto del item: ")
    
    if item in carrito: #Verifica si item ya fue agregado antes al carrito
        carrito[item]["cantidad"] += cantidad #Si el item ya existe en el carrito, suma la cantidad nueva a la cantidad que ya había
    else:
        carrito[item] = {"monto": monto, "cantidad": cantidad}#Si el item no está en el carrito, crea un nuevo elemento en el diccionario
    print(f"{cantidad} unidad(es) de {item} agregado(s) al carrito.") #Muestra un mensaje confirmando que el item fue agregado al carrito
#para quitar un item
def quitar_producto(carrito):
    print(f"Quitar un item")
    if not carrito: #si no esta en el carrito, dira que no hay nada que quitar
        print("No hay productos para eliminar.")
        return   
    mostrar_carrito(carrito)  # Mostrar el carrito antes de eliminar un producto
    item = input("Ingrese el nombre del item que desea quitar: ").strip().title().upper()
    if item in carrito:
        del carrito[item]  # Elimina el producto del diccionario
        print(f"{item} eliminado del carrito.")
    else:
        print("El producto no está en el carrito.")
#para mostrar el contenido del carrito    
def mostrar_carrito(carrito):
    print(f"Contenido del carrito:")
    if not carrito: #si no han agregado nada
        print("El carrito está vacío.")
    else: #si ya hay al menos un item
        print("\nContenido del carrito:")
        for i, (item, detalles) in enumerate(carrito.items(), start=1): #para decir que inicia en 1 y no en 0, y para ennumerar los productos
            print(f"{i}. {item} - ${detalles['monto']:} x {detalles['cantidad']}") # el signo del dolar es para el monto, no es un comando, y la x tampoco es un comando, es para decir "x\por tanta cantidad de item"
#calcular presupuesto
def totalizar_presupuesto(carrito):
    print("Presupuesto totalizado:")
    total = sum(detalles["monto"] * detalles["cantidad"] for detalles in carrito.values()) #la suma de los precios multiplicados por la cantidad
    print(f"Monto total: ${total:}")  # El símbolo de dólar bien colocado, no se pq si lo pongo de otra manerano lo lee
# Para que el programa se ejecute correctamente, no se me queria ejecutar y dure una hora averiguando el pq, y aun  no lo entiendo del todo, pero al menos ya ejecuta
if __name__ == "__main__":
    diccionario_carrito()
    #me duele la cabeza, ya ni se que hice, muchas lineas
