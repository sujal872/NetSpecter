import socket

def domain(target):
    # target = input("Enter a target: ").strip()
    try:
        ipv4 = socket.gethostbyname(target)
        try:
            ipv6 = socket.getaddrinfo(target, None, socket.AF_INET6)[0][4][0]
        except:
            ipv6 = "Not available"
        print("\n===== target LOOKUP =====")

        print(f"target: {target}")
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
        print("Could not resolve target.")

   
