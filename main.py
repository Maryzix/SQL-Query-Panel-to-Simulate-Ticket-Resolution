import sqlite3
import random

def connect_db(db_name="support_tickets.db"):
    return sqlite3.connect(db_name)

def create_schema(cursor):
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tickets (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        description TEXT,
        status TEXT,
        error_type TEXT,
        resolution TEXT
    )
    """)

def populate_sample_data(cursor):
    titles = ["Login Failure", "Data Sync Error", "Timeout in Report", "Missing Data", "Access Denied"]
    descriptions = [
        "User unable to login due to SAML authentication failure.",
        "Data from external source is not syncing properly.",
        "User experiences timeout when generating monthly report.",
        "Sales data for last week is missing from dashboard.",
        "User cannot access the financial reports section."
    ]
    error_types = ["SSO/SAML", "Data Integration", "Timeout", "Missing Data", "Permissions"]
    resolutions = [
        "Checked SAML configuration; updated IdP metadata.",
        "Restarted sync process; verified data pipeline health.",
        "Increased report generation timeout limit.",
        "Refreshed data source; forced re-indexing.",
        "Updated user role permissions in admin panel."
    ]
    for _ in range(10):
        idx = random.randint(0, 4)
        cursor.execute("""
        INSERT INTO tickets (title, description, status, error_type, resolution)
        VALUES (?, ?, ?, ?, ?)
        """, (
            titles[idx],
            descriptions[idx],
            "Open",
            error_types[idx],
            resolutions[idx]
        ))

def search_tickets_by_error(cursor, keyword):
    cursor.execute("""
    SELECT id, title, description, error_type, resolution FROM tickets
    WHERE error_type LIKE ? OR description LIKE ?
    """, (f"%{keyword}%", f"%{keyword}%"))
    return cursor.fetchall()

if __name__ == "__main__":
    conn = connect_db()
    cursor = conn.cursor()
    create_schema(cursor)
    populate_sample_data(cursor)
    conn.commit()
    
    keyword = input("🔍 Digite a palavra-chave para buscar (ex: 'SAML', 'Timeout'): ")
    results = search_tickets_by_error(cursor, keyword)
    
    if results:
        for r in results:
            print(f"\nID: {r[0]} | Title: {r[1]}\nError Type: {r[3]}\nDescription: {r[2]}\nResolution: {r[4]}\n---")
    else:
        print("Nenhum ticket encontrado com essa palavra.")
    
    conn.close()
