# DevOps / AIOps Field Kit — v0.1

Five offline MVP utilities created 2026-10-03; public distribution 2026-10-09. Free source under MIT.
These are narrow helpers, not a production-certified suite or validated paid products.
No credentials, cluster, Jenkins server, cloud, or paid API is needed to run them.
Requires Python 3.10+ and PyYAML (`python -m pip install -r requirements.txt`).

| Tool | Purpose | Boundary |
|---|---|---|
| `jenkins-chain` | Validate dependency graph and generate a sequential Jenkinsfile | Does not submit jobs; Jenkins runtime validation is pending |
| `resource-audit` | Find request > limit and missing explicit CPU/memory settings | No sizing recommendations; admission defaults and pod-level resources are outside scope |
| `probe-audit` | Find unresolved named HTTP/TCP probe ports and selected invalid settings | Does not test health endpoints; not a full Kubernetes schema validator |
| `alert-groups` | Rank alert groups from an Alertmanager JSON export | Does not infer root cause or prove duplicate notifications |
| `incident-prompt` | Build a line-numbered incident triage prompt with best-effort redaction | No LLM call; manual privacy review required; Kubernetes Secret objects/base64/PII may remain |

## Run examples

```sh
python fieldkit.py jenkins-chain examples/chain.yaml > Jenkinsfile
python fieldkit.py resource-audit examples/workload-bad.yaml
python fieldkit.py resource-audit examples/workload-good.yaml
python fieldkit.py probe-audit examples/workload-bad.yaml
python fieldkit.py probe-audit examples/workload-good.yaml
python fieldkit.py alert-groups examples/alerts.json --group-by alertname,namespace
python fieldkit.py incident-prompt examples/incident.txt > incident-prompt.md
python -m unittest -v
```

Audit exit codes: 0 = completed without selected FAIL findings (not comprehensive PASS),
1 = selected FAIL findings, 2 = malformed input. INFO/WARN do not fail the command.
Examples are deliberately constructed offline fixtures, not observed production incidents.
The image `example.invalid/demo:1` is a placeholder and is not deployable.
Supported workload kinds: Pod, Deployment, StatefulSet, DaemonSet, Job, CronJob,
ReplicaSet; List wrappers accepted. Init/ephemeral containers are outside scope.

## Jenkins conditions

Uses native Pipeline: Build Step (`build`, `wait: true`, `propagate: true`).
The graph is rendered as a sequential topological order, even for independent jobs.
`agent none` prevents the orchestrator holding an executor while waiting.
Timeout is 30 minutes; edit after review. Downstream permissions, plugin versions,
parameter passing, job existence, cancellation behavior and artifact transfer must
be checked in a disposable Jenkins. No live-runtime claim is made by this package.
Do not add a deploy-to-production example or credentials automatically.

## Evidence and demand

Run `python -m unittest -v` to reproduce the included 15 tests. Tests cover graph
errors/injection, quantities, probe failures and redaction.
See [publication QA](../../docs/PUBLICATION_QA.md) for the executed checks.
These helpers have no production certification. Examples are synthetic.
For a reproducible issue, use the repository Issues page with a sanitized input,
tool name, Python version, command and observed/expected output. Do not upload
secrets or real company data. See [technical references](../../docs/UTILITY_REFERENCES.md).
