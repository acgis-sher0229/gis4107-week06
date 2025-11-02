import gpx_utils

def test_get_get_coords_from_gpx_valid():
    expected = (-75.74, 45.38)
    gpx = '<trkpt lat="45.38" lon="-75.74">'
    actual = gpx_utils.get_coords_from_gpx(gpx)
    assert expected == actual

    expected = (-75.7472631, 45.3888995)
    gpx = '<trkpt lat="45.3888995" lon="-75.7472631">'
    actual = gpx_utils.get_coords_from_gpx(gpx)
    assert expected == actual

def test_get_get_coords_from_gpx_no_trkpt():
    expected = None, None
    gpx = '<ABC lat="45.38" lon="-75.74">'
    actual = gpx_utils.get_coords_from_gpx(gpx)
    assert expected == actual