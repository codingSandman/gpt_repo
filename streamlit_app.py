import sqlite3
import streamlit as st
from datetime import datetime

DB_NAME = 'datasets.db'


def init_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS datasets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE,
            value TEXT,
            source TEXT,
            last_update TEXT,
            last_editor TEXT,
            system_boundary TEXT,
            pcr TEXT
        )
    ''')
    c.execute('SELECT COUNT(*) FROM datasets')
    if c.fetchone()[0] == 0:
        c.execute('''INSERT INTO datasets (name, value, source, last_update, last_editor, system_boundary, pcr)
                     VALUES (?, ?, ?, ?, ?, ?, ?)''',
                  (
                      'Beispiel-Datensatz',
                      '0',
                      'https://example.com',
                      datetime.now().strftime('%d.%m.%Y'),
                      'admin',
                      'Default Systemgrenze',
                      'Default PCR'
                  ))
    conn.commit()
    conn.close()


def get_datasets():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('SELECT name FROM datasets')
    results = [r[0] for r in c.fetchall()]
    conn.close()
    return results


def get_dataset(name):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''SELECT value, source, last_update, last_editor, system_boundary, pcr FROM datasets WHERE name=?''', (name,))
    row = c.fetchone()
    conn.close()
    return row


def update_dataset(name, value, source, last_update, last_editor, system_boundary, pcr):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''UPDATE datasets SET value=?, source=?, last_update=?, last_editor=?, system_boundary=?, pcr=? WHERE name=?''',
              (value, source, last_update, last_editor, system_boundary, pcr, name))
    conn.commit()
    conn.close()


def main():
    st.title("Dataset Browser")
    init_db()

    dataset_names = get_datasets()
    selected = st.selectbox("Datensatz wählen", dataset_names)

    if selected:
        data = get_dataset(selected)
        if data:
            value, source, last_update, last_editor, system_boundary, pcr = data
            st.markdown(f"**Quelle:** [{source}]({source})")
            st.write("**Wert:**", value)
            st.write("**Letzte Aktualisierung:**", last_update)
            st.write("**Letzter Bearbeiter:**", last_editor)
            st.write("**Systemgrenze:**", system_boundary)
            st.write("**PCR:**", pcr)

            st.subheader("Datensatz bearbeiten")
            new_value = st.text_input("Wert", value)
            new_source = st.text_input("Quelle", source)
            new_last_update = st.text_input("Letzte Aktualisierung (dd.mm.yyyy)", datetime.now().strftime('%d.%m.%Y'))
            new_last_editor = st.text_input("Letzter Bearbeiter", last_editor)
            new_system_boundary = st.text_input("Systemgrenze", system_boundary)
            new_pcr = st.text_input("Product Category Rule", pcr)
            if st.button("Speichern"):
                update_dataset(selected, new_value, new_source, new_last_update, new_last_editor, new_system_boundary, new_pcr)
                st.success("Datensatz aktualisiert")
                st.experimental_rerun()


if __name__ == "__main__":
    main()
