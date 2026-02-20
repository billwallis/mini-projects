from __future__ import annotations

import collections
import dataclasses
import itertools

type Word = str
type Replacements = dict[str, str]
type Permutation = tuple[int, ...]


@dataclasses.dataclass(frozen=True, slots=True)
class CharPos:
    char: str
    pos: int


def _get_permutations(
    word: Word,
    replacements: Replacements,
) -> list[Permutation]:
    num_replacements = sum(
        collections.Counter(word).get(r, 0) for r in replacements.keys()
    )
    combinations = itertools.combinations_with_replacement(
        [0, 1], num_replacements
    )
    permutation_sets = [
        set(itertools.permutations(combo, num_replacements))
        for combo in combinations
    ]

    return sorted([p for s in permutation_sets for p in s])


def _get_replacement_positions(
    word: Word,
    replacements: Replacements,
) -> dict[int, CharPos]:
    replacement_positions: dict[int, CharPos] = dict()
    index = 0
    for i, c in enumerate(word):
        if c in replacements.keys():
            replacement_positions[index] = CharPos(char=c, pos=i)
            index += 1

    return replacement_positions


def _replace_at_position(word: Word, position: int, replacement: str) -> Word:
    return word[:position] + replacement + word[1 + position :]


def _do_perm_replacement(
    word: Word,
    replacements: Replacements,
    replacement_positions: dict[int, CharPos],
    permutation: Permutation,
) -> Word:
    for rep_i, use_rep in enumerate(permutation):
        if use_rep:
            replacement = replacement_positions[rep_i]
            word = _replace_at_position(
                word, replacement.pos, replacements[replacement.char]
            )

    return word


def replace_characters(word: Word, replacements: Replacements) -> list[Word]:
    """
    Replace characters.
    """

    permutations = _get_permutations(word, replacements)
    replacement_positions = _get_replacement_positions(word, replacements)

    return [
        _do_perm_replacement(
            word=word,
            replacements=replacements,
            replacement_positions=replacement_positions,
            permutation=permutation,
        )
        for permutation in permutations
    ]
