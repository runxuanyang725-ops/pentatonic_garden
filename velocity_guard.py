"""
Simple linter: check that velocity= uses integers or integer-producing wrappers.

"""
import re, sys, pathlib

VEL_RE = re.compile(r"velocity\s*=\s*([0-9]{1,3})\b")
BAD_RE = re.compile(r"velocity\s*=\s*\[")

def check_file(p: pathlib.Path) -> int:
    txt = p.read_text(encoding="utf-8", errors="ignore")
    bad = 0
    for i, line in enumerate(txt.splitlines(), 1):
        if BAD_RE.search(line):
            print(f"{p}:{i}: velocity must be a single integer, not a list")
            bad += 1
        # Optional: warn on out-of-range literals
        m = VEL_RE.search(line)
        if m:
            val = int(m.group(1))
            if not (0 <= val <= 127):
                print(f"{p}:{i}: velocity {val} out of range [0,127]")
                bad += 1
    return bad

def main(paths):
    exit_code = 0
    for raw in paths:
        p = pathlib.Path(raw)
        if p.is_dir():
            for f in p.rglob("*.py"):
                exit_code |= check_file(f)
        elif p.is_file():
            exit_code |= check_file(p)
    sys.exit(1 if exit_code else 0)

if __name__ == "__main__":
    main(sys.argv[1:] or ["cells"])
