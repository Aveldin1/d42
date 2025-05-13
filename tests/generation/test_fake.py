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
    with given:
        sch = schema.list(
            schema.str('test4') |
            schema.str('test3') |
            schema.str('test2') |
            schema.str('test')
        ).len(0, ...).unique()
        # Result: [], ['test', 'test3', 'test2', 'test4'] or Error
        # sch = schema.list(schema.int.min(1).max(4)).len(5).unique()
        # Result: Error
        # sch = schema.list(schema.float.min(1.0).max(4.0)).len(5).unique()
        # Result: [2.692677923681043, 2.0229881219962698, 1.605519631046103,
        # 3.6768269249998484, 3.4938458424646055]
        # sch = schema.list(schema.bytes | schema.none).unique()
        # Result: [b' tB92qJshF MSVbn25f0JeBgXZ7'] or [b'', None]
        # sch = schema.list.len(3).unique()
        # Result: [['0mD', 'j7v'], ['3WJq', 'qZli', 'l0Y'], ['MiQ', 'oECs']]
        # sch = schema.list([schema.int(1), schema.int(1)]).unique()
        # Result: Error
        # sch = schema.list([schema.int.min(1).max(2), schema.int.min(1).max(2)]).unique()
        # Result: [1, 2] or [2, 1]

    with when:
        result = fake(sch)
        print(result)

    with then:
        assert isinstance(result, list)
        assert len(set(result)) == len(result)
