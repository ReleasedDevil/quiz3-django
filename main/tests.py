from django.test import TestCase
from .models import Student


class StudentModelTest(TestCase):
    def test_student_course_field(self):
        student = Student.objects.create(
            name='Alice',
            age=20,
            student_id='S-1001',
            course='BSIT',
        )

        self.assertEqual(student.course, 'BSIT')
