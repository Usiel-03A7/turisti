#importamos las librerias que sean necesarias para las siguietes practicas

import numpy as np
from numpy.random import randn
from numpy.random.mtrand import rand, random
import pandas as pd
from pandas.core.frame import DataFrame
import random
import matplotlib.pyplot as plt

#array 1: Debe contener datos dentro del rango de  350,000 a 1'250,000.
#array 2: Debe contener datos dentro del rango de  -10 a 10.
#array 3: Debe contener datos dentro del rango de  150 a 5000.

array1=[random.randint(350000,1250000)for p in range(0,10000)] 
array2=[random.randint(-10,10)for p in range(0,10000)]
array3=[random.randint(150,5000)for p in range(0,10000)]
 
#- Exportar los tres arreglos a un solo  DataFrame de pandas y agregar al encabezado de cada arreglo el
# nombre que a continuacion se determina:

indices=['valor','Calificacion','Area']
df1=pd.DataFrame(array1)
df2=pd.DataFrame(array2)
df3=pd.DataFrame(array3)


df4=np.concatenate((df1,df2,df3),1)
df5=pd.DataFrame(df4,columns=indices)


 #- Buscar en la columna de Calificacion del DataFrame cada elemento que tenga símbolo negativo o menor o igual a 0 
 # (<=0) y elevar el numero al cuadrado para después aplicar la raíz cuadrada y el resultado guardarlo en la misma 
 # posición.

df5[df5 <=0 ]=df5**2 
df5[df5 <=0 ]=df5 ^2 


 #- Buscar en la columna de Valor del DataFrame aquellos elementos que sobrepasen del del 1'150,000 y eliminar 
 # toda la fila en la que se encuentra el dato en cuestión

df6 =df5[df5["valor"]>1150000].index
df6 =df5.drop(df6)

#- Reemplazar el por 6 en la columna calificación todos los elementos cuyo valor sea 0.

df5[df5 == 0] = 6

# - Obtener los percentiles 25, 50 y 75  del DataFrame. (tomar screenshot o captura de pantalla del resultado y 
# anexarlo a esta actividad ).

p_1=np.percentile(df5,25)
p_2=np.percentile(df5,50)
p_3=np.percentile(df5,75)


print('Porcentjes')
print('25 porciento',p_1)
print('50 porciento',p_2)
print('75 porciento',p_3)

print(df5)

#- Exportar el DataFrame a un archivo que lleve el nombre de  resultado.csv y adjuntarlo a esta actividad.
  
df5.to_csv('Resultados.csv')

#-Graficar en matplotlib la columna Valor y Calificación en los ejes X y Y respectivamente utilizando por lo menos 2 
# marcadores de matplotlib. (Guardar la grafica y anexarla a esta actividad bajo el nombre de "producto1")

df=pd.read_csv('Resultados.csv')

fig,ax=plt.subplots(2,figsize=(10,66))
ax[0].scatter(x=df['Calificacion'],y=df['valor'])
ax[0].set_xlabel('Calificacion')
ax[0].set_ylabel('Valor')


#-Graficar en matplotlib la columna Valor y Area en los ejes X y Y respectivamente utilizando por lo menos 2 
# marcadores de matplotlib.(Guardar la grafica y anexarla a esta actividad  bajo el nombre de "producto2")


df=pd.read_csv('Resultados.csv')
ax[1].scatter(x=df['valor'],y=df['Area'])
ax[1].set_xlabel('valor')
ax[1].set_ylabel('Area')

plt.show()
 