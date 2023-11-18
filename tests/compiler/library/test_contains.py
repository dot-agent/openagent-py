from openams import compiler

def test_contains():
    """ Test the behavior of `contains`.
    """

    program = compiler("""{{#if (contains val "substr")}}are equal{{else}}not equal{{/if}}""")
    assert str(program(val="no sub")) == "not equal"
    assert str(program(val="this is a substr")) == "are equal"
    assert str(program(val="this is a subsr")) == "not equal"