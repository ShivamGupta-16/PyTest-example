import pytest
from unittest.mock import patch

# Import the classes from your module (assuming it's named 'source.school')
from source.school import Classroom, TooManyStudents, Teacher, Student

@pytest.fixture
def hogwarts_classroom():
    """Fixture to create a sample classroom with Harry Potter theme."""
    teacher = Teacher("Professor McGonagall")
    students = [Student("Harry"), Student("Hermione"), Student("Ron")]
    return Classroom(teacher, students, "Transfiguration")

@pytest.mark.parametrize("new_student", [
    "Neville",
    "Luna",
    "Draco"
])
def test_add_student(hogwarts_classroom, new_student):
    """Test adding a student to the classroom."""
    student_obj = Student(new_student)
    hogwarts_classroom.add_student(student_obj)
    assert any(student.name == new_student for student in hogwarts_classroom.students)

@pytest.mark.parametrize("new_teacher", [
    "Professor Snape",
    "Professor Dumbledore"
])
def test_change_teacher(hogwarts_classroom, new_teacher):
    """Test changing the teacher of the classroom."""
    teacher_obj = Teacher(new_teacher)
    hogwarts_classroom.change_teacher(teacher_obj)
    assert hogwarts_classroom.teacher.name == new_teacher

def test_add_student_limit(hogwarts_classroom):
    """Test that adding too many students raises an exception."""
    for i in range(8):  # Add more students to reach the limit
        hogwarts_classroom.add_student(Student(f"Student {i}"))
    with pytest.raises(TooManyStudents):
        hogwarts_classroom.add_student(Student("Seamus"))

@pytest.mark.parametrize("student_name", ["Harry", "Hermione", "Ron"])
def test_remove_student(hogwarts_classroom, student_name):
    """Test removing a student from the classroom."""
    hogwarts_classroom.remove_student(student_name)
    assert not any(student.name == student_name for student in hogwarts_classroom.students)

@pytest.mark.xfail(reason="Bug in remove_student: possible iteration issue.")
def test_remove_non_existent_student(hogwarts_classroom):
    """Test removing a student who is not in the classroom."""
    initial_count = len(hogwarts_classroom.students)
    hogwarts_classroom.remove_student("Voldemort")
    assert len(hogwarts_classroom.students) == initial_count
