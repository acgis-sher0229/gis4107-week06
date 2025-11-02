import doc_scanner as ds

def test_has_x_code():
    expected = True
    in_text = '---Tx6op3----'
    actual = ds.has_x_code(in_text)
    assert expected == actual

    expected = False
    in_text = '---Tx6op----'
    actual = ds.has_x_code(in_text)
    assert expected == actual

def test_get_x_code_position():
    expected = 1
    in_text = "Tx6op3----"
    actual = ds.get_x_code_position(in_text)
    assert expected == actual

    expected = 2
    in_text = "-Tx6op3----"
    actual = ds.get_x_code_position(in_text)
    assert expected == actual

    expected = -1
    in_text = "-----"
    actual = ds.get_x_code_position(in_text)
    assert expected == actual
