import pandas as pd

'''
1.Descarga del Archivo de Datos:
    Se te proporcionará un archivo Excel (datos_ventas.xlsx) que contiene información sobre ventas de una empresa.
    
    Obtener las columnas:
    ID_Venta: Identificador único de la venta
    Fecha: Fecha de la venta
    Producto: Nombre del producto
    Cantidad: Cantidad vendida
    Precio_Unitario: Precio por unidad
    Total_Venta: Monto total de la venta (posiblemente con valores faltantes)
    Vendedor: Nombre del vendedor'''

columnas_para_vista = ["ID_Venta", "Fecha", "Producto", "Cantidad", "Precio_Unitario", "Total_Venta","Vendedor"]

'''2.1 Cargar los datos en un DataFrame usando pandas.'''

datos_de_ventas = pd.read_excel("datos_ventas.xlsx", usecols=columnas_para_vista)

'''2.2 Verificar y manejar valores faltantes (NaN), completando Total_Venta cuando sea necesario (Cantidad * Precio_Unitario).'''

datos_de_ventas['Total_Venta'] = datos_de_ventas['Total_Venta'].fillna(datos_de_ventas['Cantidad']*datos_de_ventas['Precio_Unitario'])

print(datos_de_ventas)
