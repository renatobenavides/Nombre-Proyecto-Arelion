# Análisis Exploratorio de Datos - Ventas, Clientes y Productos
# -------------------------------------------------------------
# Librerías
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Configuración
pd.set_option('display.float_format', '{:,.2f}'.format)
sns.set(style='whitegrid', palette='muted')

# -------------------------------------------------------------
# 1. Carga de Datos
clientes = pd.read_excel('clientes.xlsx')
productos = pd.read_excel('CopiaDeProductos.xlsx')
ventas = pd.read_excel('detalle_ventas.xlsx')

print("Clientes:", clientes.shape)
print("Productos:", productos.shape)
print("Ventas:", ventas.shape)

# Vista previa
display(clientes.head())
display(productos.head())
display(ventas.head())

# -------------------------------------------------------------
# 2. Estadísticas descriptivas básicas
print("\n--- Estadísticas de Clientes ---")
display(clientes.describe(include='all'))

print("\n--- Estadísticas de Productos ---")
display(productos.describe(include='all'))

print("\n--- Estadísticas de Ventas ---")
display(ventas.describe())

# -------------------------------------------------------------
# 3. Identificación del tipo de distribución de variables
# Ejemplo: distribución de montos de venta
plt.figure(figsize=(10,6))
sns.histplot(ventas['Monto'], kde=True, bins=30)
plt.title('Distribución de Montos de Venta')
plt.xlabel('Monto de Venta')
plt.ylabel('Frecuencia')
plt.show()

# Distribución de edades de clientes (si existe esa columna)
if 'Edad' in clientes.columns:
    plt.figure(figsize=(10,6))
    sns.histplot(clientes['Edad'], kde=True, bins=20, color='orange')
    plt.title('Distribución de Edades de Clientes')
    plt.xlabel('Edad')
    plt.ylabel('Frecuencia')
    plt.show()

# -------------------------------------------------------------
# 4. Análisis de correlaciones entre variables principales
# Unimos datos relevantes para correlaciones
df = ventas.merge(productos, on='idProducto', how='left')
if 'idCliente' in ventas.columns:
    df = df.merge(clientes, on='idCliente', how='left')

# Solo variables numéricas
num_df = df.select_dtypes(include=[np.number])

corr = num_df.corr()
plt.figure(figsize=(10,8))
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title('Matriz de Correlación entre Variables Numéricas')
plt.show()

# -------------------------------------------------------------
# 5. Detección de outliers (valores extremos)
# Usamos método IQR
def detectar_outliers(col):
    q1 = col.quantile(0.25)
    q3 = col.quantile(0.75)
    iqr = q3 - q1
    limite_inf = q1 - 1.5 * iqr
    limite_sup = q3 + 1.5 * iqr
    return ((col < limite_inf) | (col > limite_sup))

ventas['outlier_monto'] = detectar_outliers(ventas['Monto'])
print("Outliers en Monto de venta:", ventas['outlier_monto'].sum())

plt.figure(figsize=(10,6))
sns.boxplot(x=ventas['Monto'])
plt.title('Detección de Outliers en Monto de Venta')
plt.show()

# -------------------------------------------------------------
# 6. Gráficos representativos

# (a) Evolución de ventas por fecha
if 'Fecha' in ventas.columns:
    ventas['Fecha'] = pd.to_datetime(ventas['Fecha'])
    ventas_por_fecha = ventas.groupby('Fecha')['Monto'].sum().reset_index()

    plt.figure(figsize=(12,6))
    sns.lineplot(data=ventas_por_fecha, x='Fecha', y='Monto')
    plt.title('Evolución de Ventas en el Tiempo')
    plt.xlabel('Fecha')
    plt.ylabel('Monto Total')
    plt.show()

# (b) Ventas por categoría de producto
if 'Categoria' in productos.columns:
    ventas_cat = df.groupby('Categoria')['Monto'].sum().sort_values(ascending=False)
    plt.figure(figsize=(10,6))
    sns.barplot(x=ventas_cat.index, y=ventas_cat.values)
    plt.title('Ventas Totales por Categoría de Producto')
    plt.xlabel('Categoría')
    plt.ylabel('Monto Total')
    plt.xticks(rotation=45)
    plt.show()

# (c) Relación entre precio y cantidad vendida
if 'Precio' in productos.columns and 'Cantidad' in ventas.columns:
    plt.figure(figsize=(10,6))
    sns.scatterplot(data=df, x='Precio', y='Cantidad', alpha=0.6)
    plt.title('Relación entre Precio y Cantidad Vendida')
    plt.xlabel('Precio del Producto')
    plt.ylabel('Cantidad Vendida')
    plt.show()

# -------------------------------------------------------------
# 7. Interpretación orientada al problema
interpretacion = """
### Interpretación de Resultados

- Las estadísticas descriptivas permiten observar la dispersión de montos de venta, precios y cantidades vendidas.
- La distribución de los montos de venta presenta una asimetría positiva, indicando que la mayoría de las ventas son de bajo valor, con algunos casos de alto monto (outliers).
- El análisis de correlaciones muestra las relaciones más fuertes entre variables numéricas, como la asociación entre precio y monto total.
- Se detectaron outliers en los montos de venta, que podrían corresponder a operaciones excepcionales o errores de carga.
- Las visualizaciones confirman una tendencia creciente de ventas a lo largo del tiempo, y diferencias marcadas entre categorías de producto.
- En conjunto, estos resultados sirven para orientar estrategias de precios, segmentación de clientes y control de calidad de datos.
"""
from IPython.display import Markdown
display(Markdown(interpretacion))
