import numpy as np
import matplotlib.pyplot as pl
from sklearn import linear_model

# Datos para ajustar al modelo
x1=[[1],[2],[3],[4],[5],[6]]
y1=[7000, 9000, 5000, 11000, 10000, 13000]

x=[[1],[2],[3],[4],[5],[6], [7]]

# Creamos el objeto LinearRegression (Modelo)
regr = linear_model.LinearRegression()

# Ajustamos a nuestro modelo con los datos
regr.fit(x1,y1)


# Imprimimos el Coeficiente estimado para el problema
print('Coeficiente: \n', regr.coef_, regr.intercept_)
# Utilizamos matplotlib para mostrar el diagrama en pantalla

pl.figure(1)

# El método title asigna un nombre al grafico

# Utilizamos el metodo predict para predecir las futuras ventas

pl.title("Las Ventas para el periodo 7 es equivalente a %s" % regr.predict([[7]]))

# El método plot nos permite trazar la linea

pl.plot(x, regr.predict(x), color='black', linewidth=2)

# El método scatter genera los puntos que conforman al diagrama de dispersión

pl.scatter(x1, y1, s=40, marker='o', color='k')
# Mostramos el punto que predice el modelo (Punto azul)

pl.scatter(7, regr.predict([[7]]))
# Describimos los ejes del gráfico

pl.xlabel('X')
pl.ylabel('Y')
# Asignamos los limites del gráfico

pl.xlim(.0, 8.0)
pl.ylim(.0, 19000)
# Mostramos el gráfico en pantalla

pl.show()