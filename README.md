# gpt_repo

Dieses Repository enthält eine einfache Streamlit-Anwendung, die Daten in einer SQLite-Datenbank verwaltet. Die Anwendung speichert für jeden Datensatz folgende Informationen:

- Name des Datensatzes
- Wert des Datensatzes
- Quelle (Link)
- Datum der letzten Aktualisierung (dd.mm.yyyy)
- Name des letzten Bearbeiters
- Systemgrenze
- Product Category Rule (PCR)

## Starten der Anwendung

1. Abhängigkeiten installieren:
   ```bash
   pip install streamlit
   ```
2. Anwendung ausführen:
   ```bash
   streamlit run streamlit_app.py
   ```

Beim ersten Start wird automatisch eine Datenbank *datasets.db* mit einem Beispiel-Datensatz angelegt. 
Die Weboberfläche ermöglicht das Anzeigen und Bearbeiten der gespeicherten Daten.
