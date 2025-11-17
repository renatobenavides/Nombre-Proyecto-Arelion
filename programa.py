import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def obtener_textos_documentacion():
    """
    Esta función contiene todo el texto para cada opción del menú.
    Retorna un diccionario donde la clave es la opción y el valor es el texto.
    """
    textos = {
        '1': ("\n### 1. Tema, problema y solución ###\n"
              "\033[1mTEMA:\033[0m Identificación de Productos 'Fríos'.\n"
              "\n\033[1mPROBLEMA:\033[0m La falta de organización y análisis en nuestra base de datos de ventas ha generado una \033[1mpérdida estimada del 10 % al 15 % en ingresos mensuales\033[0m, debido a una mala gestión del inventario y a la ausencia de acciones oportunas sobre los productos con bajo rendimiento. Actualmente no se identifican con claridad los artículos menos vendidos, lo que ocasiona \033[1macumulación de stock\033[0m, \033[1mcostos innecesarios de almacenamiento\033[0m y una \033[1mdisminución en la rentabilidad general del negocio\033[0m.\n"
              "\n\033[1mSOLUCIÓN:\033[0m  Desarrollar un \033[1mplan de estrategias de optimización de ventas\033[0m, basado en la \033[1mclasificación de los productos por categorías de desempeño\033[0m:"
              "- \033[1mProductos más vendidos:\033[0m fortalecer su promoción y garantizar su disponibilidad constante."
              "- \033[1mVentas normales:\033[0m mantener un control equilibrado, monitoreando su tendencia."
              "- \033[1mMenos vendidos:\033[0m analizar causas de baja rotación, aplicar descuentos, combos o retirar del catálogo si es necesario."
              "Este plan permitirá \033[1mpriorizar la toma de decisiones\033[0m, mejorar la \033[1meficiencia en el manejo del inventario\033[0m y reducir las \033[1mpérdidas económicas\033[0m, logrando una \033[1mrecuperación estimada del 8 % al 12 % de los ingresos actuales\033[0m."),

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
        print("6. ")
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
    
    ''''''
    


clientes = pd.read_excel('clientes.xlsx')
print("Dimension del dataset Clientes:", clientes.shape)
print("\nPrimeras filas del dataset Clientes:")
print(clientes.head())

print("\nTipos de datos en el dataset Clientes:")
print(clientes.dtypes)


print("\n++++++++++++Valores nulos por cada columna+++++++++")
print(clientes.isnull().sum())

print("\n++++++++++++Duplicados por cada columna+++++++++")
print(clientes.apply(lambda x: x.duplicated().sum()))

print("\n++++++++++++Información del dataset Clientes+++++++++")
clientes.info()


print("\n++++++++++++Descripción del dataset Clientes+++++++++")

print("\n++++++++DESCRIPCIÓN DE VARIABLES NUMÉRICAS+++++++++")
print(clientes.describe())

print("\n+++++++++DESCRIPCIÓN DE VARIABLES CATEGÓRICAS++++++++")
print(clientes.describe(include=['object']))

print("\n++++++++++DESCRIPCIÓN DE VARIABLES DE FECHA++++++++++")
print(clientes.describe(include=['datetime']))


"""
Para interpretar la tabla generada por el método `describe()`:
COLUMNAS NUMÉRICAS
| Métrica           | Significado                                                                                                     |
| ----------------- | --------------------------------------------------------------------------------------------------------------- |
| **count**         | Cantidad de valores no nulos.                                                                                   |
| **mean**          | Promedio de los valores.                                                                                        |
| **std**           | Desviación estándar (qué tanto se dispersan los datos respecto al promedio).                                    |
| **min**           | Valor mínimo encontrado.                                                                                        |
| **25%, 50%, 75%** | Cuartiles → dividen la distribución: el 25%, 50% (mediana) y 75% de los datos están por debajo de esos valores. |
| **max**           | Valor máximo encontrado.                                                                                        |

COLUMNAS CATEGÓRICAS
| Métrica    | Significado                                     |
| ---------- | ----------------------------------------------- |
| **count**  | Total de valores no nulos.                      |
| **unique** | Cantidad de valores distintos (sin duplicados). |
| **top**    | Valor más frecuente.                            |
| **freq**   | Frecuencia (cuántas veces aparece ese “top”).   |

COLUMNAS DE FECHA
| Métrica    | Significado                                     |
| ---------- | ----------------------------------------------- |
| **count**  | cuántas fechas hay.                             |
| **mean**   | promedio de fechas (punto medio temporal).      |
| **min**    | primera y última fecha                          |
"""
productos = pd.read_excel('CopiaDeProductos.xlsx')
# === 2. Información general ===
print("Dimension del dataset Productos:", productos.shape)
print("\nPrimeras filas del dataset Productos:")
print(productos.head())

print("\nTipos de datos en el dataset Productos:")
print(productos.dtypes)

# === 3. Análisis de valores faltantes y duplicados ===
print("\n++++++++++++VALORES NULOS POR COLUMNA++++++++++++")
print(productos.isnull().sum())

print("\n++++++++++++DUPLICADOS POR COLUMNA++++++++++++")
print(productos.apply(lambda x: x.duplicated().sum()))

# === 4. Información del DataFrame ===
print("\n++++++++++++INFORMACIÓN DEL DATASET PRODUCTOS++++++++++++")
print(productos.info())

# === 5. Análisis descriptivo general ===
print("\n++++++++DESCRIPCIÓN DE VARIABLES NUMÉRICAS++++++++")
print(productos.describe())

print("\n++++++++DESCRIPCIÓN DE VARIABLES CATEGÓRICAS++++++++")
print(productos.describe(include=['object']))




# === 1. Carga del dataset ===
detalle_venta = pd.read_excel('detalle_ventas.xlsx')

# === 2. Información general ===
print("Dimension del dataset Detalle Ventas:", detalle_venta.shape)
print("\nPrimeras filas del dataset Detalle Ventas:")
print(detalle_venta.head())

print("\nTipos de datos en el dataset Detalle Ventas:")
print(detalle_venta.dtypes)

# === 3. Análisis de valores faltantes y duplicados ===
print("\n++++++++++++VALORES NULOS POR COLUMNA++++++++++++")
print(detalle_venta.isnull().sum())

print("\n++++++++++++DUPLICADOS POR COLUMNA++++++++++++")
print(detalle_venta.apply(lambda x: x.duplicated().sum()))

# === 4. Información del DataFrame ===
print("\n++++++++++++INFORMACIÓN DEL DATASET DETALLE VENTAS++++++++++++")
print(detalle_venta.info())

# === 5. Análisis descriptivo general ===
print("\n++++++++DESCRIPCIÓN DE VARIABLES NUMÉRICAS++++++++")
print(detalle_venta.describe())

print("\n++++++++DESCRIPCIÓN DE VARIABLES CATEGÓRICAS++++++++")
print(detalle_venta.describe(include=['object']))



# === 1. Carga del dataset ===
ventas = pd.read_excel('ventas.xlsx')



# === 2. Información general ===
print("Dimension del dataset Ventas:", ventas.shape)
print("\nPrimeras filas del dataset Ventas:")
print(ventas.head())

print("\nTipos de datos en el dataset Ventas:")
print(ventas.dtypes)

# === 3. Análisis de valores faltantes y duplicados ===
print("\n++++++++++++VALORES NULOS POR COLUMNA++++++++++++")
print(ventas.isnull().sum())

print("\n++++++++++++DUPLICADOS POR COLUMNA++++++++++++")
print(ventas.apply(lambda x: x.duplicated().sum()))

# === 4. Información del DataFrame ===
print("\n++++++++++++INFORMACIÓN DEL DATASET VENTAS++++++++++++")
print(ventas.info())

# === 5. Análisis descriptivo general ===
print("\n++++++++DESCRIPCIÓN DE VARIABLES NUMÉRICAS++++++++")
print(ventas.describe())

print("\n++++++++DESCRIPCIÓN DE VARIABLES CATEGÓRICAS++++++++")
print(ventas.describe(include=['object']))



df = detalle_venta.merge(productos, on='id_producto', how='left', suffixes=('_venta', '_producto'))
df = df.merge(ventas[['id_venta', 'fecha', 'id_cliente', 'medio_pago']], on='id_venta', how='left')
df = df.merge(clientes[['id_cliente', 'ciudad']], on='id_cliente', how='left')

df = pd.get_dummies(df, columns=['ciudad'], prefix='ciudad')

df = pd.get_dummies(df, columns=['medio_pago'], prefix='medio_pago')
df['fecha'] = pd.to_datetime(df['fecha'])

# OUTLIDERS 

def detectar_outliers(col):
    q1 = col.quantile(0.25)
    q3 = col.quantile(0.75)
    iqr = q3 - q1
    limite_inf = q1 - 1.5 * iqr
    limite_sup = q3 + 1.5 * iqr
    return (col < limite_inf) | (col > limite_sup)

df['outlier'] = detectar_outliers(df['cantidad'])
df = df[df['outlier'] == False].copy()



df = df.sort_values(by=['nombre_producto_venta', 'fecha'])

# Calcular diferencia en días entre ventas consecutivas del mismo producto
df['rotacion_dias'] = df.groupby('nombre_producto_venta')['fecha'].diff().dt.days
#groupby('nombre_producto_venta') ->Junta todas las ventas del mismo producto en un solo grupo.
# ['fecha'] ->Selecciona la columna de fechas dentro de cada grupo.
#.diff() ->Resta fecha actual – fecha anterior
# .dt.days ->Convierte la diferencia de tiempo a días
df['rotacion_dias'] = df['rotacion_dias'].fillna(0)


df['mes'] = df['fecha'].dt.to_period('M')
importe_mensual = df.groupby(['mes'])['importe'].sum().reset_index()


importe_mensual['variacion_%'] = importe_mensual['importe'].pct_change() * 100




plt.figure(figsize=(10,5))
sns.histplot(
    data=df,
    x='rotacion_dias',
    bins=40,
    kde=True,
    color='steelblue'
)

plt.title('Distribución de la Rotación de Productos')
plt.xlabel('Días entre ventas (rotación)')
plt.ylabel('Frecuencia')
plt.tight_layout()
plt.show()



sns.scatterplot(data=df, x='rotacion_dias', y='importe', hue='categoria')
plt.title('Relación entre rotación y monto vendido')
plt.show()



# Agrupar ventas por producto
# Agrupar por producto y sumar cantidad e importe total
ventas_por_producto = (
    df.groupby('nombre_producto_venta')[['cantidad', 'importe']]
      .sum()
      .reset_index()
      .sort_values(by='importe', ascending=True)
)

# Tomamos los 10 que menos plata generaron
menos_rentables = ventas_por_producto.head(10)
print(menos_rentables)

# --- Gráfico: Productos que menos facturan ---
plt.figure(figsize=(10,6))
sns.barplot(
    data=menos_rentables,
    x='importe',
    y='nombre_producto_venta',
    palette='Reds_r'
)
plt.title('Top 10 Productos que Menos Ingresos Generaron')
plt.xlabel('Importe Total ($)')
plt.ylabel('Producto')
plt.tight_layout()
plt.show()



# Top 10 menos rentables
ventas_por_producto = (
    df.groupby('nombre_producto_venta')[['cantidad', 'importe']]
      .sum()
      .reset_index()
      .sort_values(by='importe', ascending=True)
)

menos_rentables = ventas_por_producto.head(5)

lista_menos_vendidos = menos_rentables['nombre_producto_venta'].tolist()

# Filtrar el dataframe original para graficar en el tiempo
df_menos_vendidos_tiempo = df[df['nombre_producto_venta'].isin(lista_menos_vendidos)]




# Agrupar por mes y producto
ventas_mensuales_menos = (
    df_menos_vendidos_tiempo
    .groupby(['mes', 'nombre_producto_venta'])['cantidad']
    .sum()
    .reset_index()
)

plt.figure(figsize=(12, 6))
sns.barplot(
    data=ventas_mensuales_menos,
    x='mes',
    y='cantidad',
    hue='nombre_producto_venta'
)

plt.title('Cantidad vendida por mes - 5 productos menos vendidos')
plt.xlabel('Mes')
plt.ylabel('Cantidad')
plt.legend(title="Producto", bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()




# 1. Ordena los productos por ingreso total
orden_productos = (
    menos_rentables.sort_values(by="importe", ascending=True)['nombre_producto_venta']
)

# 2. Filtra y ordena el DataFrame original
df_menos_vendidos_tiempo = (
    df[df['nombre_producto_venta'].isin(lista_menos_vendidos)]
    .assign(
        producto_orden=lambda x: x['nombre_producto_venta'].map(
            {p: i for i, p in enumerate(orden_productos)}
        )
    )
    .sort_values(by=['producto_orden', 'fecha'])
    .drop(columns='producto_orden')
)

plt.figure(figsize=(10, 6))

sns.scatterplot(
    data=df_menos_vendidos_tiempo,
    x='rotacion_dias',
    y='importe',
    hue='nombre_producto_venta',   # para distinguir cada producto
    palette='tab10'
)

plt.title('Relación entre rotación y monto vendido (5 productos menos vendidos)')
plt.xlabel('rotación_dias')
plt.ylabel('importe')
plt.legend(title='Producto', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()




# Seleccionar solo columnas numéricas del subconjunto
numericas_menos = df_menos_vendidos_tiempo.select_dtypes(include=['int64','float64'])

# Matriz de correlación
corr_menos = numericas_menos.corr()

plt.figure(figsize=(10,6))
sns.heatmap(
    corr_menos,
    annot=True,
    cmap='coolwarm',
    fmt=".2f",
    linewidths=0.5
)

plt.title('Mapa de calor de correlaciones - 5 productos menos vendidos')
plt.tight_layout()
plt.show()
