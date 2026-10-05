# DevOps chain: research and production brief — 5 October 2026

Decision: next video is Jenkins artifact provenance across chained pipelines, not another isolated manifest typo.
Scope: research-driven educational content. These sources establish practitioners' questions and documented mechanisms, not market prevalence or willingness to pay. No paid product approved.

## 1. VIDEO_013 — Jenkins: successful jobs, wrong artifact
Primary practitioner source: https://community.jenkins.io/t/best-practice-for-synchronizing-artifact-retrieval-for-declarative-pipeline-stages/29709
Posted 11 April 2025; author confirms proposed solution on 17 April.
Accurate interpretation: the author describes a synchronization risk/scenario (build B #5 can be replaced by later #7 while another stage runs), not a verified production outage.
Vendor references:
- https://plugins.jenkins.io/copyartifact/
- https://www.jenkins.io/doc/pipeline/steps/pipeline-build-step/
- https://www.jenkins.io/doc/pipeline/steps/copyartifact/

Mechanism: lastSuccessful or default latest-stable selectors can select a build other than the one triggered by the orchestrating run. Capture the build step's returned build number; pass the specific identifier to packaging and copy using specific(build-number). Default copyArtifacts uses latest stable, not latest successful: do not conflate them.
Wait for downstream completion, propagate failures or explicitly inspect result. Numeric build identifiers apply to one job; the release correlation must retain job + build number, not number alone.
Archived artifacts, Copy Artifact plugin and appropriate copy permissions required. Do not weaken permission checks to make demo work.
Build selection prevents the chosen race; it is not a cryptographic provenance or security guarantee.

Hook candidate: “Your Jenkins pipeline passed. Did it package the build it started?”
Evidence sequence: orchestrator starts B #5; independent B #6 completes while slow A runs; broken selector copies B #6; correct selector copies B #5. Use original fixture numbers in recorded demo and label it as an authored lab.
Free deliverable: minimal orchestrator/producer/package Jenkinsfiles, README, exact-run selection and digest verification, plus test evidence. No new pipeline framework or SaaS.
Acceptance: actual observed archive/build IDs and artifact hashes before and after; downstream failure stops promotion; missing/deleted expected artifact fails closed; overlapping independent producer run does not change selected artifact. Digest test verifies byte equality only; it does not attest trusted source/build.
If no Jenkins execution environment is available at €0 without host changes, make a clearly labeled code walkthrough or hold the runtime demonstration. Do not present shell fixtures or source-derived outputs as Jenkins executions.
Short: 25–35 seconds, one failure and fix. Native code can be shown without claiming runtime QA. Only call the delivered template runtime-tested after actual Jenkins evidence exists.
No naming/logo changes, no public scheduling before editorial approval.

## 2. GitLab: an older deployment overwrites a newer release
Vendor source: https://docs.gitlab.com/ci/environments/deployment_safety/
Practitioner forum examples discovered:
https://forum.gitlab.com/t/single-pipeline-outdated-deployment-jobs/76431
https://forum.gitlab.com/t/prevent-outdated-deployment-jobs-for-automatic-jobs/84698
Some forum detail pages return 403; do not rely on snippets for their technical conclusions.
Fix direction: same environment resource_group to serialize deploy jobs, plus Prevent outdated deployment jobs for relevant outdated-job behavior.
Important limits: serialization does not itself reject an older release; job age uses start time, not commit timestamp. Rollback retries require a deliberate policy, not an unconditional ban on older commits.
Demo: two actual pipeline runs with differing timings; compare final release identity and explain environment scope.
Free asset: documented CI snippet and concurrency test scenario; do not invent a replacement scheduler.

## 3. PostgreSQL migration: adding an index blocks writers
First-person Reddit report:
https://www.reddit.com/r/devops/comments/1swbj6e/we_took_production_down_for_20_minutes_because_of/
Author reports 20-minute outage from index migration. Self-reported, independently unaudited, database engine not established by the report; never imply it was necessarily PostgreSQL.
Vendor validation for a PostgreSQL-specific lab:
https://www.postgresql.org/docs/current/sql-createindex.html
Mechanism: ordinary CREATE INDEX blocks table writes. CONCURRENTLY avoids that specific write exclusion, but takes more work, can wait on transactions, may leave invalid indexes and cannot run inside a transaction block.
Demo: controlled non-production database sessions; observe writer wait then compare concurrent build; show migration-runner transaction handling. Not a blanket zero-downtime guarantee.
Free asset: migration review checklist and runnable lab; no regex checker sold as safety certification.

## Reddit corroboration for artifact promotion
https://www.reddit.com/r/devops/comments/rrncr9/when_you_build_your_artifact_in_ci_and_cd_or_only/
Older discussion, not a current trend. Original post and a first-person commenter discuss building again during CD and different build-agent SDK versions. Supports choosing exact tested artifacts as an operational theme; technical fix uses vendor references above.

## Prompt included in free lab (draft)
Act as a read-only release reviewer. Given sanitized orchestrator logs, job/build IDs, source revision, archive metadata and observed SHA256 values, reconstruct which run produced each artifact and which bytes packaging actually consumed. Cite evidence IDs for each conclusion. Report MATCH, MISMATCH or UNKNOWN for job/build selection and digest equality separately. Missing evidence is UNKNOWN, never PASS. Do not infer trusted provenance from a matching digest, execute commands, request credentials or invent outputs.

## Measurement and limits
Keep the every-two-days cadence and €0 cap. Compare with VIDEO_011/012: watch time/retention if available, saves/shares, external questions about applying the template, verified downloads/usage; ND for unavailable metrics.
No paid extension until users show an explicit need and willingness to pay; paid technical work remains subject to IBM conflict check.
Prefer one complete failure→fix lab over five new utilities. If the next short cannot explain its specific fix clearly, split into two parts using the same lab rather than build new unrelated assets.
