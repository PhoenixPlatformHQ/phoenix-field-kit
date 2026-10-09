# Jenkins exact-artifact lab

Problem: packaging can copy a later build when a downstream producer runs again before a slow parallel branch finishes.

Fix: retain **job + build number** from the object returned by `build`; pass both to packaging; use `copyArtifacts(... selector: specific(build), optional: false)`; propagate downstream failures; verify archived bytes.

This package was **not executed on a Jenkins controller**. `verify_fixture.py` is a real local fixture check, explicitly not Jenkins output. It proves that build 5 and build 7 contain different bytes and that selecting 5 matches the expected digest. It does not prove controller/plugin compatibility or trusted provenance.

Runtime acceptance still required: overlapping producer build, missing expected artifact fails, downstream failure stops promotion, permissions remain in Production mode.


## Run the local fixture

From this folder (Python 3.10+):

```sh
python verify_fixture.py --build 5
python verify_fixture.py --build 7
```

Build 5 matches the expected SHA256SUMS (exit 0); build 7 contains different bytes
(exit 1). A missing build returns exit 2. This check verifies fixture integrity,
not a Jenkins deployment or artifact provenance. Review the three Jenkinsfile
templates for your own job names, permissions and plugin configuration.
License: MIT; see [../LICENSE](../LICENSE).
