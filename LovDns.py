import scapy.all as scapy

def dns_packet(packet):
    if packet.haslayer(scapy.DNSQR):
        domain = packet[scapy.DNSQR].qname.decode()
        
        exlude = ["google","bing","cloud","static","sensic"]
        if domain not in domain_repeat and not any(i in domain for i in exlude):
            domain_repeat.add(domain)
            print(f"[+] Pagina:\t{domain}")

    
def main():
    global domain_repeat
    domain_repeat = set()
    interface = "ens33"
    print(f"Paquetes Victima:\n")
    scapy.sniff(iface=interface, filter="udp and port 53", prn=dns_packet, store=False)

if __name__=="__main__":
    main()