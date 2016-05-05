import socket
import sys

SEND_BUF_SIZE = 4096
RECV_BUF_SIZE = 4096

def modify_buff_size():
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    bufsize = sock.getsockopt(socket.SOL_SOCKET,socket.SO_SNDBUF)
    print "Buffer size [Before] : %d" % bufsize

    sock.setsockopt(socket.SOL_TCP,socket.TCP_NODELAY,1)
    sock.setsockopt(socket.SOL_SOCKET,socket.SO_SNDBUF,SEND_BUF_SIZE)
    sock.setsockopt(socket.SOL_SOCKET,socket.SO_RCVBUF,RECV_BUF_SIZE)

    bufsize = sock.getsockopt(socket.SOL_SOCKET,socket.SO_SNDBUF)
    print "Buffer size [After] : %d" % bufsize

def reuse_socket_addr():
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    ## Get the old state of the SO_REUSEADDR option
    old_state = sock.getsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR)
    print "Old sock state: %s" % old_state
    ## Enable the SO_REUSEADDR option
    sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    new_state = sock.getsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR)
    print "New sock state: %s" % new_state

    local_port = 8282

    srv = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    srv.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    srv.bind(('',local_port))
    srv.listen(1)
    print "Listening on port: %s" % local_port
    while True:
        try:
            connect,addr = srv.accept()
            print "Connected by %s:%s" % (addr[0],addr[1])
        except KeyboardInterrupt:
            break
        except socket.error, msg:
            print "%s" % msg

if __name__ == "__main__":
    ##modify_buff_size()
##
    reuse_socket_addr()
