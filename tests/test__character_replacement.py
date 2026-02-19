import pytest

from src.character_replacer import replace_characters


@pytest.mark.parametrize(
    "word, replacements, expected",
    [
        # Null cases
        ("", {}, [""]),
        ("", {"": ""}, [""]),
        ("", {"a": "b"}, [""]),
        # No replacements -> no change
        ("foo", {}, ["foo"]),
        # Null replacements -> no change
        ("foo", {"": ""}, ["foo"]),
        # Replacing chars that aren't present -> no change
        ("foo", {"a": "b"}, ["foo"]),
        # Replacement chars are case-sensitive -> no change
        ("FOO", {"f": "X", "o": "0"}, ["FOO"]),
        # Single replacements
        ("foo", {"f": "b"}, ["foo", "boo"]),
        ("foo", {"o": "f"}, ["foo", "fof", "ffo", "fff"]),
        ("foo bar", {" ": "-"}, ["foo bar", "foo-bar"]),
        # Multiple replacements
        (
            "foo",
            {"f": "X", "o": "0"},
            ["foo", "fo0", "f0o", "f00", "Xoo", "Xo0", "X0o", "X00"],
        ),
        (
            "foobar baz",
            {"a": "4", "o": "0"},
            [
                "foobar baz",
                "foobar b4z",
                "foob4r baz",
                "foob4r b4z",
                "fo0bar baz",
                "fo0bar b4z",
                "fo0b4r baz",
                "fo0b4r b4z",
                "f0obar baz",
                "f0obar b4z",
                "f0ob4r baz",
                "f0ob4r b4z",
                "f00bar baz",
                "f00bar b4z",
                "f00b4r baz",
                "f00b4r b4z",
            ],
        ),
        # Missing replacement chars are "ignored"
        (
            "foo",
            {"f": "X", "o": "0", "x": "X"},
            ["foo", "fo0", "f0o", "f00", "Xoo", "Xo0", "X0o", "X00"],
        ),
    ],
)
def test__replace_characters__happy_path(
    word: str,
    replacements: dict[str, str],
    expected: list[str],
):
    assert replace_characters(word, replacements) == expected
