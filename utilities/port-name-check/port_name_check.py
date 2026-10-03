#!/usr/bin/env python3
"""Check one Service against one Deployment, offline. Apache-2.0."""
import argparse
import sys
import yaml

def check(service, deployment):
    if service.get('kind') != 'Service' or deployment.get('kind') != 'Deployment':
        raise ValueError('Expected a Service and a Deployment')
    sm, dm = service.get('metadata', {}), deployment.get('metadata', {})
    if sm.get('namespace', 'default') != dm.get('namespace', 'default'):
        raise ValueError('Namespaces differ')
    spec = service.get('spec', {})
    selector = spec.get('selector')
    template = deployment['spec']['template']
    labels = template.get('metadata', {}).get('labels', {})
    if not selector or any(labels.get(k) != v for k, v in selector.items()):
        raise ValueError('Service selector does not match this Deployment')
    declared = {(p.get('name'), p.get('protocol', 'TCP'))
                for c in template['spec'].get('containers', [])
                for p in c.get('ports', []) if p.get('name')}
    lines, failures, checked = [], 0, 0
    for p in spec.get('ports', []):
        target = p.get('targetPort', p.get('port'))
        protocol = p.get('protocol', 'TCP')
        if isinstance(target, str):
            checked += 1
            found = (target, protocol) in declared
            failures += not found
            lines.append(f"{'PASS' if found else 'FAIL'} targetPort {target!r} ({protocol}): "
                         + ('name found' if found else 'name missing in this Deployment'))
        else:
            lines.append(f'SKIP numeric targetPort {target}: listener not checked')
    if not checked:
        lines.append('NO NAMED PORT CHECKS performed')
    lines.append('Offline manifest check; live Pods and connectivity not tested.')
    return lines, failures

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('service')
    parser.add_argument('deployment')
    args = parser.parse_args()
    try:
        with open(args.service) as f: service = yaml.safe_load(f)
        with open(args.deployment) as f: deployment = yaml.safe_load(f)
        lines, failures = check(service, deployment)
    except (ValueError, KeyError, TypeError, OSError, yaml.YAMLError) as e:
        print(f'INPUT ERROR: {e}', file=sys.stderr)
        return 2
    print('\n'.join(lines))
    return 1 if failures else 0

if __name__ == '__main__':
    sys.exit(main())
