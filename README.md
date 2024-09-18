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

<img width="1440" alt="Screenshot 2024-09-17 at 22 16 12" src="https://github.com/user-attachments/assets/33a6c7c2-ddf9-4006-b971-9ecf6d40eeca">





## Design Decisions

### Framework Choice

**Django REST Framework** was chosen for its flexibility and the ability to leverage its built-in UI interface. This decision allowed me to focus more on database logic and CRUD operations rather than building UI components from scratch. **Django REST Framework** provides robust security features and scalability through its serializers. The use of serializers simplifies the conversion of complex data types into JSON or XML and ensures secure communication. This approach enhances the system's scalability by making it easier to manage and validate data structures.

### Database Choice

For this rapid development project, I used **SQLite** due to its simplicity and ease of setup. However, Django’s architecture allows for easy integration with other relational databases such as **MySQL**, **PostgreSQL**, and **Oracle**. This flexibility means that the system can be scaled and adapted to different database technologies as needed.

### Models and Database Schema

The project uses Django's powerful model system to define the database schema. This approach offers several advantages over raw SQL queries:
- **Abstraction**: Models abstract away the complexities of SQL queries, allowing for a more intuitive interaction with the database.
- **Maintainability**: Django models simplify code maintenance and updates by providing a clear and organized way to manage database interactions.
- **Security**: Django’s Object Relational Mapping protects against SQL injection attacks by using parameterized queries.

The code for the models is as follows:
```python
from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Genre(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    publication_date = models.DateField()
    isbn = models.CharField(max_length=13, unique=True)
    
    def __str__(self):
        return self.title

```
This code shows how the different entities (`Book`, `Author`, `Genre`) are connected and how data flows between them.

`Book`: Has a foreign key relationship with both Author and Genre.
`Author`: Represents the author of a book.
`Genre`: Represents the genre of a book.

## Challenges and Solutions

During development, I encountered several challenges:

### 1.Exporting Data in Different Formats:
One challenge was implementing the functionality to export book data in both CSV and JSON formats. 
The solution was to create custom Django admin actions that allow users to select books and download them in the desired format.

<img width="1107" alt="Screenshot 2024-09-17 at 22 28 53" src="https://github.com/user-attachments/assets/59847269-3f74-48bc-9d59-eabf7a9986e0">


### 2.Database Flexibility:
Since the project was developed quickly, I initially used SQLite for ease of setup. However, I ensured that the system could easily migrate to other databases like MySQL or PostgreSQL by using Django’s ORM and abstracting the database logic from the application.
<img width="419" alt="Screenshot 2024-09-17 at 22 31 39" src="https://github.com/user-attachments/assets/2df2f81d-7ee1-4e03-b082-09607673bf9f">

### Conclusion
This Book Inventory Management System is built to be a flexible, secure, and scalable solution for managing books. Its modular architecture allows it to easily grow and adapt to various use cases, making it a solid foundation for future development.
