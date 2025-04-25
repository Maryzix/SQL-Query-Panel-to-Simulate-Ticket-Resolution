# Support Ticket Simulator

Creates a SQLite database with simulated ticket data
Inserts incidents with error types such as SAML, permission, timeout, etc.
Allows you to search for tickets by keyword (by error type or description)

## Features

- SQLite database for storing support tickets
- Pre-populated sample data (errors like SAML, timeout, permissions, etc.)
- Search functionality based on keywords
- Simple analytics and troubleshooting simulation

## Getting Started

### Requirements

- Python 3.8+
- SQLite (built-in with Python)
- pytest (for testing)

### Run the Project

```bash
python main.py
