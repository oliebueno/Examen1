import math

#Clase que implementa el sistema buddy system
class BuddySystem:

    def __init__(self, bloques):
        self.tam = 2 ** math.ceil(math.log2(bloques)) #tamaño de los bloques(2^n)
        self.listas_libres = [[] for _ in range(self.tam.bit_length())] #lista de listas de bloques libres
        self.listas_libres[-1].append((0, self.tam - 1)) #agrega a la lista de bloques libres el bloque de memoria completa
        self.nombres_re = {} #diccionario de nombres reservados
        self.linea = "|" #linea que se muestra en pantalla
        pass

    #Función que reserva bloques de memoria
    def reservar(self, cantidad, nombre):
        tam = 2 ** math.ceil(math.log2(cantidad))
        i = tam.bit_length() - 1

        #Busca la lista de bloques libres que tenga bloques del tamaño que se quiere reservar
        while i < len(self.listas_libres) and not (self.listas_libres[i]):
            i += 1
        #Si el nombre ya está reservado, muestra un mensaje de error
        if nombre in self.nombres_re:
            print(f"Error: {nombre} ya tiene espacio reservado")
            return
        #Si no hay bloques libres del tamaño que se quiere reservar, muestra un mensaje de error
        if i == len(self.listas_libres):
            try:
                # Lanzar una excepción de tipo Exception con un mensaje
                raise Exception(
                    f"Error: No hay espacio suficiente para reservar {cantidad} bloques para {nombre}.")
            # Capturar y manejar la excepción si ocurre
            except Exception as e:
                # Mostrar el mensaje de la excepción
                print(e)
            return

        #Si hay bloques libres del tamaño que se quiere reservar, reserva los bloques
        inicio, final = self.listas_libres[i].pop()
        while i > tam.bit_length() - 1:
            i -= 1
            guarda = inicio + 2 ** i
            self.listas_libres[i].append((guarda, final))
            final = guarda - 1
        #Muestra un mensaje de que se reservó la memoria
        print(f"Memoria de {inicio} hasta {final} reservada por {nombre}")
        self.nombres_re[nombre] = (inicio, final)

    #Función que libera bloques de memoria
    def liberar(self, nombre):
        #Si el nombre no está reservado, muestra un mensaje de error
        if nombre not in self.nombres_re:
            try:
                raise Exception(
                    f"Error: No hay memoria reservada para el identificador {nombre}")
            except Exception as e:
                print(e)
            return
        #Si el nombre está reservado, libera los bloques de memoria
        inicio, final = self.nombres_re.pop(nombre)
        i = (final - inicio + 1).bit_length() - 1
        guarda = inicio ^ (1 << i)
        introd = False
        #Recorre la lista de bloques libres
        while i < len(self.listas_libres):
            #Si hay bloques libres, recorre la lista de bloques libres
            if self.listas_libres[i]:
                #Si el bloque que se quiere liberar está en la lista de bloques libres, lo libera
                for j, (comienzo, parada) in enumerate(self.listas_libres[i]):
                    #Si el bloque que se quiere liberar está en la lista de bloques libres, lo libera
                    if comienzo == guarda:
                        self.listas_libres[i].pop(j)
                        inicio = min(inicio, guarda)
                        final = max(final, parada)
                        introd = True
                        break
                    #Si el bloque que se quiere liberar no está en la lista de bloques libres, lo agrega
                    elif comienzo != guarda and j == len(self.listas_libres[i]) - 1:
                        self.listas_libres[i].append((inicio, final))
                        break
            #Si no hay bloques libres, agrega el bloque que se quiere liberar
            else:
                if introd:
                    self.listas_libres[i].append((inicio, final))
                    introd = False
            i += 1
            guarda = inicio ^ (1 << i)
        #Muestra un mensaje de que se liberó la memoria
        print(
            f"Memoria de {inicio} hasta {final} asociada al identificador {nombre} fue liberada.")

    #Función que muestra la memoria
    def mostrar(self):
        libre = 0
        #Recorre la lista de bloques libres
        for i in self.listas_libres:
            for comienzo, final in i:
                libre += final - comienzo + 1
        #Muestra la cantidad de bloques de memoria y la cantidad de bloques libres
        print(f"La memoria esta compuesta por un total: {self.tam} bloques")
        print(f"Cantidad de memoria libre: {libre} bloques")

        self.linea = "Memoria: |"
        #Recorre la lista de bloques libres
        for j in range(self.tam):
            if any(comienzo <= j <= final for comienzo, final in self.nombres_re.values()):
                self.linea += "[]"
            else:
                self.linea += "_"
        self.linea += "|"
        print(self.linea)

    #Función que ejecuta el programa
    def ejecutar(self):
        while True:
            obciones = input(
                "Ingrese una acción (RESERVAR, LIBERAR, MOSTRAR o SALIR): ")
            obciones = obciones.upper().split()
            if not obciones:
                continue
            if obciones[0] == "RESERVAR":
                if len(obciones) != 3:
                    print("Error: se esperan dos argumentos para RESERVAR")
                    continue
                try:
                    bloques = int(obciones[1])
                    if bloques < 1:
                        raise ValueError
                except ValueError:
                    print("Error: el primer argumento debe ser un número positivo")
                    continue
                nombre = obciones[2]
                self.reservar(bloques, nombre)
            elif obciones[0] == "LIBERAR":
                if len(obciones) != 2:
                    print(
                        "La acción LIBERAR requiere un argumento: el nombre del identificador")
                    continue
                nombre = obciones[1]
                self.liberar(nombre)
            elif obciones[0] == "MOSTRAR":
                if len(obciones) != 1:
                    print("La acción MOSTRAR no requiere ningún argumento")
                    continue
                self.mostrar()
            elif obciones[0] == "SALIR":
                break
            else:
                print(
                    "La acción ingresada no es válida. Las acciones posibles son: RESERVAR, LIBERAR, MOSTRAR o SALIR")
                continue
