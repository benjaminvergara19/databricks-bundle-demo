# Databricks notebook source

# Este es un notebook que será desplegado y ejecutado
# a través de un Databricks Asset Bundle.

print("¡Hola Mundo desde un Bundle de Databricks!")

# COMMAND ----------

#creamos el nombre del ejecutor con su otra info.
dbutils.widgets.text("nombre_ejecutor", "Nadie", "Nombre de quien ejecuta el job")

# COMMAND ----------

#leemos el motodo del widget
nombre = dbutils.widgets.get("nombre_ejecutor")

print(f"Este job fue ejecutado por: {nombre}")

# COMMAND ----------

import pandas as pd
df = pd.DataFrame([f"Ejecución completada por {nombre}"])
df.display()