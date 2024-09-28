- # Proyecto Urban Grocers 
# Betsabé Navarro Loyo. Grupo 14. Sprint 7


## Descripción del Proyecto
Este proyecto permite gestionar kits de productos para la tienda en línea Urban Grocers,
donde se pueden crear nuevos kits con diferentes parámetros y validar su
correcta creación a través de pruebas automatizadas.
Esta prueba en especifico se concentra en el parametro "name" al momento de crear un nuevo Kit

# Fuente de información 
 https://cnt-a1df3072-7424-4d52-91b2-48eb2c1f568e.containerhub.tripleten-services.com/docs/

## Tecnologías Utilizadas

- Python
- pytest
- requests

## Ejecución de Pruebas

Para ejecutar las pruebas, asegúrate de tener instalados los paquetes `pytest` y `requests`.
Ruta de archivo: Users/betsabenavarro/Desktop/Proyectos/qa-project-Urban-Grocers-app-es

# Instrucciones para las Pruebas
Las pruebas verifican lo siguiente:

El código de estado de las respuestas es 201 para las pruebas positivas y 400 para las negativas
El campo name en la respuesta coincide con el valor utilizado en la prueba.
Se manejan errores correctamente cuando los parámetros son inválidos.

# Ejemplo de Pruebas
Las siguientes pruebas están implementadas:

- Prueba positiva: El parámetro name contiene 1 carácter.
- Prueba positiva: El parámetro name contiene 511 caracteres.
- Prueba negativa: El parámetro name contiene 0 caracteres (error 400).
- Prueba negativa: El parámetro name contiene 512 caracteres (error 400).
- Prueba positiva: El parámetro name contiene caracteres especiales.
- Prueba positiva: El parámetro name contiene espacios.
- Prueba positiva: El parámetro name contiene números.
- Prueba negativa: La solicitud no contiene el parámetro name (error 400).
- Prueba negativa: El tipo del parámetro name es un número (error 400).

Todas estas pruebas y sus códigos estan en el file create_kit_name_test.py

