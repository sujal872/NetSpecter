from utils import banner
from core import domain_info
from core import ports_scan

import argparse

# Parse Ports
def parse_ports(port_input):

    if port_input.isdigit():
        return [int(port_input)]

    elif "," in port_input:
        return [int(p.strip()) for p in port_input.split(",")]

    elif "-" in port_input:
        start, end = map(int, port_input.split("-"))
        return list(range(start, end + 1))

    else:
        raise argparse.ArgumentTypeError(
            "Invalid Port Format"
        )


# Main 
def main():

    parser = argparse.ArgumentParser(

        prog="NetSpecter",

        description="""
Advanced Python Port Scanner
Supports:
- TCP Scanning
- UDP Scanning
- Banner Grabbing
- Service Detection
        """,

        epilog="""
Examples:

python main.py example.com -T
python main.py example.com -T -B -S
python main.py 192.168.1.1 -U -p 53
python main.py example.com -T -p 22,80,443
python main.py example.com -T -f
        """
    )

    # Target
    parser.add_argument(
        "target",
        help="Target Domain or IP Address"
    )

    # Ports
    parser.add_argument(
        "-p",
        "--port",
        type=parse_ports,
        default=list(range(1, 1001)),
        help="""
Port Selection:
80
22,80,443
1-1000
        """
    )

    # TCP Scan
    parser.add_argument(
        "-T",
        "--tcp",
        action="store_true",
        help="Enable TCP Scan"
    )

    # UDP Scan
    parser.add_argument(
        "-U",
        "--udp",
        action="store_true",
        help="Enable UDP Scan"
    )

    # Banner Grabbing
    parser.add_argument(
        "-B",
        "--banner",
        action="store_true",
        help="Enable Banner Grabbing"
    )

    # Service Detection
    parser.add_argument(
        "-S",
        "--service",
        action="store_true",
        help="Enable Service Detection"
    )

    # Fast Scan
    parser.add_argument(
        "-f",
        "--fast",
        action="store_true",
        help="Fast Scan Mode (Top Common Ports)"
    )

    # Verbose
    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="Verbose Output"
    )

    # Basic OS Guess
    parser.add_argument(
        "-O",
        "--os",
        action="store_true",
        help="Basic OS Guess"
    )

    parser.add_argument(
        "-o",
        "--output",
        help="Save Scan Results To File"
    )

    args = parser.parse_args()

    # Default TCP if nothing selected
    if not args.tcp and not args.udp:
        args.tcp = True

    # Fast Scan
    if args.fast:
        args.port = [
            21,22,23,25,53,
            80,110,135,139,
            143,443,445,
            3306,3389,8080
        ]

    # Domain Info
    domain_info.domain(args.target)

    # TCP Scan
    if args.tcp:

        ports_scan.tcp_scan(
            target=args.target,
            ports=args.port,
            banner=args.banner,
            service=args.service,
            verbose=args.verbose
        )

    # UDP Scan
    if args.udp:

        ports_scan.udp_scan(
            target=args.target,
            ports=args.port,
            verbose=args.verbose
        )

    # OS Guess
    if args.os:
        ports_scan.os_guess(args.target)

    #save Results
    if args.output:
        ports_scan.save_results(args.output)    


# Run
if __name__ == "__main__":
    banner.banner()
    main()