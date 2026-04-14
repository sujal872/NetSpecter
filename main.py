from utils import banner
import socket
from core import domain_info
from core import ports_scan

def main():
    domain = domain_info.domain()
    ports_scan.ports_Scanner(domain)
    
    
if __name__ == "__main__":
    banner.banner()
    main()