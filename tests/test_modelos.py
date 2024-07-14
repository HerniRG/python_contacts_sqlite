import pytest
import os
import tempfile
from app.model import ContactModel

def get_temp_db():
    temp_db = tempfile.NamedTemporaryFile(delete=False)
    temp_db.close()
    return temp_db.name

def test_create_table():
    db_name = get_temp_db()
    model = ContactModel(db_name)
    query = "SELECT name FROM sqlite_master WHERE type='table' AND name='contacts';"
    cursor = model.conn.execute(query)
    assert cursor.fetchone() is not None
    os.remove(db_name)

def test_add_contact():
    """Test adding a new contact."""
    db_name = get_temp_db()
    model = ContactModel(db_name)
    model.add_contact("John Doe", "123456789", "john.doe@example.com")
    contacts = model.get_contacts()
    assert len(contacts) == 1
    assert contacts[0][1] == "John Doe"
    assert contacts[0][2] == "123456789"
    assert contacts[0][3] == "john.doe@example.com"
    os.remove(db_name)

def test_get_contacts():
    db_name = get_temp_db()
    model = ContactModel(db_name)
    model.add_contact("Jane Doe", "987654321", "jane.doe@example.com")
    contacts = model.get_contacts()
    assert len(contacts) == 1
    assert contacts[0][1] == "Jane Doe"
    assert contacts[0][2] == "987654321"
    assert contacts[0][3] == "jane.doe@example.com"
    os.remove(db_name)

def test_delete_contact():
    db_name = get_temp_db()
    model = ContactModel(db_name)
    model.add_contact("John Doe", "123456789", "john.doe@example.com")
    contacts = model.get_contacts()
    contact_id = contacts[0][0]
    model.delete_contact(contact_id)
    remaining_contacts = model.get_contacts()
    assert len(remaining_contacts) == 0
    os.remove(db_name)