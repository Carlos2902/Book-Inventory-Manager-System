# Book Inventory Management System

## Overview
This Book Inventory Management System is built using **Django** and **Django REST Framework** to provide a robust, scalable solution for managing a collection of books. The system allows users to add, update, and delete book records, filter books based on various criteria, and export data in CSV or JSON formats. It’s designed to be easily extendable and integrates security layers to ensure the safe handling of data.

## Features
- Add, edit, and delete books
- Filter books by title, author, genre, or publication date
- Export books as CSV or JSON files
- Built-in security and scalability using Django REST Framework
- Uses SQLite for quick setup but can easily be migrated to other relational databases

## Installation and Setup

To get started with the project:

1. **Clone the repository:**

   ```bash
   git clone https://github.com/Carlos2902/Book-Inventory-Manager-System.git
   cd Book-Inventory-Manager

2. **Install Pipenv:**
   Open your terminal, navigate to the project directory and install pipenv if you don't have i
   ```bash
   pip install pipenv

3. **Install the dependencies:**
   Use Pipenv to install all the required packages, including Django and Django REST Framework:
   ```bash
   pipenv install

4. **Activate the virtual environment:**
   ```bash
   pipenv shell

5. **Apply the migrations:**
   To set up the database and create the necessary tables, run:
   ```bash
   python manage.py migrate
   
6. **Create a superuser(optional):**
   You will need an admin account to access the Django admin panel.
   You can either create a new admin account or use the following credentials:  
   **Username**: `admin`  
   **Password**: `123`
   ```bash
   python manage.py createsuperuser

8. **Run the server:**
   Start the Django development server:
   ```bash
   python manage.py runserver
   
You can now access the application at `http://localhost:8000/admin/`






## Design Decisions

### Framework Choice

**Django REST Framework** was chosen for its flexibility and the ability to leverage its built-in UI interface. This decision allowed me to focus more on database logic and CRUD operations rather than building UI components from scratch. **Django REST Framework** provides robust security features and scalability through its serializers. The use of serializers simplifies the conversion of complex data types into JSON or XML and ensures secure communication. This approach enhances the system's scalability by making it easier to manage and validate data structures.

### Database Choice

For this rapid development project, I used **SQLite** due to its simplicity and ease of setup. However, Django’s architecture allows for easy integration with other relational databases such as **MySQL**, **PostgreSQL**, and **Oracle**. This flexibility means that the system can be scaled and adapted to different database technologies as needed.

### Models and Database Schema

The project uses Django's powerful model system to define the database schema. This approach offers several advantages over raw SQL queries:
- **Abstraction**: Models abstract away the complexities of SQL queries, allowing for a more intuitive interaction with the database.
- **Maintainability**: Django models simplify code maintenance and updates by providing a clear and organized way to manage database interactions.
- **Security**: Django’s ORM protects against SQL injection attacks by using parameterized queries.

A relationship diagram is provided to illustrate the relationships between the models in the system. This diagram shows how the different entities (e.g., `Book`, `Author`, `Genre`) are connected and how data flows between them.


   
