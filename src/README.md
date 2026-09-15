Calidad de los datos

3.1 Dato faltante
Se encontró un valor faltante en el campo consumo_m3 correspondiente al barrio Norte durante el mes de marzo: Norte,,420,Marzo

¿Cómo se detectó?
Se revisaron los valores de la columna consumo_m3 y se identificó un registro cuyo valor estaba vacío.

¿Qué decisión se tomó?
No se asignó un valor artificial al registro. Para los cálculos estadísticos se excluyó este registro únicamente del análisis de la variable consumo_m3.

¿Por qué?
Asignar un valor estimado sin información adicional podría introducir un sesgo en los resultados.

3.2. Valor atípico
Se identificó el siguiente registro: Occidente,110000,450,Marzo. El consumo registrado es de 110.000 m³, mientras que los demás valores se encuentran aproximadamente entre 800 y 1.300 m³.

¿Cómo se detectó?
Se compararon los valores mínimos y máximos del consumo y se observó que 110.000 m³ se encontraba muy alejado del comportamiento general de los datos.

¿Qué decisión se tomó?
El valor se consideró un dato atípico y se excluyó temporalmente de los cálculos estadísticos principales.

¿Por qué?
El dato debe ser validado con la fuente original antes de utilizarlo para tomar decisiones. Podría tratarse de un error de digitación.

3.3. Inconsistencia en la magnitud del consumo

Se identificó una inconsistencia en la escala de los datos para el barrio Occidente, con los siguientes valores: Mes Consumo (Enero	1.050 m³, Febrero	1.080 m³, Marzo	110.000 m³)

¿Cómo se detectó?
Se compararon los consumos del mismo barrio durante los diferentes meses.

¿Qué decisión se tomó?
El registro fue excluido del análisis estadístico principal hasta que pueda ser validado.

¿Por qué?
Una variación de esta magnitud puede distorsionar significativamente los resultados y producir conclusiones incorrectas.

Análisis estadístico

Para el análisis principal se excluyeron:
El registro con consumo faltante.
El valor atípico de 110.000 m³.

Media 1.056,15 m³
Mediana	1.080 m³
Desviación estándar	166,01 m³
Mínimo 800 m³
Máximo 1.300 m³

¿El promedio es representativo?
Después de retirar el valor atípico, la media es mucho más representativa del comportamiento de los datos. La media y la mediana son relativamente cercanas ya que los datos válidos no presentan una distorsión extrema.