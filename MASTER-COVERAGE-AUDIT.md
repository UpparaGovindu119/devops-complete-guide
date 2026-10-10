# Master Coverage Audit — DevOps Interview Preparation

**Purpose:** one source of truth to track coverage across the existing DevOps course, interview Q&A, projects, command sheet, Python course, Kubernetes YAML reference, and troubleshooting guides.

**Truthful status:** documentation/checklists have been added; a checkbox is complete only after the learner performs the lab and records evidence. This file does not claim that every official documentation page has already been executed or that a job/interview outcome is guaranteed.

## How to mark complete
For each item: (1) read the linked official documentation, (2) do the task in a safe lab, (3) capture command/output or configuration, (4) diagnose a failure, (5) fix and verify, (6) explain the result in 30–60 seconds. Check off only after doing all six. Never commit credentials, tokens, private keys, kubeconfigs, or state secrets.

## A. The four requested official documentation tracks

### A1. Terraform tutorials
Official index: https://developer.hashicorp.com/terraform/tutorials

- [ ] Read the tutorial index and select tutorials relevant to the installed Terraform/provider versions.
- [ ] Install/verify Terraform and configure provider credentials safely.
- [ ] Initialise a working directory; understand providers, resources, data sources and dependencies.
- [ ] Format and validate configuration; read and review a plan before apply.
- [ ] Variables, type constraints, defaults, tfvars, locals, outputs and validation.
- [ ] Resource references, expressions, functions, conditional expressions, count and for_each.
- [ ] Modules: inputs, outputs, sources, version pinning and refactoring.
- [ ] State: state list/show/mv/rm, local vs remote backend, locking, sensitive data and drift.
- [ ] Import existing infrastructure using the documented workflow; align configuration with the real object and inspect the resulting plan.
- [ ] Lifecycle/meta-arguments, dependency ordering and replacement behaviour.
- [ ] Workspaces and environment separation; know when separate configurations/backends are preferable.
- [ ] Provider/resource version upgrades and safe plan review.
- [ ] Lab: deploy a small disposable resource, change it, inspect plan, then destroy only the lab resource.
- [ ] Lab: import an existing test resource, reconcile drift, and verify no unintended replacement.
- [ ] Record Terraform version, provider versions, command output, root cause and final plan.

### A2. Kubernetes debugging tasks
Official index: https://kubernetes.io/docs/tasks/debug/

- [ ] Inspect nodes, namespaces, Pods, Deployments, Services, endpoints and events.
- [ ] Use describe, logs, previous logs, exec and label/selector inspection.
- [ ] Debug Pending: resources, scheduling, taints/tolerations, affinity, node selectors and PVCs.
- [ ] Debug CrashLoopBackOff: logs, command/args, configuration, dependencies and probes.
- [ ] Debug ImagePullBackOff: image/tag, registry connectivity, credentials and image pull secrets.
- [ ] Debug readiness/liveness/startup probes and rollout status/history/undo.
- [ ] Debug Service with no endpoints: selectors, Pod labels and readiness.
- [ ] Debug DNS, Service networking, NetworkPolicy and application listening ports.
- [ ] Debug PVC/PV/StorageClass binding and mount errors.
- [ ] Debug RBAC 401/403; verify active identity and least-privilege permissions.
- [ ] Inspect resource requests/limits, OOMKilled, node pressure and quotas.
- [ ] Verify a fix using readiness, events, endpoints and rollout status; record before/after evidence.
- [ ] Practise only in a test cluster/namespace; do not delete production resources as a first response.

### A3. GitHub Actions troubleshooting
Official index: https://docs.github.com/en/actions/how-tos/troubleshoot-workflows

- [ ] Workflow file path, YAML syntax, event triggers and branch/path filters.
- [ ] Job dependencies, conditions, matrices, reusable workflows and concurrency.
- [ ] Correct runs-on label, hosted/self-hosted runner availability and permissions.
- [ ] Checkout, working directory, shell, environment variables and runtime versions.
- [ ] Least-privilege GITHUB_TOKEN permissions; repository/environment secrets and variables.
- [ ] Secret availability restrictions by event; never echo or print secrets.
- [ ] Cache keys/restore keys and artifact upload/download paths, names and retention.
- [ ] Diagnose first failing step from run summary and logs; distinguish setup failure from test failure.
- [ ] Dependency/service container readiness, network access, timeouts and flaky tests.
- [ ] Pin third-party actions appropriately; review permissions before granting write access.
- [ ] Lab: fix a deliberately broken workflow in a test repository, rerun, verify downstream jobs and record root cause.

### A4. AWS VPC route tables
Official guide: https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Route_Tables.html

- [ ] Identify VPC CIDR, subnet CIDRs, route tables and explicit/main associations.
- [ ] Explain local routes, destination/target, longest-prefix match and propagated routes where used.
- [ ] Public subnet: default route to attached IGW, instance public IPv4/EIP as applicable, SG/NACL and OS firewall.
- [ ] Private IPv4 egress: route to NAT Gateway in a public subnet; NAT subnet routes to IGW.
- [ ] Distinguish route table, security group (stateful) and network ACL (stateless).
- [ ] Check return/ephemeral traffic, source/destination rules and process listening on the expected port.
- [ ] Debug VPC peering/transit gateway/VPN routes when used; routes must exist on both relevant sides.
- [ ] Debug DNS settings, VPC endpoints and Flow Logs when applicable.
- [ ] Lab: draw public/private route tables and diagnose a missing route, wrong association, missing public IP, SG/NACL block and broken NAT path.
- [ ] Cost/safety: NAT Gateways and other resources can cost money. Check the estimate, use a sandbox, and clean up after verification.

## B. Existing DevOps curriculum — coverage inventory

Use these existing files rather than duplicating everything:
- Learning path: https://github.com/UpparaGovindu119/devops-complete-guide/blob/main/LEARNING-PATH.md
- Interview Q&A: https://github.com/UpparaGovindu119/devops-complete-guide/blob/main/INTERVIEW-QA.md
- Real-world projects: https://github.com/UpparaGovindu119/devops-complete-guide/blob/main/REAL-WORLD-DEVOPS-PROJECTS.md
- Top 100 commands: https://github.com/UpparaGovindu119/devops-complete-guide/blob/main/TOP-100-DEVOPS-COMMANDS.md
- Python for DevOps: https://github.com/UpparaGovindu119/devops-complete-guide/blob/main/PYTHON-FOR-DEVOPS.md
- Tool-wise troubleshooting: https://github.com/UpparaGovindu119/GitHub-Troubleshooting-Guide/blob/main/tool-wise-troubleshooting.md
- Troubleshooting interview script: https://github.com/UpparaGovindu119/GitHub-Troubleshooting-Guide/blob/main/INTERVIEW-READY.md
- Tool-wise quick sheet: https://github.com/UpparaGovindu119/GitHub-Troubleshooting-Guide/blob/main/TOOL-WISE-INTERVIEW-QUICK-SHEET.md
- Kubernetes YAML reference: https://github.com/UpparaGovindu119/GitHub-Troubleshooting-Guide/blob/main/KUBERNETES-ALL-YAML-TYPES.md
- Practical official-doc labs: https://github.com/UpparaGovindu119/GitHub-Troubleshooting-Guide/blob/main/OFFICIAL-DOCS-PRACTICAL-TROUBLESHOOTING-LABS.md

### Cross-tool interview coverage checklist
- [ ] Linux: files/permissions, processes/services, systemd, CPU/memory/disk/inodes, logs, cron, shell pipelines, exit codes.
- [ ] Networking: IP/CIDR/subnetting, TCP/UDP, DNS, HTTP/TLS, routing, NAT, ports, load balancing, proxies, firewalls.
- [ ] Git/GitHub: branches, merge/rebase, conflict, reset/revert/reflog, remotes, SSH/PAT, PR reviews, protected branches.
- [ ] Bash/PowerShell/Python: variables, loops, functions, arguments, error handling, exit codes, JSON, API automation.
- [ ] Docker: images/containers, Dockerfile, layers/cache, volumes, networks, registry, health checks, resource limits, security.
- [ ] Kubernetes: workloads, Services, Ingress, ConfigMap/Secret, probes, scheduling, RBAC, storage, autoscaling, network policies, rollouts.
- [ ] Terraform: HCL, providers, state, import, modules, variables, validation, for_each/count, lifecycle, backend, locking, drift, plan/apply safety.
- [ ] AWS: IAM, EC2, EBS, S3, VPC, route tables, IGW/NAT, SG/NACL, load balancing, autoscaling, CloudWatch, endpoints, cost and security.
- [ ] CI/CD: GitHub Actions and Jenkins basics, pipeline stages, test/build/package/deploy, artifacts, secrets, approvals, rollback.
- [ ] Observability/SRE: metrics/logs/traces, dashboards, actionable alerts, SLI/SLO/SLA, incident response, postmortems, availability and recovery.
- [ ] Security: least privilege, secret management, patching, image/dependency scanning, TLS, IAM, audit logs, supply-chain basics.
- [ ] Delivery/project skills: architecture diagram, README, deployment/runbook, rollback plan, health checks, cost estimate, trade-offs.
- [ ] Interview communication: explain what you built, your contribution, failure, evidence, root cause, fix, verification and lesson learned.

## C. Required lab evidence log
Copy one record per scenario:
- Date and lab/environment:
- Topic and expected behaviour:
- Exact symptom/error:
- Commands/config/logs checked:
- Evidence-based root cause:
- Fix and why:
- Verification output:
- Security/cost/cleanup check:
- 30–60 second interview answer:
- Status: Not started / Practised / Verified / Needs revision

## D. Final readiness gate
- [ ] Every checkbox above is either Verified or explicitly marked Needs revision.
- [ ] No secret values are present in the repository or logs.
- [ ] Terraform plan reviewed before any apply; lab resources cleaned up.
- [ ] Kubernetes fixes verified with status/events/logs rather than guesses.
- [ ] GitHub Actions workflow passes from a clean run and permissions are minimal.
- [ ] AWS route-table diagram and connectivity failure diagnosis explained without notes.
- [ ] At least one end-to-end project is demonstrable and the user can explain it honestly.
- [ ] Mock interview completed; weak answers converted into follow-up labs.

**Important:** documentation coverage is not the same as hands-on completion. This tracker helps find gaps; it cannot guarantee that every possible interview question will be asked or that every upstream documentation page remains unchanged.
