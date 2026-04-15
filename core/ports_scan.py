import socket
import threading
from datetime import datetime

lock = threading.Lock()

open_ports = 0
closed_ports = 0

def scan_port(ip, port):
    global open_ports, closed_ports
    
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        
        result = s.connect_ex((ip, port))
        
        with lock:
            if result == 0:
                print(f"[+] Port {port} is OPEN")
                open_ports += 1
            else:
                closed_ports += 1
        
        s.close()
        
    except Exception:
        pass


def ports_scanner(domain,S_p,E_p):
    global open_ports, closed_ports
    
    ip = socket.gethostbyname(domain)

    print("-" * 50)
    print("Scanning IP:", ip)
    print("Scanning started at:", datetime.now())
    print("-" * 50)

    threads = []

    try:
        for port in range(S_p, E_p):
            t = threading.Thread(target=scan_port, args=(ip, port))
            threads.append(t)
            t.start()

        # wait for all threads to finish
        for t in threads:
            t.join()

        print("\nScan Completed!")
        print(f"Open Ports : {open_ports}")
        print(f"Closed Ports : {closed_ports}")

    except KeyboardInterrupt:
        print("\nExiting Program !!!!")
    except socket.gaierror:
        print("\nHostname Could Not Be Resolved !!!!")


