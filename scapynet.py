# import scapy.all as scapy
# request = scapy.ARP()
# print(request.show())
#
from scapy.all import *
# ip = IP()
# print(ip.show())
#
# print(ip)
# print(ip.show())
#
# # my_frame = Ether() / IP()
# # print(my_frame)
# # print(my_frame.show())
#
#
#
# from scapy.all import *
# s = IP(dst="google.com")/ICMP()
# print(s.show())


# a=IP(ttl=10)
# print(a)
# print(a.src)
#
# a.dst="192.168.1.1"
#
# print(a)
# print(a.src)
#
# del(a.ttl)
# print(a.show())
#
# b=IP()
# print(b.show())

c=IP()/TCP()
print(c.show())

d=Ether()/IP()/TCP()
print(d.show())

e=IP()/TCP()/"GET /HTTP /1.0\r\n\r\n"
print(e.show())

j = a=Ether()/IP(dst="www.slashdot.org")/TCP()/"GET /index.html HTTP/1.0 \n\n"
print(hexdump(j))

#k=IP(dst="www.slashdot.org/30")
k=IP(dst="www.slashdot.org/30")
dst=Net("www.slashdot.org/30")
print([p for p in k])