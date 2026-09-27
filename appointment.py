from patient import PatientManager
from doctor import DoctorManager
from database import connect_db


class Appointment:
    def __init__(self, appointment_id, patient_id, doctor_id, date, time, reason):
        self.appointment_id = appointment_id
        self.patient_id = patient_id
        self.doctor_id = doctor_id
        self.date = date
        self.time = time
        self.reason = reason


class AppointmentManager:
    def __init__(self, patient_manager, doctor_manager):
        self.appointments = []
        self.patient_manager = patient_manager
        self.doctor_manager = doctor_manager
        self.load_appointments()

    def load_appointments(self):
        connection = connect_db()
        cursor = connection.cursor()

        cursor.execute("""
            SELECT appointment_id, patient_id, doctor_id, date, time, reason
            FROM appointments
        """)

        rows = cursor.fetchall()
        connection.close()

        for row in rows:
            appointment = Appointment(
                row[0],
                row[1],
                row[2],
                row[3],
                row[4],
                row[5]
            )

            self.appointments.append(appointment)

    def book_appointment(self):
        print("\n--- Book Appointment ---")

        appointment_id = input("Enter Appointment ID: ")

        for appointment in self.appointments:
            if appointment.appointment_id == appointment_id:
                print("Appointment ID already exists.")
                return

        patient_id = input("Enter Patient ID: ")
        doctor_id = input("Enter Doctor ID: ")
        
        patient_found = False

        for patient in self.patient_manager.patients:
            if patient.patient_id == patient_id:
              patient_found = True
              break

        if not patient_found:
           print("Patient ID not found.")
           return

        doctor_found = False

        for doctor in self.doctor_manager.doctors:
            if doctor.doctor_id == doctor_id:
               doctor_found = True
               break

        if not doctor_found:
           print("Doctor ID not found.")
           return

        date = input("Enter Date (DD-MM-YYYY): ")
        time = input("Enter Time (e.g., 9:00 AM): ")
        reason = input("Enter Reason for Visit: ")

        for appointment in self.appointments:
            if (appointment.doctor_id == doctor_id and
                    appointment.date == date and
                    appointment.time == time):
                print("Doctor is already booked at this date and time.")
                return

        appointment = Appointment(
            appointment_id,
            patient_id,
            doctor_id,
            date,
            time,
            reason
        )

        self.appointments.append(appointment)

        connection = connect_db()
        cursor = connection.cursor()

        cursor.execute("""
            INSERT INTO appointments (
                appointment_id,
                patient_id,
                doctor_id,
                date,
                time,
                reason
            )
            VALUES (?, ?, ?, ?, ?, ?)
        """, (
            appointment_id,
            patient_id,
            doctor_id,
            date,
            time,
            reason
        ))

        connection.commit()
        connection.close()


        print("Appointment booked successfully.")

    def view_appointments(self):
        print("\n--- All Appointments ---")

        if not self.appointments:
            print("No appointments found.")
            return

        for appointment in self.appointments:
            print("\nAppointment ID:", appointment.appointment_id)
            print("Patient ID:", appointment.patient_id)
            print("Doctor ID:", appointment.doctor_id)
            print("Date:", appointment.date)
            print("Time:", appointment.time)
            print("Reason:", appointment.reason)

    def search_appointment(self):
        print("\n--- Search Appointment ---")

        appointment_id = input("Enter Appointment ID: ")

        for appointment in self.appointments:
            if appointment.appointment_id == appointment_id:
                print("\nAppointment found!")
                print("Appointment ID:", appointment.appointment_id)
                print("Patient ID:", appointment.patient_id)
                print("Doctor ID:", appointment.doctor_id)
                print("Date:", appointment.date)
                print("Time:", appointment.time)
                print("Reason:", appointment.reason)
                return

        print("Appointment not found.")

    def cancel_appointment(self):
        print("\n--- Cancel Appointment ---")

        appointment_id = input("Enter Appointment ID: ").strip()

        for appointment in self.appointments:
            if appointment.appointment_id == appointment_id:

                connection = connect_db()
                cursor = connection.cursor()

                cursor.execute("""
                    DELETE FROM appointments
                    WHERE appointment_id = ?
                """, (appointment_id,))

                connection.commit()
                connection.close()

                self.appointments.remove(appointment)

                print("Appointment cancelled successfully.")
                return

        print("Appointment not found.")

    def menu(self):
        while True:
            print("\n--- Appointment Management ---")
            print("1. Book Appointment")
            print("2. View Appointments")
            print("3. Search Appointments")
            print("4. Cancel Appointment")
            print("5. Back")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.book_appointment()
            elif choice == "2":
                self.view_appointments()
            elif choice == "3":
                self.search_appointment()
            elif choice == "4":
                self.cancel_appointment()
            elif choice == "5":
                break
            else:
                print("Invalid choice. Please try again.")
