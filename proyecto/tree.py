#Primero hay que llamar a unas librerías que el programa necesitará.
from pandas import Series, DataFrame
import pandas as pd
import numpy as np
import os
import matplotlib.pylab as plt
from sklearn.cross_validation import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report
import sklearn.metrics

#Después, indicamos en qué directorio vamos a trabajar. Aquí ponéis entre paréntesis vuestro directorio.
#os.chdir(“/home/megumi/data mining/proyecto”)

#Cargamos el fichero de datos. Formato en Excel, csv.
AH_data = pd.read_csv('data.csv')

#Eliminamos los datos con valores missing porque Python no puede hacer árboles con datos missing
data_clean = AH_data.dropna()

#Para comprobar que se ha leído bien, podemos lista las variables en el fichero y sacar los principales estadísticos
data_clean.dtypes
#Principales estadísticos
data_clean.describe()

#Indicamos las variables predictoras y debajo la variable objetivo. Cada uno con los nombres de las variables que tenéis en el fichero csv.
predictors = data_clean[['a', 'b','c','d','e','f']]

targets = data_clean.VAROBJ

#Creamos la muestra de entrenamiento y de test, tanto para predictores como para la variable objetivo, siendo test el 40%
pred_train, pred_test, tar_train, tar_test = train_test_split(predictors, targets, test_size=.4)

#Comprobamos el tamaño de las diferentes muestras (pred=predictora; tar=target, objetivo). La salida en cada caso es una pareja de datos: el tamaño de la muestra y el número de variables
pred_train.shape
pred_test.shape
tar_train.shape
tar_test.shape

#Construimos el árbol con los datos de entrenamiento
classifier=DecisionTreeClassifier()
classifier=classifier.fit(pred_train,tar_train)

#Predecimos para los valores del grupo Test
predictions=classifier.predict(pred_test)

#Pedimos la matriz de confusión de las predicciones del grupo Test. La diagonal de esta matriz se lee: arriba a la izda True Negatives y abajo a la dcha True Positives. 
sklearn.metrics.confusion_matrix(tar_test,predictions)

#Sacamos el índice Accuracy Score, que resume la Matriz de Confusión y la cantidad de aciertos.
sklearn.metrics.accuracy_score(tar_test, predictions)

#Para dibujar el árbol hay que importar otra serie de cosas
from sklearn import tree
from io import StringIO
from IPython.display import Image

#Pintamos el árbol
out = StringIO()
tree.export_graphviz(classifier, out_file='treeMacarena.dot')