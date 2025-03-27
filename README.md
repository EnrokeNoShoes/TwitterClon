<h1>TwitterClon</h1>
<h2>Prueba Tecnica de un clon de Twitter hecho en Django</h2>
<h3>Levantar el servicio en Linux</h3>
<p>Paso uno generamos el entorno virtual<br>
 &nbsp;	- python3 -m venv venv</p>
<p>Activamos el entorno virtual<br>
 &nbsp; - source venv/bin/activate</p>
<p>Instalamos el archivo requirements<br>
 &nbsp;	- pip install -r requirements.txt</p>
<p>Corroboramos si la maquina esta ok con las dependencias necesarias<br>
 &nbsp;	- python -m django --version</p>
<p>Caso de que no este el sqlLite<br>
  * Realizamos las migraciones correspondientes
  <ul>
    <li>python manage.py makemigrations</li>
    <li>python manage.py migrate</li>
  </ul>
	* Creamos el superusuario para poder ingresar al servidor
 <ul>
    <li>python manage.py createsuperuser</li>
  </ul>
		 </p>
<p>Y levantamos el servicio<br>
 &nbsp;	- python manage.py runserver</p> <b>
  ![imagen](https://github.com/user-attachments/assets/3f9f6785-7e9f-4925-bccf-fb1fbf579efc)
<h3>Levantar el servicio en Windows</h3>
<p>Corroboramos que tengamos Python instalado</p>
<p>Instalamos pip <br>
&nbsp;	- python -m ensurepip –upgrade
</p>
<p>Instalamos Django <br>
&nbsp;	- pip install django
</p>
<p>Intalamos las dependencias que contiene nuestro archivo requirement <br>
&nbsp;	- pip install -r requirements.txt <br>
	![imagen](https://github.com/user-attachments/assets/dccf469d-52e5-47b7-8d02-6411a6ad0f9f)
</p>
<p>Intalamos las dependencias que contiene nuestro archivo requirement <br>
&nbsp;	- pip install -r requirements.txt <br>
	![imagen](https://github.com/user-attachments/assets/dccf469d-52e5-47b7-8d02-6411a6ad0f9f)
</p>
<p>Caso de que no este el sqlLite<br>
  * Realizamos las migraciones correspondientes
  <ul>
    <li>python manage.py makemigrations</li>
    <li>python manage.py migrate</li>
  </ul>
   * Creamos el superusuario para poder ingresar al servidor
   <ul>
    <li>python manage.py createsuperuser</li>
  </ul>
</p>
<p>Corremos el servicio <br>
&nbsp;	- python manage.py runserver <be>
	![imagen](https://github.com/user-attachments/assets/5dde7668-053f-4ff5-ad5b-d2db391a6884)
</p>

<p><strong>Obs:</strong> se levanta 2 archivos correspondientes <br>
1 - Los Templates del clon<br>
2 - Paso a paso de como levantar el servicio
</p>
