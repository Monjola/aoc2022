from src.days.day2 import generate_choice


def test_generate_choice():
    assert generate_choice("A", "X") == "Z", "expected Z got " + generate_choice("A", "X")
    assert generate_choice("B", "X") == "X", "expected X got " + generate_choice("B", "X")
    assert generate_choice("C", "X") == "Y", "expected Y got " + generate_choice("C", "X")
    assert generate_choice("A", "Y") == "X", "expected X got " + generate_choice("A", "Y")
    assert generate_choice("B", "Y") == "Y", "expected Y got " + generate_choice("B", "Y")
    assert generate_choice("C", "Y") == "Z", "expected Z got " + generate_choice("C", "Y")
    assert generate_choice("A", "Z") == "Y", "expected Y got " + generate_choice("A", "Z")
    assert generate_choice("B", "Z") == "Z", "expected Z got " + generate_choice("B", "Z")
    assert generate_choice("C", "Z") == "X", "expected X got " + generate_choice("C", "Z")


test_generate_choice()
