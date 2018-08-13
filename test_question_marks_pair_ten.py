import pytest
from question_marks_pair_ten import ThreeQuestionMarks

def test_case_one():
    t = ThreeQuestionMarks("arrb6???4xxbl5???eee5")
    assert t.count_q_marks() == True

def test_case_two():
    t = ThreeQuestionMarks("acc?7??sss?3rr1??????5")
    assert t.count_q_marks() == True

def test_case_three():
    t = ThreeQuestionMarks("5??aaaaaaaaaaaaaaaaaaa?5?5")
    assert t.count_q_marks() == False

def test_case_four():
    t = ThreeQuestionMarks("9???1???9???1???9")
    assert t.count_q_marks() == True

def test_case_five():
    t = ThreeQuestionMarks("aa6?9")
    assert t.count_q_marks() == False