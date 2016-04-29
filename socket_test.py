import socket

def test_socket_timeout(n):
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    print "Default socket timeout: %s" % s.gettimeout()
    s.settimeout(n)
    print "Current socket timeout: %s" % s.gettimeout()

if __name__ == "__main__":
    test_socket_timeout(100)
