# Tarea1

## Explicación general

Docker compose levanta los servicios de promtail, loki, grafa y 2 servicios creados con fastapi. Los servicios de fastapi son inicio de sesión y registro, los cuales son básicos ya que no tienen base de datos. 

Promtail lee los archivos de manera local en la carpeta fastapi_logs 