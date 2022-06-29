import socket # Um eien Verbindug aufzubauen
import subprocess # Um mehrere Prozzes gleichzeitig laufen zu lassen
import sys
from datetime import datetime
from art import*
import re # Um eien Format zu defenieren

# Pattern für die IP-Adresse
ip_add_pattern = re.compile("^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$")
# Pattern für die Ports
port_range_pattern = re.compile("([0-9]+)-([0-9]+)")
# Ports
port_min = 0
port_max = 65535

# Title
title = "Port Scanner\nby\nPeruKingo"
tprint(title)

# Liste von Wichtigen Ports
imp_port = [21, 22, 23, 25, 49, 67, 68, 80, 88, 110, 111, 123, 135, 137, 138, 139, 143, 161, 179, 201, 389, 443, 445, 500, 514, 520, 587, 902, 1433, 1434, 3306, 3389, 5900]
# Liste der Port die am Ende ausgegeben werden soll
open_ports = []
# User soll die IP-Adresse eingeben
while True:
    ip_add_entered = input("\nGib bitte eine IP-Adresse ein: ")
    # Überprüft ob die IP-Adresse valiede ist
    if ip_add_pattern.search(ip_add_entered):
        print(f"{ip_add_entered} es ist eine Valiede IP-Adresse")
        break

# User wahl der Scan Methode  
while True:
    methode = input("\nWillst du die Port selber wählen(s) oder das Ziehl auf wichtige Ports überprüfen lassen(w)? ")
    if methode == "w" or methode == "s":
        break
    
        
# Um die Zeitmessung zu starten
tstart = datetime.now()

# Port Scannig selber wählen
if methode == "s":
    while True:
        # User soll Ports angeben
        print("Bitte gib die Portspanne an, die du Scannen willst, in diesem Format: <int>-<int> (Beispiel: 60-120)")
        port_range = input("Portspanne: ")
        # Port überprüfen
        port_range_valid = port_range_pattern.search(port_range.replace(" ",""))
        if port_range_valid:
            port_min = int(port_range_valid.group(1))
            port_max = int(port_range_valid.group(2))
            break

    for port in range(port_min, port_max + 1):
        try:
            # Socket erstellen
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                # Jeder Port braucht 0.5 sec
                s.settimeout(0.5)
                # Benutzen den Socket um uns mit der IP-Adresse und dem Port zu verbinden
                s.connect((ip_add_entered, port))
                # Wenn es dies Zeile läft isr der Port offen
                # Hier werden die offenen Ports in die Liste gespeichert
                open_ports.append(port)

        except:
            pass

# Port Scanning mit der Liste imp_port   
elif methode == "w":
    for port in imp_port:
        try:
            # Socket erstellen
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                # Jeder Port braucht 0.5 sec
                s.settimeout(0.5)
                # Benutzen den Socket um uns mit der IP-Adresse und dem Port zu verbinden
                s.connect((ip_add_entered, port))
                # Wenn es dies Zeile läft isr der Port offen
                # Hier werden die offenen Ports in die Liste gespeichert
                open_ports.append(port)

        except:
            pass
    

# Ausgabe der Offenen Port aus der Liste open_ports
for port in open_ports:
    if port == 22:
        print(f"Port {port} ssh ist offen {ip_add_entered}.")
    elif port == 21:
        print(f"Port {port} ftp ist offen {ip_add_entered}.")
    elif port == 23:
        print(f"Port {port} telnet ist offen {ip_add_entered}.")
    elif port == 80:
        print(f"Port {port} http ist offen {ip_add_entered}.")
    elif port == 139:
        print(f"Port {port} smb ist offen {ip_add_entered}.")
    elif port == 433:
        print(f"Port {port} https ist offen {ip_add_entered}.")   
    elif port == 445:
        print(f"Port {port} smb ist offen {ip_add_entered}.")
    elif port == 3306:
        print(f"Port {port} mysql ist offen {ip_add_entered}.")
    elif port == 3389:
        print(f"Port {port} rdp ist offen {ip_add_entered}.")
    elif port == 5900:
        print(f"Port {port} vnc ist offen {ip_add_entered}.")
    else:
        # f um die Int Variablen leichter in den print-Befehl einzubetten
        print(f"Port {port} ist offen {ip_add_entered}.")

# Die Zeit berechnen, wie lange der Scan gebraucht hat   
tend = datetime.now()
diff = tend - tstart

print ("Der Scan hat " + str(diff) + " gebraucht")