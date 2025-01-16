# Car Rental Management System

## Goal

The objective of this project is to develop a robust and user-friendly Car Rental Management System that allows for the management of vehicles and rental transactions. The system ensures efficient handling of rental operations.

## Abstract

The Car Rental Management System is a Python-based application designed for managing a car rental business. It allows users to add vehicles, rent vehicles, and return them while ensuring accurate data management. The application includes validation for data input and prevents unauthorized operations, such as renting unavailable vehicles.

## Features

### Vehicle Management:
- Add vehicles to the system with details such as ID, model, brand, and daily rate.
- Display available or all vehicles in the system.
- Update the status of vehicles when rented or returned.

### Rental Management:
- Rent vehicles to users, calculating the total cost based on rental duration.
- Prevent double renting of unavailable vehicles.
- Manage rental records and update the vehicle’s availability status.

### User-Friendly Interface:
- Menu-driven console interface for ease of use.

## Expected Outcome

### The system is expected to:
- Streamline the management of car rentals.
- Provide a reliable and user-friendly platform for handling operations.

### Benefits:
- Minimized errors in rental management.
- Enhanced data organization.
- Scalability for future features like reporting or a GUI interface.

## Roles

### Team Leader (Abdullah Zahoor):
- Handles overall project coordination and ensures completion of major functionalities.
- Focuses on core functionality implementation.

### Team Member (Hiba Fareed):
- Implements user interface and error handling.

Youtube Link
-https://www.youtube.com/watch?v=td4iao1lZ0M

## Installation and Usage

### 1. Prerequisites
- Python 3.6 or later.

### 2. Installation
- Clone the repository or download the project files:
  ```bash
  git clone https://github.com/AbdullahZahoor00/car_rental_ms.git
  ```

- Navigate to the project directory:
  ```bash
  cd CarRentalSystem
  ```

- Create and activate a virtual environment (optional but recommended):
  ```bash
  python -m venv venv
  source venv/bin/activate   # macOS/Linux
  venv\Scripts\activate      # Windows
  ```

- Run the application:
  ```bash
  python main.py
  ```

## Usage

### Add Vehicles:
- Enter vehicle details such as ID, model, brand, and daily rate.

### Rent Vehicles:
- Rent an available vehicle by specifying its ID.

### Return Vehicles:
- Return rented vehicles to make them available again.

### Menu Options:
#### 1. Add Vehicle:
- Add a new vehicle to the system.

#### 2. Show Available Vehicles:
- Display all available vehicles.

#### 3. Rent a Vehicle:
- Rent a vehicle by specifying its ID.

#### 4. Return a Vehicle:
- Return a vehicle by providing its ID.

#### 5. Exit:
- Exit the application.

## Schedule Summary

| Task                        | Deadline  | Assigned To      |
|-----------------------------|-----------|------------------|
| Vehicle Management Features | Week 1    | Hiba Fareed      |
| Rental Management Features  | Week 2    | Abdullah Zahoor  |
| Testing & Bug Fixing        | Week 3    | All Members      |

## Future Enhancements

- Develop a graphical user interface (GUI) using Tkinter or PyQt.
- Add reporting features for viewing rental history and activity.
- Extend the system to include payment processing and invoicing.
- Deploy the system as a web application using Flask or Django.

## Comment & Assessment

This project demonstrates a clear understanding of Python programming and rental service workflows. The system is designed for scalability, making it suitable for further enhancements and real-world deployment.
