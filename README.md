# REPOSITORIO TRABAJO SD

Repositorio donde se encuentra el trabajo correspodiente al uso de diferentes API's.<br/>

Grupo formado por:<br/>

David José Corral Plaza<br/>
Pedro Soto Enríquez<br/>
Yassine Bouissef<br/>
Francisco Javier Rodríguez Revidiego<br/>
Alberto Espina Granados<br/>

# Tareas
<b>Coordinador:</b> David José Corral Plaza <br/>
<b>Desarolladores Twitter:</b> Pedro Soto Enríquez <br/> 
Yassine Bouisser<br>
<b>Desarrolladores Facebook:</b> Alberto Espina Granados <br/>
Francisco Javier Rodríguez Revidiego <br/>

# Documentación
El proyecto hace uso de dos API, la de Twitter y la de Facebook. Además de estas dos API, hemos hecho uso de los siguientes paquetes: Flask, python-twitter, Jinja2, twitter.

Lanzando el proyecto en un servidor local accederemos a un .html mediante el cual podremos poner en marcha las diferentes funcionalidades que presenta esta API que convina servicios tanto de Twitter como de Facebook.

La principal idea del proyecto es proveer un servicio para los diferentes usuarios que puedan realizar una integración de diferentes Redes Sociales a través de una sola plataforma para la cual no será necesario tener abiertas diferentes pestañas, sino que con estar conectados en la pestaña principal del proyecto podrá acceder a los diferentes servicios que ofrecen las Redes Sociales pero todas desde un mismo lugar.

# Instrucciones
Para poder poner en marcha el proyecto, descárguese el contenido de este repositorio en primer lugar y siga las instrucciones.
<ol>
<li>Instala virtualenv, puedes hacerlo con la orden <b>$ sudo apt-get install python-virtualenv </b> ó, si ya tienes instalado el paquete pip, <b>$ sudo pip-python install virtualenv</b>.</li>
<li>A continuación, creas un entorno virtual en virtualenv con el comando en la terminal <b>$ virtualenv api</b></li>
<li>Se crea un directorio <i>api</i>, introduce el contenido de este repositorio en dicha carpeta.</li>
<li>Con una terminal te posicionas donde has creado el entorno virtual:<ul><b>
<li>cd /home/<i>{USUARIO}</i>/api/bin/</li>
<li>$ source activate</li></b>
</ul>
</li>
<li>Si todo ha ido bien, ya tienes el entorno activado, ahora instalas los diferentes paquetes necesairos para hacer funcionar el proyecto:<ul><b>
<li>pip install Flask</li>
<li>pip install python-twitter</li>
<li>pip install Jinja2</li>
<li>pip install twitter</li>
<li>pip install facebook</li></b>
</ul>
</li>
<li>En la terminal donde estamos ejecutando el entorno virtual, ejecuta la orden <b>$ python api.py</b> abre el navegador y accede a la dirección http://127.0.0.1:5000/, ¡ya tienes el proyecto andando!</li>
</ol>

#Referencias
http://rukbottoland.com/blog/tutorial-de-python-virtualenv/<br/>
https://pypi.python.org/pypi/python-twitter/ <br/>
http://facebook-sdk.readthedocs.org/en/latest/install.html <br/>
https://dev.twitter.com/rest/public <br/>
https://developers.facebook.com/ <br/>
http://qlubox.com/blog/intalar-django-con-wsgi-y-virtualenv/ <br/>
