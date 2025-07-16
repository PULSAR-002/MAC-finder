import scapy.all as scapy

ip = '192.168.1.7/24'


arp_request = scapy.ARP(pdst=ip)
broadcast = scapy.Ether(dst='ff:ff:ff:ff:ff:ff')
arp_request_broadcast = broadcast / arp_request


answered_list = scapy.srp(arp_request_broadcast, timeout=3, verbose=False)[0]

devices = []
for sent, received in answered_list:
    print(f"IP: {received.psrc}, MAC: {received.hwsrc}")
    devices.append({'ip': received.psrc, 'mac': received.hwsrc})

print("\nDevices found:")
for device in devices:
    print(device)
    print("\n")
