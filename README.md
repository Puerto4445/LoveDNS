<!DOCTYPE html>
<html>
<body>

<h1>LoveDNS ❤️</h1>
<p>Hecho para explorar las consultas DNS en tu red. Una herramienta para ver qué dominios se visitan en tiempo real.</p>

<h2>Tabla de Contenidos</h2>
<ul>
    <li><a href="#descripción">Descripción</a></li>
    <li><a href="#requisitos">Requisitos</a></li>
    <li><a href="#instalación">Instalación</a></li>
    <li><a href="#uso">Uso</a></li>
    <li><a href="#contribución">Contribución</a></li>
    <li><a href="#licencia">Licencia</a></li>
</ul>

<h2 id="descripción">Descripción</h2>
<p>Este script utiliza Python y la magia de Scapy para escuchar las consultas DNS en tu red local y te muestra, de forma limpia y clara, los sitios web que se están solicitando.</p>
<p>Las principales características del script son:</p>
<ul>
    <li><strong>Monitoreo en Tiempo Real:</strong> Captura y muestra las consultas DNS a medida que ocurren.</li>
    <li><strong>Filtrado Inteligente:</strong> Ignora dominios de servicios en segundo plano para reducir el ruido.</li>
    <li><strong>Salida Limpia:</strong> Muestra cada dominio único solo una vez durante la sesión.</li>
</ul>

<h2 id="requisitos">Requisitos</h2>
<ul>
    <li>Python 3.x</li>
    <li>Biblioteca Scapy</li>
</ul>

<h2 id="instalación">Instalación</h2>
<ol>
    <li>Clona el repositorio:
        <pre><code>git clone https://github.com/Puerto4445/loveDNS.git</code></pre>
    </li>
    <li>Navega al directorio del proyecto:
        <pre><code>cd loveDNS</code></pre>
    </li>
    <li>Instala las dependencias:
        <pre><code>pip install scapy</code></pre>
    </li>
</ol>

<h2 id="uso">Uso</h2>
<p>El script necesita permisos de administrador para capturar paquetes de la red. Antes de ejecutar, asegúrate de que la variable <code>interface</code> dentro del script coincida con tu interfaz de red (ej. "eth0", "wlan0", "Wi-Fi").</p>
<p>Para ejecutar el script, utiliza el siguiente comando:</p>
<pre><code>sudo python loveDNS.py</code></pre>
<p>El script comenzará a mostrar los dominios detectados en la consola.</p>
