 ## Nombre del Postwork: Obteniendo estimados de locación y variabilidad

### OBJETIVO 

- Utilizar estimados de locación y variabilidad para describir las columnas numéricas de un dataset.

#### REQUISITOS 

- Niguno

#### DESARROLLO

Si estuviste en el módulo anterior, eso quiere decir que ya tienes identificado un problema, te has planteado preguntas acerca del problema, has encontrado un conjunto de datos que crees que te puede ayudar a responder tus preguntas y lo has limpiado y estructurado de manera que está listo para ser analizado.

Si no estuviste en el módulo anterior, no te preocupes. Puedes tomarte un poco de tiempo para plantearte qué proyecto quieres realizar durante este módulo.

---

**Si NO estuviste en el módulo de Procesamiento de Datos realiza antes la siguiente actividad con la ayuda de tu experta**

---

1. Elige un problema que te parezca interesante o atractivo. Ayuda que sea un tema que conozcas bien, pero no es absolutamente necesario que esa condición se cumpla.
2. Plantéate una serie de preguntas acerca de este problema o situación que te parezca que tal vez puedas responder usando análisis de datos.
3. Encuentra un dataset que tenga datos que te puedan ser útiles para responder a tus preguntas. Puedes buscar en las siguientes fuentes:

- [Kaggle](https://www.kaggle.com/)
- [FiveThirtyEight](https://data.fivethirtyeight.com/)
- [BuzzFeed News](https://github.com/BuzzFeedNews)
- [Awesome Public Datasets](https://github.com/awesomedata/awesome-public-datasets)
- [UCL Machine Learning Repository](http://archive.ics.uci.edu/ml/index.php)
- [Academic Torrents](http://academictorrents.com/browse.php)
- [Quandl](https://www.quandl.com/search)

4. Realiza una limpieza general de tu dataset (eliminación de NaNs, renombramiento de índice y columnas, formateo de strings, etc) para que esté listo para ser analizado

---

**Lo que sigue es para TODOS los estudiantes, hayan estado en el módulo de Procesamiento de Datos o no.**

---

Vamos a usar estimados de locación y variabilidad para describir nuestro dataset. Ya tenemos un dataset limpio, así que ahora toca extraer información útil de él.

Recuerda que sólo es posible obtener estimados de locación y variabilidad cuando tenemos datos numéricos (tanto discretos como continuos). La actividad consiste en lo siguiente:

1. Identifica las columnas de tu dataset que tengan datos numéricos.
2. Identifica la relevancia de esas columnas (qué tan importantes son para responder a tus preguntas).
3. Obtén los siguientes estimados de tus columnas numéricas:

  a) Promedio
  b) Mediana
  c) Media Truncada
  d) Desviación estándar
  e) Rango
  f) Percentiles 25 y 75 (por lo menos)
  g) Rango intercuartil
  
Comenta con tus compañeros qué has aprendido sobre tus datos al estudiar estas medidas.