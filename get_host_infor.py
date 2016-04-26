import socket

def get_host_info():
    host_name = socket.gethostname()

    print "Host name is %s" % host_name

    IP_address = socket.gethostbyname(host_name)

    print "IP address is %s" % IP_address

if __name__ == "__main__":
    get_host_info()
