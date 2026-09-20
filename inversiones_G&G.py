# en el menu de opciones principales agg opcion para que el usuario valore con estrellas el trato por parte del sistema de la tienda y darle opcioon de q escriba reseña y guardar con metodos futuros
# PREGUNTARLE DE LA RESEÑA CADA QUE EL USUARIO SELECCIONA COMPRAR O DEMAS OPCIONES
# continuar con la logica de las opciones en el modo supervisor
# AÑADIR OPCION EN ESTE SISTEMA DE VER EL NOMBRE DE LA PERONA SU RESEÑA Y ESTRELLITA Y GUARDAR TODO ESO EN .txt
# añadir recordatorios en partes especificas del programa
# AGG CON LA LIBRERIA RANDOM DIAS RANDOMS PARA PROMOCIONES COMO SER ENVIO A SPS
# A CHOLOMA O OTRAS CIUDADES DESCUENTOS ALEATORIOS USANDO DICCIONARIOS
#  

import time
import os
import random


historial_compras = []
carrito_compras = []


def valoracion_reseña():
  print("\ntomate un minuto de tu tiempo para evaluar el sistema de esta tienda")
  estrellas = [
    "⭐️",
    "⭐️⭐️",
    "⭐️⭐️⭐️",
    "⭐️⭐️⭐️⭐️",
    "⭐️⭐️⭐️⭐️⭐️"
  ]
  for i,estrella in enumerate(estrellas,start=1):
    print(f"{i} > {estrella}")
  while True:
    try:
      calificacion_usuario = int(input("escribe el numero de estrella  que le das:  "))
      if calificacion_usuario   <1 or calificacion_usuario >5:
        print("ERROR, porfavor ingresa un numero del 1 al 5")
        continue
      print("Consejo:  presiona enter para omitir reseña")
      opinion_usuario = input("escribe una breve opinion:  ")
      # si la opinion del usuario esta vacia poner por defecto "sin opinion"
      if opinion_usuario == "":
        opinion_usuario = "sin opinion"
      print(f"\ncalificacion: {calificacion_usuario} ⭐️")
      print(f"\nopinion: {opinion_usuario}")
      print("\n¡calificacion y opinion enviados exitosamente!")
      print("¡muchas gracias por tu calificacion y opinion! nos ayudara a seguir mejorando nuestro sistema")
      print("para Inversiones G&G es muy importante la opinion de nuestros clientes\n")
      break
    except ValueError:
      print("ERROR en la validacion de puntuacion y reseña intentalo de nuevo")
      print("RECORDATORIO: seleccionar el numero de la estrella con la que calificas")



def guardar_usuarios(nombres):
  with open("usuarios_inversionesG&G.txt", "a", encoding="utf-8") as registros:
    registros.write(f"{nombres}\n")

    
def mod_supervisor():
  clave = "12345AZ"
  intentos = 3
  controlador = True
  while controlador == True:
    clave_usuario = input("\nescribe la clave para ingresar al modo supervisor:  ").strip()
    if clave_usuario == clave:
      print("validando...")
      time.sleep(1)
      print("\n")
      print("="*31)
      print("¡Bienvenido al modo supervisor!")
      print("="*31)
      print("Cargando modo supervisor...\n")
      time.sleep(1.5)
      while True:
        try:
          opciones = [
            "registrar producto",
            "ver inventario",
            "ver usuarios registrados",
            "limpiar registros de 30 dias",
            "salir del modo supervisor"
          ]
          for i, opcion in enumerate(opciones,start=1):
            print(f"{i} > {opcion}")
          opcion_supervior = int(input("numero de opcion:  "))
          if opcion_supervior == 1:
            print("registrar producto")
          elif opcion_supervior == 2:
            print("mostrar inventario")
          elif opcion_supervior == 3:
            print("="*50)
            print("usuarios que ingresaron en los ultimos 30 dias")
            print("="*50)
            # AGG TIPOO SI NO HAY NINGUN NMBRE REGISTRADO IMPRIME SIN USUARIS REGISTRADOS
            with open("usuarios_inversionesG&G.txt", "r", encoding="utf-8") as registros:
              lista_completa =  registros.read()
              print(lista_completa)
          elif opcion_supervior == 4:
            while True:
              try:
                print("")
                borrar_usuarios = int(input("\nselecciona 1 para cancelar 0 para borrar:  "))
                if borrar_usuarios == 1:
                  print("\ncancelado\n")
                  break
                else:
                  with open("usuarios_inversionesG&G.txt", "w", encoding="utf-8") as registros:
                    pass
                  print("\nel registro de usuarios ha sido borrado exitosamente\n")
                  break
              except ValueError:
                print("ERROR, escribe sol lo que se solicita")
                  

                  
          elif opcion_supervior == 5:
            print("saliendo del modo supervisor...")
            time.sleep(1)
            print("cargando menu principal...")
            time.sleep(1)
            controlador = False
            break
          else:
            print("ERROR, escribe el numero de la opcion correspondiente")
        except ValueError:
          print("\nERROR, solo se permiten numeros dependiendo de la opcion que quieres realizar\n")
    else:
      print("validando...")
      time.sleep(1)
      print("clave incorrecta")
      intentos -=1
      print(f"intentos restantes: {intentos}")
      if intentos == 0:
        print("maximo de intentos alcanzado")
        print("cargando menu principal...")
        time.sleep(1)
        controlador = False



# ==========================================
# 2. FUNCIONES DE CATÁLOGOS Y COMPRA
# ==========================================
def inventario_completo():
    inventario = {
        "camisas de futbol": {
            "argentina": [1200, "XL, M, L, X"],
            "brasil": [1300, "XL, M, X, L"],
            "francia": [1200, "XL, X, L"],
            "marruecos": [1300, "XL, M, X"],
            "uruguay": [700, "M, XL, L"],
            "españa": [1300, "XL, M, L"],
            "mexico": [900, "XL, M, L"],
            "colombia": [700, "XL, M, S"],
            "inglaterra": [1300, "XL, M, S"],
            "ecuador": [800, "XL, X, L"],
            "qatar": [900, "XL, M, L"]
        },
        "pantalones": {
            "skinny": [1200, "36, 40, 50, 16"],
            "slim fit": [1100, "36, 40, 16, 22"],
            "regular": [400, "45, 25"],
            "relaxed": [2200, "41, 36, 21"],
            "baggy": [4000, "40, 47, 10"],
            "pantapri": [2200, "46, 29, 19"]
        },
        "tenis": {
            "nike air force": [3500, "32, 34, 10, 29"],
            "adidas ultra boost": [4500, "34, 28, 33"],
            "jordan 1 retro high": [7800, "34, 48, 30"],
            "puma": [2500, "34, 51, 45"],
            "new balance": [5200, "29, 33, 50"]
        },
        "zapatos": {
            "lucchese": [3700, "40, 29, 26"],
            "ariat": [4900, "48, 38, 27"],
            "justin boost": [4500, "32, 35, 44"],
            "tony lama": [4600, "48, 39, 30"],
            "corral boost": [3000, "32, 34, 27"]
        },
        "gorras": {
            "new era": [1200, "N/A"],
            "goorin bros": [1500, "N/A"],
            "von dutch": [900, "N/A"],
            "carhartt wip": [1000, "N/A"],
            "47 brand": [1400, "N/A"],
            "supreme": [1700, "N/A"],
            "adidas": [1200, "N/A"],
            "under": [3500, "N/A"]
        }
    }
    return inventario


def comprar(nombre_articulo, precio_articulo, talla_articulo="N/A"):
    global carrito_compras
    interruptor = False
    while not interruptor:
        desea_comprar = input("¿Deseas añadirlo al carrito? (si/no): ").lower().strip()
        if desea_comprar == "si":
            articulo = {
                "nombre": nombre_articulo,
                "precio": precio_articulo,
                "talla": talla_articulo,
            }
            carrito_compras.append(articulo)
            print("\n¡Añadido al carrito exitosamente!\n")
            valoracion_reseña()
            print("Ve a la opción número 6 para ver lo que tienes en el carrito.")
            print("Cargando menú principal...")
            time.sleep(1.9)
            interruptor = True
        elif desea_comprar == "no":
            print("\nNo hay problema, el artículo sigue disponible por si cambias de opinión.")
            print("Cargando menú principal...")
            time.sleep(1.9)
            interruptor = True
        else:
            print("ERROR: escribe solo 'si' o 'no'.")


# ==========================================
# 3. FUNCIONES SECUNDARIAS
# ==========================================


def Calcular_presupuesto():
    try:
        presupuesto_cliente = int(input("Escribe tu presupuesto en HNL: "))
        if presupuesto_cliente <= 500:
            print("¡Con tu presupuesto actual puedes llevarte varios artículos!")
        else:
            print("¡Excelente! Te alcanza para explorar casi toda la colección.")
        
        respuesta_cliente = input("¿Desea continuar en la tienda? (si/no): ").lower()
        if respuesta_cliente == "si":
            print("Redirigiendo a menú principal...")
            time.sleep(1.5)
        elif respuesta_cliente == "no":
            print("Por favor, elige la opción 9 en el menú principal para salir correctamente.")
        else:
            print("ERROR: tu respuesta debe ser solo si o no.")
    except ValueError:
        print("ERROR: escribe números enteros.")


# ==========================================
# 4. BUCLE PRINCIPAL (El corazón del sistema)
# ==========================================

tienda = inventario_completo()
corriendo = True 

# ==========================================
# 1. PANTALLA DE INICIO Y LOGIN (OPCIONAL)
# ==========================================
os.system("cls" if os.name == "nt" else "clear")
print("--- [ INVERSIONES G&G - INICIANDO SISTEMA ] ---")
mensaje = "\nConectando con base de datos...\n"
for caracter in mensaje:
    print(caracter, end='', flush=True)
    time.sleep(0.05)
time.sleep(1)
nombre_apellido_usuario = input("\nnombre y apellido:  ")
guardar_usuarios(nombre_apellido_usuario)
print("XDDDDDDDD")
print(f"\n¡Bienvenido a inversiones G&G {nombre_apellido_usuario}!\n")
time.sleep(0.5)
print("cargando...\n")
time.sleep(1)

while corriendo:
    menu_principal = [
        "Ver y comprar artículos", 
        "Quién es el dueño de Inversiones G&G", 
        "Ver ofertas del día", 
        "Calcular presupuesto", 
        "Contactar a soporte", 
        "Ver carrito", 
        "Buscador de artículos", 
        "Historial de compras",
        "ingresar al modo supervisor",
        "añadir calificacion y opinion",
        "Salir"
    ]
    
    print("="*40)
    print("          MENÚ PRINCIPAL")
    print("="*40)
    for i, menu in enumerate(menu_principal, start=1):
        print(f"{i}. {menu}")
    
    while True:
        try:
            opcion = int(input("\nEscribe el número de la opción que deseas realizar: "))
            break
        except ValueError:
            print("ERROR: escribe solo números.")
            time.sleep(1)

    # OPCIÓN 1: COMPRAR ARTÍCULOS
    if opcion == 1:
        print("="*30)
        print("CATEGORÍAS DISPONIBLES")
        print("="*30)
        sub_menu = ["Camisas de fútbol", "Pantalones jeans", "Tenis deportivos", "Zapatos", "Gorras", "Volver al menú principal"]
        for i, sub_categoria in enumerate(sub_menu, start=1):
            print(f"{i}. {sub_categoria}")
        
        while True:
            try:
                sub_opcion = int(input("\n¿Qué artículo te interesa?: "))
                break
            except ValueError:
                print("ERROR: escribe solo números.")
                time.sleep(1)
            
        # CAMISAS
        if sub_opcion == 1:
            print("="*40)
            print("    CAMISAS DE FÚTBOL DISPONIBLES")
            print("="*40)
            catalogo_camisas = tienda["camisas de futbol"]
            for i, (producto, datos) in enumerate(catalogo_camisas.items(), start=1):
                valor_precio = datos[0]
                valor_talla = datos[1]
                print(f"{i}. Camisa de {producto.capitalize()} | Precio: {valor_precio} HNL | Tallas: {valor_talla}")
            
            lista_nombres_camisas = list(catalogo_camisas.keys())  
            eleccion_valida = False         
            while not eleccion_valida:
                try:
                    camisa_elegida = int(input("\nEscribe el número de camisa que deseas comprar: ")) 
                    if 1 <= camisa_elegida <= len(lista_nombres_camisas):
                        seleccion_final = lista_nombres_camisas[camisa_elegida - 1]
                        precio_final = catalogo_camisas[seleccion_final][0]
                        tallas_disponibles_camisas = catalogo_camisas[seleccion_final][1]          
                        print(f"\n¡Excelente! Has seleccionado: Camisa de {seleccion_final.capitalize()} por {precio_final} HNL")
                        eleccion_valida = True
                    else:
                        print("ERROR: Ese número no existe. Inténtalo de nuevo.")
                except ValueError:
                    print("ERROR: escribe solo números.")

            camisa_talla_valida = False
            while not camisa_talla_valida:
                print(f"\nTallas disponibles para camisa de {seleccion_final}: {tallas_disponibles_camisas}\n")
                talla_elegida = input("\nAntes de añadir al carrito, selecciona la talla: ").upper()
                if talla_elegida in tallas_disponibles_camisas:
                    print("\nVerificando si la talla está disponible...\n")
                    time.sleep(1.2)
                    print("¡Talla disponible!\n")
                    comprar(seleccion_final, precio_final, talla_elegida)
                    camisa_talla_valida = True
                else:
                    print("Talla no disponible o inválida. Inténtalo de nuevo.")

        # PANTALONES
        elif sub_opcion == 2:
            print("="*40)
            print("    PANTALONES DISPONIBLES EN TIENDA")
            print("="*40)
            catalogo_pantalones = tienda["pantalones"]
            for i, (pantalon, datos) in enumerate(catalogo_pantalones.items(), start=1):
                valor_precio = datos[0]
                valor_talla = datos[1]
                print(f"{i}. Pantalón {pantalon.capitalize()} | Precio: {valor_precio} HNL | Tallas: {valor_talla}")
            
            lista_nombres_pantalones = list(catalogo_pantalones.keys())
            eleccion_valida_pantalon = False
            while not eleccion_valida_pantalon:
                try:
                    pantalon_elegido = int(input("\nSelecciona el número del pantalón que deseas: "))
                    if 1 <= pantalon_elegido <= len(lista_nombres_pantalones):
                        seleccion_final = lista_nombres_pantalones[pantalon_elegido - 1]
                        precio_final = catalogo_pantalones[seleccion_final][0]
                        tallas_disponibles_pantalones = catalogo_pantalones[seleccion_final][1]
                        print(f"\n¡Excelente! Has seleccionado: {seleccion_final.capitalize()} por {precio_final} HNL") 
                        eleccion_valida_pantalon = True
                    else:
                        print("ERROR: ese número no existe.")
                except ValueError:
                    print("ERROR: escribe solo números.")
                
            pantalon_talla_valida = False
            while not pantalon_talla_valida:
                print(f"Tallas disponibles para {seleccion_final}: {tallas_disponibles_pantalones}")
                talla_valida_pantalon = input("Antes de comprar, selecciona la talla del pantalón: ").upper()
                if talla_valida_pantalon in tallas_disponibles_pantalones:
                    print("Verificando si la talla está disponible...")
                    time.sleep(1.2)
                    print("\n¡Talla disponible!")
                    comprar(seleccion_final, precio_final, talla_valida_pantalon)
                    pantalon_talla_valida = True
                else:
                    print("Talla no disponible o inválida.")

        # TENIS
        elif sub_opcion == 3:
            print("="*40)
            print("    TENIS DISPONIBLES EN TIENDA")
            print("="*40)
            catalogo_tenis = tienda["tenis"]
            for i, (tenis, datos) in enumerate(catalogo_tenis.items(), start=1):
                valor_precio = datos[0]
                valor_talla = datos[1]
                print(f"{i}. {tenis.capitalize()} | Precio: {valor_precio} HNL | Tallas: {valor_talla}")
            
            lista_nombres_tenis = list(catalogo_tenis.keys())
            eleccion_valida_tenis = False
            while not eleccion_valida_tenis:
                try:
                    tenis_elegidos = int(input("\nSelecciona el número de los tenis que deseas: "))
                    if 1 <= tenis_elegidos <= len(lista_nombres_tenis):
                        seleccion_final = lista_nombres_tenis[tenis_elegidos - 1]
                        precio_final = catalogo_tenis[seleccion_final][0]
                        tallas_disponibles = catalogo_tenis[seleccion_final][1]
                        print(f"\n¡Excelente! Has seleccionado: {seleccion_final.capitalize()} por {precio_final} HNL")
                        eleccion_valida_tenis = True
                    else:
                        print("ERROR: ese número no existe.")
                except ValueError:
                    print("ERROR: escribe solo números.")
                
            calzado_valido = False
            while not calzado_valido:
                print(f"\nNúmeros de calzado disponibles para {seleccion_final}: {tallas_disponibles}\n")
                calzado_elegido = input("Antes de continuar, selecciona la talla: ")
                if calzado_elegido in tallas_disponibles:
                    print("\nVerificando si la talla está disponible...\n")
                    time.sleep(1.2)
                    print("¡Calzado disponible!")
                    comprar(seleccion_final, precio_final, calzado_elegido)
                    calzado_valido = True
                else:
                    print("\nCalzado no disponible. Por favor intenta de nuevo.\n")

        # ZAPATOS
        elif sub_opcion == 4:
            print("="*40)
            print("    ZAPATOS DISPONIBLES EN TIENDA")
            print("="*40)
            catalogo_zapatos = tienda["zapatos"]
            for i, (zapato, datos) in enumerate(catalogo_zapatos.items(), start=1):
                valor_precio = datos[0]
                valor_talla = datos[1]
                print(f"{i}. {zapato.capitalize()} | Precio: {valor_precio} HNL | Tallas: {valor_talla}")
            
            lista_nombres_zapatos = list(catalogo_zapatos.keys())
            seleccion_valida_zapatos = False
            while not seleccion_valida_zapatos:
                try:
                    zapatos_elegidos = int(input("\nSelecciona el número del zapato que quieres: "))
                    if 1 <= zapatos_elegidos <= len(lista_nombres_zapatos):
                        seleccion_final = lista_nombres_zapatos[zapatos_elegidos - 1]
                        precio_final = catalogo_zapatos[seleccion_final][0]
                        tallas_disponibles = catalogo_zapatos[seleccion_final][1]
                        print(f"\n¡Excelente! Has seleccionado {seleccion_final.capitalize()} por {precio_final} HNL")
                        seleccion_valida_zapatos = True
                    else:
                        print("\nERROR: ese número no existe.")
                except ValueError:
                    print("ERROR: escribe solo números.")

            calzado_valido_zapatos = False
            while not calzado_valido_zapatos:
                print(f"\nNúmeros de calzado disponibles para {seleccion_final}: {tallas_disponibles}\n")
                eleccion_talla_zapato = input("Antes de continuar, elige la talla del zapato: ")
                if eleccion_talla_zapato in tallas_disponibles:
                    print("Verificando si la talla está disponible...")
                    time.sleep(1.2)
                    print("¡Número de calzado disponible!")
                    comprar(seleccion_final, precio_final, eleccion_talla_zapato)
                    calzado_valido_zapatos = True
                else:
                    print("Talla no disponible.")

        # GORRAS
        elif sub_opcion == 5:
            print("="*40)
            print("    GORRAS DISPONIBLES EN TIENDA")
            print("="*40)
            catalogo_gorras = tienda["gorras"]
            for i, (gorra, datos) in enumerate(catalogo_gorras.items(), start=1):
                valor_precio = datos[0]
                print(f"{i}. Gorra {gorra.capitalize()} | Precio: {valor_precio} HNL")
            
            lista_nombres_gorras = list(catalogo_gorras.keys())
            eleccion_valida_gorras = False
            while not eleccion_valida_gorras:
                try:
                    seleccion_gorra = int(input("\nSelecciona el número de la gorra que quieres: "))
                    if 1 <= seleccion_gorra <= len(lista_nombres_gorras):
                        seleccion_final = lista_nombres_gorras[seleccion_gorra - 1]
                        precio_final = catalogo_gorras[seleccion_final][0]
                        print(f"\n¡Excelente! Has seleccionado: {seleccion_final.capitalize()} por {precio_final} HNL")
                        comprar(seleccion_final, precio_final)
                        eleccion_valida_gorras = True
                    else:
                        print("Número inválido, inténtalo de nuevo.")
                except ValueError:
                    print("ERROR: solo puedes escribir números.")

    # OPCIONES SECUNDARIAS
    elif opcion == 2:
        print("\nEl dueño y jefe legítimo de Inversiones GG es Alexis Gonzalez.")

    elif opcion == 3:
        print("\nOferta del día: ¡Hoy el envío es GRATIS en toda Choloma y San Pedro Sula!")

    elif opcion == 4:
        Calcular_presupuesto()

    elif opcion == 5:
        print("\nPuedes contactarte con soporte a los siguientes números:")
        contactos_soporte = [
          "+504 9788-8113",
          "+504 8768-0627",
          "+504 9484-1133"
        ]
        for contacto in contactos_soporte:
          print(f"> {contacto}")

    elif opcion == 6:
        print("=" * 40)
        print("          TU CARRITO DE COMPRAS")
        print("=" * 40)
        if len(carrito_compras) == 0:
            print("Tu carrito está vacío. ¡Anímate a comprar algo!\n")
            time.sleep(1)
        else:
            total_pagar = 0
            for indice, item in enumerate(carrito_compras, start=1):
                print(f"{indice}. {item['nombre'].capitalize()} // Talla: {item['talla']} // Precio: {item['precio']} HNL")
                total_pagar += item["precio"]
            print("-" * 40)
            print(f"TOTAL A PAGAR: {total_pagar} HNL")
            print("=" * 40)
            
            while True:
                pagar = input("¿Deseas pagar? (si/no): ").lower().strip()
                if pagar == "si":
                    num_factura = random.randint(1000, 9999)
                    factura = {
                        "num_factura": num_factura,
                        "productos": list(carrito_compras),
                        "total": total_pagar
                    }
                    historial_compras.append(factura)
                    carrito_compras.clear()
                    
                    print(f"\n¡Pago realizado con éxito! Factura #{num_factura} generada.")
                    print("Puedes consultar tus facturas en la Opción 8 (Historial de compras).")
                    print("Redirigiendo al menú principal...")
                    time.sleep(2)
                    break
                elif pagar == "no":
                    print("Redirigiendo al menú principal...")
                    time.sleep(1)
                    break
                else:
                    print("Error: escribe solo 'si' o 'no'.")

    # OPCIÓN 7: BUSCADOR DE ARTÍCULOS
    elif opcion == 7:
        articulos_disponibles = ["camisas de futbol", "pantalones", "tenis", "zapatos", "gorras", "salir al menu principal"]
        print("=" * 40)
        print("        BUSCADOR DE ARTÍCULOS")
        print("=" * 40)
        for i, articulo in enumerate(articulos_disponibles, start=1):
            print(f"{i} > {articulo.capitalize()}")
        
        try:
            articulo_a_buscar = int(input("\n¿Qué categoría andas buscando?: "))
            if 1 <= articulo_a_buscar <= 5:
                clave_categoria = articulos_disponibles[articulo_a_buscar - 1]
                cat_disponible = tienda[clave_categoria]
                
                print(f"\nMostrando artículos de {clave_categoria}...")
                time.sleep(0.6)
                for item_nombre in cat_disponible.keys():
                    print(f" • {item_nombre.capitalize()}")
                
                print("\nConsejo: escribe el nombre exacto del artículo")
                busqueda = input("¿Qué artículo específico andas buscando?: ").lower().strip()
                
                if busqueda in cat_disponible:
                    datos_item = cat_disponible[busqueda]
                    print(f"\n¡{busqueda.capitalize()} encontrado!")
                    print(f"Precio: {datos_item[0]} HNL | Tallas/Detalles: {datos_item[1]}")
                else:
                    print("\nPor el momento ese artículo no está disponible.")
                time.sleep(1.5)
                
            elif articulo_a_buscar == 6:
                print("Volviendo al menú principal...")
                time.sleep(1)
            else:
                print("Opción no válida.")
        except ValueError:
            print("ERROR: escribe solo números.")

    elif opcion == 8:
        print("=" * 40)
        print("        HISTORIAL DE COMPRAS")
        print("=" * 40)
        if len(historial_compras) == 0:
            print("No has realizado ninguna compra todavía.\n")
            time.sleep(1.5)
        else:
            for i, factura in enumerate(historial_compras, start=1):
                print(f"\n--- FACTURA #{factura['num_factura']} (Compra N° {i}) ---")
                for prod in factura["productos"]:
                    print(f"  • {prod['nombre'].capitalize()} | Talla: {prod['talla']} | L. {prod['precio']}")
                print(f"  TOTAL PAGADO: {factura['total']} HNL")
                print("-" * 40)
            input("\nPresiona ENTER para volver al menú principal...")

    elif opcion == 9:
        mod_supervisor()


    elif opcion == 10:
      valoracion_reseña()

      
    elif opcion == 11:
      print("\n¡Gracias por visitar Inversiones G&G! Vuelve pronto")
      print("cerrando session...")
      time.sleep(1.5)
      break

  
    else:
        print("\n❌ Opción no válida. Por favor, elige un número del 1 al 9.\n")