import unittest
from student import Student


class TestStudent(unittest.TestCase):
    def test_email(self):
        ex_student = Student('Jon', 'Snow', 4.5, None)
        self.assertEqual(ex_student.email, 'jon.snow@university.com')

        ex_student.last = 'Targaryen'
        self.assertEqual(ex_student.email, 'jon.targaryen@university.com')

    def test_fullname(self):
        ex_student = Student('Jon', 'Snow', 4.5, None)
        self.assertEqual(ex_student.fullname, 'Jon Snow')

        ex_student.last = 'Targaryen'
        self.assertEqual(ex_student.fullname, 'Jon Targaryen')

    def test_grand_scholarship_success(self):
        ex_student = Student('Jon', 'Snow', 5, None)

        ex_student.grant_scholarship()
        self.assertEqual(ex_student.scholarship, True)

    def test_scholarship_unsuccess(self):
        ex_student = Student('Jon', 'Snow', 4, None)

        ex_student.grant_scholarship()
        self.assertEqual(ex_student.scholarship, False)


if __name__ == '__main__':
    unittest.main()
