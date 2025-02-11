import pandas as pd

'''
1.1 Se te proporcionará un archivo Excel (datos_ventas.xlsx) que contiene información sobre ventas de una empresa.

1.2 Obtener las columnas:

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

'''2.3 Convertir la columna Fecha a formato datetime.'''

datos_de_ventas['Fecha'] = pd.to_datetime(datos_de_ventas['Fecha'])

'''2.4 Filtrar las ventas del año 2023.'''

datos_de_ventas = datos_de_ventas[datos_de_ventas['Fecha'].dt.year == 2023]

'''2.5 Agregar una nueva columna Mes con el mes en formato numérico extraído de Fecha.'''

datos_de_ventas['Mes']=datos_de_ventas['Fecha'].dt.month

'''2.6 Calcular el total de ventas por vendedor y por mes.'''

total_ventas_vendedor = datos_de_ventas.groupby('Vendedor')['Total_Venta'].sum().reset_index()

total_ventas_mes = datos_de_ventas.groupby('Mes')['Total_Venta'].sum().reset_index()

'''
3. Calcular el total de ventas por vendedor y por mes.
    Generación de un Nuevo Archivo Excel:
    Crear un nuevo archivo Excel (resumen_ventas.xlsx) con dos hojas:
    "Resumen_Ventas": Contiene el total de ventas por vendedor.
    "Ventas_Mensuales": Contiene el total de ventas por mes.
'''

try:

    with pd.ExcelWriter('resumen_ventas.xlsx') as writer:

        total_ventas_vendedor.to_excel(writer,sheet_name='Resumen_Ventas',index=False)
        total_ventas_mes.to_excel(writer,sheet_name='Ventas_Mensuales',index=False)

    print("El resumen de ventas se genero exitosamente.")

except:

    print("La hoja de datos de ventas presenta errores, no se ha podido generar el archivo")
