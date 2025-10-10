def obtener_textos_documentacion():
    """
    Esta función contiene todo el texto para cada opción del menú.
    Retorna un diccionario donde la clave es la opción y el valor es el texto.
    """
    textos = {
        '1': ("\n### 1. Tema, problema y solución ###\n"
              "TEMA: Identificación de Productos 'Fríos'.\n"
              "\nPROBLEMA: Nuestra base de datos actual está desorganizada, lo que nos impide identificar de manera rápida y eficiente los productos con las ventas más bajas. Esto significa que perdemos tiempo valioso y no podemos tomar decisiones ágiles para mejorar la rentabilidad.\n"
              "\nSOLUCIÓN: Implementaremos un reporte dinámico en Power BI que consolidará el catálogo completo de productos. Este reporte nos permitirá visualizar de forma inmediata y sencilla cuáles son los artículos menos vendidos, facilitando así la toma de decisiones estratégicas."),

        '2': ("\n### 2. Dataset de referencia ###\n\n"
              "Se utilizan tres fuentes de datos principales:\n\n"
              "1. Fuente: detalle_ventas\n"
              "   Definición: Registra cuántas veces se vendió cada producto y la venta a la que está relacionada.\n\n"
              "2. Fuente: productos\n"
              "   Definición: Contiene los detalles de cada producto.\n\n"
              "3. Fuente: ventas\n"
              "   Definición: Indica los datos de clientes asociados a cada venta (fecha, email, tipo de pago)."),

        '3': ("\n### 3. Estructura por tabla ###\n\n"
              "Tabla: detalle_ventas (~344 filas)\n"
              "| Campo           | Tipo | Escala  |\n"
              "|-----------------|------|---------|\n"
              "| id_venta        | int  | Nominal |\n"
              "| id_producto     | int  | Nominal |\n"
              "| cantidad        | int  | Razón   |\n\n"
              "Tabla: productos (~101 filas)\n"
              "| Campo           | Tipo | Escala  |\n"
              "|-----------------|------|---------|\n"
              "| id_producto     | int  | Nominal |\n"
              "| nombre_producto | str  | Nominal |\n"
              "| categoria       | str  | Nominal |\n"
              "| precio_unitario | int  | Razón   |\n\n"
              "Tabla: ventas (~121 filas)\n"
              "| Campo           | Tipo | Escala  |\n"
              "|-----------------|------|---------|\n"
              "| id_venta        | int  | Nominal |\n"
              "| fecha           | dt   | Nominal |\n"
              "| id_cliente      | int  | Nominal |\n"
              "| medio_pago      | str  | Nominal |"),

        '4': ("\n### 4. Escalas de medición ###\n\n"
              "1. Escala Nominal:\n"
              "   Descripción: Se usa para etiquetar variables sin un orden o valor cuantitativo. Son categorías o identificadores.\n"
              "   Ejemplos: 'id_producto', 'nombre_producto', 'categoria', 'medio_pago'.\n\n"
              "2. Escala de Razón:\n"
              "   Descripción: Es una escala numérica donde el cero tiene un significado real (ausencia de valor) y las proporciones son válidas.\n"
              "   Ejemplos: 'cantidad', 'precio_unitario'."),

        '5': ("\n### 5. Sugerencias y mejoras con Copilot ###\n\n"
              "- Separar la documentación en plantillas reutilizables (ej. un módulo textos.py).\n"
              "- Proveer un modo 'búsqueda' para localizar palabras clave.\n"
              "- Agregar una opción para 'exportar sección' a un archivo .txt.\n"
              "- Incluir tests mínimos para verificar que cada opción del menú funcione correctamente."
              "\n\n Recomendacion propia: Usar API de GitHub Copilot para sugerencias personalizadas cada vez que se ejecute."
              "\n\n Nota: Ninguna de estas mejoras se ha implementado aún.")
    }
    return textos


def iniciar_menu():
    """
    Función principal que ejecuta el bucle del menú interactivo.
    Incluye un contador de intentos inválidos (máx. 3 consecutivos).
    """
    textos_menu = obtener_textos_documentacion()

    MAX_INTENTOS = 3
    intentos_invalidos = 0

    while True:
        print("\n------ MENÚ DE DOCUMENTACIÓN DEL PROYECTO ------")
        print("1. Tema, problema y solución")
        print("2. Dataset de referencia")
        print("3. Estructura por tabla")
        print("4. Escalas de medición")
        print("5. Sugerencias y mejoras con Copilot")
        print("6. Salir")
        print("------------------------------------------------")

        opcion_usuario = input("Selecciona una opción (1-6): ").strip()

        if opcion_usuario in textos_menu:
            print(textos_menu[opcion_usuario])
            intentos_invalidos = 0  # Reinicia el contador tras una opción válida
        elif opcion_usuario == '6':
            print("\nSaliendo de la documentación... ¡Adiós! 👋")
            break
        else:
            intentos_invalidos += 1
            restantes = MAX_INTENTOS - intentos_invalidos

            if intentos_invalidos >= MAX_INTENTOS:
                print("\n❌ Has agotado los 3 intentos inválidos. Cerrando el programa. 👋")
                break
            else:
                print(f"\n❌ Opción no válida. Te quedan {restantes} intento(s). Ingresa un número del 1 al 6.")


# --- Punto de entrada del programa ---
if __name__ == "__main__":
    iniciar_menu()