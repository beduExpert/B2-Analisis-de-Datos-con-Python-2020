
## Sesión 06: Visualización de Datos Avanzada

### 1. Objetivos

- Aprender a modificar los estilos predeterminados de nuestras gráficas

Conocer y aprender a interpretar las siguientes gráficas:

- Treemaps
- Scatterplots por categorías
- Scatterplots con variables condicionantes
- Binnings Hexagonales
- Mapas cloropléticos
- Gráficas de barras apiladas

### 2. Contenido

<ins>Visualización de Datos Avanzada</ins>

En esta sesión vamos a explorar nuevas y poderosas maneras de visualizar datos. Recuerda que una gráfica sirve para hacer más evidente y clara la información que tenemos en nuestro conjunto de datos. Una visualización sólo tiene sentido si es más fácil de interpretar que los datos en crudo o si agrega información que no podemos obtener de otra manera. Visualizar sólo por el hecho de visualizar a veces hace más daño que otra cosa.

Siempre que hagas una visualización pregúntate a ti mismo: ¿Esta visualización facilita la comprensión e interpretación de mis hallazgos? Si la respuesta es sí, entonces sigue adelante.

>

---

<ins>Estilos</ins>

Cuando agregamos estilos a nuestras gráficas, es importante asegurarnos de que no estamos obscureciendo la información. Agregamos estilos por diversas razones:

1. Para que nuestra gráfica sea más clara
2. Para que sea agradable a la vista
3. Para que sea compatible en estilo al resto de nuestra presentación

Dado que muchas veces nuestros Notebooks sirven para presentar nuestros hallazgos a otros, es importante que sean agradables. Nuestras gráficas pueden ser personalizadas a mucho detalle, pero afortunadamente `matplotlib` y `seaborn` nos ofrecen algunos estilos prehechos que podemos aprovechar.

> 

[**`Ejemplo 1`**](Ejemplo-01/estilos.ipynb)

---

<ins>Treemaps</ins>

Los treemaps son graficas que sirven para visualizar datos jerárquicos usando figuras (normalmente rectángulos) anidadas. Normalmente cada nivel de nuestra jerarquía representa una segmentación utilizando una variable categórica.

Podemos generar treemaps muy fácilmente utilizando la librería `plotly`.

>

[**`Ejemplo 2`**](Ejemplo-02/treemaps.ipynb)
[**`Reto 1`**](Reto-01/treemaps.ipynb)

---

<ins>Variaciones de scatterplots</ins>

--

<ins>Scatterplots por categorías</ins>

Los scatterplots por categorías nos permiten visualizar en una misma gráfica la relación entre dos variables numéricas segmentadas por una variable categórica. La variable categórica se representa de manera visual usando diferentes colores para los puntos de la gráfica. Es muy común realizar scatterplots para visualizar relaciones entre variables y luego colorearlos utilizando una variable dependiente categórica. Así podemos comparar las diferentes categorías de la variable dependiente de manera visual.

>

[**`Ejemplo 3`**](Ejemplo-03/scatterplots_por_categorias.ipynb)

--

<ins>Scatterplots con variables condicionantes</ins>

Hay veces que un scatterplot por categorías no es suficiente para evidenciar las diferencias entre categorías. La razón podría ser que nuestro dataset es demasiado grande o que nuestra variable categórica tiene demasiadas categorías. En estos casos podemos dividir nuestro conjunto de datos utilizando la variable categórica (llamada variable condicionante) y generar un scatterplot independiente para cada una de las categorías. Hay veces que esto resulta más provechoso que graficar todos los datos en la misma gráfica.

>

[**`Ejemplo 4`**](Ejemplo-04/scatterplots_con_variables_condicionantes.ipynb)
[**`Reto 2`**](Reto-02/variaciones_de_scatterplots.ipynb)

--

<ins>Binnings Hexagonales</ins>

Otra variación de los scatterplots son los binnings hexagonales. Estas gráficas resultan muy útiles cuando tenemos tantos datos que resulta imposible visualizar las densidades de puntos sobre la gráfica.

Un binning hexagonal hace lo siguiente:

1. Divide el plano cartesiano en un número determinado de hexágonos.
2. Coloca los puntos del scatterplot sobre el plano.
3. Cuenta cuántos puntos caen en cada hexágono y le asigna ese conteo a cada hexágono.
4. Le asigna a cada hexágono un color dentro de un espectro. Entre más obscuro sea el color, más puntos había sobre de ese hexágono. Entre más claro el color, menos puntos había sobre ese hexágono.

De esta manera resulta mucho más fácil visualizar la densidad de los puntos sobre el plano, ya que el espectro se asigna de manera proporcional.

>

[**`Ejemplo 5`**](Ejemplo-05/binnings_hexagonales.ipynb)

--

<ins>Mapas cloropléticos</ins>

Cuando estamos trabajando con datos geográficos, muchas veces es necesario agregar mapas que ayuden a visualizar datos estadísticos. Una de las visualizaciones más comunes son los mapas cloropléticos (choropleth maps). Los mapas cloropléticos se parecen de alguna manera a los mapas de calor. Primero dividimos nuestro mapa en regiones (lo más común es dividir por estados o por países ). Luego coloreamos cada región de acuerdo a un espectro de color que representa la segmentación de una variable estadística.

>

[**`Ejemplo 6`**](Ejemplo-06/mapas_cloropleticos.ipynb)
[**`Reto 3`**](Reto-03/mapas_cloropleticos.ipynb)

--

<ins>Gráficas de barras apiladas</ins>

En la misma vena que los scatterplots por categorías tenemos a las gráficas de barras apiladas. Una gráfica de barras apilada se utiliza para graficar un valor numérico segmentado a partir de dos variables categóricas. La primera categoría es la que se utiliza para definir los valores del eje `x`. La segunda categoría se utiliza para dividir las barras en segmentos.

>

[**`Ejemplo 7`**](Ejemplo-07/graficas_de_barras_apiladas.ipynb)
[**`Reto 4`**](Reto-04/graficas_de_barras_apiladas.ipynb)

---

### 3. Postwork

[**`Postwork Sesión 6`**](Postwork/Readme.md)
