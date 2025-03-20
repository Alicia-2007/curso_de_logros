# Juego Wonderland Scape Room
# Se abre la clase y se declaran sus variables y datos

class JuegoScapeRoom:
    def __init__(self):
        self.opciones_iniciales = ["BOTELLA", "GALLETA"] #self se usa para manejar el flujo del juego, permitiendo que el usuario tome decisiones sin perder el estado del juego
        self.acciones_botella = ("COMER", "IR")  # al elegir botella
        self.acciones_comer = ("AZUL", "MORADO")  # al elegir botella y luego comer
        self.acciones_ir = ("HALAGOS", "INSTRUCCIONES")  # al elegir botella y luego ir
        self.acciones_galleta = ("GRIETA", "LLAVE", "CUERDA")  # al elegir galleta
        self.acciones_grieta = ("FUERZA", "BEBER")  # al elegir galleta y luego grieta
        self.acciones_llave = ("ABRIR", "NO ABRIR")  # al elegir galleta, luego llave
        self.acciones_cuerda = ("INVESTIGAR", "LEJOS")  # al elegir galleta, luego cuerda
#inicio
    def iniciar_juego(self):
        print("Te encuentras en una habitación, no sabes cómo llegaste ahí. Al ver a tu alrededor, ves que no hay puertas, solo una gran mesa en el centro con una BOTELLA que dice 'Bébeme' y una GALLETA que dice 'Cómeme'. Debes agarrar una y guardar la otra.")
        eleccion = input("¿Cuál eliges? (BOTELLA/GALLETA): ").strip().upper() #el upper es para que asi no distinga entre mayusculas y minusculas

        if eleccion == "BOTELLA":
            self.escena_botella()  #lo uso ya que luego ahi habran mas opciones
        elif eleccion == "GALLETA":
            self.escena_galleta()
        else:
            print("Opción no válida. Fin del juego.")
 #al elegir Botella 
    def escena_botella(self):
        print("Sientes un cambio raro en tu cuerpo, te das cuenta de que ahora eres diminuto. Desde esa altura puedes observar una puerta diminuta en una esquina. Tienes dos opciones: COMER la galleta y ver qué pasa, o IR a la puerta.")
        eleccion = input("¿Quieres COMER o IR?: ").strip().upper()

        if eleccion == "COMER":
            self.escena_comer()
        elif eleccion == "IR":
            self.escena_ir()
        else:
            print("Opción no válida. Fin del juego.")
#al elegir comer
    def escena_comer(self):
        print("Enhorabuena, volviste a tu estatura usual. Puedes ver que en la mesa de antes ahora hay un nuevo objeto: una caja con una inscripción que dice 'Para ser libre, oprime el botón'. La caja tiene dos botones, uno MORADO y otro AZUL.")
        eleccion = input("¿Cuál eliges? (MORADO/AZUL): ").strip().upper()

        if eleccion == "MORADO":
            print("¡Qué suerte! El botón te teletransportó a tu casa. Estás a salvo.")
        elif eleccion == "AZUL":
            print("La caja te dio un shock eléctrico y moriste electrocutado.")
        else:
            print("Opción no válida. Fin del juego.")
#al elegir ir
    def escena_ir(self):
        print("Al cruzar la puerta te encuentras con un gato morado con azul. Su nombre es Cheshire y te pregunta si el sombrero que está usando le queda bien. Tienes dos opciones: HALAGARLO o pedirle las INSTRUCCIONES para salir.")
        eleccion = input("¿Cuál eliges? (HALAGOS/INSTRUCCIONES): ").strip().upper()

        if eleccion == "HALAGOS":
            print("Hablas un rato con el gato, te ofrece ayuda, te lleva hasta tu casa y te devuelve a tu estatura usual.")
        elif eleccion == "INSTRUCCIONES":
            print("El gato es quisquilloso y se molestó de que ignoraras su pregunta. Se va sin ayudarte y quedas atrapado.")
        else:
            print("Opción no válida. Fin del juego.")
#al elegir galleta, como galleta tiene muchas opciones, repito el proceso de inicio  
    def escena_galleta(self):
        print("Sientes un cambio raro en tu cuerpo, te das cuenta de que ahora eres gigante. Desde esta altura puedes ver una grieta en el techo, una llave amarrada a la lámpara y una cuerda con la inscripción 'Jálame'.")
        eleccion = input("¿Quieres meterte por la GRIETA, agarrar la LLAVE o jalar la CUERDA?: ").strip().upper()

        if eleccion == "GRIETA":
            self.escena_grieta()
        elif eleccion == "LLAVE":
            self.escena_llave()
        elif eleccion == "CUERDA":
            self.escena_cuerda()
        else:
            print("Opción no válida. Fin del juego.")
#al elegir grieta
    def escena_grieta(self):
        print("¿Nunca escuchaste de los peligros del Cavediving? Aquí aplica el mismo principio. Eras muy grande y no entraste por completo en la grieta, quedaste atrapado. Ahora tienes dos opciones: hacer FUERZA para intentar salir o BEBER lo que te queda en la botella.")
        eleccion = input("¿Qué decides hacer? (FUERZA/BEBER): ").strip().upper()

        if eleccion == "FUERZA":
            print("Hiciste demasiada fuerza, la estructura colapsó y moriste aplastado.")
        elif eleccion == "BEBER":
            print("Como estabas atorado, no pudiste maniobrar bien. Bebiste demasiado de la botella por accidente y moriste por sobredosis.")
        else:
            print("Opción no válida. Fin del juego.")
#al elegir llave
    def escena_llave(self):
        print("Al acercarte a la llave, ves un ventanal grande en el techo que da al exterior. Se puede abrir con la llave, pero tiene una inscripción que dice 'No abrir o pagarás las consecuencias'.")
        eleccion = input("¿Eliges ABRIR o NO ABRIR el ventanal? (ABRIR/NO ABRIR): ").strip().upper()

        if eleccion == "ABRIR":
            print("¡Felicidades! Lograste salir de la habitación, encontraste el camino a casa y al beber de la botella volviste a tu estatura usual.")
        elif eleccion == "NO ABRIR":
            print("Por falta de curiosidad y cobardía, quedaste atrapado y nunca saliste.")
        else:
            print("Opción no válida. Fin del juego.")
#al elegir cuerda
    def escena_cuerda(self):
        print("Cuando jalaste la cuerda, la mesa de la sala se movió, revelando una puerta tenebrosa. ¿Decides ir a INVESTIGAR o quedarte lo más LEJOS de ahí?")
        eleccion = input("¿Qué decides hacer? (INVESTIGAR/LEJOS): ").strip().upper()

        if eleccion == "INVESTIGAR":
            print("¡Felicidades! Lograste salir de la habitación, encontrar el camino a casa y al beber de la botella volviste a tu estatura usual.")
        elif eleccion == "LEJOS":
            print("Esa puerta daba a la salida. Quedaste atrapado por cobarde.")
        else:
            print("Opción no válida. Fin del juego.")

juego = JuegoScapeRoom() #sirve para cerrar la clase
juego.iniciar_juego() #sirve para iniciar el juego y es obligatoria para iniciarlo
