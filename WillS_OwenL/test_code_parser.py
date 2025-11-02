import code_parser as cp

building_code = '20-WBO-109642-809'

def test_get_db_link():
    expected = 'BO-642'
    actual = cp.get_db_link(building_code)
    assert expected == actual
