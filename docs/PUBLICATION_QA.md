# Publication QA — 2026-10-09

Actual local runs against synthetic inputs, using Python 3.12.14 and PyYAML.
No Jenkins controller, GitLab Runner, cluster or live health endpoint was tested.
The 15 existing unit tests passed. CLI/fixture checks:

| Check | Expected exit | Actual exit |
|---|---|---|
| 15 existing unit tests | 0 | 0 |
| Jenkins chain | 0 | 0 |
| resource-audit bad | 1 | 1 |
| resource-audit corrected | 0 | 0 |
| probe-audit bad | 1 | 1 |
| probe-audit corrected | 0 | 0 |
| Alert groups | 0 | 0 |
| Incident prompt | 0 | 0 |
| Port mismatch | 1 | 1 |
| Port corrected | 0 | 0 |
| Jenkins selected build 5 | 0 | 0 |
| Jenkins selected build 7 | 1 | 1 |
| Jenkins selected build 999 | 2 | 2 |
| GitLab local race | 0 | 0 |

The Jenkins fixture now compares selected bytes with the build-5 SHA256SUMS
manifest; it no longer compares a digest with itself. Build 7 fails and missing
build 999 is rejected. The Incident Prompt output excluded the synthetic token.
The GitLab fixture's selected old-then-new lock order does not establish GitLab's
queue ordering. No production compatibility or payment intent is inferred.

Publication includes code, examples, tests, technical references and applicable
licenses. Private planning documents, raw account metadata and videos are omitted.
