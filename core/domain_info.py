import socket

def domain():
    domain = input("Enter a domain: ").strip()
    start_port = int(input("Enter a start port : "))
    End_port = int(input("Enter a End port : "))

    try:
        ipv4 = socket.gethostbyname(domain)
        try:
            ipv6 = socket.getaddrinfo(domain, None, socket.AF_INET6)[0][4][0]
        except:
            ipv6 = "Not available"
        print("\n===== DOMAIN LOOKUP =====")

        print(f"Domain: {domain}")
        print(f"IPv4: {ipv4}")
        print(f"IPv6: {ipv6}")

        print("\n===== REVERSE LOOKUP =====")

        # Add timeout to avoid long delay
        socket.setdefaulttimeout(2)

        try:
            hostname = socket.gethostbyaddr(ipv4)[0]
        except socket.herror:
            hostname = "Reverse lookup failed"

        print(f"IP: {ipv4}")
        print(f"Hostname: {hostname}")

    except socket.gaierror:
        print("Could not resolve domain.")

    return domain,start_port,End_port
