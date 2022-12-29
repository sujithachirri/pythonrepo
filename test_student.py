import unittest
from student import Student

class test_student(unittest.TestCase):
    def test_email(self):
        obj = Student("sujitha", "chirri", 59)
        self.assertEqual(obj.email,'sujitha.chirri@gmail.com')
    def test_none1_thing(self):
        ok=Student("sujitha","chirri",59)
        ok.none1_thing('middle')
        self.assertEqual(ok.none,'sujithachirrimiddle')


if __name__ == "__main__":
    unittest.main()
