# Documentación
1ra demo: asincrónica

## 1. Tema, problema y solución

### Tema:
Identificación de Productos 'Fríos'

### Problema:
La falta de organización y análisis en nuestra base de datos de ventas ha generado una **pérdida estimada del 10 % al 15 % en ingresos mensuales**, debido a una mala gestión del inventario y a la ausencia de acciones oportunas sobre los productos con bajo rendimiento.  
Actualmente no se identifican con claridad los artículos menos vendidos, lo que ocasiona **acumulación de stock**, **costos innecesarios de almacenamiento** y una **disminución en la rentabilidad general del negocio**.

### Solución:
- **Productos más vendidos:** fortalecer su promoción y garantizar su disponibilidad constante.  
- **Ventas normales:** mantener un control equilibrado, monitoreando su tendencia.  
- **Menos vendidos:** analizar causas de baja rotación, aplicar descuentos, combos o retirar del catálogo si es necesario.  

Este plan permitirá **priorizar la toma de decisiones**, mejorar la **eficiencia en el manejo del inventario** y reducir las **pérdidas económicas**, logrando una **recuperación estimada del 8 % al 12 % de los ingresos actuales**.


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

```
### 3.4 Diagrama de flujo:
![Diagrama del flujo](./menu_diagrama.png)

