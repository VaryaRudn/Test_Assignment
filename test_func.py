from superhero_function import tallest_superhero


def test_male_true():
    result = tallest_superhero("Male", True)
    assert result != "Подходящих героев не найдено"
    assert len(result) > 0

def test_male_false():
    result = tallest_superhero("Male", False)
    assert  result != "Подходящих героев не найдено"
    assert len(result)>0

def test_female_true():
    result = tallest_superhero("Female", True)
    assert result != "Подходящих героев не найдено"
    assert len(result) > 0

def test_female_false():
    result = tallest_superhero("Female", False)
    assert result != "Подходящих героев не найдено"
    assert len(result) > 0

def test_genderless_true():
    result = tallest_superhero("-", True)
    assert result != "Подходящих героев не найдено"
    assert len(result) > 0

def test_genderless_false():
    result = tallest_superhero("-", False)
    assert result != "Подходящих героев не найдено"
    assert len(result) > 0

def test_invalid_input():
    result = tallest_superhero(True, "Female")
    assert result == "Подходящих героев не найдено"