<!DOCTYPE html>
<html>
<body>

<h1>LoveDNS 🕵️‍♂️</h1>
<p>LoveDNS is a network monitoring tool designed to observe and decrypt DNS (Domain Name System) traffic on a network.
Whether you are a network architect, cybersecurity specialist, or curious enthusiast, LoveDNS empowers you to gain deep insights into DNS requests, identify unusual behavior, and enhance the security of your infrastructure.</p>

<h2>Tabla de Contenidos</h2>
<ul>
    <li><a href="#descripción">Description</a></li>
    <li><a href="#requisitos">Requirements</a></li>
    <li><a href="#instalación">installation</a></li>
    <li><a href="#uso">Use</a></li>
</ul>

<h2 id="descripción">Description</h2>
<p>This script uses Python and the magic of Scapy to listen to DNS queries on your local network and shows you, in a clean and clear way, the websites that are being requested.</p>
<p>The main features of the script are:</p>
<ul>
    <li><strong>Real-Time Monitoring:</strong> Captures and displays DNS queries as they occur.</li>
    <li><strong>Smart Filtering:</strong> Ignore background service domains to reduce noise.</li>
    <li><strong>Clean Exit:</strong> Display each unique domain only once during the session.</li>
</ul>
<img width="1125" height="522" alt="Captura desde 2025-09-03 22-39-28" src="https://github.com/user-attachments/assets/3fb1824d-f2bb-4d36-a908-63b5f7f178c3" />
<h2 id="requisitos">Requirements</h2>
<ul>
    <li>Python 3.x</li>
    <li>Scapy</li>
    <li>colorama</li>
</ul>

<h2 id="instalación">installation</h2>
<ol>
    <li>Clone the repository:
        <pre><code>git clone https://github.com/Puerto4445/LoveDNS.git</code></pre>
    </li>
    <li>Navigate to the project directory:
        <pre><code>cd loveDNS</code></pre>
    </li>
    <li>Install the dependencies:
        <pre><code>pip install -r requirements.txt</code></pre>
    </li>
</ol>

<h2 id="uso">Use</h2>
<p>The script requires administrator permissions to capture network packets. Before running, ensure that the <code>interface</code> variable within the script matches your network interface (e.g., “eth0,” “wlan0,” “Wi-Fi”).</p>
<p>To run the script, use the following command:</p>
<pre><code>sudo python LoveDNS_Monitor.py</code></pre>
<p>The script will begin displaying the detected domains in the console.</p>
