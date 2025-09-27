# Documentación
1ra demo: asincrónica

## 1. Tema, problema y solución

**Tema:**
Productos que menos se venden
**Problema:**

Tenemos la base de datos desordenada y queremos hallar rapidamente los productos que menos se venden.
**Solución:**
Crear un reporte en Power bi con el catalogo completo donde se vea facilmente los productos menos vendidos.

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

INICIO
  // Cargar previamente todos los textos de la documentación en una estructura
  // de datos, como un diccionario, donde cada opción del menú es una llave.
  CARGAR textos_documentacion

  // Ejemplo de lo que contendría textos_documentacion:
  // textos_documentacion['opcion1'] = "TEMA: Productos que menos se venden..."
  // textos_documentacion['opcion2'] = "DATASET DE REFERENCIA: Fuente: detalle_ventas..."
  // textos_documentacion['opcion3'] = "ESTRUCTURA POR TABLA: Para productos.csv, las columnas son..."
  // etc.

MIENTRAS Verdadero:
  // Mostrar al usuario las opciones disponibles
  MOSTRAR Menú:
    1. Tema, problema y solución
    2. Dataset de referencia
    3. Estructura por tabla
    4. Escalas de medición
    5. Sugerencias y mejoras (Ejemplo)
    6. Salir

  // Esperar a que el usuario ingrese un número
  LEER opcion_usuario

  // Evaluar la opción ingresada por el usuario
  SI opcion_usuario == 1:
    IMPRIMIR el texto asociado a "Tema, problema y solución"
  
  SI opcion_usuario == 2:
    IMPRIMIR el texto asociado a "Dataset de referencia"

  SI opcion_usuario == 3:
    IMPRIMIR el texto asociado a "Estructura por tabla"

  SI opcion_usuario == 4:
    IMPRIMIR el texto asociado a "Escalas de medición"

  SI opcion_usuario == 5:
    IMPRIMIR el texto asociado a "Sugerencias y mejoras"

  SI opcion_usuario == 6:
    // Si el usuario elige salir, se rompe el ciclo y el programa termina
    IMPRIMIR "Saliendo de la documentación..."
    ROMPER bucle
  
  // Opcional: Manejar casos donde el usuario no ingresa un número válido
  SINO:
    IMPRIMIR "Opción no válida. Por favor, elige un número del 1 al 6."

FIN


### 3.4 Diagrama de flujo:

Adjuntar imagen del diagrama de flujo y el link del archivo
`![Diagrama de flujo](diagrama_flujo.png)`
`[Diagrama de flujo](htttps://www.url-del-archivo.com)`

### 4. Sugerencias y mejoras aplicadas con Copilot

- Separar la documentación en plantillas reutilizables (por ejemplo, textos.py) y desacoplarla del código del menú.
- Proveer un modo “búsqueda” para localizar palabras clave dentro de la documentación (e.g., “precio”, “escala”).
- Agregar una opción “exportar sección” para guardar en .txt/.md lo mostrado por pantalla.
- Incluir tests mínimos para el router de opciones (verifica que cada número abra la sección correcta).
