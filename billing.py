from database import connect_db

class Bill:
    def __init__(
        self,
        bill_id,
        patient_id,
        appointment_id,
        consultation_fee,
        additional_charges
    ):
        self.bill_id = bill_id
        self.patient_id = patient_id
        self.appointment_id = appointment_id
        self.consultation_fee = consultation_fee
        self.additional_charges = additional_charges

        self.total_amount = (
            consultation_fee + additional_charges
        )


class BillingManager:
    def __init__(self, patient_manager, appointment_manager):
        self.bills = []
        self.patient_manager = patient_manager
        self.appointment_manager = appointment_manager
        self.load_bills()

    def load_bills(self):
        connection = connect_db()
        cursor = connection.cursor()

        cursor.execute("""
            SELECT bill_id, patient_id, appointment_id, 
                   consultation_fee, additional_charges,
                     total_amount
            FROM bills
        """)

        rows = cursor.fetchall()
        connection.close()

        for row in rows:
            bill = Bill(
                row[0],
                row[1],
                row[2],
                row[3],
                row[4]
            )

            self.bills.append(bill)

    def create_bill(self):
        print("\n--- Create Bill ---")

        bill_id = input("Enter Bill ID: ").strip()

        for bill in self.bills:
            if bill.bill_id == bill_id:
                print("Bill ID already exists.")
                return

        patient_id = input("Enter Patient ID: ").strip()
        appointment_id = input("Enter Appointment ID: ").strip()

        appointment_found = False

        for appointment in self.appointment_manager.appointments:
            if (
                appointment.appointment_id == appointment_id
                and appointment.patient_id == patient_id
            ):
                appointment_found = True
                break

        if not appointment_found:
            print("Appointment not found for this patient.")
            return

        additional_charges = input(
            "Enter Additional Charges: "
        ).strip()

        try:
            additional_charges = float(additional_charges)

            if additional_charges < 0:
                print("Additional charges cannot be negative.")
                return

        except ValueError:
            print("Additional charges must be a number.")
            return

        doctor_id = appointment.doctor_id

        doctor = None

        for item in self.appointment_manager.doctor_manager.doctors:
            if item.doctor_id == doctor_id:
                doctor = item
                break

        if doctor is None:
            print("Doctor not found.")
            return

        consultation_fee = doctor.consultation_fee

        bill = Bill(
            bill_id,
            patient_id,
            appointment_id,
            consultation_fee,
            additional_charges
        )

        self.bills.append(bill)

        connection = connect_db()
        cursor = connection.cursor()

        cursor.execute("""
            INSERT INTO bills (
                bill_id,
                patient_id,
                appointment_id,
                consultation_fee,
                additional_charges,
                total_amount
            )
            VALUES (?, ?, ?, ?, ?, ?)
        """, (
            bill.bill_id,
            bill.patient_id,
            bill.appointment_id,
            bill.consultation_fee,
            bill.additional_charges,
            bill.total_amount
        ))

        connection.commit()
        connection.close()

        print("\nBill created successfully.")
        print("Consultation Fee:", consultation_fee)
        print("Additional Charges:", additional_charges)
        print("Total Amount:", bill.total_amount)

    def view_bills(self):
        print("\n--- All Bills ---")

        if not self.bills:
            print("No bills found.")
            return

        for bill in self.bills:
            print("\nBill ID:", bill.bill_id)
            print("Patient ID:", bill.patient_id)
            print("Appointment ID:", bill.appointment_id)
            print("Consultation Fee:", bill.consultation_fee)
            print("Additional Charges:", bill.additional_charges)
            print("Total Amount:", bill.total_amount)
            print("-" * 30)

    def menu(self):
        while True:
            print("\n--- Billing Management ---")
            print("1. Create Bill")
            print("2. View Bills")
            print("3. Back")

            choice = input("Enter your choice: ").strip()

            if choice == "1":
                self.create_bill()
            elif choice == "2":
                self.view_bills()
            elif choice == "3":
                break
            else:
                print("Invalid choice. Please try again.")