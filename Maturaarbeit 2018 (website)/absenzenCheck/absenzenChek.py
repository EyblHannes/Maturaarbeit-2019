#um den Absenzen-Check zu aktivieren muss diese Python-Datei ausgeführt werden.
#Dieser Skript führt alle 24 Stunden einen PHP-Script mit dem gleichen Namen aus, 
#welcher die absenzen-DB nach gültigen und ungültigen Absenzen prüft.

import subprocess, datetime


while(true)
    if(datetime.datetime.now().hour == 12)
        subprocess.call("absenzenCheck.php")

