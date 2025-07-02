import scapy.all as scapy
import argparse
from termcolor import colored

def dns_packet(packet):
    if packet.haslayer(scapy.DNSQR):
        domain = packet[scapy.DNSQR].qname.decode()
        
        exlude = ["google","bing","cloud","static","sensic","s3t3d2y9","firefox"]
        if domain not in domain_repeat and not any(i in domain for i in exlude):
            domain_repeat.add(domain)
            print(colored(f"[+] Pagina:\t{domain}","green"))

            
def get_argument():
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
        global domain_repeat
        domain_repeat = set()
        interface = get_argument()
        print(f"Paquetes Victima:\n")
        scapy.sniff(iface=interface, filter="udp and port 53", prn=dns_packet, store=False)
    except ValueError:
        print(colored(f"[!] Error!","red"))

if __name__=="__main__":
    main()
