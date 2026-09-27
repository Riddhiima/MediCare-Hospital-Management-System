import unittest
from patient import Patient
from doctor import Doctor
from validation import is_valid_phone, is_valid_age


class TestPatient(unittest.TestCase):
    def test_patient_creation(self):
        patient = Patient("P001", "Rahul Sharma", 25, "Male", "9876543210")

        self.assertEqual(patient.patient_id, "P001")
        self.assertEqual(patient.name, "Rahul Sharma")
        self.assertEqual(patient.age, 25)


class TestDoctor(unittest.TestCase):
    def test_doctor_creation(self):
        doctor = Doctor("D001", "Dr. Priya Sharma", "Cardiology", 1000)

        self.assertEqual(doctor.doctor_id, "D001")
        self.assertEqual(doctor.specialization, "Cardiology")
        self.assertEqual(doctor.consultation_fee, 1000)

class TestValidation(unittest.TestCase):

    def test_valid_phone(self):
        self.assertTrue(is_valid_phone("9876543210"))

    def test_invalid_phone(self):
        self.assertFalse(is_valid_phone("12345"))

    def test_valid_age(self):
        self.assertTrue(is_valid_age("25"))

    def test_invalid_age(self):
        self.assertFalse(is_valid_age("150"))

if __name__ == "__main__":
    unittest.main()
