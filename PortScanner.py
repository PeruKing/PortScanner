import socket # Um eien Verbindug aufzubauen
import subprocess # Um mehrere Prozzes gleichzeitig laufen zu lassen
import sys
from datetime import datetime

 # Ein Target defenieren
target = "preply.com"
# Um die IP Adresse von einem Hostname zu bekommen
targetip = socket.gethostbyname(target)

# Um die Zeitmessung zu starten
tstart = datetime.now()

try:
    # Die Ports durchgehen
    for p in range(1, 23): 
        # Sokcet erstellen .AF_INET (IPv4), .SOCK_STREAM (Datenübertragungsrate)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Ergebiss erstellen _ex heißt, dass er keine Fehler ausgibt
        res = sock.connect_ex((targetip, p))
        # Wenn das Ergebiss 0 ist haben wir ein offenen Port
        if res == 0:
            print ("Der Port: " + str(p) + " ist offen")
        # Socket Verbindung schließen
        sock.close()
except Exception:
    print ("Ein Fehler ist aufgetreten")
    sys.exit()

# Die Zeit berechnen, wie lange der Scan gebraucht hat   
tend = datetime.now()
diff = tend - tstart

print ("Der Scan hat " + str(diff) + " gebraucht")