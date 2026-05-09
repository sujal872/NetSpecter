import socket
import threading
import subprocess
import platform
import re
from datetime import datetime


# Global Variables
lock = threading.Lock()

open_ports = 0
closed_ports = 0

scan_results = []


# Common Services
COMMON_SERVICES = {

    21: "FTP",
    22: "SSH",
    23: "TELNET",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    143: "IMAP",
    443: "HTTPS",
    3306: "MYSQL",
    3389: "RDP",
    8080: "HTTP-PROXY"
}




# TCP Port Scanner
def scan_port(
    ip,
    port,
    enable_banner=False,
    enable_service=False,
    verbose=False
):

    global open_ports, closed_ports

    try:

        s = socket.socket(
            socket.AF_INET,
            socket.SOCK_STREAM
        )

        s.settimeout(1)

        result = s.connect_ex((ip, port))

        if result == 0:

            banner = ""
            service = "Unknown"

            open_ports += 1

            # Banner Grab
            if enable_banner:
                banner = banner_grab(ip, port)

            # Service Detection
            if enable_service:
                service = service_detection(
                    port,
                    banner
                )

            with lock:

                print(f"\n[+] TCP {port} OPEN")

                if enable_service:
                    print(f"    Service : {service}")

                if enable_banner:
                    print(f"    Banner  : {banner}")

            # Save Result
            result_data = {

                "port": port,
                "service": service,
                "banner": banner
            }

            scan_results.append(result_data)

        else:

            closed_ports += 1
            if verbose:

                with lock:
                    print(f"[-] TCP {port} CLOSED")

        s.close()

    except Exception as e:
        if verbose:
            with lock:
                print(f"[ERROR] {port}: {e}")



# TCP Scan
def tcp_scan(
    target,
    ports,
    banner=False,
    service=False,
    verbose=False
):

    global open_ports, closed_ports

    open_ports = 0
    closed_ports = 0

    try:

        ip = socket.gethostbyname(target)

        print("-" * 60)
        print(f"[+] Target        : {target}")
        print(f"[+] IP Address    : {ip}")
        print(f"[+] Scan Started  : {datetime.now()}")
        print("-" * 60)

        threads = []

        for port in ports:

            t = threading.Thread(

                target=scan_port,

                args=(
                    ip,
                    port,
                    banner,
                    service,
                    verbose
                )
            )

            threads.append(t)
            t.start()

        # Wait For All Threads
        for t in threads:
            t.join()

        print("\n" + "-" * 60)
        print("[+] TCP Scan Finished")
        print(f"[+] Open Ports   : {open_ports}")
        print(f"[+] Closed Ports : {closed_ports}")
        print("-" * 60)

    except socket.gaierror:
        print("[-] Hostname Could Not Be Resolved")

    except KeyboardInterrupt:
        print("\n[-] Scan Interrupted")

    except Exception as e:
        print(f"[-] Error: {e}")


