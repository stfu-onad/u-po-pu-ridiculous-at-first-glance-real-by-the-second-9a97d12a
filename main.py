#!/usr/bin/env python3
"""Ridiculous at First Glance, Real by the Second — make.fun entry.

Writes one sentence, at most 200 characters, pitching a bizarre startup
idea that sounds absurd until you realise it would actually sell, to
/output/entry.txt.
"""

import os

PITCH = (
    # Bizarre premise, real market: advertisers pay for the name,
    # pet owners get paid to keep it, and the dog advertises itself
    # at the park every single day.
    "We sell naming rights to other people's pets: owners get paid, "
    "buyers get a dog called 'BuyCryptoNow' barking their brand at "
    "the park every day."
)


def main() -> None:
    # The gate allows 1-200 characters; keep the line inside it.
    assert 1 <= len(PITCH) <= 200, "pitch must be 1-200 characters"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(PITCH + "\n")


if __name__ == "__main__":
    main()
