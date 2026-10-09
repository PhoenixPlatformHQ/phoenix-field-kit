# Phoenix Field Kit

Free tools and reproducible labs for concrete infrastructure and CI/CD failures.
Start with one local example; no cluster, credentials or paid API is needed for
the offline helpers and fixtures. These are narrow prototypes and templates.

## Download

- [Five DevOps / AIOps utilities — ZIP](https://raw.githubusercontent.com/PhoenixPlatformHQ/phoenix-field-kit/main/downloads/phoenix-devops-aiops-v0.1.zip)
- [Port Name Checker — ZIP](https://raw.githubusercontent.com/PhoenixPlatformHQ/phoenix-field-kit/main/utilities/port-name-check/port-name-check-free.zip)
- [Complete repository — ZIP](https://github.com/PhoenixPlatformHQ/phoenix-field-kit/archive/refs/heads/main.zip)

The five-tool ZIP includes `utilities/devops-aiops` and documentation. After
extracting it, open a terminal in `utilities/devops-aiops`. With Python 3.10+:

```sh
python -m venv .venv
# Linux/macOS:
. .venv/bin/activate
# Windows PowerShell alternative:
# .venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python fieldkit.py jenkins-chain examples/chain.yaml
python -m unittest -v
```

Use `python3` instead of `python` where that is your Python 3 command.

## Choose a tool

| Problem | Free resource | Boundary |
|---|---|---|
| Chained Jenkins jobs need an explicit dependency order | [Jenkins Chain](utilities/devops-aiops/README.md) — `jenkins-chain` | Generates a sequential Jenkinsfile; controller runtime not tested |
| CPU/memory request exceeds its limit | [Resource Audit](utilities/devops-aiops/README.md) — `resource-audit` | Selected static checks, no sizing recommendation |
| Probe refers to an undeclared port name | [Probe Audit](utilities/devops-aiops/README.md) — `probe-audit` | Selected static checks, no endpoint test |
| Alert export needs grouping | [Alert Groups](utilities/devops-aiops/README.md) — `alert-groups` | Counts records, no root-cause or deduplication claim |
| Incident evidence needs a structured triage prompt | [Incident Prompt](utilities/devops-aiops/README.md) — `incident-prompt` | Local prompt and best-effort redaction; inspect before sharing |
| Service targetPort name differs from Deployment ports | [Port Name Checker](utilities/port-name-check) | One Service + Deployment; no live connectivity test |
| Packaging selects the wrong Jenkins build | [Exact-artifact lab](labs/jenkins-exact-artifact) | Local fixture + templates; not controller output |
| A stale deployment overwrites a newer release | [GitLab deploy-race lab](labs/gitlab-deploy-race) | Local fixture + YAML fragment; not GitLab Runner output |

## Follow the series and report a problem

Follow [Phoenix on TikTok](https://www.tiktok.com/@phoenixplatformhq) or
[YouTube](https://www.youtube.com/channel/UCR8s1SbzXYewvR-Tf9UJ82Q) for reproducible
DevOps failure demos and free labs. Star this repository to find the kit again.

For a reproducible issue or an unmet workflow need, [open a GitHub issue](https://github.com/PhoenixPlatformHQ/phoenix-field-kit/issues).
Include the tool, version/commit, sanitized example, command, exit code, expected
and actual result. Do not post credentials, personal data or company logs.

## More resources

- [DNS Doctor](https://github.com/PhoenixPlatformHQ/dns-doctor) — separate Kubernetes DNS troubleshooting CLI.
- [MCP / AI Agent Production Safety Checklist](agentic-ops/MCP_PRODUCTION_SAFETY_CHECKLIST.md).
- [Executed publication checks](docs/PUBLICATION_QA.md).
- [Technical references](docs/UTILITY_REFERENCES.md).
- [Licenses](LICENSES.md).

Audit exit 0 means no selected failures in the provided input; it does not certify
health, connectivity, production readiness or complete redaction. Sample images
and job names are placeholders. These free resources do not establish paid demand.
