import pytest
import doc_scanner as ds

@pytest.mark.parametrize("CSIS_code,expected",[
    ("T6op3",True),
    ("banana",False),
    ("BTTx6op3528",True)
    ])

def _x_test(CSIS_code, expected):
    assert ds.has_x_code(CSIS_code) == expected