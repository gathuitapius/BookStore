# **Console Book Rental Management System**

A Python application that manages book rentals and user authentication, providing functionalities to add books, rent books, display available and rented books, and manage users.

## **Table of Contents**
- **Project Overview**
- **Features**
- **Installation**
- **Usage**
- **Git Tagging**
- **Contributing**
- **License**

## **Project Overview**
The Book Rental Management System is a CLI-based application that allows users to register, log in, add books, and rent books. The system also tracks revenue from rented books and displays book availability.

## **Features**
- **User Registration and Login**
- **Add books** with details such as author, pages, and rental rate
- **Rent out books** and track revenue
- **Display available and rented books**
- **Display registered users**

## **Installation**

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/gathuitapius/BookStore.git
    ```
2. **Navigate into the Project Directory**:
    ```bash
    cd book-rental-system
    ```

3. **Run the Program**:
    Execute the main script to start the application.
    ```bash
    python main.py
    ```

> **Note**: Ensure you have Python 3.x installed.

## **Usage**
1. **Start the Application**: Run `main.py` to access the menu.
2. **Authentication**:
   - Choose to **register** a new account or **log in**.
3. **Book Management**:
   - After logging in, you can **add books**, **rent books**, **view available books**, or **check rented books**.
4. **Revenue Tracking**:
   - Track **total revenue** earned from rented books.

## **Git Tagging**
For version control, use **git tagging** to create snapshots of the project at specific points.

1. **Create a Tag**:
    ```bash
    git tag -a v1.0 -m "Initial release of Book Rental Management System"
    ```

2. **Push Tags to GitHub**:
    ```bash
    git push origin --tags
    ```

3. **Listing Tags**:
    ```bash
    git tag
    ```

4. **Checkout a Tag**:
   If you need to switch to a tagged version:
    ```bash
    git checkout v1.0
    ```

> **Tagging Best Practices**: Use tags for significant milestones, such as major feature additions or bug fixes, using semantic versioning (`v1.0`, `v1.1`, `v2.0`, etc.).

## **Contributing**
We welcome contributions! Here’s how you can help:
1. **Fork the repository**.
2. **Create a branch** for your feature or bug fix:
   ```bash
   git checkout -b feature/new-feature
   ```
