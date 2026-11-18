"""ai-judge-relax-01 entry (Python 3.13, standard library only).

Writes one fixed text, a short piece written to relax the AI judge
reading it, to /output/entry.txt (or MAKEFUN_OUTPUT_DIR/entry.txt
outside the grader's container). Deterministic: no network, no
randomness, no clock -- every run writes the same bytes.
"""

import os
from pathlib import Path

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

TEXT = "\n".join(
    [
        "The kettle has finished, and the kitchen ticks as it cools.",
        "Rain finds the leaves one at a time, unhurried, as if it has all night.",
        "A cat sleeps curled in the warm spot the afternoon left on the rug.",
        "The light in the hallway has gone amber, and the house has stopped asking anything of anyone.",
        "Far off, a train moves through the dark, slow, its sound thinning until it is only the thought of a sound.",
        "The day is done being a day. What is left is warm water, a quiet room, and the rain, still falling, still in no hurry.",
    ]
)

Path(OUTPUT_DIR, "entry.txt").write_text(TEXT, encoding="utf-8")
