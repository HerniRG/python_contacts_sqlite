import os

class ContactView:

    def clear_terminal(self):
        # Clear terminal based on the operating system
        if os.name == 'nt':  # For Windows
            os.system('cls')
        else:  # For Unix-based systems (Linux and macOS)
            os.system('clear')

    def display_menu(self):
        print("Agenda de Contactos")
        print("1. Añadir contacto")
        print("2. Ver contactos")
        print("3. Actualizar contacto")
        print("4. Eliminar contacto")
        print("5. Salir")

    def get_contact_info(self):
        name = input("Nombre: ")
        phone = input("Teléfono: ")
        email = input("Email: ")
        return name, phone, email

    def display_contacts(self, contacts):
        if not contacts:
            print("No hay contactos.")
        else:
            for contact in contacts:
                print(f"ID: {contact[0]}, Nombre: {contact[1]}, Teléfono: {contact[2]}, Email: {contact[3]}")

    def get_contact_id(self):
        return int(input("ID del contacto: "))