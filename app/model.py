import sqlite3

class ContactModel():
    def __init__(self, db_name="contacts.db"):
        self.conn = sqlite3.connect(db_name)
        self.create_table()

    def create_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS contacts (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            phone TEXT NOT NULL,
            email TEXT
        )
        """
        self.conn.execute(query)
        self.conn.commit()

    def add_contact(self, name, phone, email):
        query = "INSERT INTO contacts (name, phone, email) VALUES (?, ?, ?)"
        self.conn.execute(query, (name, phone, email))
        self.conn.commit()

    def get_contacts(self):
        query = "SELECT * FROM contacts"
        cursor = self.conn.execute(query)
        return cursor.fetchall()

    def update_contact(self, contact_id, name, phone, email):
        query = "UPDATE contacts SET name = ?, phone = ?, email = ? WHERE id = ?"
        self.conn.execute(query, (name, phone, email, contact_id))
        self.conn.commit()

    def delete_contact(self, contact_id):
        query = "DELETE FROM contacts WHERE id = ?"
        self.conn.execute(query, (contact_id,))
        self.conn.commit()