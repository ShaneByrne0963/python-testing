import unittest
from student import Student
from datetime import timedelta
from unittest.mock import patch


class TestStudent(unittest.TestCase):

    def setUp(self):
        self.student = Student('John', 'Doe')

    def test_full_name(self):
        self.assertEqual(self.student.full_name, 'John Doe')

    def test_alert_santa(self):
        self.student.alert_santa()

        self.assertTrue(self.student.naughty_list)

    def test_email_address(self):
        self.assertEqual(self.student.email_address, 'john.doe@email.com')

    def test_apply_extension(self):
        previous_end_date = self.student.end_date
        self.student.apply_extension(42)

        self.assertEqual(
            self.student.end_date, previous_end_date + timedelta(days=42)
        )

    def test_course_schedule_success(self):
        with patch('student.requests.get') as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = "Success"

            schedule = self.student.course_schedule()
            self.assertEqual(schedule, "Success")

    def test_course_schedule_failed(self):
        with patch('student.requests.get') as mocked_get:
            mocked_get.return_value.ok = False

            schedule = self.student.course_schedule()
            self.assertEqual(
                schedule, 'Something went wrong with the request!'
            )


if __name__ == "__main__":
    unittest.main()
