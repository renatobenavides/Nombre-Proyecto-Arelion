import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#Esto es por una cuestion estetica
pd.set_option('display.float_format', '{:,.2f}'.format)
sns.set(style='whitegrid', palette='muted')

clientes = pd.read_excel('clientes.xlsx')
productos = pd.read_excel('CopiaDeProductos.xlsx')
detalle = pd.read_excel('detalle_ventas.xlsx')
ventas = pd.read_excel('ventas.xlsx')

print("Clientes:", clientes.shape)
print("Productos:", productos.shape)
print("Detalle Ventas:", detalle.shape)
print("Ventas:", ventas.shape)

print("Clientes")
print(clientes.head())
print("Productos")
print(productos.head())
print("Detalle de Ventas")
print(detalle.head())
print("Ventas")
print(ventas.head())

df = detalle.merge(productos, on='id_producto', how='left', suffixes=('_venta', '_producto'))
df = df.merge(ventas[['id_venta', 'fecha', 'id_cliente', 'medio_pago']], on='id_venta', how='left')
df = df.merge(clientes[['id_cliente', 'ciudad']], on='id_cliente', how='left')

df['fecha'] = pd.to_datetime(df['fecha'])

print("\n--- Estadísticas Generales ---")
print(df[['cantidad', 'importe', 'precio_unitario_venta']].describe())

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
# Distribucion de ventas(importe)
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


top10 = ventas_por_producto.head(10)
print(top10)

bottom10 = ventas_por_producto.tail(10)
print(bottom10)

q1 = ventas_por_producto['cantidad'].quantile(0.33)
q2 = ventas_por_producto['cantidad'].quantile(0.66)
def clasificar_producto(cant):
    if cant < q1:
        return 'Bajo'
    elif cant < q2:
        return 'Normal'
    else:
        return 'Alto'

ventas_por_producto['categoria_venta'] = ventas_por_producto['cantidad'].apply(clasificar_producto)

#Correlación entre cantidad e importe
plt.figure(figsize=(8,5))
sns.countplot(x='categoria_venta', data=ventas_por_producto, palette=['#2b83ba','#abdda4','#fdae61'])
plt.title('Clasificación de Productos según Nivel de Ventas')
plt.xlabel('Categoría de Desempeño')
plt.ylabel('Cantidad de Productos')
plt.show()

plt.figure(figsize=(10,6))
sns.histplot(ventas_por_producto['importe'], bins=30, kde=True)
plt.title('Distribución de Ingresos por Producto')
plt.xlabel('Importe total vendido')
plt.ylabel('Frecuencia')
plt.show()



plt.figure(figsize=(8,6))
sns.scatterplot(data=ventas_por_producto, x='cantidad', y='importe', alpha=0.7)
plt.title('Relación entre Cantidad Vendida e Importe Total')
plt.xlabel('Cantidad Total Vendida')
plt.ylabel('Importe Total')
plt.show()

# Outliders
def detectar_outliers(col):
    q1 = col.quantile(0.25)
    q3 = col.quantile(0.75)
    iqr = q3 - q1
    limite_inf = q1 - 1.5 * iqr
    limite_sup = q3 + 1.5 * iqr
    return ((col < limite_inf) | (col > limite_sup))

ventas_por_producto['outlier'] = detectar_outliers(ventas_por_producto['cantidad'])
outliers = ventas_por_producto[ventas_por_producto['outlier'] == True]

plt.figure(figsize=(10,6))
sns.boxplot(x=ventas_por_producto['cantidad'])
plt.title('Detección de Outliers en Cantidades Vendidas')
plt.show()

print("Cantidad de productos considerados outliers:", outliers.shape[0])

#Evolucion de ventas en el tiempo
ventas_tiempo = (
    df.groupby('fecha')['importe']
    .sum()
    .reset_index()
    .sort_values('fecha')
)

plt.figure(figsize=(12,6))
sns.lineplot(data=ventas_tiempo, x='fecha', y='importe')
plt.title('Evolución de las Ventas Totales en el Tiempo')
plt.xlabel('Fecha')
plt.ylabel('Importe Total')
plt.show()

'''Analisis de categoria por producto'''
ventas_categoria = (
    ventas_por_producto.groupby('categoria_venta')['importe']
    .sum()
    .sort_values(ascending=False)
)

plt.figure(figsize=(10,6))
sns.barplot(x=ventas_categoria.index, y=ventas_categoria.values, palette='viridis')
plt.title('Ventas Totales por Categoría de Producto')
plt.xlabel('Categoría')
plt.ylabel('Importe Total')
plt.xticks(rotation=45)
plt.show()
