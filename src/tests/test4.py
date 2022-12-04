from src.days.day4 import fully_contains, Assignment


def test_fully_contains():
    assert fully_contains(Assignment(35,49),Assignment(34,50)) == True
    assert fully_contains(Assignment(33,49),Assignment(34,50)) == False

test_fully_contains()