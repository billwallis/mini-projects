import textwrap

import pytest

from src.character_replacer.main import main


def test__cli__happy_path(capsys: pytest.CaptureFixture):
    assert main(["--word", "foo", "--replacements", "f:X", "o:0"]) == 0

    stdout, stderr = capsys.readouterr()
    assert stderr == ""
    assert stdout == textwrap.dedent(
        """\
        foo
        fo0
        f0o
        f00
        Xoo
        Xo0
        X0o
        X00
        """
    )


def test__cli__raises_error__when_replacement_does_not_have_colon():
    with pytest.raises(ValueError):
        main(["--word", "foo", "--replacements", "abc"])


@pytest.mark.parametrize(
    "replacements",
    [["ab:cd"], ["ab:"], [":cd"], ["a:b", "c:d", "ef:gh"]],
)
def test__cli__raises_error__when_replacement_is_too_long(
    replacements: list[str],
):
    with pytest.raises(ValueError):
        main(["--word", "foo", "--replacements", "ab:cd"])
