import csv
import random
from datetime import datetime, timedelta

# Generieren zufälliger Prozesse und Betreffs
prozesse = ["Prozess_A", "Prozess_B", "Prozess_C", "Prozess_D", "Prozess_E"]
betreffs = ["Aufgabe_X", "Aufgabe_Y", "Aufgabe_Z", "Aufgabe_W", "Aufgabe_V"]

# Generieren zufälliger Zeitpunkte
def random_time():
    start_time = datetime.now() - timedelta(days=random.randint(0, 30), hours=random.randint(0, 23), minutes=random.randint(0, 59))
    duration = timedelta(minutes=random.randint(1, 120))  # Prozessdauer zwischen 1 und 120 Minuten
    end_time = start_time + duration
    return start_time.strftime("%Y-%m-%d %H:%M:%S"), end_time.strftime("%Y-%m-%d %H:%M:%S")

# CSV-Datei erstellen und mit zufälligen Daten füllen
filename = "./data/zufaellige_prozessdaten.csv"
with open(filename, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['id', 'StartUhrZeit', 'EndUhrzeit', 'Prozess', 'Betreff'])
    
    for i in range(1, 1001):
        start, end = random_time()
        writer.writerow([i, start, end, random.choice(prozesse), random.choice(betreffs)])

filename
