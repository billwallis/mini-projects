import textwrap

import pytest
from morse_code_translator import translate


@pytest.mark.parametrize(
    "morse_code, expected",
    [
        ("", ""),
        (
            textwrap.dedent(
                """
                .-- . ----. ...- . / .- .-.. .-- .- -.-- ... / -.. . ..-. .. -. . -.. / --- ..- .-. ... . .-.. ...- . ... / -... -.-- / - .... . / .- -... .. .-.. .. - -.-- / - --- / --- ...- . .-. -.-. --- -- . / - .... . / .. -- .--. --- ... ... .. -... .-.. . .-.-.-
                -.-- --- ..- / -.-. .- -. / -.. --- / .. - -.-.--
                """
            ).strip(),
            "we've always defined ourselves by the ability to overcome the impossible.\nyou can do it!",
        ),
    ],
)
def test__morse_code_can_be_translated(morse_code: str, expected: str):
    assert translate(morse_code) == expected
