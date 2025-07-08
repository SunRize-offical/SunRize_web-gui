import socket

def is_mc_online(ip='192.168.1.100', port=25565):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(2)
    try:
        s.connect((ip, port))
        s.close()
        return True
    except:
        return False

