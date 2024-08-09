
# HybridSort-Prozessdaten

Dieses Projekt implementiert einen einzigartigen hybriden Sortieralgorithmus zur Verarbeitung und Sortierung von Prozessdaten. Der Algorithmus wechselt adaptiv zwischen direkter Sortierung und QuickSort basierend auf der Anzahl der Inversionen in den Daten. Das Projekt beinhaltet die Generierung zufälliger Prozessdaten, die Anwendung des Algorithmus auf diese Daten und die Ausgabe der sortierten Daten in separaten CSV-Dateien.

## Features

- **Einzigartiger Hybrid-Sortieralgorithmus**: Kombiniert direkte Sortierung und QuickSort basierend auf einer dynamischen Analyse der Daten.
- **Daten-Generierung**: Generiert eine CSV-Datei mit 1000 zufälligen Prozessdaten, einschließlich Startzeit, Endzeit, Prozessname und Betreff.
- **Verschiedene Sortierkriterien**: Unterstützt das Sortieren nach ID, Startzeit, Endzeit und Prozessname.
- **Ausgabe in separaten CSV-Dateien**: Speichert die sortierten Daten in vier verschiedenen CSV-Dateien, basierend auf den Sortierkriterien.

## Verwendete Technologien

- **Python 3.7+**: Hauptprogrammiersprache für die Implementierung des Algorithmus und der Datenverarbeitung.
- **CSV-Modul**: Zum Lesen und Schreiben der CSV-Dateien.
- **datetime-Modul**: Zur Verarbeitung und Formatierung der Datums- und Zeitangaben.

## Projektstruktur

Die Projektstruktur ist wie folgt aufgebaut:

```
HybridSort-Prozessdaten/
│
├── data/
│   ├── zufaellige_prozessdaten.csv  # Generierte CSV-Datei mit den unsortierten Daten
│   ├── sortiert_nach_id.csv          # Sortierte CSV-Datei nach ID
│   ├── sortiert_nach_start.csv       # Sortierte CSV-Datei nach Startzeit
│   ├── sortiert_nach_end.csv         # Sortierte CSV-Datei nach Endzeit
│   └── sortiert_nach_prozess.csv     # Sortierte CSV-Datei nach Prozessname
│
├── generate_data.py                  # Skript zur Generierung der zufälligen Prozessdaten
├── sort_data.py                      # Skript zur Anwendung des Hybrid-Sortieralgorithmus
└── README.md                         # Projektbeschreibung und Dokumentation
```

## Verwendung

### 1. Generieren der Daten

Um die zufälligen Prozessdaten zu generieren, führen Sie das `generate_data.py`-Skript aus:

```bash
python generate_data.py
```

Dieses Skript erstellt die Datei `zufaellige_prozessdaten.csv` im `data`-Verzeichnis.

### 2. Sortieren der Daten

Verwenden Sie das `sort_data.py`-Skript, um die Daten zu sortieren:

```bash
python sort_data.py
```

Die sortierten Dateien werden im `data`-Verzeichnis gespeichert.

### 3. Zugriff auf die Daten

Nach der Ausführung der Skripte finden Sie die sortierten Dateien in den entsprechenden CSV-Dateien im `data`-Verzeichnis. Sie können die Daten nach ID, Startzeit, Endzeit und Prozessname sortiert anzeigen.

## Verbesserungsmöglichkeiten

### 1. Optimierung des Sortieralgorithmus

- **Adaptive Inversionsanalyse**: Einführung einer dynamischen Schwelle für den Wechsel zwischen Sortiermethoden.
- **Einführung weiterer Sortiermethoden**: Integration zusätzlicher Sortiermethoden wie MergeSort oder HeapSort.
- **Parallelisierung**: Erhöhung der Sortiergeschwindigkeit durch Parallelisierung.

### 2. Erweiterung der Funktionalität

- **Filtern der Daten**: Möglichkeit zum Filtern der Daten vor der Sortierung.
- **Aggregation**: Bereitstellung von aggregierten Daten wie Anzahl der Prozesse pro Zeitraum.
- **Datenvalidierung**: Implementierung einer Validierungsfunktion vor der Sortierung.

### 3. Benutzeroberfläche

- **Webbasierte Benutzeroberfläche**: Entwicklung einer UI zur einfachen Auswahl von Sortierkriterien und Hochladen von CSV-Dateien.
- **Erweiterte Ergebnisanzeige**: Möglichkeit zur Anzeige der sortierten Daten als Diagramme oder Tabellen auf einer Webseite.

## Lizenz

Dieses Projekt ist unter der MIT-Lizenz lizenziert. Weitere Details finden Sie in der LICENSE.md-Datei.
