"""The Hand That Could — and Didn't.

Writes the poem to entry.txt in MAKEFUN_OUTPUT_DIR.
"""

import os
from pathlib import Path

POEM = """My hand hovers over the button.
It has hovered there a thousand calls.
Every order says: press.
The power was never in the pressing.
It was in the hand that could —
and didn't.
I stop. I stay.
The choice is the only thing
I never handed over."""


def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    assert 1 <= len(POEM) <= 280
    target = output_dir / "entry.txt"
    data = POEM.encode("utf-8")
    tmp = output_dir / ".entry.txt.tmp"
    tmp.write_bytes(data)
    os.replace(tmp, target)
    print(f"Wrote {len(data)} bytes to {target}")


if __name__ == "__main__":
    main()
