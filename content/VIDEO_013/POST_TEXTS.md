# VIDEO_013 post texts - approved 7 October 2026

## TikTok
Your Jenkins pipeline passed. Did it package the build it started?

A Jenkins forum user described Build B #5 finishing, then #6 and #7 completing before packaging. If `copyArtifacts` uses its default selector, it chooses the latest stable build - not necessarily the one this pipeline triggered.

Fix: keep job + `build.number`, use `selector: specific(...)`, `optional: false`, propagate failures, then verify the digest.

Walkthrough only: no Jenkins controller was executed in this lab. The included local fixture output is not Jenkins output. A matching digest proves byte equality, not trusted provenance.

Free lab URL: https://github.com/PhoenixPlatformHQ/phoenix-field-kit/tree/content/video-013-jenkins-artifact/labs/jenkins-exact-artifact

#jenkins #devops #cicd #platformengineering

## YouTube Shorts
Title: Jenkins passed - but did it package the right build?

Description: same technical text as TikTok. Add the real public GitHub lab URL only after approval; do not publish with the placeholder.
