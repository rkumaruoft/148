# You may need to import pytest in order to run your tests.
# You are free to import hypothesis and use hypothesis for testing.
# This file will not be graded for style with PythonTA
from course import *
from survey import *
from criterion import *
from grouper import Group, Grouping, Grouper, AlphaGrouper, GreedyGrouper


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

    def test_has_answer_no_answer(self) -> None:
        student = Student(0, 'Helen')
        question = MultipleChoiceQuestion(0, 'how?', ['A', 'B', 'C'])
        assert not student.has_answer(question)

    def test_set_answer_first_set(self) -> None:
        student = Student(0, 'Helen')
        question = MultipleChoiceQuestion(0, 'how?', ['A', 'B', 'C'])
        answer = Answer('A')
        student.set_answer(question, answer)
        assert student.get_answer(question) == answer

    def test_set_answer_reset(self) -> None:
        student = Student(0, 'Helen')
        question = MultipleChoiceQuestion(0, 'how?', ['A', 'B', 'C'])
        answer1 = Answer('A')
        answer2 = Answer('B')
        student.set_answer(question, answer1)
        assert student.get_answer(question) == answer1
        student.set_answer(question, answer2)
        assert student.get_answer(question) == answer2


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
        assert len(course.students) == 0

    def test_all_answered(self) -> None:
        """
        Test that all_answered returns true when a student
        has all the answers for a survey
        """
        cs = Course('CSC148')
        q1 = MultipleChoiceQuestion(1, 'why?', ['a', 'b'])
        q2 = NumericQuestion(2, 'what?', -2, 4)
        q1_answer = Answer('a')
        q2_answer = Answer(1)
        questions = [q1, q2]
        happy_survey = Survey(questions)
        helen = Student(0, 'Helen')
        tammy = Student(0, 'Tammy')
        students = [helen, tammy]
        cs.enroll_students(students)
        helen.set_answer(q1, q1_answer)
        tammy.set_answer(q1, q1_answer)
        helen.set_answer(q2, q2_answer)
        tammy.set_answer(q2, q2_answer)
        assert cs.all_answered(happy_survey)

    def test_all_answered_invalid_answer(self) -> None:
        cs = Course('CSC148')
        q1 = MultipleChoiceQuestion(1, 'why?', ['a', 'b'])
        q2 = NumericQuestion(2, 'what?', -2, 4)
        q1_answer = Answer('a')
        q2_answer = Answer(1)
        questions = [q1, q2]
        happy_survey = Survey(questions)
        helen = Student(0, 'Helen')
        tammy = Student(1, 'Tammy')
        students = [helen, tammy]
        cs.enroll_students(students)
        helen.set_answer(q1, q1_answer)
        tammy.set_answer(q1, q1_answer)
        helen.set_answer(q2, q2_answer)
        tammy.set_answer(q2, q1_answer)  # invalid
        assert not cs.all_answered(happy_survey)

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

    def test_validate_answer_invalid(self) -> None:
        question = YesNoQuestion(0, 'happy?')
        answer = Answer(1)
        assert not question.validate_answer(answer)

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
        ques = MultipleChoiceQuestion(0, 'How cold is it',
                                      ['Very', 'Not at all', 'It\'s okay'])
        assert (ques.get_similarity(a, b)) == 1.0


class TestNumericQuestion:
    def test_get_similarity(self) -> None:
        question = NumericQuestion(0, 'how happy?', 0, 4)
        answer = Answer(2)
        answer1 = Answer(4)
        assert question.get_similarity(answer, answer1) == 0.5



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

    def test_is_valid_invalid(self) -> None:
        question = CheckboxQuestion(0, 'happy?', ['a', 'b'])
        answer = Answer(1)
        assert not answer.is_valid(question)


###############################################################################
# Task 6 Test cases
###############################################################################
class TestCriterionClass:
    def test_single_answer_homogenous(self) -> None:
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

    def test_score_answers_all_same(self) -> None:
        q1 = NumericQuestion(0, 'how much?', 0, 10)
        answer1 = Answer(0)
        answer2 = Answer(0)
        answer3 = Answer(0)
        answers = [answer1, answer2, answer3]
        criteria = HomogeneousCriterion()
        assert criteria.score_answers(q1, answers) == 1.0

    def test_score_answers(self) -> None:
        q1 = NumericQuestion(0, 'how much?', 0, 10)
        answer1 = Answer(0)
        answer2 = Answer(5)
        answer3 = Answer(0)
        answers = [answer1, answer2, answer3]
        criteria = HomogeneousCriterion()
        assert criteria.score_answers(q1, answers) == 0.6666666666666666


###############################################################################
# Task 7 Test cases
###############################################################################
class TestGroupClass:
    def test_group_len(self):
        """
        Test that __len__ returns the correct length of the members
        list in  the group
        """
        members = [Student(0, 'John'), Student(1, 'Jen'), Student(2, 'Janet')]
        group = Group(members)
        assert len(group) == len(members)

    def test_group_contains(self):
        """
        Test that __contains__ returns True when a student is
        present in the group
        """
        members = [Student(0, 'John'), Student(1, 'Jen')]
        janet = Student(2, 'Janet')
        members.append(janet)
        group = Group(members)
        assert janet in group

    def test_group_not_contains(self):
        """
        Test that __contains__ returns False when a student is not
        present in the group
        """
        members = [Student(0, 'John'), Student(1, 'Jen')]
        janet = Student(2, 'Janet')
        group = Group(members)
        assert janet not in group

    def test_group_get_members(self):
        """
        Test that get_members return a shallow copy of the original list
        """
        members = [Student(0, 'John'), Student(1, 'Jen')]
        group = Group(members)
        ret_members = group.get_members()
        janet = Student(2, 'Janet')
        ret_members.append(janet)
        assert janet not in group.get_members()


###############################################################################
# Task 8 Test cases
###############################################################################
class TestGroupingClass:
    def test_add_group_true(self):
        """
        Test that the add_group method adds a valid group to the grouping class
        """
        grouper = Grouping()
        group1 = Group([Student(0, 'John'),
                        Student(1, 'Jen'),
                        Student(2, 'Janet')])
        group2 = Group([Student(3, 'Mike'),
                        Student(4, 'Michael'),
                        Student(5, 'Mason')])
        grouper.add_group(group1)
        grouper.add_group(group2)
        ret_groups = grouper.get_groups()
        assert group1 in ret_groups and group2 in ret_groups

    def test_add_group_false(self):
        """
        Test that add_group does not add a group which has the same member
        already present in another group in the grouping
        """
        grouping = Grouping()
        steve = Student(6, 'Steve')
        group1 = Group([Student(0, 'John'),
                        Student(1, 'Jen'),
                        Student(2, 'Janet'), steve])
        group2 = Group([Student(3, 'Mike'),
                        Student(4, 'Michael'),
                        Student(5, 'Mason'), steve])
        grouping.add_group(group1)
        grouping.add_group(group2)
        ret_groups = grouping.get_groups()
        assert group1 in ret_groups and group2 not in ret_groups


###############################################################################
# Task 9 Test cases
###############################################################################
class TestSurvey:
    def test_get_question(self) -> None:
        q1 = YesNoQuestion(0, 'how?')
        q2 = YesNoQuestion(1, 'what?')
        q3 = YesNoQuestion(2, 'when?')
        s = Survey([q1, q2, q3])
        assert s.get_questions() == [q1, q2, q3]

    def test_get_criterion(self) -> None:
        q1 = YesNoQuestion(0, 'how?')
        q2 = YesNoQuestion(1, 'what?')
        q3 = YesNoQuestion(2, 'when?')
        s = Survey([q1, q2, q3])
        assert isinstance(s._get_criterion(q1), HomogeneousCriterion)
        s.set_criterion(HeterogeneousCriterion(), q1)
        assert isinstance(s._get_criterion(q1), HeterogeneousCriterion)

    def test_get_weight(self) -> None:
        q1 = YesNoQuestion(0, 'how?')
        s = Survey([q1])
        assert s._get_weight(q1) == 1
        s.set_weight(2, q1)
        assert s._get_weight(q1) == 2

    def test_set_weight(self) -> None:
        q1 = YesNoQuestion(0, 'how?')
        q2 = YesNoQuestion(1, 'when?')
        s = Survey([q1, q2])
        s.set_weight(2, q2)
        assert s._get_weight(q2) == 2

    def test_set_criterion(self) -> None:
        q1 = YesNoQuestion(0, 'how?')
        s = Survey([q1])
        s.set_criterion(HeterogeneousCriterion(), q1)
        assert isinstance(s._get_criterion(q1), HeterogeneousCriterion)

    def test_score_students(self):
        q1 = YesNoQuestion(0, 'how?')
        q2 = YesNoQuestion(1, 'when?')
        q3 = YesNoQuestion(2, 'how?')
        true_answer = Answer(True)
        false_answer = Answer(False)
        s = Survey([q1, q2, q3])
        s.set_criterion(LonelyMemberCriterion(), q1)
        helen = Student(0, 'Helen')
        tammy = Student(1, 'Tammy')
        amy = Student(2, 'Amy')
        helen.set_answer(q1, true_answer)
        helen.set_answer(q2, true_answer)
        helen.set_answer(q3, true_answer)
        tammy.set_answer(q1, true_answer)
        tammy.set_answer(q2, true_answer)
        tammy.set_answer(q3, true_answer)
        amy.set_answer(q1, false_answer)
        amy.set_answer(q2, true_answer)
        amy.set_answer(q3, true_answer)
        assert round(s.score_students([helen, tammy, amy]), 2) == 0.67

    def test_score_grouping(self) -> None:
        q1 = YesNoQuestion(0, 'how?')
        q2 = YesNoQuestion(1, 'when?')
        q3 = YesNoQuestion(2, 'how?')
        true_answer = Answer(True)
        false_answer = Answer(False)
        s = Survey([q1, q2, q3])
        s.set_criterion(LonelyMemberCriterion(), q1)
        helen = Student(0, 'Helen')
        tammy = Student(1, 'Tammy')
        amy = Student(2, 'Amy')
        jen = Student(3, 'Jen')
        helen.set_answer(q1, true_answer)
        helen.set_answer(q2, true_answer)
        helen.set_answer(q3, true_answer)
        tammy.set_answer(q1, true_answer)
        tammy.set_answer(q2, true_answer)
        tammy.set_answer(q3, true_answer)
        amy.set_answer(q1, true_answer)
        amy.set_answer(q2, true_answer)
        amy.set_answer(q3, true_answer)
        jen.set_answer(q1, true_answer)
        jen.set_answer(q2, true_answer)
        jen.set_answer(q3, true_answer)
        grouping = Grouping()
        grouping.add_group(Group([
            helen, amy]))
        grouping.add_group(Group([
            tammy, jen
        ]))
        score = s.score_grouping(grouping)
        assert score == 1.0



###############################################################################
# Task 10 Test cases
###############################################################################
class TestGrouperClass:
    def test_alpha_grouper(self) -> None:
        """
        Test that make_grouping of the alpha grouper class makes correct groups
        based on the alphabetical order of names of the students
        """
        grouper = AlphaGrouper(2)
        survey = Survey(get_questions_list())
        course = Course('CSC')
        students = get_students_list()
        course.enroll_students(students)
        grouping = grouper.make_grouping(course, survey)
        test_grouping = Grouping()
        test_grouping.add_group(
            Group([
                Student(3, 'Anna'),
                Student(5, 'Daliyah')]))
        test_grouping.add_group(
            Group([
                Student(4, 'Gene'),
                Student(1, 'Jen')]))
        test_grouping.add_group(
            Group([
                Student(6, 'Louise'),
                Student(0, 'Mabel')]))
        test_grouping.add_group(
            Group([
                Student(2, 'Sanjay'),
                Student(7, 'Tina')]))
        ret_groups = grouping.get_groups()
        test_groups = test_grouping.get_groups()
        for i in range(len(ret_groups)):
            s = ret_groups[i].get_members()
            for j in range(len(s)):
                assert s[j].id == test_groups[i].get_members()[j].id

    def test_alpha_grouper_odd(self) -> None:
        """
        Test that make_grouping of the alpha grouper class makes correct groups
        based on the alphabetical order of names of the students when the group
        size is odd
        """
        grouper = AlphaGrouper(3)
        survey = Survey(get_questions_list())
        course = Course('CSC')
        students = get_students_list()
        course.enroll_students(students)
        grouping = grouper.make_grouping(course, survey)
        test_grouping = Grouping()
        test_grouping.add_group(
            Group([
                Student(3, 'Anna'),
                Student(5, 'Daliyah'),
                Student(4, 'Gene')]))
        test_grouping.add_group(
            Group([
                Student(1, 'Jen'),
                Student(6, 'Louise'),
                Student(0, 'Mabel')]))
        test_grouping.add_group(
            Group([
                Student(2, 'Sanjay'),
                Student(7, 'Tina')]))
        ret_groups = grouping.get_groups()
        test_groups = test_grouping.get_groups()
        for i in range(len(ret_groups)):
            s = ret_groups[i].get_members()
            for j in range(len(s)):
                assert s[j].id == test_groups[i].get_members()[j].id

    def test_greedy_grouper(self) -> None:
        q = get_questions_list()
        s1 = Student(0, 'John')
        s1.set_answer(q[0], Answer('Easy'))
        s1.set_answer(q[1], Answer('Yes'))
        s1.set_answer(q[2], Answer(True))
        s1.set_answer(q[3], Answer(10))
        s2 = Student(2, 'Lia')
        s2.set_answer(q[0], Answer(['Complicated', 'Easy']))
        s2.set_answer(q[1], Answer('Yes'))
        s2.set_answer(q[2], Answer(True))
        s2.set_answer(q[3], Answer(10))
        s3 = Student(1, 'Millie')
        s3.set_answer(q[0], Answer('Huh'))
        s3.set_answer(q[1], Answer('Maybe'))
        s3.set_answer(q[2], Answer(False))
        s3.set_answer(q[3], Answer(100))
        course = Course('CSC')
        course.enroll_students([s1, s2, s3])
        grouper = GreedyGrouper(2)
        grouping = grouper.make_grouping(course, Survey(q))
        test_grouping = Grouping()
        test_grouping.add_group(Group([s1, s2]))
        test_grouping.add_group(Group([s3]))

        ret_groups = grouping.get_groups()
        test_groups = test_grouping.get_groups()
        for i in range(len(ret_groups)):
            s = ret_groups[i].get_members()
            for j in range(len(s)):
                assert s[j].id == test_groups[i].get_members()[j].id


# helper methods
def get_questions_list() -> list[Question]:
    return [
        CheckboxQuestion(0, 'What is life?',
                         ['I don\'t know', 'Complicated', 'Easy']),
        MultipleChoiceQuestion(1, 'Are you alive?',
                               ['Yes', 'I think so', 'No']),
        YesNoQuestion(2, 'Am I alive?'),
        NumericQuestion(3, 'How many fingers do you have?', 0, 10)
    ]


def get_students_list() -> list[Student]:
    return [Student(0, 'Mabel'),
            Student(1, 'Jen'),
            Student(2, 'Sanjay'),
            Student(3, 'Anna'),
            Student(4, 'Gene'),
            Student(5, 'Daliyah'),
            Student(6, 'Louise'),
            Student(7, 'Tina')]
