import scapy.all as scapy
import argparse
from termcolor import colored
from pyfiglet import Figlet
import subprocess

def Show_Banner(text):
    figlet = Figlet(font="smslant")
    ascii_art = figlet.renderText(text)
    try:
        lolcat_process = subprocess.Popen(['lolcat'], stdin=subprocess.PIPE)
        lolcat_process.communicate(input=ascii_art.encode())
    except FileNotFoundError:
        print(ascii_art)

def Banner():
    Show_Banner("LOVEDNS")
    print("@puerto4444")
    print("-"*30)

def DNS_Packet(packet):
    """
    Processes a packet to extract DNS domain names.

    This function checks if the packet contains a DNS Question Record (DNSQR) layer.
    If it does, it extracts the domain name, decodes it, and adds it to a global
    'domain_repeat' set to prevent duplicates. Additionally, it excludes domains
    that contain certain predefined keywords (e.g., "google", "bing").
    Valid domains are printed in green to the console.

    Args:
        packet: The Scapy network packet to be inspected.
    """
    if packet.haslayer(scapy.DNSQR):
        domain = packet[scapy.DNSQR].qname.decode()
        
        exlude = ["google","bing","static","sensic","s3t3d2y9","firefox"]
        if domain not in domain_repeat and not any(i in domain for i in exlude):
            domain_repeat.add(domain)
            print(colored(f"[+] Pagina:\t{domain}","green"))
            
def Get_Argument():
    """
    Retrieves the network interface argument from the command line.

    Uses the argparse module to define and parse the '-i' or '--interface' argument.
    This argument is required and specifies the network interface to monitor
    (e.g., 'ens33' or 'eth0').

    Returns:
        str: The name of the network interface provided by the user.
    """
    parser = argparse.ArgumentParser(description="DNS")
    parser.add_argument(
        "-i",
        "--interface",
        dest="target",
        required=True,
        help="Interface (Ex: -i ens33/eth0)",
    )
    option = parser.parse_args()
    return option.target

def main():
    try:
        Banner()
        global domain_repeat
        domain_repeat = set()
        interface = Get_Argument()
        print(f"T4rg3t P4ck4g35:\n")
        scapy.sniff(iface=interface, filter="udp and port 53", prn=DNS_Packet, store=False)
    except ValueError:
        print(colored(f"[!] 3®®<>®!","red"))

if __name__=="__main__":
    main()
