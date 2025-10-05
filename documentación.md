# Documentación
1ra demo: asincrónica

## 1. Tema, problema y solución

**Tema:**
Identificación de Productos 'Fríos'

**Problema:**
Nuestra base de datos actual está desorganizada, lo que nos impide identificar de manera rápida y eficiente los productos con las ventas más bajas. Esto significa que perdemos tiempo valioso y no podemos tomar decisiones ágiles para mejorar la rentabilidad.

**Solución:**
Implementaremos un reporte dinámico en Power BI que consolidará el catálogo completo de productos. Este reporte nos permitirá visualizar de forma inmediata y sencilla cuáles son los artículos menos vendidos, facilitando así la toma de decisiones estratégicas.

## 2. Dataset de referencia:

**Fuente:**
detalle_ventas

**Definición:**
detalle_ventas: Cuantas veces se vendio cada producto y la venta a la que esta relacionada.

**tabla_ejemplo archivo.csv** ~344 filas
| Campo            | Tipo | Escala   | 
|------------------|------|----------| 
| id_venta         | int  | Nominal  | 
| id_producto      | int  | Nominal  | 
| nombre_producto  | str  | Nominal  | 
| cantidad         | int  | Razón    |
| precio_unitario  | int  | Razón    |
| importe          | int  | Razón    |

**Fuente:**
productos

**Definición:**
detalle_ventas: Los detalles de cada producto. 

**tabla_ejemplo archivo.csv** ~101 filas
| Campo            | Tipo | Escala   | 
|------------------|------|----------| 
| id_producto      | int  |Nominal   |
| nombre_producto  | str  |Nominal   |
| categoria        | str  |Nominal   |
| precio_unitario  | int  |Razón     |

**Fuente:**
ventas

**Definición:**
detalle_ventas: Nos indica los datos de clientes (fecha, mail y tipos de pago)

**tabla_ejemplo archivo.csv** ~121filas
| Campo            | Tipo | Escala   | 
|------------------|------|----------| 
| id_venta         | int  |Nominal   |
| fecha            | dt   |Nominal   |
| id_cliente       | int  |Nominal   |
| nombre_cliente   | str  |Nominal   |
| email            | str  |Nominal   |
| medio_pago       | str  |Nominal   |


 
## 3. Información, pasos, pseudocódigo y diagrama del programa (Sprint 1)

### 3.1 Contenidos accesibles desde el menú

1. Tema, problema y solución.
2. Dataset de referencia. Resumen de fuente y definición.
3. Estructura por tabla. Columnas, tipo y escala de medición.
4. Escalas de medición. Descripción y ejemplos.
5. Sugerencias y mejoras con Copilot.
6. Salir.

### 3.2 Pasos
Paso A: El Trabajo del "Ayudante Inteligente" 🐍 (con Python)
1. Hallar, regularizar y unir los datos correctos.
Antes de cualquier cálculo, se realiza un pequeño análisis para entender los datos. Luego, el programa leerá los dos archivos clave: productos.csv y detalle_ventas.csv.

2. Sumar las ventas totales por producto.
El script revisará todas las transacciones en el archivo detalle_ventas.csv y sumará la cantidad total de unidades vendidas para cada producto.

3. Consolidar todo en una gran lista.
Se tomará el catálogo completo de productos.csv y se le añadirá una columna con las ventas totales. Es fundamental que, si un producto nunca se vendió, aparezca en esta lista final con un cero en sus ventas para no perderlo de vista.

4. Ordenar y limpiar la lista.
Una vez que la tabla esté completa, se ordenará de menor a mayor según la cantidad vendida, poniendo los productos "fríos" al principio. También se limpiará cualquier dato para asegurar la calidad del reporte.

5. Guardar la lista final.
Finalmente, el script guardará esta tabla perfecta y ordenada en un nuevo archivo listo para ser visualizado: reporte_productos_frios.csv.

Paso B: La Visualización en el "Tablero Mágico" 📊 (con Power BI)
1. Cargar la lista final y procesada.
Se abrirá Power BI y se importará el archivo reporte_productos_frios.csv, que ya contiene toda la información limpia y calculada por nuestro Ayudante Inteligente.

2. Crear una tabla simple de resultados.
Dentro del tablero de Power BI, se creará una tabla que mostrará de forma clara el nombre del producto, su categoría y el total de unidades que se vendieron.

3. ¡Ver la solución al instante!
Gracias a que los datos ya vienen limpios y ordenados desde Python, la tabla mostrará inmediatamente los productos menos vendidos en la parte superior, listos para el análisis y la toma de decisiones.

### 3.3 Pseudocódigo

# Documentación del Proyecto

Este documento detalla la estructura, contenido y lógica de un sistema de consulta de información de ventas.

---

## 1. Contenido de la Documentación

A continuación se describen las diferentes secciones de información disponibles en el menú interactivo.

### Tema, Problema y Solución

* **TEMA:** Productos que menos se venden.
* **PROBLEMA:** La base de datos está desordenada y se necesita hallar rápidamente los productos con ventas más bajas.
* **SOLUCIÓN:** Crear un reporte en Power BI con el catálogo completo donde se visualicen fácilmente los productos menos vendidos.

### Dataset de Referencia - Resumen de Fuentes

1.  **Fuente: `detalle_ventas`**
    * **Definición:** Registra cuántas veces se vendió cada producto y la venta a la que está relacionada.

2.  **Fuente: `productos`**
    * **Definición:** Contiene los detalles y catálogo de cada producto.

3.  **Fuente: `ventas`**
    * **Definición:** Indica los datos de clientes asociados a cada venta (fecha, email, tipo de pago).

### Estructura por Tabla

**Tabla: `detalle_ventas` (~344 filas)**

| Campo       | Tipo | Escala  |
|-------------|------|---------|
| `id_venta`    | int  | Nominal |
| `id_producto` | int  | Nominal |
| `cantidad`    | int  | Razón   |

**Tabla: `productos` (~101 filas)**

| Campo           | Tipo | Escala  |
|-----------------|------|---------|
| `id_producto`   | int  | Nominal |
| `nombre_producto`| str  | Nominal |
| `categoria`     | str  | Nominal |
| `precio_unitario`| int  | Razón   |

**Tabla: `ventas` (~121 filas)**

| Campo      | Tipo | Escala  |
|------------|------|---------|
| `id_venta`   | int  | Nominal |
| `fecha`      | dt   | Nominal |
| `id_cliente` | int  | Nominal |
| `medio_pago` | str  | Nominal |

### Escalas de Medición - Descripción y Ejemplos

1.  **Escala Nominal:**
    * **Descripción:** Se usa para etiquetar variables sin un orden o valor cuantitativo. Son categorías o identificadores.
    * **Ejemplos en el dataset:** `id_producto`, `nombre_producto`, `categoria`, `medio_pago`.

2.  **Escala de Razón:**
    * **Descripción:** Es una escala numérica donde el cero tiene un significado real (ausencia de valor) y las proporciones son válidas (20 es el doble de 10).
    * **Ejemplos en el dataset:** `cantidad`, `precio_unitario`.

### Sugerencias y Mejoras con Copilot

* Separar la documentación en plantillas reutilizables (por ejemplo, `textos.py`) y desacoplarla del código del menú.
* Proveer un modo 'búsqueda' para localizar palabras clave dentro de la documentación (e.g., 'precio', 'escala').
* Agregar una opción 'exportar sección' para guardar en `.txt`/`.md` lo mostrado por pantalla.
* Incluir tests mínimos para el router de opciones (verifica que cada número abra la sección correcta).

---

## 2. Lógica del Menú Interactivo (Pseudocódigo)

El siguiente pseudocódigo describe el funcionamiento del menú que presenta la documentación.

```pseudocode
MIENTRAS Verdadero:
    // Mostrar al usuario las opciones disponibles
    IMPRIMIR "\n------ MENÚ DE DOCUMENTACIÓN DEL PROYECTO ------"
    IMPRIMIR "1. Tema, problema y solución"
    IMPRIMIR "2. Dataset de referencia"
    IMPRIMIR "3. Estructura por tabla"
    IMPRIMIR "4. Escalas de medición"
    IMPRIMIR "5. Sugerencias y mejoras con Copilot"
    IMPRIMIR "6. Salir"
    IMPRIMIR "------------------------------------------------"
    
    // Esperar a que el usuario ingrese un número
    LEER opcion_usuario
    
    // Evaluar la opción ingresada por el usuario usando una estructura de casos
    SEGUN opcion_usuario HACER:
        CASO 1:
            IMPRIMIR texto_opcion_1
        CASO 2:
            IMPRIMIR texto_opcion_2
        CASO 3:
            IMPRIMIR texto_opcion_3
        CASO 4:
            IMPRIMIR texto_opcion_4
        CASO 5:
            IMPRIMIR texto_opcion_5
        CASO 6:
            // Si el usuario elige salir, se imprime un mensaje y se rompe el ciclo
            IMPRIMIR "Saliendo de la documentación..."
            ROMPER BUCLE
        DE OTRO MODO:
            // Manejar casos donde el usuario no ingresa un número válido
            IMPRIMIR "Opción no válida. Por favor, elige un número del 1 al 6."


### 3.4 Diagrama de flujo:

Adjuntar imagen del diagrama de flujo y el link del archivo
`![Diagrama de flujo](diagrama_flujo.png)`
`[Diagrama de flujo](htttps://www.url-del-archivo.com)`

