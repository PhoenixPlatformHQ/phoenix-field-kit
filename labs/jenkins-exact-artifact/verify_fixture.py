#!/usr/bin/env python3
"""Select local fixture bytes and check the expected manifest. Not Jenkins output."""
import argparse
import hashlib
from pathlib import Path
import sys

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--build', type=int, default=5)
    args = parser.parse_args()
    root = Path(__file__).parent / 'fixtures' / 'producer-b'
    expected_dir = root / '5' / 'artifact'
    try:
        expected_hash, expected_name = (expected_dir / 'SHA256SUMS').read_text().split()
        selected = root / str(args.build) / expected_name
        actual_hash = hashlib.sha256(selected.read_bytes()).hexdigest()
    except (OSError, ValueError) as exc:
        print('INPUT ERROR: ' + str(exc), file=sys.stderr)
        return 2
    print('LOCAL FIXTURE - NOT JENKINS OUTPUT')
    print('expected job=producer-b build=5 sha256=' + expected_hash)
    print(f'selected job=producer-b build={args.build} sha256={actual_hash}')
    matched = actual_hash == expected_hash
    print('selected: MATCH' if matched else 'selected: MISMATCH')
    return 0 if matched else 1

if __name__ == '__main__':
    sys.exit(main())
