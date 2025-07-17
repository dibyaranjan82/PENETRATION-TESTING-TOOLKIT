import socket

def scan_ports(target, ports=[21, 22, 23, 80, 443, 8080]):
    print(f"[+] Scanning Target: {target}")
    for port in ports:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.5)
            result = sock.connect_ex((target, port))
            if result == 0:
                print(f"[OPEN] Port {port}")
            else:
                print(f"[CLOSED] Port {port}")
            sock.close()
        except socket.error as err:
            print(f"[ERROR] {err}")
