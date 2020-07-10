<div style="text-align: right"><strong>Curso Data Analysis - Módulo 4</br>PREWORK de Estimados de Locación y Variabilidad</strong></div>

<div style="text-align: center; color:#FF0000"><strong>PREWORK</br>SESIÓN 1</strong></div>

### Introducción

¡Bienvenido al módulo de Data Analysis con Python! Este módulo está enfocado en dos áreas de la Ciencia de Datos:

1. Análisis Estadístico
2. Visualización de Datos

Usando las técnicas que aprenderás en este módulo serás capaz de extraer información útil de un conjunto de datos y presentarla de maneras comprensibles y atractivas.

Todos los conjuntos de datos que usaremos en este módulo habrán sido limpiados con anterioridad, para que podamos concentrarnos en los conocimientos nuevos que vamos a adquirir.

El Procesamiento de Datos, que fue el tema del módulo anterior, estará siempre presente a cada paso del proceso, puesto que no hay una separación absoluta entre Procesamiento, Exploración, Análisis y Visualización. De todas maneras, se ha hecho un gran esfuerzo por eliminar la necesidad de Procesamiento lo más posible.

¡Mucha suerte!

#### Objetivos

- Utilizar Google Colab en conjunción con Google Drive y Github.
- Identificar tipos de datos estructurados existen.
- Identificar los estimados de locación y en qué momento son útiles.
- Identificar valores típicos y atípicos.
- Realizar cálculos estadísticos robustos.
- Identificar los estimados de variabilidad y en qué momento son útiles.
- Identificar los estadísticos de orden.

---

**Si tomaste el módulo anterior y sabes cómo usar Google Colab, cómo leer conjuntos de datos desde Google Drive y cómo acceder a los Retos del módulo directamente desde el repositorio, puedes saltarte la siguiente sección**

---

### Software que vamos a usar

Para realizar los ejercicios de este módulo vamos a usar Jupyter Notebooks, Google Drive y Google Colab. A continuación vamos a ver como realizar la preparación de estas herramientas para que puedas sacar el mejor provecho.

### Creando un Acceso Directo hacia los Datasets

Dado que este es un curso de Análisis de Datos, es obvio que vamos a estar usando muchos conjuntos de datos.

Para poder acceder a ellos durante el módulo, lo primero que necesitas es una cuenta de Google Drive. Si aún no tienes una puedes ir a [este link](https://accounts.google.com/signup/v2/webcreateaccount?service=writely&continue=https%3A%2F%2Faccounts.google.com%2FManageAccount%3Fnc%3D1&gmb=exp&biz=false&flowName=GlifWebSignIn&flowEntry=SignUp) para crear una. Ya que hayas creado tu cuenta, puedes proseguir con los siguientes pasos.

Los conjuntos de datos que vamos a usar se encuentran [aquí](https://drive.google.com/drive/u/1/folders/1oXUNacyjuHpGBkmESnKIDA5s03UnS8Vg). Accede al link para ir a la carpeta donde están guardados los datasets de la sesión. Verás algo como esto (puede ser un poco distinto):

<div style="padding: 10px; margin: 20px"><img src='./Imgs/pre_1.png'></div>

En caso de que no hayas hecho login en tu cuenta de Drive, hazlo ahora usando la cuenta que creaste en un paso anterior. Es importante que accedas a la carpeta de Datasets y hagas login desde tu cuenta para poder realizar los pasos siguientes.

Da click en la parte superior, donde está el nombre de la carpeta "Datasets". El siguiente menú se desplegará:

<div style="padding: 10px; margin: 20px"><img src='./Imgs/pre_2.png'></div>

Ahora, lo único que vamos a hacer es agregar un Acceso Directo desde nuestro Drive a esta carpeta. Da click en "Add Shortcut To Drive" (o "Agrega Acceso a Directo a tu Drive") y verás esto:

<div style="padding: 10px; margin: 20px"><img src='./Imgs/pre_3.png'></div>

Elige el lugar en tu Drive donde quieres crear el Acesso Directo y da click en "Add Shortcut" (o "Agregar Acceso Directo"):

<div style="padding: 10px; margin: 20px"><img src='./Imgs/pre_4.png'></div>

Listo, ahora puedes acceder a esta carpeta "Datasets" desde tu Google Drive.

Vamos a ver ahora cómo vamos a aprovechar esto desde Google Colab.

### Google Colab

#### Leyendo los Datasets desde Google Colab

Ve a [este link](https://colab.research.google.com/notebooks/intro.ipynb) para acceder a Google Colab.

Primero vamos a aprender cómo acceder a la carpeta Datasets desde Google Colab.

Da click en "File/New Notebook":

<div style="padding: 10px; margin: 20px"><img src='./Imgs/pre_5.png'></div>

Acabas de crear un Jupyter Notebooks (no te preocupes, ya aprenderemos cómo usarlo).

Vamos a aprender a conectar nuestro Notebook con Google Drive.

Primero, da click en la carpetita que aparece en el menú de la izquierda:

<div style="padding: 10px; margin: 20px"><img src='./Imgs/pre_6.png'></div>

Aparecerá algo como esto:

<div style="padding: 10px; margin: 20px"><img src='./Imgs/pre_7.png'></div>

Da click en "Mount Drive" (o "Montar Drive") y una celda como la siguiente aparecerá:

<div style="padding: 10px; margin: 20px"><img src='./Imgs/pre_8.png'></div>

Da click en el botón de Play y obtendrás lo siguiente:

<div style="padding: 10px; margin: 20px"><img src='./Imgs/pre_12.png'></div>

Sigue el "url" y has login con tu cuenta de Google:

<div style="padding: 10px; margin: 20px"><img src='./Imgs/pre_9.png'></div>

Una vez que hagas login, verás una pantalla como ésta:

<div style="padding: 10px; margin: 20px"><img src='./Imgs/pre_13.png'></div>

Copia el código y luego regresa a tu Jupyter Notebook. Pega el código en donde te piden que lo hagas y pulsa "Enter". Listo:

<div style="padding: 10px; margin: 20px"><img src='./Imgs/pre_10.png'></div>

Ahora, en el menú de la izquierda pica "Refresh" o "Refrescar" y verás tu Drive montado:

<div style="padding: 10px; margin: 20px"><img src='./Imgs/pre_11.png'></div>

Si vas a la ruta donde creaste tu Acceso Directo, ¡puedes ver que todos los datasets están disponibles desde ahí!

<div style="padding: 10px; margin: 20px"><img src='./Imgs/pre_14.png'></div>

Esto todavía no te va a hacer mucho sentido, pero si yo quisiera leer un dataset desde mi programa, sólo tendría que hacer algo como esto:

<div style="padding: 10px; margin: 20px"><img src='./Imgs/pre_15.png'></div>

Ya aprendemos a leer archivos más adelante, pero lo importante es que sepas que ya tienes acceso desde Google Colab a todos los conjuntos de datos del módulo. Cada vez que abras un nuevo Jupyter Notebooks, tendrás que volver a realizar el montado de tu Google Drive.

#### Abriendo los Retos del módulo desde Google Colab

Vamos a ver ahora cómo vamos a abrir los Retos del módulo usando Google Colab. Es muy sencillo.

Primero que nada, necesitas el link del repositorio donde están guardados todos los Retos. El link es el siguiente: https://github.com/beduExpert/B2-Analisis-de-Datos-con-Python-2020.git.

Ahora, en Google Colab, da click en "File/Open Notebook":

<div style="padding: 10px; margin: 20px"><img src='./Imgs/pre_16.png'></div>

Verás algo como esto:

<div style="padding: 10px; margin: 20px"><img src='./Imgs/pre_17.png'></div>

Da click en la pestaña de Github, pega el link del repositorio y da "Enter". Verás algo así:

<div style="padding: 10px; margin: 20px"><img src='./Imgs/pre_18.png'></div>

Ahora puedes leer los archivos del repositorio desde Google Colab. ¡Genial! Para todos los ejercicios que hagas, asegúrante de elegir la branch "student", para que tengas acceso a los archivos correctos:

<div style="padding: 10px; margin: 20px"><img src='./Imgs/pre_19.png'></div>

Ahora, simplemente tienes que elegir el archivo que quieras leer. Google Colab sólo puede leer achivos de tipo `.ipynb`. Por ejemplo, si quiero acceder al primer Reto de la Sesión 1, tendría que abrir este archivo:

<div style="padding: 10px; margin: 20px"><img src='./Imgs/pre_20.png'></div>

Si doy click, el Reto se abre y estoy listo:

<div style="padding: 10px; margin: 20px"><img src='./Imgs/pre_21.png'></div>

---

**Aquí finalizan las instrucciones de uso de Google Colab, Google Drive y Github. A partir de aquí todo el material es nuevo.**

---

### Requisitos

En este módulo se asume que ya sabes utilizar tanto Jupyter Notebooks como la librería `pandas`. Si tienes alguna duda sobre cómo funcionan esas herramientas, puedes visitar los siguientes links:

- [Intro a Jupyter Notebook](https://ligdigonzalez.com/introduccion-a-jupyter-notebook/)
- [Intro a pandas](https://discoverdatasciencelab.com/2018/10/23/introduccion-a-pandas/)

### Estimados de locación y variabilidad

El módulo anterior estuvo enfocado en aprender a procesar nuestros datasets para dejarlos limpios y ordenados. La razón por la que aprendimos eso fue para poder procesar nuestros datasets de manera que estén listos para extraer información útil de ellos. En este módulo aprendemos qué información podemos extraer de nuestros datasets, por qué queremos extraerla, cómo nos puede ser útil y cómo usar Python para este objetivo.

Lo primero que aprenderemos son estimados de locación y variabilidad. Pero para entender la razón por la que son útiles, primero necesitamos echar un vistazo a los tipos de datos estructurados con los que podemos toparnos.

### Datos estructurados

Hay básicamente dos tipos de datos estructurados con los que podemos toparnos:

1. Numéricos
2. Categóricos

Estos a su vez se subdividen en los siguientes:

1. Numéricos
  a) Discretos: Datos que sólo pueden tomar el valor de un número entero, como conteos o edades de personas.
  b) Continuos: Datos que pueden toman cualquier valor dentro de un intervalo.
2. Categóricos: Datos que sólo pueden tomar un conjunto específico de valores que representan un conjunto de posibles categorías.
  a) Binarios: Datos categóricos que sólo tienen dos categorías posibles.
  b) Ordinales: Datos categóricos que tienen un orden explícito, como rankings de películas que van del 1 al 10.
  
Los estimados que vamos a aprender hoy se utilizan para analizar datos numéricos. Y ahora veremos su utilidad.

### ¿Por qué queremos estimados de locación y variabilidad?

Los datos numéricos pueden tener una gran cantidad de variabilidad. Dentro de una sola `Serie` caben muchos valores posibles: es importante tener una idea general de cuál es nuestro valor "típico" y qué tan lejos o cerca se encuentran los demás valores. Los estimados de locación nos dan este valor "típico", que podemos pensar como el valor que mejor describe a nuestro conjunto de datos. Los estimados de variabilidad (o dispersión) miden que tan dispersos se encuentran los demás datos de ese valor central.

Este valor típico puede obtenerse utilizando los datos de toda la **población** (es decir, la totalidad de elementos sobre los que se está haciendo el análisis) o de una **muestra** de la población (un subconjunto de los elementos que se toma previamenente para realizar el análisis). Si quieres entender mejor la diferencia entre población y muestra, puedes [dar click aquí](https://www.diferenciador.com/poblacion-y-muestra/#:~:text=Poblaci%C3%B3n%20se%20refiere%20al%20universo,poblaci%C3%B3n%20para%20realizar%20un%20estudio.&text=Selecci%C3%B3n%20de%20una%20parte%20de,a%20ser%20sujeto%20de%20estudio.).

### Estimados de locación

Hay muchas maneras de obtener nuestro valor "típico", pero vamos a aprender solamente las 3 más comunes.

#### Promedio (mean)

El promedio (mean en inglés) se obtiene sumando todos los datos y luego dividiéndolos entre la cantidad de datos que tenemos. Este estimado toma en cuenta todos los datos de nuestro conjunto. Por ejemplo, si tenemos los valores `3, 7, 1, 4`, primero los sumaríamos para obtener `15` y despúes los dividiríamos entre `4` (la cantidad de valores que tenemos) para obtener `3.75`. Este valor, `3.75` es nuestro valor típico que mejor describe nuestro conjunto.

#### Mediana (median)

La mediana se obtiene ordenando de menor a mayor nuestros valores y luego obteniendo el valor que está justo a la mitad de la secuencia. Por ejemplo, si tenemos `3, 7, 1, 4, 5`, primero tendríamos que ordenarlos: `1, 3, 4, 5, 7` y después obtener el valor que está justo en medio: `4`. `4` sería nuestro valor típico.

En el caso de que la cantidad de valores sea par, se toma el promedio de los valores que están en medio. Por ejemplo, si tenemos `3, 7, 1, 4`, primero los ordenamos: `1, 3, 4, 7`. Y después sacamos el promedio entre `3` y `4` para obtener `3.5` como valor típico.

Si eres observador, te habrás percatado de que utilizando el mismo conjunto de datos (`3, 7, 1, 4`) obtuvimos valores típicos distintos utilizando el promedio y la mediana. ¿Cuál es el criterio entonces para elegir la una o la otra?

### Valores atípicos

Así como hay valores típicos que sirven para describir nuestro dataset usando un solo valor, también existen valores que son *radicalmente* distintos al valor típico. Estos valores se encuentran tan alejados del valor típico que pueden pensarse como anomalías en nuestro conjunto de datos.

Piensa por ejemplo en los ingresos económicos mensuales del pueblo mexicano. Si hacemos un conjunto de datos de todos los ingresos mensuales y obtenemos un valor típico, encontraríamos que hay algunos valores en nuestro conjunto que difieren por una gran cantidad del valor típico. Por ejemplo, los ingresos mensuales de Carlos Slim, uno de los humanos más ricos del planeta, definitivamente **no** son representativos de lo que sucede "en general".

Hay veces que tomar en cuenta estos valores atípicos tiene sentido, pero muchas otras veces es importante lidiar con ellos para obtener un estimado de locación que realmente sea representativo de la población.

Ya que el *promedio* toma en cuenta **todos** los datos de nuestro conjunto, es muy sensible a los valores atípicos y fácilmente puede sesgarse si hay algún valor demasiado grande o demasiado pequeño. La *mediana*, en cambio, es mucho más *robusta*, puesto que los valores atípicos extremos no afectan demasiado su desempeño.

Se le llama *robusto* a un estimado estadístico que no es tan sensible a la presencia de valores atípicos.

Podemos simplificar diciendo que el promedio es preferible cuando no tenemos tantos valores atípicos y la mediana es preferible cuando tenemos valores atípicos que podrían afectar nuestro análisis.

#### Media truncada

La media truncada es un estimado que nos sirve para volver más *robusto* nuestro promedio. Funciona de la siguiente forma:

1. Primero ordenamos nuestros datos de menor a mayor.
2. Después truncamos un porcentaje de nuestros datos al inicio y al final. Por ejemplo, si elegimos eliminar el 5% de los datos, eliminaríamos 2.5% de los datos al inicio de la secuencia y 2.5% al final.
3. Con los datos restantes, obtenemos nuestro promedio usando el algoritmo original.

La media truncada, al eliminar cierto porcentaje de datos al inicio y al final de nuestra secuencia, intenta disminuir el impacto de los valores atípicos sobre nuestro estimado. Es común eliminar entre el 5% y el 25% de nuestros datos al calcular una media truncada. Obviamente si tenemos un dataset pequeño va a ser preferible tomar la mediana a la media truncada, ya que esta última implica la eliminación de algunas de nuestras muestras.

### Estimados de variabilidad

Ya que tenemos nuestro estimado de locación (el valor "típico") de nuestro dataset, el siguiente paso es saber qué tan lejanos o cercanos a este valor típico se encuentran los demás datos. Para esto utilizamos los estimados de variabilidad. Uno de los estimados más comunes es la desviación estándar.

#### Desviación estándar

La desviación estándar nos da la "desviación típica" de nuestros datos alrededor del valor típica. Es decir, qué tan dispersos podemos esperar que estén nuestros datos alrededor de nuestro estimado de locación.

Para obtener la desviación estándar, se obtienen primero todas las diferencias entre cada valor y nuestro valor típico. Después se eleva cada valor al cuadrado, se suman todos estos valores, se dividen entre la cantidad de valores - 1, y finalmente se saca la raíz cuadrada del valor resultante.

Si quieres entender paso a paso el algoritmo para calcular la desviación estándar, puedes [revisar este link](https://es.khanacademy.org/math/probability/data-distributions-a1/summarizing-spread-distributions/a/calculating-standard-deviation-step-by-step).

Los valores que se encuentren dentro de 1 desviación estándar del promedio pueden ser considerados comunes y esperados. El único problema es que la desviación estándar también es bastante sensible a valores atípicos. Si tenemos muchos valores atípicos muy extremos, nuestro cálculo podría no ser muy representativo de la población.

Un estimado de variabilidad más *robusto* es la *desviación absoluta de la mediana*. No vamos a entrar en detalle, pero si quieres aprender cómo funciona, puedes leerlo [aquí](https://www.cienciasinseso.com/privacidad/desviacion-absoluta-mediana/).

### Estadísticos de Orden

Otra manera de estimar la dispersión de nuestros datos es analizando los datos ordenándolos de menor a mayor. Este tipo de análisis se llaman estadísticos de orden porque dependen de que nuestros datos estén ordenados de forma ascendente.

Veamos algunos de estos cálculos.

#### Rango

El rango es la diferencia entre el valor mínimo y el valor máximo de nuestro datos. El valor mínimo y el máximo nos pueden dar un buen indicador de la presencia de valores atípicos (sobre todo si los comparamos contra el estimado de locación). El rango es útil pero no es una estadística robusta, ya que si tenemos tan sólo 1 valor atípico demasiado extremo, nuestro rango cambia muy radicalmente.

Para hacer esta estadística más *robusta*, podemos aplicar la misma técnica que utilizamos en la media truncada y eliminar una porción de los datos al inicio y al final de nuestro conjunto.

#### Percentiles

En un conjunto de datos, el percentil `P` es un valor que indica que por lo menos `P%` de los valores en el conjunto tienen este valor o un valor menor; mientras que `(100-P)%` de los valores tienen este valor o un valor mayor. Por ejemplo, para obtener el percentil 80 primero ordenamos nuestro conjunto de manera ascendente y después elegimos un valor de manera que el 80% de los valores en nuestro conjunto sean iguales o menores a ese valor.

Digamos que tenemos este dataset: `1, 2, 3, 4, 5, 6, 7, 8, 9`. El percentil 75 sería `7`, ya que el 75% de los datos son menores a `8`. El percentil 25 sería `3`, mientras que el percentil 50 sería `5`. 

El percentil 0 es el valor mínimo (`1`), mientras que el percentil 100 sería el valor máximo (`9`). Por lo tanto el rango podría pensarse como la diferencia entre el percentil 100 y el percentil 0.

#### Rango intercuartílico

Otra estadística que es utilizada comunmente es el rango intercuartílico, que está definido como la diferencia entre el percentil 75 y el percentil 50. Es decir, en nuestro dataset `1, 2, 3, 4, 5, 6, 7, 8, 9` el rango intercuartílico sería `7 - 3 = 4`.

Sabiendo los percentiles y el rango intercuartílico, podemos darnos una idea bastante precisa de la dispersión de nuestros datos. Por ejemplo, si tenemos un conjunto de datos que cumpla con las siguientes características:

- El valor mínimo es 0
- El valor máximo es 100
- El percentil 25 es 15
- El percentil 75 es 40
- El rango intercuartílico es 25
- La mediana es 25

Podemos deducir viendo estos números que la mayoría de los datos están mucho más cercanos al valor mínimo que al valor máximo. Esto significa que hay un "sesgo" hacia los valores pequeños (pequeños en este contexto, claro) y que parece ser que hay valores muy grandes que están tan distantes de la mediana y de la mayoría de los valores que pueden ser considerados valores atípicos.

---

Desarrollaremos nuestra intuición acerca de estas estadísticas usando visualizaciones en la siguiente sesión, pero por lo pronto, en la sesión aprenderás a calcular todas estas medidas usando Python y pandas.

¡Mucha suerte!

---

**Quiz**

1. ¿Cómo se llaman los tipos de datos que solamente tienen dos valores posibles?

* Categóricos
* Continuos
* **Binarios**
* Discretos
* Estructurados

2. ¿Cómo se le llama a los estimados que son menos sensibles a la presencia de valores atípicos?

* Insensible
* Fuerte
* Estable
* **Robusto**
* Tenaz

3. ¿Cuál de los siguientes es un estimado de variabilidad?

* **Desviación estándar**
* Promedio
* Media truncada
* Mediana
* Media ponderada

4. ¿Qué es el rango?

* La diferencia entre el promedio y la mediana
* La diferencia entre la desviación estándar y el promedio
* La diferencia entre la mediana y el percentil 100
* **La diferencia entre el valor máximo y el mínimo**
* La diferencia entre la desviación estándar y la mediana

5. ¿Qué es el Rango Intercuartílico?

* **La diferencia entre el percentil 75 y el percentil 25**
* La diferencia entre el percentil 100 y el percentil 0
* La diferencia entre el percentil 75 y el percentil 0
* La diferencia entre el percentil 100 y el percentil 50
* La diferencia entre el percentil 50 y el percentil 25
