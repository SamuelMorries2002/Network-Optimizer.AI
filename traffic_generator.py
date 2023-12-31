from scapy.all import * 
import random
def run_traffic():

 target_ip = '172.203.51.72' 

# ICMP for connectivity testing
 ping = IP(dst=target_ip)/ICMP()  
 sendp(ping,count=50,iface="Wi-Fi")

#ICMP Destination Unreachable
 unreach = IP(dst=target_ip, proto=1)/ICMP(type=3, code=3) 
 sendp(unreach, count=25,iface="Wi-Fi")

# IGMP for multicast testing
 query = IP(dst=target_ip, proto=2)/IGMP(type=0x11)
 sendp(query, count=10,iface="Wi-Fi")

# IP testing
 frag = IP(dst=target_ip, frag=1, proto=1)/ICMP()/("X"*1400)
 sendp(frag, count=50,iface="Wi-Fi") 

 proto = IP(dst=target_ip, proto=255)/UDP()
 sendp(proto, count=10,iface="Wi-Fi")

# ARP testing
 arp = ARP(pdst=target_ip, opcode=1) 
 sendp(arp, count=30,iface="Wi-Fi")
