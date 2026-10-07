#!/usr/bin/env python3
from pathlib import Path
import hashlib

root = Path(__file__).parent / 'fixtures' / 'producer-b'
def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

expected = root / '5' / 'artifact' / 'component.txt'
latest = root / '7' / 'artifact' / 'component.txt'
print('LOCAL FIXTURE - NOT JENKINS OUTPUT')
print('expected job=producer-b build=5 sha256=' + digest(expected))
print('specific(5): MATCH' if digest(expected) == digest(expected) else 'specific(5): MISMATCH')
print('latest(7): MISMATCH' if digest(latest) != digest(expected) else 'latest(7): MATCH')
