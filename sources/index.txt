========
 Python
========

.. rst-class:: python

   .. image:: _static/python-logo.png

.. rst-class:: movile

   .. image:: _static/movile.png

.. rst-class:: date

27 de Abril de 2015

Historia
========

.. rst-class:: guido

   .. image:: _static/guido.jpg

* Creado a finales 1980 por Guido Van Rossum como un sucesor del lenguaje ABC.

* V0.9.0 en 1991: aparecían clases con herencia y excepciones.

* V1.0 en 1994: incluye características de programación funcional.

* Python 2.0: implementó listas por comprensión y recolección de basura.

* 6/3/2001: código/documentación le pertenece a Python Software Foundation
  (PSF).

* Python 2.2 unificó una jerarquía los tipos de datos y clases.

* 8/12/2008: salió Python 3.0, el cual no tiene compatibilidad con la serie
  2.x.

¿Y qué es?
==========

* Es un lenguaje de programación interpretado que tiene por filosofía hacer
  incapié sobre una sintaxis que favorezca el código legible.

* Es *multiparadigma*: soporta POO, programación estructurada y en menor medida
  programación funcional.

* Es multiplataforma.

* Tiene fuertes influencias de otros lenguajes (Lisp, Haskel, Java)

* Su nombre es en honor al show de humoristas *Monty Python*.

Sintaxis de Python
==================

.. rst-class:: keep-calm

   .. image:: _static/keep-calm.png

Sintaxis
========

Declaración de variables:

.. code-block:: python

   >>> x = 1
   >>> print x
   1
   >>> x = "hola, ¿qué tal?"
   >>> print x
   hola, ¿qué tal?

Funciones:

.. code-block:: python

   >>> def callme(x):
   ...     print "call me, %s?" % x
   ...
   >>> callme("maybe")
   call me, maybe?

Sintaxis
========

Comentarios:

.. code-block:: python

   x = 1  # Esto es un comentario en 1 línea
   """
   Este es un comentario
   en
   muchas
   lineas
   """
   # Así también
   # se puede comentar

Sintaxis
========

Declaración de clases:

.. code-block:: python

   class Parrilla:
       """
       La parrilla asa la carne sobre las brasas.
       """
       def prender(self):
           self._estado = "prendida"  # Atributo privado
           self.__como_estamos()

       def asar(self):
           self._estado = "asando"
           self.__como_estamos()

      def __como_estamos(self):  # Método privado
          """
          Imprime el estado.
          """
          print "La parrilla está %s" % self._estado

Sintaxis
========

Instanciación de clases y uso de objetos:

.. code-block:: python

   >>> p = Parrilla()
   >>> p.prender()
   La parrilla está prendida
   >>> # También podemos acceder a la estructura privada del objeto:
   >>> p._estado
   'prendida'
   >>> p._Parrilla__como_estamos()
   La parrilla está prendida
   >>> # Incluso podemos manipular el objeto creando nuevos atributos:
   >>> p._xxx = 125
   >>> p._xxx
   125

Herramientas
============

.. rst-class:: herramientas

   .. image:: _static/herramientas.jpg

Pip
===

Es un sistema de administración de paquetes de Python. En las versiones >=2.7.9
y >=3.4 se incluye pip en la instalación por defecto.

.. code-block:: bash

   ~$ pip install nombre-del-paquete
   ~$ pip install nombre-del-paquete==3.2.1  # versión específica
   ~$ pip uninstall paquete-obsoleto
   ~$ pip install -r requirements.txt

Ejemplo de un archivo de requerimientos:

.. literalinclude:: requirements.txt

Virtualenv
==========

**El escenario:** un host conteniendo múltiples aplicaciones las cuales cada
una de ellas está atada a las versiones de sus dependencias. Actualizar o
modificar directa o indirectamente estos paquetes para cumplir con las
necesidades de otro proyecto puede significar no cumplir con los requisitos
mínimos de los que ya están instalados.

**La solución:** *virtualenv*: una herramienta para crear ambientes Python
aislados.

Virtualenv
==========

Ejemplo de uso:

.. code-block:: bash

   ~$ virtualenv example
   New python executable in example/bin/python
   Installing setuptools, pip...done.
   ~$ source example/bin/activate
   (example) ~$ pip install requests
   Collecting requests
     Downloading requests-2.6.2-py2.py3-none-any.whl (470kB)
       100% |################################| 471kB 28kB/s 
   Installing collected packages: requests
   
   Successfully installed requests-2.6.2
   (example) ~$ deactivate
   ~$

Paquetes
========

.. rst-class:: paquetes

   .. image:: _static/paquetes.png

requests
========

Haciendo requests HTTP a la vieja usanza: urllib

.. literalinclude:: examples/requests_1.py

requests
========

Haciendo requests HTTP con el nuevo módulo requests:

.. literalinclude:: examples/requests_2.py

Fabric
======

.. rst-class:: fabric

   .. image:: _static/fabric.png

**El escenario:** Multiples tareas repetitivas en servidores remotos,
utilizando conexiones SSH para acceder a ellos. De tener un ambiente productivo
donde se de el crecimiento horizontal el número de veces que debe realizarse
una tarea rutinaria puede crecer de manera alarmante.

**La solución:** Automatizar las interacciones locales y remotas que se
realizan en la consola de comandos, utilizando la biblioteca *Fabric*.

Fabric
======

Ejemplo de un fabfile:

.. literalinclude:: examples/fabfile.py

Fabric
======

Ejemplo de uso de Fabric:

.. code-block:: bash

   ~$ fab hola
   [localhost] Executing task 'hola'
   hola!
   
   Done.
   ~$ fab touch
   [localhost] Executing task 'touch'
   [localhost] local: touch /tmp/ariel
   
   Done.

Fabric
======

Otro ejemplo de uso de Fabric:

.. code-block:: bash

   ~$ fab production remote_pull
   [localhost] Executing task 'production'
   [www.ariel17.com.ar] Executing task 'remote_pull'
   [www.ariel17.com.ar] run: cd www
   [www.ariel17.com.ar] Login password for 'ariel17': 
   [www.ariel17.com.ar] run: git pull
   [www.ariel17.com.ar] out: fatal: Not a git repository (or any of the parent
   directories): .git
   [www.ariel17.com.ar] out: 
   
   
   Fatal error: run() received nonzero return code 128 while executing!
   
   Requested: git pull
   Executed: /bin/bash -l -c "git pull"
   
   Aborting.
   Disconnecting from www.ariel17.com.ar... done.
   run() received nonzero return code 128 while executing!
   

Otros paquetes útiles
=====================

* **argparse**: parser para opciones de líneas de comando, argumentos y
  subcomandos. 

* **Scrapy**: un framework para parsear, consumir y navegar páginas HTML.
  Ofrece implementaciones base para crear fácilmente bots que consuman sitios.

  .. rst-class:: scrapy

     .. image:: _static/scrapy.png

* **Pilas Engine**: un motor de video juegos argentino. Creado por Hugo
  Ruscitti.

  .. image:: _static/pilas.png

Hecho con Python
================

.. rst-class:: powered

   .. image:: _static/powered.png

Salt
====

.. rst-class:: salt
   
   .. image:: _static/salt.png

.. rst-class:: salt-platform
   
   .. image:: _static/salt-platform.png

Sentry
======

.. rst-class:: sentry
   
   .. image:: _static/sentry.png

.. rst-class:: sentry-event
   
   .. image:: _static/sentry-event.png

Sphinx
======

.. rst-class:: sphinx
   
   .. image:: _static/sphinx.png

.. rst-class:: sphinx-page
   
   .. image:: _static/sphinx-page.png

Frameworks web
==============

.. rst-class:: usually

   .. image:: _static/usually.jpg

Flask
=====

.. rst-class:: flask

   .. image:: _static/flask.png

.. literalinclude:: examples/flask.py

Django
======

.. rst-class:: django

   .. image:: _static/django.png

.. rst-class:: django-pony

   .. image:: _static/django-pony.png

Otros
=====

.. rst-class:: webpy

   .. image:: _static/webpy.gif

.. rst-class:: pyramid

   .. image:: _static/pyramid.png

.. rst-class:: turbogears

   .. image:: _static/turbogears.jpg

¿Preguntas?
===========

.. rst-class:: preguntas

   .. image:: _static/preguntas.jpg

Dónde continuar
===============

* Python: http://www.python.org/
* Python Argentina - PyAr: http://python.org.ar/
* ``#pyar`` en Freenode
* PEP 20 - The Zen of Python: https://www.python.org/dev/peps/pep-0020/
* *Learn Python the hard way*: http://learnpythonthehardway.org/

¡Muchas gracias!
================

.. rst-class:: movile-thankyou

   .. image:: _static/movile.png

.. rst-class:: me

   Ariel Gerardo Ríos

.. rst-class:: personal-data

   |email|

.. rst-class:: personal-data

   |twitter|_

.. _twitter: https://twitter.com/ariel_17_
.. |twitter| replace:: @ariel_17_
.. |email| replace:: ariel.rios@movile.com
