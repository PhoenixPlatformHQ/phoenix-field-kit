#!/usr/bin/env python3
"""Local fixture for an out-of-order deployment race. Not GitLab output."""

from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from threading import Lock
from typing import Any
from time import sleep

TARGET = Path("deployed-version.txt")


def deploy(version: str, delay: float, lock: Any = None) -> None:
    def write() -> None:
        sleep(delay)
        TARGET.write_text(version + "\n", encoding="utf-8")
        print(f"deployed {version}")

    if lock is None:
        write()
    else:
        with lock:
            write()


def run_unsafe() -> str:
    with ThreadPoolExecutor(max_workers=2) as pool:
        pool.submit(deploy, "v1-old", 0.35)
        pool.submit(deploy, "v2-new", 0.05)
    return TARGET.read_text(encoding="utf-8").strip()


def run_serialized() -> str:
    deployment_lock = Lock()
    with ThreadPoolExecutor(max_workers=2) as pool:
        first = pool.submit(deploy, "v1-old", 0.12, deployment_lock)
        sleep(0.02)
        second = pool.submit(deploy, "v2-new", 0.02, deployment_lock)
        first.result()
        second.result()
    return TARGET.read_text(encoding="utf-8").strip()


if __name__ == "__main__":
    unsafe = run_unsafe()
    print(f"unsafe final: {unsafe}")
    assert unsafe == "v1-old"

    serialized = run_serialized()
    print(f"serialized final: {serialized}")
    assert serialized == "v2-new"

    TARGET.unlink(missing_ok=True)
    print("fixture: PASS")

