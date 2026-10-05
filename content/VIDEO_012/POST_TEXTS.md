# VIDEO_012 — approved by Fabio

Status: Editorially approved on 5 October 2026. Scheduled in Metricool: TikTok 5 October 2026 20:45 Europe/Rome (388815192); YouTube 20:47 (388815414). Both PENDING, publication not yet confirmed. Free quota verified from authenticated UI. Publication check 5 October 22:21; results check 7 October 22:21.

## YouTube title

Exit code 0 is not a Kubernetes connectivity test

## TikTok caption / YouTube description

Your check exits 0. Did it actually test the port?

Real offline run: this port-name checker skips numeric targetPort 8081 and reports "NO NAMED PORT CHECKS performed". Exit 0 means no named-port failures were found. It does not mean the app is reachable.

Our constructed YAML declares containerPort 8080. That difference deserves investigation; a declaration alone does not prove what the process actually listens on.

Next check: inspect the live Service and its EndpointSlices, then verify the application's listening port. These live checks were NOT run in this demo.

Free checker and original examples — Python 3 + PyYAML:
https://raw.githubusercontent.com/PhoenixPlatformHQ/phoenix-field-kit/0f9a9ac47778b84c1391ef2ca01d9461ccc10f30/utilities/port-name-check/port-name-check-free.zip

YouTube Shorts: copy the URL manually; description links are not clickable.

What does your CI check skip?
#kubernetes #devops #platformengineering

## Publication gates

1. Explicit human approval of the exact MP4 SHA256 and these texts.
2. Verify actual Metricool plan and residual monthly account allowance, including posts already published and reserved capacity. Two destinations use two posts. Queue count does not prove quota.
3. Refresh both networks' queue/history and best-time scores just before scheduling.
4. Confirm public checker download is still available.
5. Keep AI disclosure consistent with the actual locally synthesized voice and authored visuals; review platform settings before submission.

## Candidate slots observed 5 October 2026

| Network | Local hour | Metricool score |
|---|---|---|
| TikTok | 10:00 | 1089 |
| TikTok | 12:00 | 1050 |
| TikTok | 18:00 | 1096 |
| YouTube | 16:00 | 9351 |
| YouTube | 18:00 | 7229 |

These are test hypotheses, not proven optimal times for this audience.
No times are reserved. Candidate preferences today: TikTok 18:00, YouTube 16:00.
