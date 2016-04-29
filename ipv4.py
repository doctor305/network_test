import socket
from binascii import hexlify

def convert_ip4_address(ip_addr):
    packed_ip_addr = socket.inet_aton(ip_addr)
    unpacked_ip_addr = socket.inet_ntoa(packed_ip_addr)
    print "IP address: %s  =>  Packed: %s, Unpacked: %s" % \
          (ip_addr,hexlify(packed_ip_addr),unpacked_ip_addr)
def convert_integer(data):
    #32bit
    print "Original: %s ==> Long host byte order: %s, Network byte order: %s" \
          % (data,socket.ntohl(data),socket.htonl(data))
    #16bit
    print "Original: %s ==> Short host byte order: %s, Network byte order: %s" \
          % (data,socket.ntohs(data),socket.htons(data))

if __name__ == "__main__":
    convert_ip4_address('192.168.1.1')

    convert_integer(1234)
