from utils import banner
import socket
from core import domain_info
from core import ports_scan
import argparse

# python main.py  facebook.com -TCP/UDP -sp 80 /-mp 90,92 /-rp 100-200 -sV -O / -f /--fast
def parse_ports(port_input):
    # Case 2: single port
    if port_input.isdigit():
        return [int(port_input)]

    # Case 3: multiple ports (comma separated)
    elif "," in port_input:
        return [int(p.strip()) for p in port_input.split(",")]

    # Case 4: range
    elif "-" in port_input:
        start, end = map(int, port_input.split("-"))
        return list(range(start, end + 1))

    else:
        raise argparse.ArgumentTypeError("Invalid port format")


#Main 
def main():
    parser = argparse.ArgumentParser(
    description="NetSpecter Tool",
    epilog="Example : python main.py  example.com -TCP/UDP -sp 80 /-mp 90,92 /-rp 100-200 -sV -O / -f /--fast"
    )

    parser.add_argument("target",help="Domain name for scan usnig NetSpecter")
    parser.add_argument(
        "-p",
        "--port",
        type=parse_ports,
        help="Port(s): single (80), multiple (22,80), range (1-100)",
        default=list(range(1, 1001)) #default case
    )

    args = parser.parse_args()
    
    domain_info.domain(args.target)
    ports_scan.ports_scanner(args.target,args.port)

if __name__ == "__main__":
    banner.banner()
    main()

