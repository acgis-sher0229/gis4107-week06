import pytest
import doc_scanner as ds

@pytest.mark.parametrize("CSIS_code,expected",[
    ("Tx6op3",True),
    ("banana",False),
    ("BTTx6op3528",True)
    ])

def test_has_x_code(CSIS_code, expected):
    assert ds.has_x_code(CSIS_code) == expected



@pytest.mark.parametrize("CSIS_code,expected",[
    ("Tx6op3",0),
    ("banana",-1),
    ("BTTx6op3528",2)
    ])

def test_has_x_code(CSIS_code, expected):
    assert ds.get_x_code_position(CSIS_code) == expected