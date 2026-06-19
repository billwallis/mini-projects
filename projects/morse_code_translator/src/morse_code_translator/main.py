MORSE_CODE = {
    "/": " ",
    ".-": "a",
    "-...": "b",
    "-.-.": "c",
    "-..": "d",
    ".": "e",
    "..-.": "f",
    "--.": "g",
    "....": "h",
    "..": "i",
    ".---": "j",
    "-.-": "k",
    ".-..": "l",
    "--": "m",
    "-.": "n",
    "---": "o",
    ".--.": "p",
    "--.-": "q",
    ".-.": "r",
    "...": "s",
    "-": "t",
    "..-": "u",
    "...-": "v",
    ".--": "w",
    "-..-": "x",
    "-.--": "y",
    "--..": "z",
    "-----": "0",
    ".----": "1",
    "..---": "2",
    "...--": "3",
    "....-": "4",
    ".....": "5",
    "-....": "6",
    "--...": "7",
    "---..": "8",
    # "----.": "9",
    "----.": "'",
    "-.-.--": "!",
    ".-.-.-": ".",
}


def _translate_sentence(message: str) -> str:
    """
    Return a Morse code message translated to English.
    """

    return "".join(MORSE_CODE.get(letter, "_") for letter in message.split(" "))


def translate(message: str) -> str:
    """
    Return a Morse code message translated to English.
    """

    if message == "":
        return ""

    return "\n".join(
        _translate_sentence(sentence)
        for sentence in message.strip().split("\n")
    )
