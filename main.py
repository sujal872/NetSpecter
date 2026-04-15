from utils import banner
import socket
from core import domain_info
from core import ports_scan

def main():
    domain,s_p,e_p = domain_info.domain()
    ports_scan.ports_scanner(domain,s_p,(e_p+1))
    
    
if __name__ == "__main__":
    banner.banner()
    main()