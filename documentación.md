# Documentación
1ra demo: asincrónica

## 1. Tema, problema y solución

### Tema:
Identificación de Productos que menos se venden

Problema:
La base de datos de ventas muestra una baja rotación en algunos productos, lo que impide detectar a tiempo cuáles artículos se venden con poca frecuencia. Esto afecta la eficiencia del negocio y las oportunidades de venta.

Solución:
Calcular la rotación de productos: medir cada cuánto tiempo se vende un producto (por ejemplo, en días).
Clasificar los productos: alta o baja rotación según su frecuencia de venta.

Objetivo:
Creación de modelo de machine learning que va a clasificar si el producto es de baja o alta rotacion

Algoritmo elegido:
Algoritmo de clasificación

Entradas:
- Campos (features) calculados de los productos

Salida:
- Booleano que nos indicará si el producto tiene alta  o baja rotación

Metricas:
- Metricas para algoritmos de clasificacion F1 score, presicion, Recall, Matriz de confusion. 


Acciones correctivas para equipo comercial:
Promocionar los productos de baja rotación.
Ajustar precios o realizar descuentos.
Revisar el catálogo para retirar artículos con ventas nulas o muy espaciadas.
Esto permitirá optimizar la gestión del inventario, reducir costos de almacenamiento y mejorar la disponibilidad de productos con alta demanda.


## 2. Dataset de referencia:

**Fuente:**
detalle_ventas

**Definición:**
Registra cuántas veces se vendió cada producto y la venta a la que está relacionada.

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
Contiene los detalles de cada producto. 

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
Indica los datos de clientes asociados a cada venta (fecha, email, tipo de pago).

**tabla_ejemplo archivo.csv** ~121filas
| Campo            | Tipo | Escala   | 
|------------------|------|----------| 
| id_venta         | int  |Nominal   |
| fecha            | dt   |Nominal   |
| id_cliente       | int  |Nominal   |
| nombre_cliente   | str  |Nominal   |
| email            | str  |Nominal   |
| medio_pago       | str  |Nominal   |


**Fuente:**
cliente

**Definición:**
Indica todos los datos del cliente

**tabla_ejemplo archivo.csv** ~344 filas
| Campo            | Tipo | Escala   | 
|------------------|------|----------| 
| id_cliente       | int  | Nominal  | 
| nombre_cliente   | str  | Nominal  | 
| email            | str  | Nominal  |
| ciudad           | str  | Nominal  |
| fecha_alta       | dt   | Nominal  |

 
## 3. Información, pasos, pseudocódigo y diagrama del programa (Sprint 1)

### 3.1 Contenidos accesibles desde el menú

1. Tema, problema y solución.
2. Dataset de referencia. Resumen de fuente y definición.
3. Estructura por tabla. Columnas, tipo y escala de medición.
4. Escalas de medición. Descripción y ejemplos.
5. Sugerencias y mejoras con Copilot.
6. Salir.

### 3.2 Pasos
Objetivo del proceso

El propósito de esta sección es documentar el funcionamiento del menú interactivo que permite acceder a las diferentes partes del proyecto. Este menú simula una navegación estructurada dentro de una documentación técnica, facilitando al usuario la consulta del tema, dataset, estructura de tablas, escalas de medición y sugerencias de mejora del sistema.

### Paso A: Diseño lógico mediante pseudocódigo

Antes de implementar el programa en Python, se elaboró un pseudocódigo para representar de manera clara la lógica del flujo del menú. En él, se utiliza una estructura de repetición MIENTRAS Verdadero que mantiene activo el menú hasta que el usuario seleccione la opción “Salir”.

Cada número ingresado corresponde a una sección del proyecto, y se emplea una estructura condicional SEGÚN...HACER (similar al match o if-elif en Python) para mostrar el contenido correspondiente.

El pseudocódigo también incluye el manejo de errores, garantizando que el sistema informe al usuario cuando se introduce una opción inválida. De esta forma, se logra una base lógica robusta y ordenada antes de programar el código definitivo.

### Paso B: Implementación práctica en Python

A partir del pseudocódigo anterior, se desarrolló un programa modular utilizando funciones en Python para mantener un código limpio y escalable.

La función obtener_textos_documentacion() contiene toda la información que se muestra en el menú, organizada en un diccionario donde las claves son los números del menú y los valores son los textos de cada sección. Esto facilita la actualización o ampliación del contenido sin modificar la lógica principal.

La función iniciar_menu() implementa el bucle principal (while True), que presenta las opciones al usuario, recibe su selección y muestra la información correspondiente. Además, incluye validaciones para asegurar que solo se acepten números del 1 al 6 y finaliza correctamente cuando se elige la opción “Salir”.

El menú funciona como una interfaz simple y funcional para navegar por la documentación del proyecto, permitiendo al usuario revisar cada sección de manera ordenada, intuitiva y adaptable a futuras ampliaciones.

### 3.3 Pseudocódigo

El siguiente pseudocódigo describe el funcionamiento del menú que presenta la documentación.

```pseudocode
MIENTRAS Verdadero:
    Mostrar menu
    Leer opcion_usuario

    SEGUN opcion_usuario HACER:
        CASO 1..5: mostrar textos
        CASO 6..10: ejecutar funciones de graficos o modelo
        CASO 11: salir
        OTRO: mostrar error
```
### 3.4 Diagrama de flujo:
![Diagrama del flujo](./menu_diagrama.png) <-- Hay q modificar esto 

### 4. Graficos generados

- Distribucion de rotacion
- Productos menos rentables
- Series mensuales de productos menos vendidos
- Scatter rotacion vs importe

## 5. Modelo de machine learning

#### Objetivo del modelo (predecir o clasificar)

El objetivo del modelo es clasificar los productos en dos categorias:

- Alta rotacion
- Baja rotacion

Segun su comportamiento de ventas dentro del periodo analizado.


Se utiliza regresion logistica para clasificar productos segun su rotacion.
Incluye:

- Split train/test
- Escalado de variables
- Precision y recall
- Matriz de confusion
- Curva ROC + AUC

- Algoritmo elegido y justificacion

Se utiliza un algoritmo de clasificacion supervisada. Este tipo de algoritmos permite asignar una categoria (alta/baja rotacion) a cada producto en base a las features calculadas.

La eleccion se justifica porque:

- La salida es binaria.

- Permite evaluar el desempeño con metricas especificas como F1, precision y recall.

- Es adecuado para conjuntos de datos pequeños como el presente.


### Entradas (X) y salida (y)

X (features):

- Frecuencia de venta por producto.
- Dias promedio entre ventas.
- Cantidad total vendida.
- Precio unitario.
- Variables derivadas de las tablas de detalle_ventas, productos y ventas.

y (target):

- 1 = Alta rotacion.
- 0 = Baja rotacion.

### Metricas de evaluacion

Se utilizan metricas propias de problemas de clasificacion:

- Precision
- Recall
- F1-score (principal)
- Matriz de confusion: Estas permiten evaluar correctamente modelos desbalanceados, como suele ocurrir cuando hay pocos productos de alta rotacion.

### Modelo ML implementado

Se implemento un modelo clasificador (ej: Logistic Regression, Decision Tree o similar segun la version del .py). El codigo incluye:

- Preparacion de features.
- Normalizacion o escalado cuando corresponde.
- Entrenamiento del modelo.
- Evaluacion con las metricas anteriores.


### Division train/test y entrenamiento

El dataset se divide tipicamente en:
- 80% entrenamiento
- 20% test

El entrenamiento se realiza sobre las features X y el target y, generando luego predicciones para la muestra de test.

### Predicciones y metricas calculadas

El modelo genera:

- Predicciones para cada producto.
- Matriz de confusion.
- Valores de precision, recall y F1.

Estos resultados se muestran en pantalla desde el .py actualizado.

### Resultados visualizados en graficos

El programa incluye visualizacion mediante graficos, tales como:

- Distribucion de categorias (alta vs baja rotacion).
- Importancia de features.
- Grafico de confusion.

Estos graficos permiten entender mejor el desempeno y comportamiento del modelo.