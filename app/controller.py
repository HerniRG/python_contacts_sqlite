import time
from app.model import ContactModel
from app.view import ContactView

class ContactController:
    def __init__(self):
        self.view = ContactView()
        self.model = ContactModel()

    def run(self):
        while True:
            self.view.clear_terminal()
            self.view.display_menu()
            choice = input("Selecciona una opción: ")

            if choice == "1":
                self.add_contact()
            elif choice == "2":
                self.view_contacts()
            elif choice == "3":
                self.update_contact()
            elif choice == "4":
                self.delete_contact()
            elif choice == "5":
                break
            else:
                print("Opción no válida")
            
            # Esperar a que el usuario presione Enter antes de volver al menú
            input("\nPresiona Enter para continuar...")

    def add_contact(self):
        try:
            name, phone, email = self.view.get_contact_info()
            self.model.add_contact(name, phone, email)
            print("Contacto añadido")
        except ValueError as e:
            print(f"Error: {e}")

    def view_contacts(self):
        contacts = self.model.get_contacts()
        self.view.display_contacts(contacts)

    def update_contact(self):
        try:
            contact_id = self.view.get_contact_id()
            if contact_id <= 0:
                raise ValueError("ID de contacto no válido. Debe ser un número positivo.")
            name, phone, email = self.view.get_contact_info()
            self.model.update_contact(contact_id, name, phone, email)
            print("Contacto actualizado")
        except ValueError as e:
            print(f"Error: {e}")

    def delete_contact(self):
        try:
            contact_id = self.view.get_contact_id()
            if contact_id <= 0:
                raise ValueError("ID de contacto no válido. Debe ser un número positivo.")
            self.model.delete_contact(contact_id)
            print("Contacto eliminado")
        except ValueError as e:
            print(f"Error: {e}")