import pandas as pd
import matplotlib.pyplot as plt

# Datos de ejemplo (fecha, precio de cierre)
data = {
    'Fecha': pd.date_range(start='2023-01-01', end='2023-12-31', freq='B'),
    'PrecioCierre': [100, 105, 110, 95, 120, 115, 105, 110, 112, 108, 115, 120]
}

df = pd.DataFrame(data)
df.set_index('Fecha', inplace=True)

# Crear el gráfico de trading
fig, ax = plt.subplots(figsize=(10, 6))

# Gráfico de precios de cierre
ax.plot(df.index, df['PrecioCierre'], label='Precio de Cierre', color='blue')

# Marcar puntos de compra y venta (ejemplo)
compras = df[df['PrecioCierre'] < df['PrecioCierre'].shift(1)]
ventas = df[df['PrecioCierre'] > df['PrecioCierre'].shift(1)]

ax.scatter(compras.index, compras['PrecioCierre'], marker='^', color='green', label='Compra')
ax.scatter(ventas.index, ventas['PrecioCierre'], marker='v', color='red', label='Venta')

# Configuración adicional
ax.set_title('Gráfico de Trading')
ax.set_xlabel('Fecha')
ax.set_ylabel('Precio de Cierre')
ax.legend()

# Mostrar el gráfico
plt.show()
