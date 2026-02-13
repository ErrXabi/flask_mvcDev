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
- Controllers: Se guardan todas las rutas de cada libro, socio, API y autenticación, devolviendo vistas. Desde aquí se hace la llamada a los servicios.
- Forms: Son las plantillas para cada formulario, con validaciones de FlaskWTF.
- Models: Son los modelos para el libro, socio y usuario. Definen qué columnas se van a guardar en la BD, de qué tipo son y las relaciones entre las tablas.
- Services: Es donde se ejecutan las funciones que ha llamado el controlador, y sirven para consultar, actualizar, guardar y eliminar información de la BD.
- Static: Guarda archivos como el CSS.
- Templates: Están los HTMLs de la aplicación, dentro están los componentes reutilizables para cada página, los formularios de registro y login y cada página para gestionar
los libros y los socios.
- Utils: Es donde se guardan los decoradores para utilizarlos en los controladores. En este caso está el decorador que protege las rutas, comprobando que el usuario
que ha iniciado sesión es administrador.

POSIBLES MEJORAS FUTURAS:
- Permitir que los socios puedan iniciar sesión y gestionar sus propios libros
- Permitir que los autores puedan agregar sus propios libros