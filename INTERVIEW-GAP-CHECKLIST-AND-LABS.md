# DevOps Interview Gap Checklist and Hands-on Labs

Use this master checklist with the existing learning path, interview Q&A, commands, and project guides. Mark an item complete only after you can explain it, run it, diagnose a failure, and verify the fix.

## Practice method
For each lab, record: goal → commands/config → expected result → failure injected → root cause → fix → verification → 30-second interview answer. Practise only in a safe lab, check cloud costs, and clean up resources.

## 1. Linux and operating systems
- [ ] Filesystem, navigation, permissions (chmod, chown), ownership, links, archives, grep/find/sed/awk.
- [ ] Processes and signals (ps, top, kill, systemctl), services, startup, cron.
- [ ] CPU, memory, disk, inode, ports, open files (free, df -h, df -i, du, ss, lsof).
- [ ] Logs with journalctl, /var/log, tail -f; environment variables and exit codes.
- [ ] Lab: diagnose full disk, stopped service, permission denied, and a process on the wrong port.

## 2. Networking fundamentals
- [ ] TCP vs UDP, DNS, HTTP/HTTPS, TLS, IP/subnet/CIDR, gateway, routing, NAT, ports.
- [ ] Tools: ip addr, ip route, ss -tulpn, dig/nslookup, curl -v, ping, traceroute/tracepath.
- [ ] Lab: distinguish DNS failure, routing failure, refused connection, timeout, and TLS/certificate failure.

## 3. Git and GitHub
- [ ] Working tree/index/commit, branches, merge vs rebase, reset vs revert, stash, tags, remotes.
- [ ] Resolve merge conflicts; recover safely with git reflog; use .gitignore.
- [ ] Pull requests, reviews, protected branches, permissions, PAT/SSH authentication, fork workflow.
- [ ] Lab: resolve a conflict; diagnose wrong remote, detached HEAD, rejected push, and authentication failure.

## 4. Docker
- [ ] Image vs container, Dockerfile, layers/cache, tags, registry, volumes, bind mounts, networks.
- [ ] Commands: docker ps -a, logs, inspect, exec, stats, build, run, network, volume.
- [ ] Health checks, multi-stage builds, non-root user, secrets hygiene, resource limits.
- [ ] Lab: fix bad build context, missing environment variable, container exit, port mapping, and volume permission issue.

## 5. Kubernetes
- [ ] Pod, Deployment, ReplicaSet, StatefulSet, DaemonSet, Job/CronJob, Service, Ingress, ConfigMap, Secret.
- [ ] Requests/limits, probes, scheduling, taints/tolerations, affinity, namespaces, RBAC, PV/PVC, HPA.
- [ ] Commands: kubectl get/describe/logs/events/exec, rollout status/history/undo, get endpoints.
- [ ] Lab: diagnose Pending, CrashLoopBackOff, ImagePullBackOff, failed probes, Service selector mismatch, DNS failure, PVC pending, and RBAC denial.
- [ ] Explain request path: client → DNS/Ingress or LoadBalancer → Service → ready Pod.

## 6. Terraform — high-priority hands-on
- [ ] init, fmt, validate, plan, apply, destroy, show, output, state, import, replace.
- [ ] Providers, resources, data sources, variables, terraform.tfvars, outputs, locals, validation, count, for_each, dynamic.
- [ ] Dependency graph, implicit/explicit depends_on, lifecycle, provisioner limitations, modules and module outputs.
- [ ] State: local vs remote backend, locking, state list/show/mv/rm, sensitive state, drift, refresh/plan.
- [ ] Import existing infrastructure; understand import blocks and CLI import workflow; match configuration to imported resources.
- [ ] Lab: import existing EC2, fix a wrong resource address, resolve state lock safely, detect drift, refactor to a module, and use for_each without accidental replacement.
- [ ] Safety: inspect plan before apply; never manually edit state or force-unlock without confirming the lock owner.

## 7. AWS core and VPC networking — high-priority hands-on
- [ ] IAM users/roles/policies, least privilege, EC2, EBS, S3, CloudWatch, Load Balancers, Auto Scaling.
- [ ] VPC, CIDR, public/private subnets, route tables and associations, IGW, NAT Gateway, security groups, NACLs, DNS, endpoints.
- [ ] Public EC2 needs a public IPv4/EIP as applicable, route to IGW, and permitted security-group/NACL traffic.
- [ ] Private subnet outbound IPv4 commonly uses a NAT Gateway in a public subnet; this does not make the private instance directly internet-reachable.
- [ ] Security groups are stateful; network ACLs are stateless. Check ephemeral return ports in NACLs.
- [ ] Lab: build/draw public-private subnet routes; troubleshoot missing route, IGW attachment, public IP, SG/NACL block, and broken NAT path.
- [ ] Lab: access private EC2 using a controlled approach such as Systems Manager or a tightly restricted bastion; never expose SSH to the world.
- [ ] Use VPC Flow Logs and reachability analysis where available; verify routes and rules before changing them.

## 8. GitHub Actions / CI-CD
- [ ] Workflow YAML: on, jobs, runs-on, steps, uses, run, needs, if, matrix, reusable workflows.
- [ ] Triggers: push, pull_request, workflow_dispatch, schedule; branch/path filters.
- [ ] Secrets vs variables, GITHUB_TOKEN permissions, environments/approvals, artifacts, caches, concurrency.
- [ ] Pin actions thoughtfully; understand hosted vs self-hosted runners and runner labels.
- [ ] Lab: fix runs-on typo, invalid YAML/indentation, wrong trigger, missing permissions, unavailable secret, bad working directory, cache miss, artifact not found, and failing test step.
- [ ] Diagnose from run summary and step logs; rerun only after identifying root cause.

## 9. Jenkins, monitoring, scripting and projects
- [ ] Jenkins pipeline stages, agents, credentials binding, parameters, webhooks, failed builds and console logs.
- [ ] Monitoring: metrics vs logs vs traces, Prometheus/Grafana concepts, alert thresholds, actionable alerts.
- [ ] Python/Bash basics: arguments, loops, functions, exit codes, error handling, JSON, API calls, safe retries.
- [ ] Lab: CI pipeline tests an app, builds a container, and publishes an artifact/image without committing credentials.
- [ ] Complete one end-to-end project: Git → CI test → Docker image → registry → Kubernetes deployment → monitoring/logging.
- [ ] Explain architecture, trade-offs, security, rollback, failure handling, and cost in interview language.

## 10. Interview readiness gate
- [ ] Explain each tool in 30–60 seconds without memorized-only answers.
- [ ] For every project, explain your contribution, architecture, a failure, debugging steps, and outcome.
- [ ] Practise scenario questions, command demonstrations, YAML/HCL reading, and mock interviews.
- [ ] Keep a mistake log and repeat failed labs until you can diagnose without looking at the answer.

## Official references
- Terraform tutorials: https://developer.hashicorp.com/terraform/tutorials
- Kubernetes debugging: https://kubernetes.io/docs/tasks/debug/
- GitHub Actions troubleshooting: https://docs.github.com/en/actions/how-tos/troubleshoot-workflows
- AWS VPC route tables: https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Route_Tables.html
- Terraform state: https://developer.hashicorp.com/terraform/language/state
- Kubernetes debugging applications: https://kubernetes.io/docs/tasks/debug/debug-application/
- GitHub Actions workflow syntax: https://docs.github.com/en/actions/writing-workflows/workflow-syntax-for-github-actions
