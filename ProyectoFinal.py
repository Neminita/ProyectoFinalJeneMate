print("---------------------------")
print("Bienvenido a VuelosDuoc")
print("---------------------------")
filas = 6
columnas = 7
ANormal = 78900
AVip = 240000
descuento = 0
descuento2 = 0
l_rut = []
l_nom = []
l_tel = []
l_ban = []
l_asiento = []
asientos = [[(i * columnas + j + 1) for j in range(columnas)] for i in range(filas)]


# Definicion de Funcion para crear el menú de asientos y sus arreglos
def Masientos():
    for fila in asientos:
        print("|", end="")
        for asiento in fila:
            if asiento == "x":
                print("   x", end="")
            else:
                print(f"{asiento:4}", end="")
        print("|")


# Datos de usuario para ingresar en normal.


def UsuarioNormal():
    global l_rut, l_ban, l_nom, l_tel, l_asiento
    print("Ingrese sus datos correspondientes. ")
    global RutUs, NomUs, TelefUs, BancoUs
    RutUs = str(input("Ingrese su rut sin guíon ni puntos: "))
    l_rut.append(RutUs)
    NomUs = str(input("Ingrese su nombre completo: "))
    l_nom.append(NomUs)
    TelefUs = int(input("Ingrese su teléfono de contacto: "))
    l_tel.append(TelefUs)
    BancoUs = str(input("Ingrese el nombre de su banco: "))
    l_ban.append(BancoUs)
    if (
        BancoUs == "BancoDuoc"
        or BancoUs == "Bancoduoc"
        or BancoUs == "bancoDuoc"
        or BancoUs == "BancoDuoc"
        or BancoUs == "BANCODUOC"
        or BancoUs == "bancoduoc"
    ):
        descuento = (ANormal) * 0.15
        print("El valor NORMAL de éste pasaje es:", (ANormal - descuento))
    else:
        descuento = 0
        print("El valor de éste pasaje es:", (ANormal))


# Datos de usuario para ingresar en Vip.
def UsuarioVip():
    global l_rut, l_ban, l_nom, l_tel, l_asiento
    print("Ingrese sus datos correspondientes. ")
    global RutUs, NomUs, TelefUs, BancoUs
    RutUs = str(input("Ingrese su rut sin guíon ni puntos: "))
    l_rut.append(RutUs)
    NomUs = str(input("Ingrese su nombre completo: "))
    l_nom.append(NomUs)
    TelefUs = int(input("Ingrese su teléfono de contacto: "))
    l_tel.append(TelefUs)
    BancoUs = str(input("Ingrese el nombre de su banco: "))
    l_ban.append(BancoUs)

    if (
        BancoUs == "BancoDuoc"
        or BancoUs == "Bancoduoc"
        or BancoUs == "bancoDuoc"
        or BancoUs == "BancoDuoc"
        or BancoUs == "BANCODUOC"
        or BancoUs == "bancoduoc"
    ):
        descuento = (AVip) * 0.15
        print("El valor VIP de éste pasaje es:", (AVip - descuento))
    else:
        descuento = 0
        print("El valor de éste pasaje es:", (ANormal))
    # Primera interfaz de menú.


def menu():
    while True:
        try:
            cont = 0
            print("Elija una opcion porfavor")
            print("1. Ver asientos disponibles.")
            print("2. Comprar asiento.")
            print("3. Anular vuelo.")
            print("4. Modificar datos.")
            print("5. Salir.")
            OpMenu = int(input())
            if OpMenu == 1:
                Masientos()
            elif OpMenu == 2:
                Masientos()
                eleccion = int(input("Seleccione un asiento: "))
                if eleccion in [asiento for fila in asientos for asiento in fila]:
                    for i, fila in enumerate(asientos):
                        for j, asiento in enumerate(fila):
                            if asiento == eleccion:
                                asientos[i][j] = "   X"
                                break                
                if eleccion >= 1 and eleccion <= 30:
                    l_asiento.append(eleccion)
                    print(
                        """
                ¿Quisiera confirmar su compra?
                1.Si
                2.No
                """
                    )
                    confus = int(input())
                    if confus == 1:
                        UsuarioNormal()

                    else:
                        cont = 0
                elif eleccion > 30 and eleccion <= 42:
                    l_asiento.append(eleccion)
                    print(
                        """
                ¿Quisiera confirmar su compra?
                1.Si
                2.No
                """
                    )
                    confus = int(input())
                    if confus == 1:
                        UsuarioVip()
                    else:
                        cont = 0
                else:
                    print("El valor no se ha encontrado.")
            elif OpMenu == 3:
                print(
                    """
                ¿Quisiera Anular envío?
                1.Si
                2.No
                """
                )
                anulacion = int(input())
                if anulacion == 1:
                    print("Su anulación ha sido exitosa!")
                    l_nom.remove(NomUs)
                    l_asiento.remove(asiento)
                    l_ban.remove(BancoUs)
                    l_rut.remove(RutUs)
                    l_tel.remove(TelefUs)

                else:
                    print("Se ha cancelado su anulación!")
                    
            elif OpMenu == 4:
                print("Modificación de datos. ")
                nom = (input("Porfavor ingrese su nombre: "))
                
                if nom in l_nom:
                    eleccion = int(input("Porfavor ingrese su asiento: "))
                    if eleccion in l_asiento: # Verifica que la variable elección esté dentro de la lista de asientos.
                        while True:
                            print(""" 
                                        Modificación de datos
                                1) Modificar nombre.
                                2) Modificar telefono.
                                3) Listar datos.
                                4) Salir.
                                    
                                """)
                            op = int(input("Ingrese una opción valida: "))

                            if op == 1:
                                print("Lista de nombres: ", l_nom)
                                nom1 = input("Ingrese nombre a modificar: ")
                                if nom1 in l_nom:
                                    l_nom.remove(nom1)
                                    nom2 = input("Ingrese nombre nuevo: ")
                                    l_nom.append(nom2)
                                    print("Nombre modificado correctamente.")
                                else:
                                    print("Ingrese un nombre valido.")
                            elif op == 2:
                                print("Lista de telefonos: ", l_tel)
                                tel1 = int(input("Ingrese telefono a modificar: "))
                                if tel1 in l_tel:
                                    l_tel.remove(tel1)
                                    tel2 = int(input("Ingrese telefono nuevo: "))
                                    l_tel.append(tel2)
                                else:
                                    print("Ingrese un telefono valido.")
                            elif op == 3:
                                print("Datos")
                                print("Lista de asientos reservados: ", l_asiento)
                                print("Lista de numeros: ", l_tel)
                                print("Lista de nombres: ", l_nom)
                                print("Lista de bancos: ", l_ban)

                            
                if eleccion >= 1 and eleccion <= 30:
                                l_asiento.append(eleccion)
                                print(
                        """
                ¿Quisiera confirmar su compra?
                1.Si
                2.No
                """
                    )
                confus = int(input())
                if confus == 1:
                        UsuarioNormal()

                else:
                    cont = 0
            elif eleccion > 30 and eleccion <= 42:
                    l_asiento.append(eleccion)
                    print(
                        """
                ¿Quisiera confirmar su compra?
                1.Si
                2.No
                """
                    )
                    confus = int(input())
                    if confus == 1:
                        UsuarioVip()
                    else:
                        cont = 0
            else:
                print("El valor no se ha encontrado.")
        except ValueError:
            print("INGRESE OPCIÓN VALIDA")
