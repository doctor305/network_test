import socket

def find_service_name(port,protocolname):
    print "Port : %s ==> service name : %s" % (port,socket.getservbyport(port,protocolname))


if __name__ == "__main__":
    find_service_name(80,'tcp')
    find_service_name(53,'udp')
