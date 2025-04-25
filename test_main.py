import sqlite3
from main import create_schema, populate_sample_data, search_tickets_by_error

def test_ticket_search():
    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()
    create_schema(cursor)
    populate_sample_data(cursor)
    conn.commit()
    results = search_tickets_by_error(cursor, "SAML")
    assert any("SAML" in r[2] or "SAML" in r[3] for r in results)
    conn.close()


def test_timeout_error():
    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()
    create_schema(cursor)
    populate_sample_data(cursor)
    conn.commit()
    results = search_tickets_by_error(cursor, "Timeout")
    assert any("Timeout" in r[2] or "Timeout" in r[3] for r in results)
    conn.close()