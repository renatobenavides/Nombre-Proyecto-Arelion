# Codigo reorganizado con menu extendido
# Sin acentos, estilo argentino, respetando tu logica original
# Solo se reordena y se agregan mas items al menu

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import precision_score, recall_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import roc_curve, roc_auc_score
import seaborn as sns
import matplotlib.pyplot as plt


###########################################################
# 1. TEXTOS Y MENU
###########################################################

def obtener_textos_documentacion():
    textos = {
        '1': """
### 1. Tema, problema y solucion
TEMA: Identificacion de productos con baja rotacion.
PROBLEMA: La falta de un analisis consistente impide tomar decisiones.
SOLUCION: Identificar productos con baja demanda para mejorar stock.
""",
        '2': """
### 2. Dataset de referencia
Tablas:
- detalle_ventas
- productos
- ventas
- clientes
""",
        '3': """
### 3. Estructura por tabla
Detalle_ventas (~344 filas)
Campos principales: id_venta, id_producto, cantidad, importe
""",
        '4': """
### 4. Escalas de medicion
- Nominal
- Razon
- Intervalo
- Ordinal
""",
        '5': """
### 5. Sugerencias con Copilot
- Separar documentacion en plantillas
- Automatizar generacion de reportes
"""
    }
    return textos


def mostrar_menu():
    print("\n------ MENU PRINCIPAL ------")
    print("1. Informacion del problema")
    print("2. Dataset de referencia")
    print("3. Estructura de tablas")
    print("4. Escalas de medicion")
    print("5. Sugerencias con Copilot")
    print("6. Mostrar graficos: rotacion")
    print("7. Mostrar graficos: productos menos rentables")
    print("8. Mostrar graficos: series mensuales (5 menos vendidos)")
    print("9. Mostrar graficos: scatter rotacion vs importe")
    print("10. Ejecutar modelo de regresion logistica")
    print("11. Salir")
    print("----------------------------")


def iniciar_menu(contexto):
    textos_menu = obtener_textos_documentacion()
    MAX_INTENTOS = 3
    intentos_invalidos = 0

    while True:
        mostrar_menu()
        opcion = input("Selecciona una opcion (1-11): ").strip()

        if opcion in textos_menu:
            print(textos_menu[opcion])
            intentos_invalidos = 0

        elif opcion == '6':
            contexto['graficos_rotacion']()

        elif opcion == '7':
            contexto['graficos_menos_rentables']()

        elif opcion == '8':
            contexto['graficos_series_mensuales']()

        elif opcion == '9':
            contexto['scatter_rotacion_importe']()

        elif opcion == '10':
            contexto['ejecutar_modelo']()

        elif opcion == '11':
            print("Saliendo del menu...")
            break

        else:
            intentos_invalidos += 1
            if intentos_invalidos >= MAX_INTENTOS:
                print("Demasiados intentos invalidos. Cerrando.")
                break
            print("Opcion invalida. Intenta nuevamente.")


###########################################################
# 2. CARGA DE DATOS (MISMO CODIGO QUE TENIAS)
###########################################################

clientes = pd.read_excel('clientes.xlsx')
productos = pd.read_excel('CopiaDeProductos.xlsx')
detalle_venta = pd.read_excel('detalle_ventas.xlsx')
ventas = pd.read_excel('ventas.xlsx')

# Merge original

df = detalle_venta.merge(productos, on='id_producto', how='left', suffixes=('_venta', '_producto'))
df = df.merge(ventas[['id_venta', 'fecha', 'id_cliente', 'medio_pago']], on='id_venta', how='left')
df = df.merge(clientes[['id_cliente', 'ciudad']], on='id_cliente', how='left')

df = pd.get_dummies(df, columns=['ciudad'], prefix='ciudad')
df = pd.get_dummies(df, columns=['medio_pago'], prefix='medio_pago')
df['fecha'] = pd.to_datetime(df['fecha'])

# outliers

def detectar_outliers(col):
    q1 = col.quantile(0.25)
    q3 = col.quantile(0.75)
    iqr = q3 - q1
    lim_inf = q1 - 1.5 * iqr
    lim_sup = q3 + 1.5 * iqr
    return (col < lim_inf) | (col > lim_sup)

df['outlier'] = detectar_outliers(df['cantidad'])
df = df[df['outlier'] == False].copy()

# rotacion

df = df.sort_values(by=['nombre_producto_venta', 'fecha'])
df['rotacion_dias'] = df.groupby('nombre_producto_venta')['fecha'].diff().dt.days
df['rotacion_dias'] = df['rotacion_dias'].fillna(0)

df['mes'] = df['fecha'].dt.to_period('M')


###########################################################
# 3. FUNCIONES DE GRAFICOS
###########################################################

def graficos_rotacion():
    plt.figure(figsize=(10,5))
    sns.histplot(data=df, x='rotacion_dias', bins=40, kde=True)
    plt.title('Distribucion de rotacion de productos')
    plt.tight_layout()
    plt.show()


def graficos_menos_rentables():
    ventas_prod = df.groupby('nombre_producto_venta')[['cantidad','importe']].sum().reset_index()
    ventas_prod = ventas_prod.sort_values(by='importe')
    menos = ventas_prod.head(10)

    plt.figure(figsize=(10,6))
    sns.barplot(data=menos, x='importe', y='nombre_producto_venta', palette='Reds_r')
    plt.title('Top 10 productos que menos ingresos generaron')
    plt.tight_layout()
    plt.show()


def graficos_series_mensuales():
    ventas_prod = df.groupby('nombre_producto_venta')[['cantidad','importe']].sum().reset_index()
    menos = ventas_prod.sort_values(by='importe').head(5)
    lista = menos['nombre_producto_venta'].tolist()

    df_sub = df[df['nombre_producto_venta'].isin(lista)]

    ventas_mens = df_sub.groupby(['mes','nombre_producto_venta'])['cantidad'].sum().reset_index()

    plt.figure(figsize=(12,6))
    sns.barplot(data=ventas_mens, x='mes', y='cantidad', hue='nombre_producto_venta')
    plt.title('Cantidad vendida por mes - 5 menos vendidos')
    plt.tight_layout()
    plt.show()


def scatter_rotacion_importe():
    ventas_prod = df.groupby('nombre_producto_venta')[['cantidad','importe']].sum().reset_index()
    menos = ventas_prod.sort_values(by='importe').head(5)
    lista = menos['nombre_producto_venta'].tolist()

    df_sub = df[df['nombre_producto_venta'].isin(lista)]

    plt.figure(figsize=(10,6))
    sns.scatterplot(data=df_sub, x='rotacion_dias', y='importe', hue='nombre_producto_venta')
    plt.title('Relacion entre rotacion y monto vendido (5 menos vendidos)')
    plt.tight_layout()
    plt.show()


###########################################################
# 4. MODELO DE MACHINE LEARNING
###########################################################

def ejecutar_modelo():
    print('\nEjecutando modelo de regresion logistica...')

    df_tmp = df.copy()
    df_tmp['total_cantidad'] = df_tmp.groupby('id_producto')['cantidad'].transform('sum')
    df_tmp['total_importe'] = df_tmp.groupby('id_producto')['importe'].transform('sum')
    df_tmp['total_transacciones'] = df_tmp.groupby('id_producto')['id_venta'].transform('nunique')

    umbral = df_tmp['total_transacciones'].median()
    df_tmp['baja_rotacion'] = (df_tmp['total_transacciones'] < umbral).astype(int)

    X = df_tmp[['cantidad','importe','rotacion_dias']]
    y = df_tmp['baja_rotacion']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

    scaler = StandardScaler()
    X_train_s = scaler.fit_transform(X_train)
    X_test_s = scaler.transform(X_test)

    modelo = LogisticRegression(max_iter=1000)
    modelo.fit(X_train_s, y_train)

    y_pred = modelo.predict(X_test_s)

    print('Precision:', precision_score(y_test, y_pred))
    print('Recall:', recall_score(y_test, y_pred))

    cm = confusion_matrix(y_test, y_pred)
    plt.figure(figsize=(5,4))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
    plt.title('Matriz de confusion')
    plt.show()

    y_prob = modelo.predict_proba(X_test_s)[:,1]
    fpr, tpr, _ = roc_curve(y_test, y_prob)
    auc = roc_auc_score(y_test, y_prob)

    plt.figure(figsize=(6,5))
    plt.plot(fpr, tpr, label=f'AUC = {auc:.3f}')
    plt.plot([0,1],[0,1],'--')
    plt.title('Curva ROC')
    plt.legend()
    plt.show()


###########################################################
# 5. INICIO DEL PROGRAMA
###########################################################

contexto = {
    'graficos_rotacion': graficos_rotacion,
    'graficos_menos_rentables': graficos_menos_rentables,
    'graficos_series_mensuales': graficos_series_mensuales,
    'scatter_rotacion_importe': scatter_rotacion_importe,
    'ejecutar_modelo': ejecutar_modelo
}

if __name__ == '__main__':
    iniciar_menu(contexto)
