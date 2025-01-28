import socket
import common_ports

def get_open_ports(target, port_range, verbose = False):
    open_ports = []

    try:
        parts = target.split(".")
        valid_ip = len(parts) == 4 and all(part.isdigit() for part in parts)

    except ValueError:
        valid_ip = False

    host = target
    if valid_ip:
        try:
            target_ip = socket.gethostbyname(target)
        except socket.gaierror:
            return 'Error: Invalid IP address'
    
    else:
        try:
            target_ip = socket.gethostbyname(target)
        except socket.gaierror:
            return 'Error: Invalid hostname'

    for port in range(port_range[0], port_range[1] + 1):
        clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        clientsocket.settimeout(5)
https://github.com/simon-bouchard/freeCodeCamp-PortScanner
        try:
            clientsocket.connect((target_ip, port))
            open_ports.append(port)
        
        except:
            pass

        finally:
            clientsocket.close()

    if not verbose:
        return(open_ports)

    if valid_ip:
        ip = target_ip
        try:
            host = socket.gethostbyaddr(ip)[0]
        except:
            host = target_ip
    
    if host == target_ip:
        ports = f'Open ports for {host}\nPORT     SERVICE'
    else:
        ports = f'Open ports for {host} ({target_ip})\nPORT     SERVICE'

        


    for port in open_ports:
        service = common_ports.ports_and_services.get(port, 'Service not found')
        ports += f'\n{port}' + ' ' * (9 - len(str(port))) + service
    
    return(ports)