import scapy.all as scapy

def sniff_packets(interface, count=10):
    # Sniff 'count' number of packets on the given interface
    packets = scapy.sniff(iface=interface, count=count)
    return packets

def print_packet_info(packet):
    # Print relevant information for each packet
    print("[+] New Packet:")
    print("Source IP:", packet[scapy.IP].src)
    print("Destination IP:", packet[scapy.IP].dst)
    
    # Check if the packet has TCP or UDP layer
    if scapy.TCP in packet:
        print("Protocol: TCP")
        print("Source Port:", packet[scapy.TCP].sport)
        print("Destination Port:", packet[scapy.TCP].dport)
        print("Payload:", packet[scapy.TCP].payload)
    elif scapy.UDP in packet:
        print("Protocol: UDP")
        print("Source Port:", packet[scapy.UDP].sport)
        print("Destination Port:", packet[scapy.UDP].dport)
        print("Payload:", packet[scapy.UDP].payload)
    else:
        print("Protocol: Other")
        print("Payload:", packet.payload)

def start_sniffing(interface, count):
    print(f"[*] Sniffing {count} packets on interface {interface}...")
    packets = sniff_packets(interface, count)
    
    for packet in packets:
        print_packet_info(packet)

# Usage
if __name__ == "__main__":
    interface = "wifi"  # Change to your network interface
    packet_count = 10    # Number of packets to capture
    
    start_sniffing(interface, packet_count)
