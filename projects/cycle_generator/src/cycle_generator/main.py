"""
Given a list of names, randomly create a single directed cycle between
everyone.

Useful for, say, a Secret Santa pairing.
"""
# cycle-gen --help
# cycle-gen foo bar baz
# cycle-gen --file 'projects/cycle_generator/src/cycle_generator/names.csv' --oneline

from __future__ import annotations

import argparse
import collections
import pathlib
import random
from collections.abc import Sequence


class DuplicateNamesError(Exception):
    pass


def shuffle_names(list_of_names: list[str]) -> list[str]:
    names = sorted(set(list_of_names), key=lambda _: random.random())  # noqa: S311
    if len(names) != len(list_of_names):
        duplicates = [
            f"    {k} ({v} times)"
            for k, v in collections.Counter(list_of_names).items()
            if v != 1
        ]
        raise DuplicateNamesError(
            f"duplicate names found\n{'\n'.join(duplicates)}"
        )

    return names


def generate_cycle(list_of_names: list[str], oneline: bool) -> str:
    names = shuffle_names(list_of_names)
    if len(names) == 1:
        return names[0]

    cycle = ""
    if oneline:
        cycle += names[0]
        for name in names[1:]:
            cycle += f" --> {name}"
    else:
        for i in range(len(names)):
            left, right = names[i - 1], names[i]
            cycle += f"{left} --> {right}\n"
        cycle = cycle.rstrip("\n")

    return cycle


def main(argv: Sequence[str] | None = None) -> int:
    """
    Parse the arguments and run the command.
    """

    parser = argparse.ArgumentParser()
    parser.add_argument("names", nargs="*")
    parser.add_argument("--file", type=pathlib.Path, required=False)
    parser.add_argument(
        "--oneline",
        action=argparse.BooleanOptionalAction,
        default=False,
    )
    args = parser.parse_args(argv)

    if len(args.names) == 0 and args.file is None:
        parser.print_usage()
        print("cycle-gen: error: either 'names' or '--file' must be specified")
        return 2
    elif len(args.names) != 0 and args.file is not None:
        parser.print_usage()
        print("cycle-gen: error: 'names' and '--file' cannot both be specified")
        return 2

    if len(args.names) != 0:
        names = args.names
    else:
        assert isinstance(args.file, pathlib.Path)  # noqa: S101
        names = args.file.read_text().rstrip("\n").split("\n")

    try:
        print(generate_cycle(names, args.oneline))
        return 0
    except DuplicateNamesError as err:
        print(f"cycle-gen: error: {err}")
        return 1
    except Exception as err:
        print(f"cycle-gen: unhandled exception: {err}")
        return 125


if __name__ == "__main__":
    raise SystemExit(main())  # pragma: no cover
