import os

class ContactView:

    def display_menu(self):
        self.clear_terminal()
        print("="*30)
        print("       Agenda de Contactos      ")
        print("="*30)
        print("1. Añadir contacto")
        print("2. Ver contactos")
        print("3. Actualizar contacto")
        print("4. Eliminar contacto")
        print("5. Salir")
        print("="*30)

    def get_contact_info(self):
        print("\nIntroduce los datos del contacto:")
        name = input("Nombre: ")
        phone = input("Teléfono: ")
        email = input("Email: ")
        return name, phone, email

    def display_contacts(self, contacts):
        if not contacts:
            print("\nNo hay contactos.\n")
        else:
            print("\nLista de Contactos:")
            print("="*30)
            for contact in contacts:
                print(f"ID: {contact[0]}, Nombre: {contact[1]}, Teléfono: {contact[2]}, Email: {contact[3]}")
            print("="*30)

    def get_contact_id(self):
        return int(input("ID del contacto: "))

    def clear_terminal(self):
        # Clear terminal based on the operating system
        if os.name == 'nt':  # For Windows
            os.system('cls')
        else:  # For Unix-based systems (Linux and macOS)
            os.system('clear')