# Port Name Check — prototype

An offline checker for one Kubernetes Service and one Deployment. No network access and no cluster credentials.

## Run

Python 3 and PyYAML are required:

```sh
python -m pip install PyYAML
python port_name_check.py service-broken.yaml deployment.yaml
python port_name_check.py service-fixed.yaml deployment.yaml
```

Exit codes: 0 = no named-port mismatch found; 1 = mismatch; 2 = invalid or unsupported input. Numeric ports are explicitly skipped; exit 0 is NOT proof of connectivity.

The checker verifies namespace, selector and name/protocol against the supplied Deployment template. It does not discover other workloads, inspect actual Pods, validate full Kubernetes schemas or test application listeners. Init/sidecar container ports are not supported.

The samples are illustrative files, not observed cluster incidents. The corrected example passes an offline consistency check only.

Source: https://kubernetes.io/docs/concepts/services-networking/service/#port-definitions

License: Apache-2.0 for the checker and sample manifests; use is at your own discretion.
