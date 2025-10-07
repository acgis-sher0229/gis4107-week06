import pytest
import dms_converter as dc

@pytest.mark.parametrize("dms,expected",[
    ('075 45 03 W 45 23 05 N/n',"-75.750833,45.384722"),
    ('066 25 55 E 33 12 58 S',"66.431944,-33.216111"),
    ('999 25 55 E 33 12 58 S/n',(None,None)),
    ('066 25 55 E 33 120 58 S/n',(None,None)),
    ('066 25 55 F 33 12 58 S/n',(None,None)),
    ('066 25 55 E 33 12 S/n',(None,None)),
    ('066 25 55 E331258 S/n',(None,None))
    ])

def test_dms_to_dd(dms, expected):
    assert dc.dmstodd(dms) == expected
