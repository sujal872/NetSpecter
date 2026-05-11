![NetSpecter Banner](assets/banner.png)

# 👻 NetSpecter

> Scan in Silence. Strike with Precision.

NetSpecter is a modular and high-performance network scanning and reconnaissance tool inspired by Nmap.  
Built using Python, it is designed for learning networking, ethical hacking, and understanding how professional scanners work internally.

The project focuses on:
- Speed
- Simplicity
- Modular architecture
- Real-world scanning concepts

---

# ⚡ Features

## Current Features

- TCP Port Scanning
- UDP Port Scanning
- Multi-threaded Scanning Engine
- Banner Grabbing
- Service Detection
- Fast Scan Mode
- Verbose Output
- Custom Port Selection
- Scan Result Saving
- Clean CLI Interface

---

# 🧠 Supported Scan Modes

| Scan Type | Supported |
|---|---|
| TCP Connect Scan | ✅ |
| UDP Scan | ✅ |
| Banner Grabbing | ✅ |
| Service Detection | ✅ |
| Fast Scan | ✅ |
| Multi-threading | ✅ |

---

# 📂 Project Structure

```bash
NetSpecter/
│
├── main.py
│
├── core/
│   ├── ports_scan.py
│   ├── domain_info.py
│
├── utils/
│   ├── banner.py
│
├── assets/
│   └── banner.png
│
├── results/
│
├── requirements.txt
│
└── README.md

```

# 🚀 Installation
```bash
Clone Repository
git clone https://github.com/sujal872/NetSpecter.git

Enter Directory
cd NetSpecter

Install Requirements
pip install -r requirements.txt

```

# ▶️ How to use NetSpecter ?
```bash
--- Basic TCP Scan ---
python main.py example.com

--- TCP Scan With Banner Grabbing ---
python main.py example.com -T -B

--- TCP Scan With Service Detection ---
python main.py example.com -T -S

--- Full Scan ---
python main.py example.com -T -B -S

--- UDP Scan ---
python main.py example.com -U

--- Scan Specific Ports ---
- Single Port
python main.py example.com -p 80

- Multiple Ports
python main.py example.com -p 22,80,443

- Port Range
python main.py example.com -p 1-1000

--- Fast Scan Mode ---
Scans only common ports.
python main.py example.com -f

--- Verbose Mode ---
python main.py example.com -v

--- Save Results ---
python main.py example.com -T -B -S -o result.txt

```

# 🛠 Command Line Arguments

Argument	Description
-T	        Enable TCP Scan
-U	        Enable UDP Scan
-B	        Enable Banner Grabbing
-S	        Enable Service Detection
-p	        Select Ports
-f	        Fast Scan Mode
-v	        Verbose Output
-o	        Save Results To File
-O	        Basic OS Guess

# 📸 Example Output

```bash
[+] TCP 22 OPEN
    Banner : SSH-2.0-OpenSSH_8.2
    Service: OpenSSH

[+] TCP 80 OPEN
    Banner : HTTP/1.1 200 OK
    Service: Apache

```

# 🧪 Tested On

- Kali Linux
- Ubuntu
- Windows 10/11
- Metasploitable 2
- Local Virtual Labs



# 📌 Planned Features

- SYN Stealth Scan
- Async Scanning Engine
- Advanced OS Fingerprinting
- JSON/CSV Export
- Interactive Shell
- Progress Bars
- Colored Terminal Output
- Custom Packet Crafting
- NSE-like Scripts
- Web Dashboard



# ⚠️ Disclaimer

This project is developed strictly for:

- Educational purposes
- Ethical hacking labs
- Authorized environments
- Security research

### Do NOT use this tool against systems without permission.

## The developer is not responsible for misuse or illegal activity.

# 👨‍💻 Author
- Sujal Karnwal
- Cybersecurity & SOC Enthusiast

# ⭐ Support

### If you like this project:

- Star the repository
- Fork the project
- Contribute improvements
- Share feedback