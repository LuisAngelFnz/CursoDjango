# CursoDjango

Tome este curso con la finalidad de empezar con una de las versiones más antiguas de Django(1.9.1) y así poder ver las diferencias con la versión hasta el día de hoy 4.0.2(2022-02-22)  .

Se realizo con linux Fedora 33


# Requerimientos

### Python 3.9.9
### Entorno Linux

## Preparacion del Repo
~~~
git clone https://github.com/LuisAngelFnz/CursoDjango.git
~~~
~~~
cd CursoDjango
~~~
Crear un archivo con el nombre '.env' en la ruta RefugioAnimal/ con el siguiente contenido:
~~~
mail_host="smtp.gmail.com"
mail_user="TuCorreo"
mail_password="Contraseña Generada desde gmail con la verifacion de dos pasos"
mail_port=587
~~~


## Entorno Virtual(Opcional)
Si no quieres instalar Django directo en tú python global

El paquere "virtualenv" se requiere tener en el python global para crear entornos virtuales
~~~
python -m pip install virtualenv
~~~
Con el paquere "virtualenv" instalado ya podemos crear entornos virtuales.<br>
Vamos a crear un entorno virtual dentro del proyecto posicionados dentro del proyecto("cd CursoDjango").
~~~
python -m venv .venv
~~~
".venv" es el nombre de la carpeta del entorno virtual se puede cambiar el nombre por el que gustes.


Activamos el entorno virtual
~~~
source .venv/bin/activate
~~~

Cuando termines de ocupar el entorno y requieres regresar al python global ejecuta el siguiente comando
~~~
deactivate
~~~

## Instalar Django y paquetes
Ya sea que estas en el python global o en el entorno virtual se tienen que instalar django con el siguiente comando
~~~
python -m pip install django==4.0.1
~~~
Se tiene que instalar el paquete que lee el archivo ".env" que contiene las variables que usa el proyecto para reestablecer contraseñas.
~~~
python -m pip install django-environ
~~~
Instalar lo siguiente para la funcionalidad de los Serializers y APIs
~~~
python -m pip install djangorestframework
~~~

## Django migraciones
Se deben realizar las migraciones para crear la base de datos, ocupe SQLite para no instalar una BD:
~~~
./manage.py migrate
~~~

## Crear Super Usuario
En la carpeta del proyecto pegar la siguiente instrucción y proporcionar lo que django requiere(muy importante recordar)
~~~
./manage.py createsuperuser
~~~

## Arrancar el Servidor
~~~
./manage.py runserver
~~~

Copiar la url que nos proporciona django en la consola en mi caso fue
~~~
http://127.0.0.1:8000/
~~~

y la pegamos en el navegador para ver la funcionalidad.

Gracias...
<br>
## Links

`Link del curso` : <https://codigofacilito.com/cursos/django>
<br>
<br>
![](https://static.djangoproject.com/img/logos/django-logo-negative.png)

![](https://www.python.org/static/community_logos/python-logo-master-v3-TM-flattened.png)

