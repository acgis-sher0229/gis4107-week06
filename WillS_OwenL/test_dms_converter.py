import csv
import dms_converter as dc

def test_dms2dd():
    expected = -75.25, 45.25
    dms_coords = '075 15 00 w 45 15 00 n\n'
    actual = dc.dms2dd(dms_coords)
    assert expected == actual

    expected = -75.25, -45.25
    dms_coords = '075 15 00 w 45 15 00 s\n'
    actual = dc.dms2dd(dms_coords)
    assert expected == actual

def test_dms2dd_bad_coords():
    expected = (None, None)
    for dms in ['181 00 00 w 45 15 00 n',
                '180 15 00 w 45 15 00 n',
                '180 00 01 w 45 15 00 n',
                '075 15 00 w 91 00 00 n',
                '075 15 00 w 90 15 00 n',
                '075 15 00 w 90 00 01 n']:
        actual = dc.dms2dd(dms)
        assert expected == actual
    
