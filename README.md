# Munich Transportion Messages

This repository contains a Python script to scrape and gather messages from the Munich transport complaint platform. The script scrapes data within a specified geographical area, fetches detailed information for each message, and saves the results to JSON files.

<img src="https://github.com/TrafficGCN/munich-transportion-messages/blob/main/Download.png?raw=true" width="100%" align="right">
<br />

## Terms of Use and Data Refrences
To use or publish this data, you must follow the terms of use, which can be found at https://muenchenunterwegs.de/p/impressum https://muenchenunterwegs.de/kontakt and cite the data from the City of Munich Mobilitätsreferat.

## Features

- Scrapes messages related to all modes of transport from the specified area in Munich.
- Fetches detailed infobox and message data for each message.
- Saves combined data and a slim export with just message details.

## Requirements

- Python 3.6+
- `requests`
- `math`
- `time`
- `json`

## Installation

1. Clone this repository:
    ```sh
    git clone https://github.com/thomas.fink/munich-transport-messages.git
    cd munich-transport-messages
    ```

2. Install the required Python packages:
    ```sh
    pip install requests
    ```

## Usage

1. Run the script to scrape the entire area and fetch message details:
    ```sh
    python scrape_map.py
    ```

2. The script will save two files:
    - `combined_response.json`: The combined data of all messages scraped from the specified area.
    - `updated_combined_response_with_details.json`: The combined data with infobox and message and answers.
    - `slim_export.json`: A slim export containing only the message and answers.

## Script Explanation

The script performs the following steps:

1. **Scrape Entire Area**: Scrapes messages within a specified bounding box, tile by tile.
2. **Save Initial Response**: Saves the initial combined response to `combined_response.json`.
3. **Fetch Infobox and Message Details**: Loads the combined response and fetches infobox and message details for each message.
4. **Save Final Data**: Saves the updated data with details and a slim export with just the message details.

## Configuration

- You can modify the area boundaries, zoom level, number of rows, and tile size in the script to customize the scraping area and granularity.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


# Münchner Verkehrsmeldungen

Dieses Repository enthält ein Python-Skript, um Nachrichten von der Münchner Beschwerdeplattform für Verkehrsmeldungen zu sammeln. Das Skript sammelt Daten innerhalb eines bestimmten geografischen Gebiets, ruft detaillierte Informationen für jede Nachricht ab und speichert die Ergebnisse in JSON-Dateien.

<img src="https://github.com/TrafficGCN/munich-transportion-messages/blob/main/Download.png?raw=true" width="100%" align="right">
<br />

## Nutzungsbedingungen und Datenreferenzen
Um diese Daten zu verwenden oder zu veröffentlichen, müssen Sie die Nutzungsbedingungen beachten, die Sie unter https://muenchenunterwegs.de/p/impressum https://muenchenunterwegs.de/kontakt finden, und die Daten des Mobilitätsreferats der Stadt München zitieren.

## Funktionen

- Sammelt Nachrichten zu allen Verkehrsmodi aus dem angegebenen Gebiet in München.
- Ruft detaillierte Infobox- und Nachrichtendaten für jede Nachricht ab.
- Speichert kombinierte Daten und einen kompakten Export mit nur den Nachrichtendetails.

## Anforderungen

- Python 3.6+
- `requests`
- `math`
- `time`
- `json`

## Installation

1. Klonen Sie dieses Repository:
    ```sh
    git clone https://github.com/thomas.fink/munich-transport-messages.git
    cd munich-transport-messages
    ```

2. Installieren Sie die erforderlichen Python-Pakete:
    ```sh
    pip install requests
    ```

## Nutzung

1. Führen Sie das Skript aus, um das gesamte Gebiet zu durchsuchen und Nachrichtendetails abzurufen:
    ```sh
    python scrape_map.py
    ```

2. Das Skript speichert zwei Dateien:
    - `combined_response.json`: Die kombinierten Daten aller gesammelten Nachrichten aus dem angegebenen Gebiet.
    - `updated_combined_response_with_details.json`: Die kombinierten Daten mit Infobox- und Nachrichten und Antworten.
    - `slim_export.json`: Ein kompakter Export, der nur die Nachrichten und Antworten enthält.

## Erklärung des Skripts

Das Skript führt die folgenden Schritte aus:

1. **Gesamtes Gebiet durchsuchen**: Sammelt Nachrichten innerhalb eines bestimmten Begrenzungsrahmens, Kachel für Kachel.
2. **Anfängliche Antwort speichern**: Speichert die anfängliche kombinierte Antwort in `combined_response.json`.
3. **Infobox- und Nachrichtendetails abrufen**: Lädt die kombinierte Antwort und ruft Infobox- und Nachrichtendetails für jede Nachricht ab.
4. **Endgültige Daten speichern**: Speichert die aktualisierten Daten mit Details und einen kompakten Export mit nur den Nachrichtendetails.

## Konfiguration

- Sie können die Gebietsgrenzen, die Zoomstufe, die Anzahl der Zeilen und die Kachelgröße im Skript anpassen, um das Durchsuchungsgebiet und die Granularität zu konfigurieren.

## Lizenz

Dieses Projekt ist unter der MIT-Lizenz lizenziert - siehe die [LICENSE](LICENSE) Datei für Details.
