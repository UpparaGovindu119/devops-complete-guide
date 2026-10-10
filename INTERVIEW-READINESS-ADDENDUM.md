# DevOps Interview Readiness Addendum

This addendum complements the main learning path with practical troubleshooting, AWS networking, Terraform workflows, and interview practice. Use it as a lab checklist, not as a claim that every topic is mastered.

## 1. Linux and networking troubleshooting

For each issue: reproduce it safely, inspect evidence, change one thing, and verify.

| Symptom | First checks | Useful commands |
|---|---|---|
| Service is down | service status, recent logs, listening port | systemctl status nginx; journalctl -u nginx -n 100 --no-pager; ss -lntp |
| Disk full | filesystem space and inode usage | df -h; df -i; du -xhd1 /var |
| High CPU / memory | top processes and memory pressure | top; ps aux --sort=-%cpu; free -h |
| Permission denied | owner, mode, parent directory permissions | ls -l; namei -l /path/to/file; id |
| DNS fails | resolver and name resolution | getent hosts example.com; nslookup example.com |
| Port unreachable | listening process, firewall, network path | ss -lntp; curl -v http://host:port; nc -vz host port |
| HTTP 5xx | app logs, upstream health, reverse proxy | curl -I URL; journalctl -u app -n 100 |

Practice: service starts then exits; log file grows quickly; app works locally but not from another host; DNS name fails but IP works; SSH times out; process cannot bind to a port.

## 2. AWS VPC and routing essentials

A subnet is public when its route table has a route to an Internet Gateway (IGW); an instance also needs public addressing and suitable security rules for direct IPv4 internet access. A private subnet commonly uses a NAT Gateway in a public subnet for outbound IPv4 access. A route alone does not override security groups, network ACLs, host firewall rules, or missing public addressing.

### Route-table checklist
1. Identify the VPC and the subnet's explicitly associated or main route table.
2. Check the most-specific matching route for the destination.
3. Confirm the target exists and is available: IGW, NAT Gateway, transit gateway, peering, or another target.
4. Check Security Groups (stateful) and Network ACLs (stateless; inbound and outbound rules).
5. Check whether the instance has a public IP when testing direct internet reachability.
6. Verify from the instance with DNS and connectivity tests; do not rely only on the console route entry.

### Interview comparison
- IGW: enables internet routing for eligible resources; it does not automatically make every subnet/instance public.
- NAT Gateway: lets private-subnet resources initiate outbound IPv4 connections; unsolicited inbound internet connections are not allowed through it.
- Security Group: stateful, attached to network interfaces/resources.
- Network ACL: stateless, applied at subnet boundary.
- Route table: selects the next hop; it is not a firewall.

Official reference: https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Route_Tables.html

## 3. Terraform practical workflow and failure recovery

Safe everyday sequence:
1. terraform fmt -check
2. terraform init
3. terraform validate
4. terraform plan
5. Review the plan, then terraform apply only when expected
6. terraform output and terraform state list

Read the plan before applying. Confirm account, region, workspace, state, and affected resources before any destructive action.

### Topics to practise
- Input variables, types, defaults, validation blocks, outputs, and locals.
- count vs for_each; stable resource addressing.
- Modules, input/output contracts, and version pinning.
- State purpose, locking, remote backend, and secure state storage.
- Drift detection with terraform plan.
- Import existing infrastructure, then align configuration with the imported object.
- Provider/version constraints and dependency lock file.
- Lifecycle settings and understanding replacement before apply.

### Troubleshooting
| Symptom | First response |
|---|---|
| Provider/init error | Check provider constraints, lock file, backend config, network and credentials |
| Resource already exists | Confirm it is the intended object; import or reconcile configuration rather than blindly deleting |
| State lock error | Verify no run is active and identify the lock owner before recovery |
| Unexpected replacement | Inspect immutable arguments, resource address changes, provider changes, and drift |
| Wrong resource count/address | Check count indexes or for_each keys; use a reviewed moved block/state move where appropriate |
| Authentication error | Confirm identity, account, region, and least-privilege permissions; never print secrets |

Official tutorials: https://developer.hashicorp.com/terraform/tutorials

## 4. GitHub Actions and CI/CD

Know workflow triggers, jobs, steps, runners, job dependencies, artifacts, caches, environment protection, secrets, permissions, and deployment verification.

Troubleshooting sequence:
1. Check the workflow file path: .github/workflows/*.yml or .yaml.
2. Validate YAML indentation and trigger filters.
3. Open the failed run and find the first failing step.
4. Check runner OS, working directory, tool versions, dependency lock files, and shell syntax.
5. Check permissions and secret names. Never print secret values.
6. Reproduce the failing command locally when practical.
7. Rerun and verify the resulting artifact/deployment, not only a green build.

Official guide: https://docs.github.com/en/actions/how-tos/troubleshoot-workflows

## 5. Kubernetes debugging essentials

Start with resource state, events, logs, and rollout history before changing manifests.

Useful commands:
- kubectl get pods -A
- kubectl describe pod POD -n NAMESPACE
- kubectl logs POD -n NAMESPACE --all-containers
- kubectl logs POD -n NAMESPACE --previous
- kubectl get events -n NAMESPACE --sort-by=.metadata.creationTimestamp
- kubectl get deploy,svc,ingress -n NAMESPACE
- kubectl rollout status deployment/NAME -n NAMESPACE

| Symptom | Inspect |
|---|---|
| CrashLoopBackOff | logs, exit code, command/args, config, probes, resources |
| ImagePullBackOff | image name/tag, registry access, imagePullSecrets, network |
| Pod Pending | scheduler events, requests vs capacity, node selectors/taints, PVC binding |
| Service has no response | selectors/labels, EndpointSlices, target port, readiness, NetworkPolicy |
| Rollout stuck | new ReplicaSet, probes, image pull, rollout events |

Official guide: https://kubernetes.io/docs/tasks/debug/

## 6. Monitoring and project proof

For each project, explain architecture and request/data flow; infrastructure and why each component is needed; CI stages and deployment gates; secrets and IAM; logs, metrics, dashboards and alerts; recovery/rollback; cost controls; and improvements.

Practise two end-to-end projects:
1. Terraform + AWS networking: VPC, public/private subnets, route tables, IGW/NAT design, security rules, and EC2. Explain NAT Gateway cost and clean up lab resources.
2. Container CI/CD: application → Docker image → GitHub Actions build/test → registry → deployment, with logs, health checks and rollback.

## 7. Interview answer structure

Use Situation → Checks → Root cause → Fix → Verification → Prevention.

Example: “The service was unreachable. I checked service status and listening ports, reviewed recent logs, then tested DNS and connectivity. I corrected the misconfigured route or security rule, verified the endpoint with curl, and added a monitoring check.”

If you have not personally used a feature, say so honestly and explain how you would investigate it. Do not claim production experience for a lab project.

## 8. Readiness checklist

- [ ] Explain public vs private subnet and trace traffic using route tables.
- [ ] Read a Terraform plan and identify create/update/replace/destroy actions.
- [ ] Diagnose a failed GitHub Actions run from logs.
- [ ] Diagnose CrashLoopBackOff and ImagePullBackOff.
- [ ] Explain SG vs NACL and IGW vs NAT Gateway.
- [ ] Demonstrate Linux service, disk, process, DNS, and port troubleshooting.
- [ ] Walk through two projects without reading notes.
- [ ] Give a concise answer and verify each fix.

## Official references
- Terraform tutorials: https://developer.hashicorp.com/terraform/tutorials
- Kubernetes debugging: https://kubernetes.io/docs/tasks/debug/
- GitHub Actions troubleshooting: https://docs.github.com/en/actions/how-tos/troubleshoot-workflows
- AWS VPC route tables: https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Route_Tables.html
