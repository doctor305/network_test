import socket
from binascii import hexlify

def convert_ip4_address(ip_addr):
    packed_ip_addr = socket.inet_aton(ip_addr)
    unpacked_ip_addr = socket.inet_ntoa(packed_ip_addr)
    print "IP address: %s  =>  Packed: %s, Unpacked: %s" % (ip_addr,hexlify(packed_ip_addr),unpacked_ip_addr)


if __name__ == "__main__":
    convert_ip4_address('192.168.1.1')
