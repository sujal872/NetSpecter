# import sys
import socket
from datetime import datetime
 
# Defining a target
# if len(sys.argv) == 2:
#     # translate hostname to IPv4
#     target = socket.gethostbyname(sys.argv[1]) 
# else:
#     print("Invalid amount of Argument")

# domain = input("Enter a domain : ")
def ports_Scanner(domain):
   ip = socket.gethostbyname(domain) 

   print("-" * 50)
   print("Scanning IP : " + ip)
   print("Scanning started at : " + str(datetime.now()))
   print("-" * 50)
   
   try:
      closed = 0
      opened = 0
      
      # will scan ports between 1 to 65,535
      for port in range(80,100):
         s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
         socket.setdefaulttimeout(1)
         
         # returns an error indicator
         result = s.connect_ex((ip,port))
         if result ==0:
               print("Port {} is open".format(port))
               opened = opened + 1
         else:
               closed = closed + 1
            
         s.close()

      print(f"Open Ports : {opened}\nClosed Ports : {closed}")

         
   except KeyboardInterrupt:
         print("\n Exiting Program !!!!")
   except socket.gaierror:
         print("\n Hostname Could Not Be Resolved !!!!")
