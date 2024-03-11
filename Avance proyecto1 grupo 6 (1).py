access = int(input("Desea acceder a Grypo6Airlines? \n Si.1 \n No.0 \n Opcion: " ))
while access != 0:
    print("Bienvenido a Grupo6Airlines")
    print("Por favor, seleccione una opcion:")
    print("1. Reservar un vuelo")
    print("2. futura opcion")
    print("3. futura opcion")
    print("4. futura opcion")
    print("0. Salir")
   

    opcionSelect = int(input("Opcion: "))

    if opcionSelect == 1:
        print("Introduzca los datos solicitados ")

        nombreUsuario = input("Nombre: ")
        apellidoUsuario = input("Apellido: ")

        edadUsuario = int(input("Edad: "))
        while edadUsuario < 18:                 #evalua si el usuario es mayor de 18 anios 
            print("Lo sentimos, debes tener al menos 18 años para reservar un vuelo.")
            edadUsuario = int(input("introduce tu edad de nuevo: "))

        cedula = input("Número de pasaporte: ")
        while len(cedula) < 9:                  #evalua si el número de cédula sobrepasa los 9 caracteres
            print("El numero de cedula no debe sobrepasar los 9 caracteres.")
            cedula = input("Por favor, introduce el número de cedula de nuevo: ")

        print("Introducir los detalles del vuelo")

        print("Destinos disponibles:")
        print("1. Paris, Francia")
        print("2. CDMX, Mexico  ")
        print("3. Dubai, Emiratos Arabes Unidos")
        print("4. futura opcion")
        print("5. futura opcion")
        print("6. futura opcion")

        destinoVuelo = int(input("Seleccione el número correspondiente a su destino: "))
        while destinoVuelo < 1 or destinoVuelo > 3: #permite al usuario elegir a que destino quiere ir 
            print("Por favor, seleccione un numero valido de la lista de destinos.")
            destinoVuelo = int(input("Seleccione el número correspondiente a su destino de nuevo: "))

        if destinoVuelo == 1:
            destino = "Paris, Francia"
        elif destinoVuelo == 2:
            destino = "CDMX, Mexico "
        else:
            destino = "Dubai, Emiratos Arabes Unidos"

        fechaVuelo = input("Fecha del vuelo (dd-mm-aaaa): ")        #estos datos no los pudimos validar sin importar librerias
        horaVuelo = input("Hora del vuelo (HH:MM): ")               #estos datos no los pudimos validar sin importar librerias

        asientoVuelo = int(input("Numero de asiento, solo quedan asientos del 1 al 100 disponibles: "))
        while asientoVuelo < 1 or asientoVuelo > 100:                  #Evalua si el input que dio el usuario es entre 0 y 100
            print("El numero de asiento debe estar entre 1 y 100.")
            asientoVuelo = int(input("Por favor, introduce el número de asiento de nuevo: "))

        print(f"Gracias por proporcionar sus datos, " + nombreUsuario + " " + apellidoUsuario + ".")
        print(f"Edad: {edadUsuario}")
        print(f"Número de pasaporte: {cedula}")
        print(f"Destino del vuelo: {destino}")
        print(f"Fecha del vuelo:  {fechaVuelo}")
        print(f"Hora del vuelo:  {horaVuelo}")
        print(f"Número de asiento: {asientoVuelo}.")
    elif opcionSelect == 0:
        print("Gracias por viajar en Grupo6Airlines. ¡Lo esperamos en su siguiente viaje!")
        break
    else:
        print("Opción invalida. Por favor, seleccione una opcion valida.")
                                #8/3/2024
                                
