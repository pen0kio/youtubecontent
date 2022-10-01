#!/bin/python3
from scapy.all import *

print(r"""  ______            _              ___  ___ _       _                 
  | ___ \          | |             |  \/  |(_)     | |                
  | |_/ /_   _   __| | _ __  __ _  | .  . | _  ___ | |__   _ __  __ _ 
  |    /| | | | / _` || '__|/ _` | | |\/| || |/ __|| '_ \ | '__|/ _` |
  | |\ \| |_| || (_| || |  | (_| | | |  | || |\__ \| | | || |  | (_| |
  \_| \_|\__,_| \__,_||_|   \__,_| \_|  |_/|_||___/|_| |_||_|   \__,_|
                                                                   """)
print("  ****************************************************************")
print(Fore.YELLOW + "  * Copyright of Rudra Kumar Mishra,                             *")
print("  ****************************************************************\n")

#IP Packet
l3 = IP(dst='127.0.0.1')

#Packet_1 
l4 = TCP()
packet1 = l3/l4
send(packet1)

# #Packet_2 Setting Source and Destination Port
l4 = TCP(dport=1, sport=2)
packet2 = l3/l4
send(packet2)

#Packet_3 Setting Up TCP flags and Sequence number
l4 = TCP(dport=1, sport=2, flags='S', seq=1)
packet3 = l3/l4
send(packet3)
# S for SYN
# A for ACK
# R for RST
# F for FIN


#--------------TCP_Options------------------#
 
#Packet_4 Changing Window Size
l4 = TCP(dport=1, sport=2, flags='S', seq=1, window=65535, options=[('WScale', 10)])
packet4 = l3/l4
send(packet4)

#Packet_5 No operations permitted
l4 = TCP(dport=1, sport=2, flags='S', seq=1, window=65535, options=[('WScale', 10), ('NOP', 0)])
packet5 = l3/l4
send(packet5)

# #Packet_6 MSS 
l4 = TCP(dport=1, sport=2, flags='S', seq=1, window=65535, options=[("MSS", 1400)])
packet6 = l3/l4
send(packet6)