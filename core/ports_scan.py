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


# Banner Grabbing
def banner_grab(ip, port):

    try:

        s = socket.socket(
            socket.AF_INET,
            socket.SOCK_STREAM
        )

        s.settimeout(2)

        s.connect((ip, port))

        # HTTP Request
        if port in [80, 8080, 8000]:

            request = (
                b"GET / HTTP/1.1\r\n"
                b"Host: target\r\n"
                b"Connection: close\r\n\r\n"
            )

            s.send(request)

        banner = s.recv(4096).decode(
            errors="ignore"
        )

        s.close()

        if banner:
            return banner.strip()[:200]

        return "No Banner"

    except:
        return "No Banner"



# Service Detection
def service_detection(port, banner=""):

    service = COMMON_SERVICES.get(
        port,
        "Unknown"
    )

    b = banner.lower()

    if "apache" in b:
        service = "Apache"

    elif "nginx" in b:
        service = "Nginx"

    elif "openssh" in b:
        service = "OpenSSH"

    elif "mysql" in b:
        service = "MySQL"

    elif "ftp" in b:
        service = "FTP"

    return service



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



# UDP Scan
def udp_scan(target, ports, verbose=False):

    try:

        ip = socket.gethostbyname(target)

        print("-" * 60)
        print(f"[+] Starting UDP Scan On {ip}")
        print("-" * 60)

        for port in ports:

            try:

                s = socket.socket(
                    socket.AF_INET,
                    socket.SOCK_DGRAM
                )

                s.settimeout(1)

                s.sendto(b"test", (ip, port))

                try:

                    data, _ = s.recvfrom(1024)

                    print(f"[+] UDP {port} OPEN")

                except socket.timeout:

                    if verbose:
                        print(
                            f"[-] UDP {port} OPEN|FILTERED"
                        )

                s.close()

            except Exception as e:

                if verbose:
                    print(
                        f"[ERROR] UDP {port}: {e}"
                    )

        print("\n[+] UDP Scan Finished")

    except Exception as e:
        print(f"[-] UDP Scan Error: {e}")



# Basic OS Detection
def os_guess(target):

    print("\n" + "-" * 60)
    print("[+] Basic OS Detection")
    print("-" * 60)

    try:

        system = platform.system().lower()

        # Windows
        if system == "windows":
            command = ["ping", "-n", "1", target]

        # Linux
        else:
            command = ["ping", "-c", "1", target]

        output = subprocess.check_output(
            command,
            universal_newlines=True
        )

        # Extract TTL
        ttl_match = re.search(
            r"ttl[=\s](\d+)",
            output,
            re.IGNORECASE
        )

        if ttl_match:

            ttl = int(ttl_match.group(1))

            print(f"[+] TTL Value : {ttl}")

            if ttl <= 64:
                print("[+] Possible OS : Linux/Unix")

            elif ttl <= 128:
                print("[+] Possible OS : Windows")

            else:
                print(
                    "[+] Possible OS : Cisco/Network Device"
                )

        else:
            print("[-] TTL Value Not Found")

    except Exception as e:
        print(f"[-] OS Detection Failed: {e}")



# Save Results
def save_results(filename):

    try:
        with open(f'results/{filename}', "w") as f:

            f.write(
                "========== NetSpecter Scan ==========\n\n"
            )

            for result in scan_results:

                f.write(
                    f"Port    : {result['port']}\n"
                )

                f.write(
                    f"Service : {result['service']}\n"
                )

                f.write(
                    f"Banner  : {result['banner']}\n"
                )

                f.write("-" * 40 + "\n")

        print(f"\n[+] Results Saved To {filename}")

    except Exception as e:
        print(f"[-] Save Failed: {e}")