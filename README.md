# MediCare Hospital Management System

## Project Overview

MediCare Hospital Management System is a command-line application developed in Python to handle some of the basic operations of a hospital.

The project uses **Object-Oriented Programming (OOP)** and **SQLite** to store and manage data. The aim is to keep the system simple, modular, and easy to use while also demonstrating concepts such as validation, database connectivity, error handling, and unit testing.

The system currently includes four main modules:

- Patient Management
- Doctor Management
- Appointment Management
- Billing Management

The project focuses on simplicity, validation, error handling, database persistence, and modular design.

---

## Features

### 1. Patient Management

The Patient Management module allows users to:

- Register new patients
- View all registered patients
- Search for a patient
- Update patient information
- Validate patient age and phone number
- Store patient details in the SQLite database

### 2. Doctor Management

The Doctor Management module allows users to:

- Add doctors
- View all registered doctors
- Search for a doctor
- Update doctor information
- Validate consultation fees
- Store doctor details in the SQLite database

### 3. Appointment Management

The Appointment Management module allows users to:

- Book appointments
- View appointments
- Search appointments
- Cancel appointments
- Check whether the selected patient and doctor exist
- Prevent duplicate appointment IDs
- Prevent double booking of a doctor at the same date and time
- Store appointment details in the SQLite database

### 4. Billing Management

The Billing Management module allows users to:

- Create bills for appointments
- Automatically retrieve the doctor's consultation fee
- Add additional charges
- Calculate the total bill amount
- View generated bills
- Store billing information in the SQLite database

---

## Technologies Used

- **Python 3**
- **Object-Oriented Programming (OOP)**
- **SQLite**
- **sqlite3**
- **unittest**

The main application uses only Python's standard library, so no external packages are required.

---

## Project Structure

```text
MediCare_Hospital_Management/
│
├── main.py
├── patient.py
├── doctor.py
├── appointment.py
├── billing.py
├── database.py
├── validation.py
├── requirements.txt
├── statement.md
│
├── tests/
│   └── test_basic.py
│
├── Diagrams/
```

---

## Database

The application uses **SQLite** for persistent data storage.

The following tables are created automatically when the application starts:

- `patients`
- `doctors`
- `appointments`
- `bills`

The database file is:

```text
medicare.db
```

It is created automatically by the application, so there is no need to create the database manually.

---

## How to Run

### 1. Install Python

Make sure Python 3 is installed on your computer.

On Windows, you can check the installation using:

```bash
py --version
```

### 2. Open the Project Folder

Open a terminal in the project directory:

```bash
cd MediCare_Hospital_Management
```

### 3. Run the Application

Run the following command:

```bash
py main.py
```

The main menu will appear:

```text
==================================================
       MEDICARE HOSPITAL MANAGEMENT SYSTEM
==================================================
1. Patient Management
2. Doctor Management
3. Appointment Management
4. Billing Management
5. Exit
```

Enter the number corresponding to the operation you want to perform.

---

## Testing

The project includes automated unit tests using Python's built-in `unittest` framework.

To run the tests, use:

```bash
py -m unittest discover -s tests -p "test_*.py"
```

The tests currently cover:

- Patient object creation
- Doctor object creation
- Valid phone numbers
- Invalid phone numbers
- Valid ages
- Invalid ages

---

## Validation and Error Handling

The application includes validation and error handling to prevent incorrect input and unexpected program failures.

Examples include:

- Age validation
- Phone number validation
- Consultation fee validation
- Prevention of duplicate patient IDs
- Prevention of duplicate doctor IDs
- Prevention of duplicate appointment IDs
- Prevention of duplicate bill IDs
- Validation of patient and doctor IDs during appointment booking
- Prevention of doctor double booking
- Validation of additional billing charges

These checks help maintain consistent data and make the application easier to use.

---

## Object-Oriented Design

The project follows Object-Oriented Programming principles.

The main classes used in the application are:

- `Patient`
- `PatientManager`
- `Doctor`
- `DoctorManager`
- `Appointment`
- `AppointmentManager`
- `Bill`
- `BillingManager`

The entity classes represent individual objects, while the manager classes handle operations related to their respective modules.

---

## User Interface

The application uses a **Command-Line Interface (CLI)**.

Separate menus are provided for:

- Patient Management
- Doctor Management
- Appointment Management
- Billing Management

The interface is kept simple so that users can navigate the system using numbered menu options.

---

## Project Documentation

Additional project information and requirements are documented in:

```text
statement.md
```

The project design diagrams are maintained in the `Diagrams/` folder.

The folder contains:

- `MediCare ER Diagram.png` – database/ER design
- `Medicare UML Diagram.png` – Python OOP/class design
- `Data Flow Diagram.png` – system architecture and data flow
- `Use flow Diagram.png` – system users and their interactions
- `Book appointment.png` – appointment booking workflow


---

## Future Scope

The current project intentionally focuses on the core hospital management functions.

Some possible future enhancements are:

- Medical records
- Laboratory management
- Admission and bed management
- Prescription management
- Advanced reports
- User authentication
- Role-based access
- Graphical User Interface (GUI)

These features are outside the scope of the current version of the project.

---

## Author

Developed as a Python Programming project.