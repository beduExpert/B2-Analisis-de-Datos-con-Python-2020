
## Sesión 08: Introducción a Machine Learning: Clasificación No Supervisada y Supervisada

### 1. Objetivos

- Conocer la definición de Machine Learning, qué es y cómo se utiliza
- Aplicar un algoritmo de K-Medias
- Interpretar los resultados de K-Medias
- Aplicar un algoritmo de Regresión Logística
- Evaluar un modelo de Regresión Logística utilizando matriz de confusión y curva ROC / AUC

### 2. Contenido

---

<ins>¿Qué es Machine Learning?</ins>

Machine Learning es el estudio de algoritmos por computadora que mejoran automáticamente a través del entrenamiento y la experiencia. Se llama Machine **Learning** justamente por que este proceso de mejora y actualización a través de la experiencia es lo que hacemos nosotros los humanos cuando aprendemos. Los algoritmos de Machine Learning construyen modelos matemáticos a partir de conjuntos de datos con los que se entrenan, para poder realizar predicciones o decisiones basándose en los patrones que hayan encontrado. Un humano no programa explícitamente el comportamiento de un algoritmo de Machine Learning, sólo decide sus parámetros de entrenamiento y elige el conjunto de datos con el que se le va a entrenar.

Algunas de las cosas que podemos hacer con Machine Learning son:

1. Predicción: predecir qué va a suceder en el futuro o predecir cómo se va a comportar una variable si modificamos otras variables.
2. Clasificación: clasificar una muestra univariada o multivariable dependiendo de sus características.
3. Generación: aprender patrones de nuestros datos para poder generar nuevos datos que sean similares a los originales.
4. Aprendizaje no Supervisado: aprender a realizar acciones o tomar decisiones a partir de la vivencia de una situación específica.

Vamos a comentar las siguientes preguntas:

1. ¿Qué ejemplos conocen de cada una de estas categorías?
2. ¿En qué cosas de las que usamos día con día encontramos modelos de Machine Learning?
3. ¿Sabes cuál es la diferencia entre Machine Learning e Inteligencia Artificial?
4. ¿Sabes cuál es la diferencia entre Machine Learning y Deep Learning (Aprendizaje Profundo)?
5. ¿Cómo crees que el uso de Machine Learning pueda cambiar el mundo en el que vivimos?
6. ¿Crees que el cambio sea para bien o para mal?

> 

---

<ins>Agrupamiento por K-Medias (Clasificación No Supervisada)</ins>

El agrupamiento por K-Medias pertenece a la categoría de algoritmos de clasificación no supervisada. Resulta muy útil cuando tenemos un dataset que queremos dividir por grupos pero no sabemos exactamente qué grupos queremos y cuáles son sus características. Lo único que tenemos que decidir de antemano es *cuántos* grupos queremos, y el algoritmo intentará agrupar nuestros datos en esa cantidad de grupos.

Clasificación No Supervisada quiere decir que no tenemos un conjunto de datos etiquetado de antemano. Por lo tanto, a menos que estemos dispuestos a revisar nuestro conjunto dato por dato y etiquetarlo de acuerdo a nuestros propios parámetros, la única forma de clasificar nuestros datos es utilizando un algoritmo de clasificación no supervisada.

> 

[**`Ejemplo 1`**](Ejemplo-01/k_medias.ipynb)
[**`Reto 1`**](Reto-01/k_medias.ipynb)

---

<ins>Regresión Logística (Clasificación Supervisada)</ins>

La regresión logística nos sirve para resolver problemas de clasificación binaria supervisada.

- *Binaria* significa que los datos pueden ser clasificados solamente en dos categorías: positivo y negativo (sí y no; 0 y 1).
- *Supervisada* significa que sabemos exactamente cuáles son las dos categorías en las que queremos agrupar a nuestros datos, y que además tenemos un conjunto de datos de entrenamiento que ha sido clasificado de antemano.

¿Por qué se llama Regresión al igual que la Regresión Lineal? La Regresión Logística también busca la ecuación de una línea, pero luego pasa el resultado por otro tipo de función que nos da un resultado probabilístico. Las probabilidades se encuentran en un intervalo entre 0 y 1. Para decidir cuál de las dos clasificaciones regresar como resultado, definimos un *umbral* entre 0 y 1. Por ejemplo, podemos definir un umbral de 0.4. Entonces, cada vez que obtenemos una probabilidad menor a 0.4, regresamos la clasificación negativa (no; 0); de igual manera, cada vez que obtenemos un valor mayor a 0.4, regresamos una clasificación positiva (sí; 1).

> 

[**`Ejemplo 2`**](Ejemplo-02/regresion_logistica.ipynb)
[**`Reto 2`**](Reto-02/regresion_logistica.ipynb)

---

<ins>Matriz de confusión</ins>

Para evaluar un modelo de clasificación binaria podemos utilizar algo llamado matriz de confusión. Una matriz de confusión se ve así:

<div style="padding: 10px; margin: 20px"><img src='./Imgs/sesion_8-6.png'></div>

Es una matriz de 2x2 donde el eje x son los resultados estimados por el modelo entrenado y el eje y es la realidad (las etiquetas originales en nuestro dataset de prueba).

Analicemos a detalle esta matriz de confusión.

> 

[**`Ejemplo 3`**](Ejemplo-03/matriz_de_confusion.ipynb)
[**`Reto 3`**](Reto-03/matriz_de_confusion.ipynb)

---

<ins>Curva ROC / AUC</ins>

La curva ROC / AUC es un método de evaluación de modelos de clasificación utilizando diferentes *umbrales*. Una gráfica de curva ROC / AUC se ve así:

<div style="padding: 10px; margin: 20px"><img src='./Imgs/sesion_8-9.png'></div>

Veamos esta gráfica con más detalle.

> 

[**`Ejemplo 4`**](Ejemplo-04/curva_roc_auc.ipynb)
[**`Reto 4`**](Reto-04/curva_roc_auc.ipynb)

---

### 3. Postwork

[**`Postwork Sesión 8`**](Postwork/Readme.md)
