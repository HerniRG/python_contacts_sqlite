# Contact Manager Console Application

This is a simple console-based contact manager application using Python and SQLite. The application follows the Model-View-Controller (MVC) pattern to separate concerns and organize the code.

## Features
- Add new contacts
- View all contacts
- Update existing contacts
- Delete contacts

## Project Structure
- `app/model.py`: Handles database operations and manages the contact data.
- `app/view.py`: Manages user input and output in the console.
- `app/controller.py`: Acts as an intermediary between the model and view, handling the logic of the application.
- `main.py`: The entry point to run the application.

## Getting Started
1. Clone the repository:
   ```
   git clone https://github.com/HerniRG/python_contacts_sqlite.git
   ```
2. Ensure you have Python 3.12 installed.
3. Navigate to the project directory:
   ```
   cd python_contacts_sqlite
   ```
4. Run the application:
   ```
   python main.py
   ```

## Requirements
- Python 3.12
- SQLite