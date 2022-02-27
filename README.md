# CursoDjango

Tome este curso con la finalidad de empezar con una de las versiones más antiguas de Django(1.9.1) y así poder ver las diferencias con la versión hasta el día de hoy 4.0.2(2022-02-22)  .

Se realizo con linux Fedora 33


# Requerimientos

### Python 3.9.9
En mi caso lo baje de la pagina oficial de python: <br><https://www.python.org/downloads/source/>
<br>`sudo su dnf install nombre_paquete_descargado`

Para comprobar si lo tenemos instalado
<br>`python --version`

### Entorno Virtual(Opcional)
Esto es por si no quieres instalar Django directo en tu python global
Instalamos el paquete de python para crear entornos virtuales(que practicamente es una carpeta)
<br>`python -m pip install virtualenv`

Creamos la carpeta para el entorno virtual(la crea con varios archivos dentro) o sea un mini python dentro de esa carpeta
<br>`python -m venv nombre_carpeta_entorno_virtual`

Nos movemos a la carpeta del entorno
<br>`cd nombre_carpeta_entorno_virtual`

Y activamos el entorno virtual
<br>`source bin/activate`

P.D:
Cuan ya se no se requiera nada con el proyecto y requiere salir del entorno virtual.
<br>`deactivate`

### Django 4.0.1

<br>`python -m pip install django=4.0.1`

#### Instalación del proyecto
Si creaste el entorno virtual entonces de preferencia posicionate dentro de la carptea del entorno virtual.

Clonamos el repositorio
<br>`git clone https://github.com/LuisAngelFnz/CursoDjango.git`

Nos movemos dentro de la carpeta creada
<br>`cd CursoDjango`

Ejecutamos el proyecto

<br>`python manage.py runserver`

Listo ahora copiamos la url que nos sale en mi caso fue
http://127.0.0.1:8000/

y la pegamos en el navegador para ver la funcionalidad.

el usuario administrador es :
<br>`usuario1`
y el password es: 
<br>`password1`

![](https://static.djangoproject.com/img/logos/django-logo-negative.png)

![](https://www.python.org/static/community_logos/python-logo-master-v3-TM-flattened.png)


##Links

`Link del curso` : <https://codigofacilito.com/cursos/django>
