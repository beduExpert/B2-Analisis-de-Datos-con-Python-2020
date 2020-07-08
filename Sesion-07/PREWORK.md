<div style="text-align: right"><strong>Curso Data Analysis - Módulo 4</br>PREWORK de Pruebas A/B y Procesamiento de Lenguaje Natural</strong></div>

<div style="text-align: center; color:#FF0000"><strong>PREWORK</br>SESIÓN 7</strong></div>

### Introducción

En esta sesión vamos a ver un par de temas que es muy importante conocer como científico de datos. Estos 2 temas son muy grandes y complejos como para incluirlos completos en un curso de esta naturaleza, pero después de lo que aprenderás el día de hoy tendrás la preparación suficiente como para explorarlos más a detalle en caso de que algún día lo necesites.

Recuerda siempre que el camino del científico de datos es el camino del eterno aprendizaje. Hay demasiado conocimiento como para aprehenderlo todo de una sola vez. De igual manera, esta disciplina está desarrollándose a velocidades vertiginosas, por lo que todo el tiempo hay que estarse actualizando con los nuevos descubrimientos y las técnicas más modernas. Nunca dejes de aprender, nunca dejes de cuestionar, y recuerda que todo lo que necesites siempre está a una búsqueda en Google de distancia.

#### Objetivos

- Entender la teoría alrededor de las Pruebas A/B, los tests de permutaciones, el Valor P y el Alfa
- Aprender el concepto de Procesamiento de Lenguaje Natural y en qué tipo de datos se aplica

---

### Pruebas A/B

Una prueba A/B (A/B Test) es un experimento con dos grupos de personas para establecer cuál de dos tratamientos, procedimientos, productos, etc, es superior. Este tipo de experimentos es muy común, por ejemplo, cuando se está intentando determinar si un tratamiento médico es superior a otro ya existente, o si el tratamiento tiene algún beneficio real.

En el mundo de la ciencia de datos es muy común hacer pruebas A/B para comparar por ejemplo:

- Interfaces para una web app o una app móvil: queremos saber cuál es más fácil de usar y cuál genera más interacción.
- Precios de un producto: queremos saber qué precio es más adecuado y genera más ventas.
- Diferentes flujos de ventas: queremos saber cuál es más efectivo y cuál genera más clicks.
- Estrategias de marketing: queremos saber cuál genera más clicks en nuestros anuncios y por lo tanto incrementa las ventas.

Hay otros usos pero estos son algunos de los más comunes. Para poder comparar dos tratamientos, procedimientos o productos necesitamos tener dos grupos de personas, donde cada grupo experimenta uno de los tratamientos y el otro grupo experimenta el otro.

En una prueba A/B cada persona que va a probar el tratamiento es un *sujeto*. Los sujetos son asignados *aleatoriamente* a un grupo. Es muy importante que la asignación sea aleatoria para evitar sesgos (sí, la aleatoriedad como mecanismo para controlar los sesgos es un tema muy común, ¿verdad?). Si la asignación es realmente aleatoria sabemos que cualquier diferencia entre los grupos se debe a una de dos razones:

1. El efecto real de los tratamientos
2. Suerte

Uno de los grupos es denominado el *grupo control* y es el grupo al que no se le aplica el tratamiento nuevo que estamos intentando probar. El grupo control experimenta el tratamiento habitual o ningún tratamiento. Es decir, si hemos estado utilizando una estrategia de marketing por un tiempo considerable, esta estrategia la vamos a considerar como la estrategia habitual. El grupo control va a seguir experimentando esta misma estrategia, mientras que el *grupo experimental* es el que recibe el nuevo tratamiento. La razón por la que hacemos esto es para tener una manera de realizar una comparación efectiva. Si todas las personas experimentaran el nuevo tratamiento, no sabríamos si las diferencias (o falta de diferencias) que estamos observando se deben al tratamiento o a otros factores.

Antes de comenzar nuestra prueba A/B es importante haber elegido ya cuál métrica o estadística será utilizada para comparar el comportamiento de nuestros grupos. Esto es muy importante, ya que elegir una métrica **después** de haber realizado la prueba A/B también es una manera de introducir sesgos en nuestro experimento.

### Test de hipótesis o prueba de significación

Un test de hipótesis se utiliza para asegurarnos de que el efecto que hemos observado en nuestros experimentos no fue causado por azar. La mente humana tiene una inclinación natural a observar patrones en datos. Por esta razón necesitamos metodologías que impidan que seamos engañados por el azar.

Cuando realizamos una prueba A/B, la suposición de referencia es llamada *hipótesis nula*. La hipótesis nula es la hipótesis de que cualquier efecto que observemos va a ser causado por el azar. Lo que esperamos es que podamos demostrar que la hipótesis nula no es cierta.

La *hipótesis alternativa* es la hipótesis que queremos comprobar. Es lo que esperamos demostrar como cierto. Por ejemplo, una hipótesis alternativa podría ser:

- Este nuevo precio para nuestro producto genera más ganancias netas
- Esta nueva campaña de marketing genera más clicks
- Esta nueva interfaz mantiene durante más tiempo la atención y el interés de nuestros usuarios

A menos que podamos demostrar que la hipótesis alternativa es cierta, no realizaremos ningún cambio al tratamiento habitual. ¿Cómo entonces comprobamos que la hipótesis alternativa es cierta? ¿Cómo llevamos a cabo el test de hipótesis?

### Test de permutación

Hay varias maneras de intentar comprobar que la hipótesis alternativa es cierta. Nosotros vamos a aprender una de las más comunes, el test de permutación. En un test de permutación, mezclamos los datos de nuestros dos grupos y después realizamos un muestreo sin reposición para configurar dos grupos del mismo tamaño que los anteriores. En estos nuevos grupos revisamos nuestra estadística de interés. De esta manera podemos comparar nuestros hallazgos con los originales y saber si el efecto que observamos fue a causa del azar o del tratamiento.

El algoritmo entonces es el siguiente:

1. Combina los resultados de ambos grupos en un mismo conjunto de datos
2. Revuelve los datos
3. Usando muestreo aleatorio sin reposición, construye un nuevo grupo A del mismo tamaño que el original.
4. El resto de los datos conforman nuestro nuevo grupo B.
5. Cuantifica la métrica o estadística que calculaste con los grupos originales y guarda el resultado.
6. Repite los pasos 1-5 `R` veces para obtener una distribución de la estadística de interés.

Ya que hemos obtenido la distribución muestral de la estadística que nos interesa, hay que comparar nuestro resultado original contra esta distribución. Si el resultado original se encuentra dentro de lo que podríamos considerar un 'valor típico', entonces quiere decir que nuestro resultado está en el rango de lo que podría ser considerado *azaroso*. Si nuestro resultado original es claramente un 'valor atípico', entonces concluimos que el azar no fue responsable de nuestros hallazgos: es decir, es *estadísticamente significativo*.

### Significación estadística

El resultado de un experimento se considera estadísticamente significativo entonces si el valor es más extremo de lo que el azar podría producir. Construyendo la distribución muestral y revisando si nuestro resultado entra dentro de lo que podría considerarse 'típico' o no, nos da una idea de si nuestro resultado pudo haber sido generado por el azar o no. Pero una gráfica no nos da una medida tan precisa. Para tener un valor numérico, podemos obtener algo llamado `Valor P` (P-Valor, P-Value).

#### Valor P

El Valor P es la frecuencia en la que un modelo azaroso produce resultados tan extremos como el que obtuvimos en nuestro experimento. Obtener este valor es sencillo: simplemente calcula la proporción de muestras producidas por el test de permutación que tienen un valor más extremo que el obtenido en tu experimento.

Un malentendido muy común es creer que el Valor P representa la probabilidad de que tu resultado haya sido causado por el azar. Pero esto es un error, lo que realmente nos dice el Valor P es la probabilidad de que, teniendo un modelo generado aleatoriamente, obtengamos un resultado tan extremo como el de nuestro experimento.

#### Alfa (Alpha)

El valor Alfa es el valor con el que determinamos qué tan inusual es nuestro resultado observado. Básicamente es el umbral que nuestro Valor P tiene que pasar para que podamos considerarlo 'estadísticamente significativo'. Normalmente se utilizan Alfas de 5% o 1%. Es decir, si nuestro Alfa es 5% y nuestro valor P es 0.045, esto significa que hay una probabilidad menor al 5% de que un modelo azaroso genere un resultado tan extremo como el nuestro, y por lo tanto lo consideraríamos 'estadísticamente significativo'. Es importantísimo decidir nuestro valor Alfa de antemano, para evitar sesgos a la hora de calcularlo.

Hay mucha controversia alrededor del Valor P, puesto que muchas veces se le ha considerado como 'la prueba irrefutable de que mi hipótesis es cierta', cuando la realidad es que hay que considerar muchas otras cosas para tener cierta certidumbre de que hemos comprobado algo. La realidad es que un Valor P debe de ser complementado con el resto de nuestras herramientas estadísticas, así como con transparencia total, para que pueda ser considerado útil.

Así que la próxima vez que leas que los resultados de un experimento son 'estadísticamente significativos' no pienses que entonces la hipótesis ha sido comprobada. Mejor pregúntate: ¿cómo hicieron el experimento? ¿Qué medidas tomaron para evitar los sesgos? ¿Ha sido ya replicado este experimento? ¿Qué otras medidas estadísticas y visualizaciones están presentando para soportar con mayor solidez su hipótesis?

### Procesamiento de Lenguaje Natural

Hasta ahora todos los análisis que hemos realizado dependen de que nuestros datos sean datos estructurados. Es de alguna manera sencillo aplicar análisis estadístico a datos estructurados porque tienen comportamientos que son más fáciles de predecir. Un número 2 siempre será mayor a un 1. El número 10 siempre se encontrará antes que el número 100. Una categoría binaria sólo tiene dos valores posibles y no hay más que hacerle. ¿Pero qué pasa con el lenguaje que usamos los humanos? ¿Qué tipo de datos son esos?

El lenguaje humano, o lenguaje natural, se considera datos no estructurados porque es bastante más impredecible que los datos estructurados. Aunque hay cierto orden gracias a las reglas gramaticales y de sintaxis, las posibles combinaciones de palabras y los errores gramaticales que podemos encontrar en todas partes hacen que el análisis sea mucho más complicado.

El Procesamiento del Lenguaje Natural incluye una serie de técnicas que han sido desarrolladas para analizar lenguaje natural. Hoy en día se aplica en cosas como detección de lenguaje hablado, comprensión de lenguaje escrito y generación de lenguaje.

#### ¿Reglas o estadística?

Anteriormente, el procesamiento de lenguaje natural se intentó realizar definiendo una serie de reglas que le ayudaran a una computadora a comprender el lenguaje. El problema es que esta aproximación tomaba muchísimo tiempo y no era muy exacta. Desde los 80s y 90s los investigadores de lenguaje natural han acudido a herramientas estadísticas para solucionar este problema.

Por ejemplo, un modelo que traduce entre dos idiomas (como el que usamos constantemente en Google Translate) no fue generado a partir de reglas de traducción. Más bien se entrena un modelo utilizando enormes cantidades de textos que están escritos en ambos idiomas que se pretenden traducir, de manera que el modelo pueda 'aprender' a traducir encontrando patrones en los textos.

Nosotros no vamos a aprender a entrenar este tipo de modelos en este módulo, puesto que eso más bien le atañe al Machine Learning (del cual hablaremos un poco en la siguiente sesión), pero durante el Work aprenderás algunas técnicas sencillas que puedes utilizar para comprender mejor el contenido de textos en lenguaje natural

Puedes leer un poco más acerca del procesamiento de lenguaje natural [aquí](https://www.iic.uam.es/inteligencia/que-es-procesamiento-del-lenguaje-natural/).

---