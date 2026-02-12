DESCRIPCIÓN DEL PROYECTO:
Es una aplicación web hecha en Python con Flask sobre la gestión de una biblioteca, desde la vista del administrador, donde se pueden consultar
todos los libros, los libros disponibles, buscar un libro por título, pretar y devolver un libro, ver todos los socios registrados, ver los socios que 
tengan un libro prestado y registrar nuevos socios.

INSTRUCCIONES PARA EJECUTAR LA APLICACIÓN:
Al utilizar el proyecto hay que crear el directorio venv con :
python -m venv venv

Despues hay que instalar las dependencias con :
pip install -r requirements.txt

Siempre que se instalen nuevas dependencias hay que actualizar el archivo requirements.txt con:
pip freeze > requirements.txt

EXPLICACIÓN BREVE DE LA ESTRUCTURA DEL CÓDIGO:


POSIBLES MEJORAS FUTURAS:
- Permitir que los socios puedan iniciar sesión y gestionar sus propios libros
- Permitir que los autores puedan agregar sus propios libros