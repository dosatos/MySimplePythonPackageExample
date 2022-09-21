from my_module.main import to_string


def test_to_string():
    assert to_string(['first', 'second']) == 'first, second'
