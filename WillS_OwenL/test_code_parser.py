import pytest
import code_parser as cod_par

@pytest.mark.parametrize("link_code,expected",[
    ("20-WBO-109642-809",'BO-642'),
    ("43-GGF-114524-998",'GF-524'),
    ("45-ABC-692001-003","BC-001")
    ])

def test_get_db_link(link_code, expected):
    assert cod_par.get_db_link(link_code) == expected
