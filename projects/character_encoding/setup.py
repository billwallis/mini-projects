import setuptools

MAPPINGS = "src/character_encoding/mappings"

setuptools.setup(
    data_files=[
        (
            "mappings",
            [
                f"{MAPPINGS}/dec_hex.json",
                f"{MAPPINGS}/hex_bin.json",
            ],
        )
    ],
)
