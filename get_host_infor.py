import socket

def get_self_info():
    host_name = socket.gethostname()
    print "Host name is %s" % host_name

    IP_address = socket.gethostbyname(host_name)
    print "IP address is %s" % IP_address
    return host_name,IP_address

def remote_machine_info(hostname):
    try:
        print "%s IP addres is %s" % (hostname,socket.gethostbyname(hostname))
    except socket.error, err_msg:
        print "%s: %s" % (hostname,err_msg)
    

if __name__ == "__main__":
    get_self_info()

    remote_machine_info("www.baidu.com")
    remote_machine_info("abc")
