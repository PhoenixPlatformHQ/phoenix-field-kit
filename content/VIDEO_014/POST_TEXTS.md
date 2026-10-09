# VIDEO_014

YouTube title: New release deployed. Then the old pipeline replaced it.

+Your newer release deployed first. Then an older pipeline put stale code back into production.

Three controls: resource_group serializes deployments; process_mode controls queue selection; Prevent outdated deployment jobs is a separate setting. For continuous delivery, evaluate newest_ready_first with idempotent deploy scripts.

Manual jobs and rollback retries need review: job age uses job start time, not commit chronology.

The demo is a real local Python fixture, not GitLab Runner output. GitLab configuration is explained from official documentation; it was not executed on a GitLab server.

Free fixture and YAML template: https://github.com/PhoenixPlatformHQ/phoenix-field-kit/tree/content/video-014-gitlab-deploy-race/labs/gitlab-deploy-race

#gitlab #devops #cicd #platformengineering
