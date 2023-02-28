# TODO: Add the test cases that you'll be submitting to this file!
#       Make sure your test cases are all named starting with
#       test_ and that they have unique names.

# You may need to import pytest in order to run your tests.
# You are free to import hypothesis and use hypothesis for testing.
# This file will not be graded for style with PythonTA
from pytest import *
from course import Student, Course
from survey import Answer, Question


###############################################################################
# Task 2 Test cases
###############################################################################
def test_set_answer() -> None:
    """
    test that set_answer saves the answer correctly for a given question
    """
    ans = Answer('Good')
    ques = Question(0, 'How are you doing')
    student = Student(0, 'John')
    student.set_answer(ques, ans)
    assert student._answers[ques.id] == ans


def test_get_answer() -> None:
    """
    test that get_answer returns correct answer for a question
    """
    ans = Answer('Good')
    ques = Question(0, 'How are you doing')
    student = Student(0, 'John')
    student.set_answer(ques, ans)
    assert student.get_answer(ques) == ans


def test_has_answer() -> None:
    """
    test that has_answer returns true for the question for which
    it has a correct answer
    """
    ans = Answer('Good')
    ques = Question(0, 'How are you doing')
    student = Student(0, 'John')
    student.set_answer(ques, ans)
    assert student.has_answer(ques)


###############################################################################
# Task 3 Test cases
###############################################################################
def test_enroll_student_duplicate() -> None:
    """
    test that enroll_student does not enter two student with same ID
    """
    student1 = Student(0, "John")
    student2 = Student(0, "Jenny")
    student3 = Student(1, "Mike")
    course = Course('CSC148')
    course.enroll_students([student1, student2, student3])
    assert student2 not in course.students

###############################################################################
# Task 4 Test cases
###############################################################################
# TODO: Add your test cases below


###############################################################################
# Task 5 Test cases
###############################################################################
# TODO: Add your test cases below


###############################################################################
# Task 6 Test cases
###############################################################################
# TODO: Add your test cases below


###############################################################################
# Task 7 Test cases
###############################################################################
# TODO: Add your test cases below


###############################################################################
# Task 8 Test cases
###############################################################################
# TODO: Add your test cases below


###############################################################################
# Task 9 Test cases
###############################################################################
# TODO: Add your test cases below


###############################################################################
# Task 10 Test cases
###############################################################################
# TODO: Add your test cases below
