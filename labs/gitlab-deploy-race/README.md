# VIDEO_014 — GitLab deploy race

Free local fixture and GitLab YAML walkthrough for out-of-order deployments.

## Claim under test

Two deployment jobs targeting the same environment can overlap or be selected in an unexpected order. A newer release can finish first, then an older release can overwrite it. `resource_group` serializes jobs, but ordering is controlled separately and the default process mode is `unordered`.

## What this lab proves

`run_fixture.py` is a deterministic local concurrency fixture. It demonstrates the state transition, not GitLab Runner behavior:

- unsafe case: `v2` lands first, then stale `v1` overwrites it;
- serialized case: `v1` completes before `v2`, leaving `v2` deployed.

This is **not GitLab output** and does not exercise a GitLab controller or runner.

Run:

```bash
python3 run_fixture.py
```

## GitLab controls shown in the video

1. Add the same `resource_group` to every deployment job targeting the environment.
2. Choose an explicit process mode appropriate to the workflow. For continuous delivery, GitLab documents `newest_ready_first` for preferring the newest ready job; deployment scripts must be idempotent.
3. Enable **Prevent outdated deployment jobs** as a separate protection. It rejects an older deployment when GitLab considers a newer deployment current.

`resource_group` and outdated-job protection solve different failure modes; neither should be described as a universal rollback strategy.

## Sources

- https://docs.gitlab.com/ci/environments/deployment_safety/
- https://docs.gitlab.com/ci/resource_groups/
- https://gitlab.com/gitlab-org/gitlab/-/issues/408981


## Template boundaries

`gitlab-ci.safe.yml` is a fragment for review, not a complete application pipeline.
`deploy.sh` is an application-specific script you must supply. The process mode
and outdated-job protection are separate settings; this YAML does not configure
them. The serialized fixture deliberately runs old then new and is not evidence
that GitLab's default unordered queue preserves that order.

The fixture creates then deletes `deployed-version.txt` in the working directory;
run it in this lab folder without a pre-existing file of that name.
License: MIT; see [../LICENSE](../LICENSE).
