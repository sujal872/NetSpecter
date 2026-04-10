def banner():
    import time
    from colorama import Fore, Style, init

    init(autoreset=True)

    logo = r"""
███╗   ██╗███████╗████████╗███████╗██████╗ ███████╗ ██████╗████████╗███████╗██████╗ 
████╗  ██║██╔════╝╚══██╔══╝██╔════╝██╔══██╗██╔════╝██╔════╝╚══██╔══╝██╔════╝██╔══██╗
██╔██╗ ██║█████╗     ██║   ███████╗██████╔╝█████╗  ██║        ██║   █████╗  ██████╔╝
██║╚██╗██║██╔══╝     ██║   ╚════██║██╔═══╝ ██╔══╝  ██║        ██║   ██╔══╝  ██╔══██╗
██║ ╚████║███████╗   ██║   ███████║██║     ███████╗╚██████╗   ██║   ███████╗██║  ██║
╚═╝  ╚═══╝╚══════╝   ╚═╝   ╚══════╝╚═╝     ╚══════╝ ╚═════╝   ╚═╝   ╚══════╝╚═╝  ╚═╝
"""

    # Animated print (line by line)
    for line in logo.split("\n"):
        print(Fore.RED + Style.BRIGHT + line.center(90))
        time.sleep(0.03)

    print(Fore.GREEN + Style.BRIGHT + "\n" + "━" * 90)

    print(Fore.LIGHTGREEN_EX + Style.BRIGHT + "      Scan in Silence. Strike with Precision.".center(90))

    print(Fore.GREEN + "━" * 90)

    time.sleep(0.2)

    info = f"""
{Fore.YELLOW}[+] Tool      : NetSpecter
{Fore.YELLOW}[+] Type      : Network Scanner & Recon Tool
{Fore.YELLOW}[+] Engine    : Multi-threaded / Async Ready
{Fore.YELLOW}[+] Mode      : Stealth Reconnaissance

{Fore.RED}[!] Use only for educational & authorized testing!
"""

    for line in info.split("\n"):
        print(line.center(90))
        time.sleep(0.02)

    print(Fore.GREEN + "━" * 90)