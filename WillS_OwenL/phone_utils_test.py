import pytest
import phone_utils as pu

@pytest.mark.parametrize("phone_number,expected",[
    ("111-111-1111",True),
    ("efhfwuewf--8",False),
    ("111-1111-111",False)
    ])

def test_phone_utils(phone_number, expected):
    assert pu.is_valid_phone_number(phone_number) == expected
