from database import connect_db


class Doctor:
    def __init__(self, doctor_id, name, specialization, consultation_fee):
        self.doctor_id = doctor_id
        self.name = name
        self.specialization = specialization
        self.consultation_fee = consultation_fee

    def display(self):
        print(f"ID: {self.doctor_id}")
        print(f"Name: {self.name}")
        print(f"Specialization: {self.specialization}")
        print(f"Consultation Fee: Rs. {self.consultation_fee}")
        print("-" * 30)


class DoctorManager:
    def __init__(self):
        self.doctors = []
        self.load_doctors()

    def load_doctors(self):
        connection = connect_db()
        cursor = connection.cursor()

        cursor.execute("""
            SELECT doctor_id, name, specialization, consultation_fee
            FROM doctors
        """)

        rows = cursor.fetchall()
        connection.close()

        for row in rows:
            doctor = Doctor(
                row[0], 
                row[1], 
                row[2], 
                row[3]
            )
            self.doctors.append(doctor)

    def add_doctor(self):
        print("\n--- Add Doctor ---")

        doctor_id = input("Doctor ID: ").strip()

        if any(d.doctor_id == doctor_id for d in self.doctors):
            print("Doctor ID already exists.")
            return

        name = input("Name: ").strip()
        specialization = input("Specialization: ").strip()
        consultation_fee = input("Consultation Fee: ").strip()

        try:
            consultation_fee = float(consultation_fee)
            if consultation_fee < 0:
                raise ValueError
        except ValueError:
            print("Consultation fee must be a valid non-negative number.")
            return

        doctor = Doctor(
            doctor_id,
            name,
            specialization,
            float(consultation_fee)
        )

        self.doctors.append(doctor)

        connection = connect_db()
        cursor = connection.cursor()

        cursor.execute("""
            INSERT INTO doctors (
                doctor_id,
                name,
                specialization,
                consultation_fee
            )
            VALUES (?, ?, ?, ?)
        """, (
            doctor_id,
            name,
            specialization,
            float(consultation_fee)
        ))

        connection.commit()
        connection.close()

        print("Doctor added successfully.")

    def view_doctors(self):
        print("\n--- Doctor List ---")

        if not self.doctors:
            print("No doctors registered.")
            return

        for doctor in self.doctors:
            doctor.display()

    def search_doctor(self):
        doctor_id = input("Enter Doctor ID: ").strip()

        for doctor in self.doctors:
            if doctor.doctor_id == doctor_id:
                doctor.display()
                return

        print("Doctor not found.")

    def update_doctor(self):
        print("\n--- Update Doctor ---")

        doctor_id = input("Enter Doctor ID: ").strip()

        for doctor in self.doctors:
            if doctor.doctor_id == doctor_id:
                print("\nDoctor found.")
                print("Press Enter to keep the existing value.")

                name = input(f"Name [{doctor.name}]: ").strip()

                specialization = input(
                    f"Specialization [{doctor.specialization}]: "
                ).strip()

                consultation_fee = input(
                    f"Consultation Fee [{doctor.consultation_fee}]: "
                ).strip()

                if name:
                    doctor.name = name

                if specialization:
                    doctor.specialization = specialization

                if consultation_fee:
                    try:
                        new_consultation_fee = float(consultation_fee)

                        if new_consultation_fee < 0:
                            print("Consultation fee cannot be negative.")
                            return

                        doctor.consultation_fee = new_consultation_fee

                    except ValueError:
                        print("Consultation fee must be a number.")
                        return

                connection = connect_db()
                cursor = connection.cursor()

                cursor.execute("""
                    UPDATE doctors
                    SET name = ?, specialization = ?, consultation_fee = ?
                    WHERE doctor_id = ?
                """, (
                    doctor.name,
                    doctor.specialization,
                    doctor.consultation_fee,
                    doctor.doctor_id
                ))

                connection.commit()
                connection.close()

                print("Doctor updated successfully.")
                return

        print("Doctor not found.")

    def menu(self):
        while True:
            print("\n--- Doctor Management ---")
            print("1. Add Doctor")
            print("2. View Doctors")
            print("3. Search Doctor")
            print("4. Update Doctor")
            print("5. Back")

            choice = input("Enter your choice: ").strip()

            if choice == "1":
                self.add_doctor()
            elif choice == "2":
                self.view_doctors()
            elif choice == "3":
                self.search_doctor()
            elif choice == "4":
                self.update_doctor()
            elif choice == "5":
                break
            else:
                print("Invalid choice.")
