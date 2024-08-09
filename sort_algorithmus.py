
import csv
import random
from datetime import datetime

# Einlesen der generierten CSV-Datei
input_file = 'data/zufaellige_prozessdaten.csv'

# Auslesen der Daten
with open(input_file, mode='r', newline='') as file:
    reader = csv.DictReader(file)
    data = [(int(row['id']), row['StartUhrZeit'], row['EndUhrzeit'], row['Prozess'], row['Betreff']) for row in reader]

# Definieren des Sortieralgorithmus
def hybrid_sort(arr, key=lambda x: x):
    def analyze_data(arr):
        # Berechnung von Inversionen ohne Varianz für Datumswerte
        inversions = sum(1 for i in range(len(arr)) for j in range(i+1, len(arr)) if key(arr[i]) > key(arr[j]))
        return inversions

    def quicksort(arr):
        if len(arr) <= 1:
            return arr
        pivot = key(arr[len(arr) // 2])
        left = [x for x in arr if key(x) < pivot]
        middle = [x for x in arr if key(x) == pivot]
        right = [x for x in arr if key(x) > pivot]
        return quicksort(left) + middle + quicksort(right)

    if len(arr) <= 1:
        return arr

    inversions = analyze_data(arr)
    if inversions < len(arr) // 2:
        return sorted(arr, key=key)
    else:
        return quicksort(arr)

# Sortieren nach jeder Spalte
sorted_by_id = hybrid_sort(data, key=lambda x: x[0])
sorted_by_start = hybrid_sort(data, key=lambda x: datetime.strptime(x[1], "%Y-%m-%d %H:%M:%S"))
sorted_by_end = hybrid_sort(data, key=lambda x: datetime.strptime(x[2], "%Y-%m-%d %H:%M:%S"))
sorted_by_prozess = hybrid_sort(data, key=lambda x: x[3])

# Definieren der Dateinamen für die sortierten Dateien
output_files = {
    'id': 'data/sortiert_nach_id.csv',
    'StartUhrZeit': 'data/sortiert_nach_start.csv',
    'EndUhrzeit': 'data/sortiert_nach_end.csv',
    'Prozess': 'data/sortiert_nach_prozess.csv'
}

# Speichern der sortierten Daten in separaten Dateien
with open(output_files['id'], mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['id', 'StartUhrZeit', 'EndUhrzeit', 'Prozess', 'Betreff'])
    writer.writerows(sorted_by_id)

with open(output_files['StartUhrZeit'], mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['id', 'StartUhrZeit', 'EndUhrzeit', 'Prozess', 'Betreff'])
    writer.writerows(sorted_by_start)

with open(output_files['EndUhrzeit'], mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['id', 'StartUhrZeit', 'EndUhrzeit', 'Prozess', 'Betreff'])
    writer.writerows(sorted_by_end)

with open(output_files['Prozess'], mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['id', 'StartUhrZeit', 'EndUhrzeit', 'Prozess', 'Betreff'])
    writer.writerows(sorted_by_prozess)
