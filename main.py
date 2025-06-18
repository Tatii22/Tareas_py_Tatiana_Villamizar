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

def cargarDatos():
    with open(nomArchivo, 'r') as archivo:
        return json.load(archivo)

def cargarDatos():
    try:
        with open(nomArchivo, 'r') as archivo:
            return json.load(archivo)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        return {"tableros": []} 
def guardarDatos():
    with open(nomArchivo, 'w') as archivo:
        json.dump(tareas, archivo, indent=4)
    print("💾 Datos guardados correctamente.")
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

def lista(nomTareas : str, codigo: int, nombre: str):
    return {"Nombre tablero": nomTareas, "codigo": codigo, "nombre": nombre}

def tarjeta(nomTareas : str, codigo: int, nombre: str):
    return {"Nombre lista": nomTareas, "codigo": codigo, "nombre": nombre}


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
    print("\n=== TABLEROS ===")
    for t in tareas["tableros"]:
        print(f"🧩 Código: {t['codigo']} - Nombre: {t['nombre']}")

def listarListas():
    print("\n=== LISTAS ===")
    for l in tareas["listas"]:
        print(f"📋 Código: {l['codigo']} - Nombre: {l['nombre']} - Tablero: {l['Nombre tablero']}")

def listarTarjetas():
    print("\n=== TARJETAS ===")
    for t in tareas["tarjetas"]:
        print(f"📌 Código: {t['codigo']} - Nombre: {t['nombre']} - Lista: {t['Nombre lista']}")



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
            guardarDatos()
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
                    guardarDatos()
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
                    guardarDatos()
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
        print("\nGESTION DE LISTAS")
        print(submenu)
        opc = validarInput("Seleccione una opcion: \n", valMin=1, valMax=5)
        if opc == 1:
            if not tareas["tableros"]:
                print("​⚠️ No hay tableros creados aun.")
                return
                 
            listarTableros()
            nomTab = input("🔍 Indica el nombre del tablero que deseas asignar a la lista: ")
            for t in tareas["tableros"]:
                if t["nombre"] == nomTab:
                    print(f"📖 Tablero actual: {t}")           
                    listaI = tareas["listas"]
                    nuevoId = max([b["codigo"] for b in listaI], default=0) + 1
                    datosLista = [ 
                            {"titulo":"Ingrese el Nombre de la Lista\n", "type": "texto"}
                        ]
                    datos = solicitarDatos(datosLista)
                    nuevaLista = lista(nomTab, nuevoId, datos[0])
                    #Guardamos en tareas
                    tareas["listas"].append(nuevaLista)
                    print("✅ ¡Lista registrada exitosamente!")
                    print(tareas["listas"])
                    guardarDatos()
                    break
        elif opc == 2:
            listarListas()
        elif opc == 3:
            listarListas()
            nomList = input("🔍 Indica el nombre de la Lista que deseas actualizar: ")
            for t in tareas["listas"]:
                if t["nombre"] == nomList:
                    print(f"📖 Lista actual: {t}")
                    campos = [
                        {"titulo":"Ingrese el nuevo Nombre de la Lista\n", "type": "texto"}
                        ]
                    datos = solicitarDatos(campos)
                    t["nombre"] = datos[0]
                    print("✅ ¡Lista actualizado exitosamente!")
                    encontrado = True
                    guardarDatos()
                    break

            if not encontrado:
                print("❌ Lista no encontrado.")
        
        elif opc == 4:
            listarListas()
            nomList = input("🔍 Indica el nombre de la Lista que deseas eliminar: ")
            for t in tareas["listas"]:
                if t["nombre"] == nomList:
                    print(f"Lista actual: {t}")
                    confirma = input("⚠️ ¿Estas seguro de eliminarla? S o N\n")
                    if confirma.upper() == "N":
                        print("❎ Se cancela eliminación")
                        cancelado = True
                        break
                    tareas["listas"].remove(t)
                    print("✅ Lista eliminado.")
                    encontrado = True
                    guardarDatos()
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
            
            listarListas()
            nomList = input("🔍 Indica el nombre de la Lista que deseas asignar: ")
            for t in tareas["listas"]:
                if t["nombre"] == nomList:
                    listaI = tareas["tarjetas"]
                    nuevoId = max([b["codigo"] for b in listaI], default=0) + 1
                    datosTarjeta = [ 
                            {"titulo":"Ingrese el Nombre de la tarjeta\n", "type": "texto"}
                        ]
                    datos = solicitarDatos(datosTarjeta)
                    nuevaTarjeta = tarjeta(nomList,nuevoId, datos[0])
                    #Guardamos en tareas
                    tareas["tarjetas"].append(nuevaTarjeta)
                    print("✅ ¡Tarjeta registrada exitosamente!")
                    print(tareas["tarjetas"])
                    guardarDatos()
                    break
        elif opc == 2:
            print("Todas en general")
            listarTarjetas()
        elif opc == 3:
            listarTarjetas()
            nomTar = input("🔍 Indica el nombre de la Tarjeta que deseas actualizar: ")
            for t in tareas["tarjetas"]:
                if t["nombre"] == nomTar:
                    print(f"Tarjeta actual: {t}")
                    campos = [
                        {"titulo":"Ingrese el nuevo Nombre de la Tarjeta\n", "type": "texto"}
                    ]
                    datos = solicitarDatos(campos)

                    t["nombre"] = datos[0]
                    print("✅ ¡Tarjeta actualizado exitosamente!")
                    encontrado = True
                    guardarDatos()
                    break

            if not encontrado:
                print("❌ Tarjeta no encontrado.")
        elif opc == 4:
            listarTarjetas()
            nomTar = input("🔍 Indica el nombre de la Tarjeta que deseas eliminar: ")
            for t in tareas["tarjetas"]:
                if t["nombre"] == nomTar:
                    print(f"Tarjeta actual: {t}")
                    confirma = input("⚠️ ¿Estas seguro de eliminarla? S o N\n")
                    if confirma.upper() == "N":
                        print("❎ Se cancela eliminación")
                        cancelado = True
                        break
                    tareas["tarjetas"].remove(t)
                    print("✅ Tarjeta eliminado.")
                    encontrado = True
                    guardarDatos()
                    break

            if not encontrado and not cancelado:
                print("❌ Tarjeta no encontrado.")
        elif opc == 5:
            enterParaContinuar()
            break
        else:
            enterParaContinuar("ESTA MAL, INTENTALO DE NUEVO")

  

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