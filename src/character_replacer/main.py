import argparse
from collections.abc import Sequence

from character_replacer import replace_characters

SUCCESS = 0
FAILURE = 1


def _parse_replacements(replacements: list[str]) -> dict[str, str]:
    reps = dict()
    for replacement in replacements:
        err_msg = f"Invalid replacement value {replacement!r}"
        if ":" not in replacement:
            raise ValueError(f"{err_msg} (no ':' found)")

        from_, to = replacement.split(":")
        if len(from_) > 1 or len(to) > 1:
            raise ValueError(f"{err_msg} (too many characters)")

        reps[from_] = to

    return reps


def main(argv: Sequence[str] | None = None) -> int:
    """
    Parse the arguments and run the hook.
    """

    parser = argparse.ArgumentParser()
    parser.add_argument("--word", required=True)
    parser.add_argument("--replacements", nargs="*", required=True)
    args = parser.parse_args(argv)

    words = replace_characters(
        word=args.word,
        replacements=_parse_replacements(args.replacements),
    )
    [print(word) for word in words]

    return SUCCESS
