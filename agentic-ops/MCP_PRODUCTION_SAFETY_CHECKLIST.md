# MCP / AI Agent Production Safety

## 10 checks before an agent can touch production

AI agents can invoke tools when a platform exposes machine-consumable interfaces such as APIs or MCP tools. Treat that access path as a production interface: authenticate it, authorize each capability, constrain its scope, record its actions and verify outcomes.

## What this checklist is

A short pre-production review for teams connecting an AI agent to operational tools. Use it before enabling production access and repeat it whenever identities, tools, permissions or workflows change.

## What this checklist is not

- A claim that MCP or AI agents are insecure by default.
- A substitute for threat modeling, platform security review or incident response.
- A guarantee that an integration is secure.
- Permission to expose production credentials during testing.

## The checklist

| CONTROL | WHY IT MATTERS | VERIFY |
|---|---|---|
| 1. Least-privilege identity | A dedicated machine identity limits what the agent can reach and separates its actions from human operators. | Confirm the identity is unique to the workload, has no inherited admin role and can access only required resources. |
| 2. Per-tool authorization | Access to one integration must not silently authorize every operation it exposes. | Map every enabled tool to allowed actions and deny unapproved tools by default. Test one allowed and one denied call. |
| 3. Explicit production scope | Ambiguous targets can turn a valid action into a production mistake. | Require an allowlist for environments, clusters, namespaces, accounts and resource types. Reject missing or out-of-scope targets. |
| 4. Approval gates for high-risk actions | Destructive or high-impact mutations need deliberate authorization at execution time. | Require approval for delete, privileged access, secret changes, broad configuration changes and other defined high-risk actions. Verify denial and timeout behavior. |
| 5. Auditable tool calls | Teams need to reconstruct who or what requested, approved and executed an action. | Record identity, tool, sanitized arguments, target, approval, timestamp, result and correlation ID in protected logs. |
| 6. Secret isolation | Prompts, model context and ordinary logs are not secret stores. | Use short-lived credentials from a dedicated secret boundary. Confirm secrets are redacted and never returned in tool output or traces. |
| 7. Sandbox and execution boundaries | Tool execution should not grant unrestricted host, network or filesystem access. | Document the runtime boundary and allowlists. Test blocked filesystem paths, network destinations and subprocess capabilities. |
| 8. Rate and action limits | Bounded automation reduces blast radius from loops, retries and unexpected plans. | Set per-tool rate, concurrency, retry, time and mutation limits. Verify the system stops when a limit is reached. |
| 9. Rollback and kill switch | Operators need a fast way to stop automation and recover from a bad change. | Demonstrate identity revocation, tool disablement and workflow cancellation. Document rollback or restoration for every mutating tool. |
| 10. Post-action verification | A successful API response does not prove the intended production state. | Define a read-after-write check, expected invariants and failure escalation. Verify actual state before reporting success. |

## Example approval flow

```text
Agent proposes: restart workload payments-api in payments-prod
        ↓
Policy checks: identity + tool + target + action limits
        ↓
Approval gate: operator sees exact action, target and rollback plan
        ↓ approve / deny / expire
Tool executes with short-lived scoped credentials
        ↓
Platform records request, approval, sanitized arguments and result
        ↓
Independent read verifies rollout state and workload health
        ↓
Agent reports verified outcome or escalates failure
```

Approval should be bound to the exact action and target. Any material change to the proposed operation requires a new authorization decision.

## Release decision

Do not enable production access while any required control is unverified. Record the evidence, owner and review date for each check.

## Primary references

- [Model Context Protocol — Tools](https://modelcontextprotocol.io/specification/2025-06-18/server/tools): MCP servers can expose tools that models can discover and invoke; the specification recommends human visibility and the ability to deny invocations.
- [NIST SP 800-53 Rev. 5](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final): security and privacy controls including access control, least privilege, audit and accountability.
- [NIST SP 800-207 — Zero Trust Architecture](https://csrc.nist.gov/pubs/sp/800/207/final): authentication and authorization are evaluated before access to enterprise resources.
