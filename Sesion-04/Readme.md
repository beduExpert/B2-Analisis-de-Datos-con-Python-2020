
## Sesión 04: Correlaciones y Regresión Linear Simple

### 1. Objetivos

- Comprender el concepto de correlación entre variables y por qué es relevante.
- Comprender el significado del coeficiente de correlación e interpretarlo.
- Hacer matrices de correlaciones y a graficarlas usando heatmaps.
- Hacer gráficas de dispersión e interpretarlas.
- Aprender el concepto de Gráficas de Pares.
- Aprender el concepto de Regresión Linear Simple y cómo funciona el proceso de entrenamiento e interpretación.

### 2. Contenido

<ins>Correlaciones y el coeficiente de correlación de Pearson</ins>

Decimos que dos variables están correlacionadas positivamente si el aumento de valores en una de ellas está relacionado con el aumento de valores en la otra; y si la disminución de valores en una está relacionado a la disminución de valores en la otra.

En cambio, decimos que está correlacionadas negativamente si el aumento en los valores de una está relacionado a la disminución de los valores en la otra, y viceversa.

En esta sesión aprenderemos a calcular el coeficiente de correlación de Pearson para cuantificar la correlación entre dos variables numéricas.

>

[**`Ejemplo 1`**](Ejemplo-01/coeficiente_de_pearson.ipynb)
[**`Reto 1`**](Reto-01/coeficiente_de_pearson.ipynb)

---

<ins>Matriz de correlaciones y mapas de calor</ins>

Revisar nuestras correlaciones una por una es algo lento. Además dificulta la comparación entre múltiples variables. ¿Te has dado cuenta de que este tema de la comparación aparece una y otra vez? Las comparaciones nos dan puntos de referencia para evaluar las magnitudes de los fenónemos que observamos.

Vamos a aprender cómo generar coeficientes de correlación para muchas variables al mismo tiempo.

>

[**`Ejemplo 2`**](Ejemplo-02/matriz_de_correlaciones.ipynb)
[**`Reto 2`**](Reto-02/matriz_de_correlaciones.ipynb)

---

<ins>Scatterplots o gráficas de dispersión</ins>

Ya viste varios scatterplots en Ejemplos y Retos anteriores. Ahora vas a aprender a hacerlos con tus propias manos. Un scatterplot es una gráfica de dos variables donde cada punto representa una muestra conformada por un valor `x` y un valor `y`.

Las gráficas de dispersión resultan muy útiles en la búsqueda de relaciones entre variables.

>

[**`Ejemplo 3`**](Ejemplo-03/graficas_de_dispersion.ipynb)
[**`Reto 3`**](Reto-03/graficas_de_dispersion.ipynb)

---

<ins>Pairplots o Gráficas de Pares</ins>

Existe un tipo de gráfica llamada Pairplot que nos permite de una manera muy rápida visualizar las relaciones bivariadas entre un conjunto de variables.

Veamos cómo puede complementar a una matriz de correlación para facilitar nuestros análisis.

>

[**`Ejemplo 4`**](Ejemplo-04/pairplots.ipynb)

---

<ins>Regresión Lineal Simple</ins>

Después de haber analizado a mucha profundidad las relaciones bivariadas existentes en nuestro dataset podemos preguntarnos si será posible que la relación entre dos variables sea tan fuerte como para poder prededir una a partir de la otra.

La predicción se ha vuelto muy solicitada en el mundo últimamente y la regresión lineal simple es el algoritmo más básico y sencillo para intentar realizarla.

Veamos qué significa hacer una regresión lineal simple y cómo aplicarla.

>

[**`Ejemplo 5`**](Ejemplo-05/regresion_lineal_simple.ipynb)
[**`Reto 4`**](Reto-04/regresion_lineal_simple.ipynb)

---

### 3. Postwork

[**`Postwork Sesión 4`**](Postwork/Readme.md)
