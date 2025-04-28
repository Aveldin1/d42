from baby_steps import given, then, when
from pytest import raises

from d42 import fake, schema


def test_fake():
    with when:
        res = fake(schema.int)

    with then:
        isinstance(res, int)


def test_fake_incorrect_type():
    with when, raises(Exception) as exception:
        fake(object)

    with then:
        assert exception.type is TypeError
        assert str(exception.value) == (
            "Expected 'schema' to be an instance of 'd42.declaration.types.Schema', "
            "got <class 'object'> instead"
        )


def test_fake_unique_list():
    # Кейсы
    # sch = schema.list(
    #     schema.str('test4') |
    #     schema.str('test3') |
    #     schema.str('test2') |
    #     schema.str('test')
    # ).len(0, ...).unique()
    # sch = schema.list(schema.int.min(1).max(4)).len(5).unique()
    # sch = schema.list(schema.list(schema.str('A'))).unique()
    with given:
        sch = schema.list(schema.int).unique()

    with when:
        result = fake(sch)
        print(result)

    with then:
        assert isinstance(result, list)
        assert len(set(result)) == len(result)
