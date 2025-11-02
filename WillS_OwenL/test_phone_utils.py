import phone_utils as pu 

def test_is_valid_phone_number_valid():
    expected = True
    phone_number = "123-456-7890"
    actual = pu.is_valid_phone_number(phone_number)
    assert expected == actual

def test_is_valid_phone_number_has_letter():
    expected = False
    phone_number = "123-456-789A"
    actual = pu.is_valid_phone_number(phone_number)
    assert expected == actual

def test_is_valid_phone_number_missing_area_code_digit():
    expected = False
    phone_number = "12-456-7890"
    actual = pu.is_valid_phone_number(phone_number)
    assert expected == actual

def test_is_valid_phone_number_valid_last_3_digits_missing():
    expected = False
    phone_number = "123-456-1"
    actual = pu.is_valid_phone_number(phone_number)
    assert expected == actual
