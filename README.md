# Tarea1

## Explicación general

Docker compose levanta los servicios de promtail, loki, grafa y 2 servicios creados con fastapi. Los servicios de fastapi son inicio de sesión y registro, los cuales son básicos ya que no tienen base de datos. 

Promtail lee los archivos de manera local en la carpeta fastapi_logs, tal que fastapi1 es el login y fastapi2 es el register. Asimismo, cada servicio tiene su archivo de logs

## Cómo utilizarlo
- Docker-compose build
- Docker-compose up -d 

## Puertos de cada servicio
- 3100 loki
- 3000 grafana
- 8001 login
- 8000 registro