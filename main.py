import json

#Gestion de tableros
    #Crear, mostrar, actualizar, eliminar
#Gestion de listas
    #Crear, mostrar, actualizar, eliminar
#Gestion de tarjetas
    #Crear, mostrar, actualizar, eliminar
#Datos almacenados en json
#----
nomArchivo = "Gestor_Tareas.json"
#Validaciones
def enterParaContinuar(mensaje : str = "Enter para continuar..."):
    input(mensaje)

def validarInput(titulo : str, valMin: int = 0, valMax: int = 5):
    while True:
        try:
            rta = int(input(titulo))
            if rta >= valMin and rta <= valMax:
                return rta
            else:
                print(f"Por favor ingrese solo valores permitidos... \nRango de {valMin} a {valMax}")
                enterParaContinuar()
        except:
            enterParaContinuar("ESTA MAL, INTENTALO DE NUEVO")

def validarInput(titulo : str, valMin: int = 0, valMax: int = 5):
    while True:
        try:
            rta = int(input(titulo))
            if rta >= valMin and rta <= valMax:
                return rta
            else:
                print(f"Por favor ingrese solo valores permitidos... \nRango de {valMin} a {valMax}")
                enterParaContinuar()
        except:
            enterParaContinuar("OIGA ESTA MAL, INTENTALO DE NUEVO")

"""
nuevoId = max([b["codigo"] for b in lista], default=0) + 1
    datosBoletos = [
        {"mensaje": "👤 Ingresa tu nombre:\n", "type": "texto"},
        {"mensaje": "💵 ¿Cuánto deseas apostar? (mínimo $1.000):\n", "type": "dinero"}
    ]
    datos = solicitarDatos(datosBoletos)
    dineroDisponible = datos[1]

    boletosComprados = seleccionBoletos(dineroDisponible)

    nuevoUsuario = boleto(nuevoId, datos[0], datos[1])
    nuevoUsuario["boletos"] = boletosComprados

    loteria["boletos"].append(nuevoUsuario)
    print("✅ Datos registrados correctamente.")
    print("-------------------------------------")

"""
def solicitarDatos(campos:list):
    respuesta = []
    for c in campos:
        if c["type"] == "entero":
            respuesta.append(validarInput(c["titulo"], 1 , 100))
        elif c["type"] == "texto":
            respuesta.append(input(c["titulo"]))
    return respuesta

def tablero(codigo: int, nombre: str):
    return {"codigo": codigo, "nombre": nombre}


#MENUS
menu = """
,---.    ,---.    .-''-.  ,---.   .--.  ___    _ 
|    \  /    |  .'_ _   \ |    \  |  |.'   |  | |
|  ,  \/  ,  | / ( ` )   '|  ,  \ |  ||   .'  | |
|  |\_   /|  |. (_ o _)  ||  |\_ \|  |.'  '_  | |
|  _( )_/ |  ||  (_,_)___||  _( )_\  |'   ( \.-.|
| (_ o _) |  |'  \   .---.| (_ o _)  |' (`. _` /|
|  (_,_)  |  | \  `-'    /|  (_,_)\  || (_ (_) _)
|  |      |  |  \       / |  |    |  | \ /  . \ /
'--'      '--'   `'-..-'  '--'    '--'  ``-'`-'' 

1. Gestion de tableros
2. Gestion de listas
3. Gestion de tarjetas 
4. Cargar datos
5. ❌ Salir  
"""
submenu = """
Elige
1.Crear
2.Visualizar
3.Actualizar
4.Eliminar
5.❌ Salir  
"""
#Creación de biblioteca
tareas = {
    "tableros" : [],
    "listas":[],
    "tarjetas":[]
}

#listas
def listarTableros():
    print("\n LISTADO DE TABLEROS\n")
    for tablero in tareas["tableros"]:
        print(f"{tablero['codigo']} {tablero['nombre']}\n")
    enterParaContinuar()
def listarListas():
    print("\n LISTADO DE LISTAS\n")
    for lista in tareas["listas"]:
        print(f"{lista['codigo']} {lista['nombre']}\n")
    enterParaContinuar()
def listarTarjetas():
    print("\n LISTADO DE TARJETAS\n")
    for tarjeta in tareas["tarjetas"]:
        print(f"{tarjeta['codigo']} {tarjeta['nombre']}\n")
    enterParaContinuar()
# CRUD tableros
encontrado = False
cancelado = False
def gestionarTablero():
    while True:
        
        print("GESTION DE TABLEROS")
        print(submenu)
        opc = validarInput("Seleccione una opcion: \n", valMin=1, valMax=5)
        if opc == 1:
            lista = tareas["tableros"]
            nuevoId = max([b["codigo"] for b in lista], default=0) + 1
            datosTablero = [ 
                    {"titulo":"Ingrese el Nombre del tablero\n", "type": "texto"}
                ]
            datos = solicitarDatos(datosTablero)
            nuevoTablero = tablero(nuevoId, datos[0])
            #Guardamos en tareas
            tareas["tableros"].append(nuevoTablero)
            print("✅ ¡Tablero registrado exitosamente!")
            print(tareas["tableros"])
        elif opc == 2:
            listarTableros()
        elif opc == 3:
            listarTableros()
            nomTab = input("🔍 Indica el nombre del tablero que deseas actualizar: ")
            for t in tareas["tableros"]:
                if t["nombre"] == nomTab:
                    print(f"📖 Tablero actual: {t}")
                    campos = [
                        {"titulo":"Ingrese el nuevo Nombre del tablero\n", "type": "texto"}
                    ]
                    datos = solicitarDatos(campos)

                    t["nombre"] = datos[0]
                    print("✅ ¡Tablero actualizado exitosamente!")
                    encontrado = True
                    break

            if not encontrado:
                print("❌ Tablero no encontrado.")
        elif opc == 4:
            listarTableros()
            nomTab = input("🔍 Indica el nombre del tablero que deseas eliminar: ")
            for t in tareas["tableros"]:
                if t["nombre"] == nomTab:
                    print(f"Tablero actual: {t}")
                    confirma = input("⚠️ ¿Estas seguro de eliminarlo? S o N\n")
                    if confirma.upper() == "N":
                        print("❎ Se cancela eliminación")
                        cancelado = True
                        break
                    tareas["tableros"].remove(t)
                    print("✅ Tablero eliminado.")
                    encontrado = True
                    break

            if not encontrado and not cancelado:
                print("❌ Tablero no encontrado.")
        elif opc == 5:
            enterParaContinuar()
            break
        else:
            enterParaContinuar("ESTA MAL, INTENTALO DE NUEVO")

#CRUD GESTION DE LISTAS
def gestionListas():
    while True:
        print("GESTION DE LISTAS")
        print(submenu)
        opc = validarInput("Seleccione una opcion: \n", valMin=1, valMax=5)
        if opc == 1:
            if not tareas["tableros"]:
                print("​⚠️ No hay tableros creados aun.")
                return
           
            listaI = tareas["listas"]
            nuevoId = max([b["codigo"] for b in listaI], default=0) + 1
            datosLista = [ 
                    {"titulo":"Ingrese el Nombre de la Lista\n", "type": "texto"}
                ]
            datos = solicitarDatos(datosLista)
            nuevaLista = tablero(nuevoId, datos[0])
            #Guardamos en tareas
            tareas["listas"].append(nuevaLista)
            print("✅ ¡Lista registrada exitosamente!")
            print(tareas["listas"])
        elif opc == 2:
            print("Aun no se puede")
            listarListas()
        elif opc == 3:
            listarListas()
            nomTab = input("🔍 Indica el nombre de la Lista que deseas actualizar: ")
            for t in tareas["listas"]:
                if t["nombre"] == nomTab:
                    print(f"📖 Lista actual: {t}")
                    campos = [
                        {"titulo":"Ingrese el nuevo Nombre de la Lista\n", "type": "texto"}
                    ]
                    datos = solicitarDatos(campos)

                    t["nombre"] = datos[0]
                    print("✅ ¡Lista actualizado exitosamente!")
                    encontrado = True
                    break

            if not encontrado:
                print("❌ Lista no encontrado.")
        elif opc == 4:
            listarListas()
            nomTab = input("🔍 Indica el nombre de la Lista que deseas eliminar: ")
            for t in tareas["listas"]:
                if t["nombre"] == nomTab:
                    print(f"Lista actual: {t}")
                    confirma = input("⚠️ ¿Estas seguro de eliminarla? S o N\n")
                    if confirma.upper() == "N":
                        print("❎ Se cancela eliminación")
                        cancelado = True
                        break
                    tareas["listas"].remove(t)
                    print("✅ Lista eliminado.")
                    encontrado = True
                    break

            if not encontrado and not cancelado:
                print("❌ Lista no encontrado.")
        elif opc == 5:
            enterParaContinuar()
            break
        else:
            enterParaContinuar("ESTA MAL, INTENTALO DE NUEVO")

#CRUD GESTION DE TARJETAS
def gestionTarjetas():
    while True:
        print("GESTION DE TARJETAS")
        print(submenu)
        opc = validarInput("Seleccione una opcion: \n", valMin=1, valMax=5)
        if opc == 1:
            if not tareas["listas"]:
                print("​⚠️ No hay listas creadas aun.")
                return
           
            listaI = tareas["tarjetas"]
            nuevoId = max([b["codigo"] for b in listaI], default=0) + 1
            datosTarjeta = [ 
                    {"titulo":"Ingrese el Nombre de la tarjeta\n", "type": "texto"}
                ]
            datos = solicitarDatos(datosTarjeta)
            nuevaTarjeta = tablero(nuevoId, datos[0])
            #Guardamos en tareas
            tareas["tarjetas"].append(nuevaTarjeta)
            print("✅ ¡Tarjeta registrada exitosamente!")
            print(tareas["tarjetas"])
        elif opc == 2:
            print("Todas en general")
            listarTarjetas()
        elif opc == 3:
            listarTarjetas()
            nomTab = input("🔍 Indica el nombre de la Tarjeta que deseas actualizar: ")
            for t in tareas["tarjetas"]:
                if t["nombre"] == nomTab:
                    print(f"Tarjeta actual: {t}")
                    campos = [
                        {"titulo":"Ingrese el nuevo Nombre de la Tarjeta\n", "type": "texto"}
                    ]
                    datos = solicitarDatos(campos)

                    t["nombre"] = datos[0]
                    print("✅ ¡Tarjeta actualizado exitosamente!")
                    encontrado = True
                    break

            if not encontrado:
                print("❌ Tarjeta no encontrado.")
        elif opc == 4:
            listarTarjetas()
            nomTab = input("🔍 Indica el nombre de la Tarjeta que deseas eliminar: ")
            for t in tareas["tarjetas"]:
                if t["nombre"] == nomTab:
                    print(f"Tarjeta actual: {t}")
                    confirma = input("⚠️ ¿Estas seguro de eliminarla? S o N\n")
                    if confirma.upper() == "N":
                        print("❎ Se cancela eliminación")
                        cancelado = True
                        break
                    tareas["tarjetas"].remove(t)
                    print("✅ Tarjeta eliminado.")
                    encontrado = True
                    break

            if not encontrado and not cancelado:
                print("❌ Tarjeta no encontrado.")
        elif opc == 5:
            enterParaContinuar()
            break
        else:
            enterParaContinuar("ESTA MAL, INTENTALO DE NUEVO")

def asignarOrden():
    pass

def guardarDatos(nomArchivo = "Gestor_Tareas.json"):
    with open(nomArchivo,'w',encoding='utf-8') as archivo:
        json.dump(tareas, archivo, indent=4)
        

while True:
    print(menu)
    opc = validarInput("Seleccione una opcion: \n", valMin=1, valMax=5)
    if opc == 1:
        gestionarTablero()
    elif opc == 2:
        gestionListas()
    elif opc == 3:
        gestionTarjetas()
    elif opc == 4:
        guardarDatos()
    elif opc == 5:
        enterParaContinuar("¡Chaooo!")
        break
    else:
        enterParaContinuar("ESTA MAL, INTENTALO DE NUEVO")