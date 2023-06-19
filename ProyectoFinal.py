print("---------------------------")
print("Bienvenido a VuelosDuoc")
print("---------------------------")
filas = 6
columnas = 7
ANormal = 78900
AVip = 240000
descuento = 0
descuento2 = 0

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