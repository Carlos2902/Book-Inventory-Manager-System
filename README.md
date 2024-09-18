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
   You will need an admin account to access the Django admin panel. You can either create a new admin account or use the following credentials:  
   **Username**: `admin`  
   **Password**: `123`
   ```bash
   python manage.py createsuperuser

7. **Run the server:**
   Start the Django development server:
   ```bash
   python manage.py runserver
   
You can now access the application at `http://localhost:8000/admin/`



   
