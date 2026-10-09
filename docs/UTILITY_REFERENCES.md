# Technical references

Primary documentation to read alongside the source and its stated limitations:

- Jenkins native Build Step: https://www.jenkins.io/doc/pipeline/steps/pipeline-build-step/
- Jenkins Copy Artifact: https://plugins.jenkins.io/copyartifact/
- Kubernetes resources: https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/
- Kubernetes probes: https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/
- Kubernetes Service ports: https://kubernetes.io/docs/concepts/services-networking/service/#port-definitions
- Alertmanager API/export model: https://github.com/prometheus/alertmanager/tree/main/api/v2
- GitLab deployment safety: https://docs.gitlab.com/ci/environments/deployment_safety/
- GitLab resource groups: https://docs.gitlab.com/ci/resource_groups/

The CLI audits only selected fields in supplied local files. These links are
references, not evidence that our helpers implement the complete platform rules.
