"""
Given a list of names, randomly create a single directed cycle between
everyone.

Useful for, say, a Secret Santa pairing.
"""
# python -m projects.cycle_generator.src.cycle_generator.main --help
# python -m projects.cycle_generator.src.cycle_generator.main foo bar baz
# python -m projects.cycle_generator.src.cycle_generator.main $(cat 'projects/cycle_generator/src/cycle_generator/names.csv') --oneline

from __future__ import annotations

import argparse
import collections
import random
from collections.abc import Sequence


def shuffle_names(list_of_names: list[str]) -> list[str]:
    names = sorted(set(list_of_names), key=lambda _: random.random())  # noqa: S311
    if len(names) != len(list_of_names):
        duplicates = [
            f"    {k} ({v} times)"
            for k, v in collections.Counter(list_of_names).items()
            if v != 1
        ]
        raise ValueError(f"duplicate names found!\n{'\n'.join(duplicates)}")

    return names


def generate_cycle(list_of_names: list[str], oneline: bool) -> None:
    names = shuffle_names(list_of_names)
    if len(names) == 1:
        print(names[0])
        return

    if oneline:
        print(names[0], end="")
        for name in names[1:]:
            print(f" --> {name}", end="")
        print(flush=True)
    else:
        for i in range(len(names)):
            left, right = names[i - 1], names[i]
            print(f"{left} --> {right}")


def main(argv: Sequence[str] | None = None) -> int:
    """
    Parse the arguments and run the command.
    """

    parser = argparse.ArgumentParser()
    parser.add_argument("names", nargs="+")
    parser.add_argument(
        "--oneline",
        action=argparse.BooleanOptionalAction,
        default=False,
    )
    args = parser.parse_args(argv)

    try:
        generate_cycle(args.names, args.oneline)
        return 0
    except Exception as err:
        print(f"error: {err}")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())  # pragma: no cover
