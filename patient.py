from database import connect_db
from validation import is_valid_phone, is_valid_age

class Patient:
    def __init__(self, patient_id, name, age, gender, phone):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.gender = gender
        self.phone = phone

    def display(self):
        print(f"ID: {self.patient_id}")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender}")
        print(f"Phone: {self.phone}")
        print("-" * 30)


class PatientManager:
    def __init__(self):
        self.patients = []
        self.load_patients()

    def load_patients(self):
        connection = connect_db()
        cursor = connection.cursor()

        cursor.execute("""
            SELECT patient_id, name, age, gender, phone
            FROM patients
        """)

        rows = cursor.fetchall()
        connection.close()

        for row in rows:
            patient = Patient(
                 row[0],
                 row[1],
                 row[2],
                 row[3],
                 row[4]
            )
            self.patients.append(patient)

    def add_patient(self):
        print("\n--- Register Patient ---")

        patient_id = input("Patient ID: ").strip()

        if any(p.patient_id == patient_id for p in self.patients):
            print("Patient ID already exists.")
            return

        name = input("Name: ").strip()
        age = input("Age: ").strip()
        gender = input("Gender: ").strip()
        phone = input("Phone: ").strip()

        if not is_valid_age(age):
            print("Invalid age. Please enter an age between 1 and 120.")
            return

        if not is_valid_phone(phone):
            print("Invalid phone number. Please enter a 10-digit phone number.")
            return

        patient = Patient(patient_id, name, int(age), gender, phone)
        self.patients.append(patient)

        connection = connect_db()
        cursor = connection.cursor()

        cursor.execute("""
            INSERT INTO patients (patient_id, name, age, gender, phone)
            VALUES (?, ?, ?, ?, ?)
        """, (patient_id, name, int(age), gender, phone))

        connection.commit()
        connection.close()

        print("Patient registered successfully.")

    def view_patients(self):
        print("\n--- Patient List ---")

        if not self.patients:
            print("No patients registered.")
            return

        for patient in self.patients:
            patient.display()

    def search_patient(self):
        patient_id = input("Enter Patient ID: ").strip()

        for patient in self.patients:
            if patient.patient_id == patient_id:
                patient.display()
                return

        print("Patient not found.")

    def update_patient(self):
        print("\n--- Update Patient ---")

        patient_id = input("Enter Patient ID: ").strip()

        for patient in self.patients:
            if patient.patient_id == patient_id:
                print("\nPatient found.")
                print("Press Enter to keep the existing value.")

                name = input(f"Name [{patient.name}]: ").strip()
                age = input(f"Age [{patient.age}]: ").strip()
                gender = input(f"Gender [{patient.gender}]: ").strip()
                phone = input(f"Phone [{patient.phone}]: ").strip()

                if name:
                    patient.name = name

                if age:
                    if not is_valid_age(age):
                       print("Invalid age. Please enter an age between 1 and 120.")
                       return
                    patient.age = int(age)

                if gender:
                    patient.gender = gender

                if phone:
                    if not is_valid_phone(phone):
                        print("Invalid phone number. Please enter a 10-digit phone number.")
                        return
                    patient.phone = phone

                connection = connect_db()
                cursor = connection.cursor()

                cursor.execute("""
                    UPDATE patients
                    SET name = ?, age = ?, gender = ?, phone = ?
                    WHERE patient_id = ?
                """, (
                    patient.name,
                    patient.age,
                    patient.gender,
                    patient.phone,
                    patient.patient_id
                ))

                connection.commit()
                connection.close()

                print("Patient updated successfully.")
                return

        print("Patient not found.")

    def menu(self):
        while True:
            print("\n--- Patient Management ---")
            print("1. Register Patient")
            print("2. View Patients")
            print("3. Search Patient")
            print("4. Update Patient")
            print("5. Back")

            choice = input("Enter your choice: ").strip()

            if choice == "1":
                self.add_patient()
            elif choice == "2":
                self.view_patients()
            elif choice == "3":
                self.search_patient()
            elif choice == "4":
                self.update_patient()
            elif choice == "5":
                break
            else:
                print("Invalid choice.")
