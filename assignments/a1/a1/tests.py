# You may need to import pytest in order to run your tests.
# You are free to import hypothesis and use hypothesis for testing.
# This file will not be graded for style with PythonTA
from pytest import *
from course import *
from survey import *
from criterion import *


###############################################################################
# Task 2 Test cases
###############################################################################
class TestStudentCLass:
    def test_set_answer(self) -> None:
        """
        test that set_answer saves the answer correctly for a given question
        """
        ans = Answer(20)
        ques = NumericQuestion(0, 'How old are you', 0, 100)
        student = Student(0, 'John')
        student.set_answer(ques, ans)
        assert student._answers[ques.id] == ans

    def test_get_answer(self) -> None:
        """
        test that get_answer returns correct answer for a question
        """
        ans = Answer(20)
        ques = NumericQuestion(0, 'How old are you', 0, 100)
        student = Student(0, 'John')
        student.set_answer(ques, ans)
        assert student.get_answer(ques) == ans

    def test_has_answer(self) -> None:
        """
        test that has_answer returns true for the question for which
        it has a correct answer
        """
        ans = Answer(20)
        ques = NumericQuestion(0, 'How old are you', 0, 100)
        student = Student(0, 'John')
        student.set_answer(ques, ans)
        assert student.has_answer(ques)


###############################################################################
# Task 3 Test cases
###############################################################################
class TestCourseClass:
    def test_enroll_student_duplicate(self) -> None:
        """
        test that enroll_student does not enter two student with same ID
        """
        student1 = Student(0, "John")
        student2 = Student(0, "Jenny")
        student3 = Student(1, "Mike")
        course = Course('CSC148')
        course.enroll_students([student1, student2, student3])
        assert student2 not in course.students

    def test_all_answered(self) -> None:
        """
        Test that all_answered returns true when a student
        has all the answers for a survey
        """
        # TODO: implement this later

    def test_get_students(self) -> None:
        """
        Test that get_students returns the correctly sorted tuple of students
        """
        student1 = Student(0, "John")
        student2 = Student(2, "Jenny")
        student3 = Student(1, "Mike")
        course = Course('CSC148')
        course.enroll_students([student1, student2, student3])
        assert course.get_students() == (student1, student3, student2)


###############################################################################
# Task 4 Test cases
###############################################################################
class TestQuestionClass:

    def test_validate_answer(self) -> None:
        """
        Test that the validate_answer returns true for a valid answer to the
        YesNoQuestion
        """
        ans = Answer(True)
        ques = YesNoQuestion(0, 'Earth is round')
        assert ques.validate_answer(ans)

    def test_get_similarity_1(self) -> None:
        """
        Test that the get_similarity returns 1 for two answers with same content
        """
        ans1 = Answer(True)
        ans2 = Answer(True)
        ques = YesNoQuestion(0, 'Earth is round')
        assert ques.get_similarity(ans1, ans2) == 1.0

    def test_get_similarity_0(self) -> None:
        """
        Test that get_similarity returns 0 for answers with different content
        """
        ans1 = Answer(True)
        ans2 = Answer(False)
        ques = YesNoQuestion(0, 'Earth is round')
        assert ques.get_similarity(ans1, ans2) == 0.0

    def test_checkbox_similarity(self) -> None:
        a = Answer('abc')
        b = Answer('cbd')
        ques = CheckboxQuestion(0, 'How cold is it',
                                ['Very', 'Not at all', 'It\'s okay'])
        assert ques.get_similarity(a, b) == 0.5

    def test_get_similarity_multiple_choice(self) -> None:
        a = Answer('abc')
        b = Answer('abc')
        ques = MultipleChoiceQuestion(0,    'How cold is it',
                                      ['Very', 'Not at all', 'It\'s okay'])
        assert (ques.get_similarity(a, b)) == 1.0


###############################################################################
# Task 5 Test cases
###############################################################################
class TestAnswerClass:

    def test_is_valid_multiple_choice(self) -> None:
        """
        Test that is_valid returns true for a valid answer to a
        MultipleChoiceQuestion
        """
        ques = MultipleChoiceQuestion(0, 'How are you?',
                                      ['Good', 'Great', 'Okay'])
        ans = Answer('Great')
        assert ans.is_valid(ques)

    def test_is_valid_checkbox(self) -> None:
        """
        Test that is_valid returns true for a valid answer to a checkbox
        question
        """
        ques = CheckboxQuestion(0, 'What is earth?',
                                ['Planet', 'Flat', 'Round', 'Star'])
        ans = Answer(['Planet', 'Round'])
        assert ans.is_valid(ques)


###############################################################################
# Task 6 Test cases
###############################################################################
class TestCriterionClass:
    def test_single_answer(self) -> None:
        """
        Test that the score_answer returns 1.0 for only one valid answer in
        homogeneous criterion
        """
        a = Answer('Very')
        ques = MultipleChoiceQuestion(0, 'How cold is it',
                                      ['Very', 'Not at all', 'It\'s okay'])
        criterion = HomogeneousCriterion()
        assert criterion.score_answers(ques, [a]) == 1.0

    def test_single_answer_heterogeneous(self) -> None:
        """
        Test that the score_answer returns 0.0 for only one valid answer
        in heterogeneous criterion
        """
        a = Answer('Very')
        ques = MultipleChoiceQuestion(0, 'How cold is it',
                                      ['Very', 'Not at all', 'It\'s okay'])
        criterion = HeterogeneousCriterion()
        assert criterion.score_answers(ques, [a]) == 0.0

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
