from patient import PatientManager
from doctor import DoctorManager
from appointment import AppointmentManager
from billing import BillingManager
from database import create_tables

def main():
    create_tables()

    
    patient_manager = PatientManager()
    doctor_manager = DoctorManager()
    appointment_manager = AppointmentManager(
      patient_manager,
      doctor_manager
    )
    billing_manager = BillingManager(
      patient_manager,
      appointment_manager
    )

    while True:
        print("\n" + "=" * 50)
        print("       MEDICARE HOSPITAL MANAGEMENT SYSTEM")
        print("=" * 50)
        print("1. Patient Management")
        print("2. Doctor Management")
        print("3. Appointment Management")
        print("4. Billing Management")
        print("5. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            patient_manager.menu()
        elif choice == "2":
            doctor_manager.menu()
        elif choice == "3":
            appointment_manager.menu()
        elif choice == "4":
            billing_manager.menu()
        elif choice == "5":
            print("Thank you for using MediCare.")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()
