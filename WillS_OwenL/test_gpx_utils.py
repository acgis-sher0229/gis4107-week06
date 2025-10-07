import pytest
import gpx_utils as gu

@pytest.mark.parametrize("gpx,expected",[
    ('<trkpt lat="45.3888995" lon="-75.7472631">','-75.7472631,45.3888995'),
    ('<trkpt lat="54" lon="31.415">','31.415,54'),
    ('< lat="-8" lon="-6">',(None,None))
    ])

def test_get_coords_from_gpx(gpx, expected):
    assert gu.get_coords_from_gpx(gpx) == expected
