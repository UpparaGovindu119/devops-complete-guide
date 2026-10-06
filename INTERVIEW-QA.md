# DevOps Interview Q&A with Real-World Scenarios

This file prepares you for DevOps interviews with practical scenarios, frequently asked questions, and strong answer structure.

---

## 1. Basic DevOps Questions

### Q1: What is DevOps?
**Answer:**
DevOps is a combination of software development and IT operations. It focuses on automation, continuous delivery, monitoring, and collaboration to make software delivery faster and more reliable.

### Q2: Why is DevOps important?
**Answer:**
It reduces manual work, improves release speed, increases application reliability, enables faster rollback and recovery, and supports continuous delivery.

### Q3: What is CI/CD?
**Answer:**
CI = Continuous Integration
- Developers merge code often
- Build and test automatically

CD = Continuous Delivery / Deployment
- Automatically deploy application after validation

### Q4: Difference between CI and CD?
**Answer:**
CI focuses on automated code validation and build verification.
CD focuses on automated delivery or deployment of validated changes to environments.

### Q5: What are the main goals of DevOps?
**Answer:**
- Faster delivery
- Reduced deployment failures
- Better monitoring
- Faster recovery
- Better collaboration

---

## 2. Linux Questions

### Q6: What is the command to check disk usage?
**Answer:**
```bash
df -h
du -sh /path
```

### Q7: What is the command to monitor live logs?
**Answer:**
```bash
tail -f /var/log/app.log
```

### Q8: How do you check if a port is in use?
**Answer:**
```bash
ss -lntp | grep 8080
netstat -tulpn | grep 8080
```

### Q9: What is the difference between `tail` and `head`?
**Answer:**
- `head` shows beginning of file
- `tail` shows end of file
- `tail -f` follows updates in real time

### Q10: What is `chmod 755`?
**Answer:**
It gives owner full permissions and group/others read and execute permission only.

---

## 3. Git Questions

### Q11: What is Git?
**Answer:**
Git is a version control system used to track code changes and collaborate across teams.

### Q12: Difference between git pull and git fetch?
**Answer:**
- `git fetch` downloads remote updates without merging
- `git pull` does fetch + merge in one step

### Q13: What is a merge conflict?
**Answer:**
It happens when two developers change the same line or same file in different ways, and Git cannot decide automatically.

### Q14: How do you resolve a merge conflict?
**Answer:**
Edit the conflicting file manually, remove conflict markers, then stage and commit the result.

### Q15: Why should you not commit `.env` files?
**Answer:**
They may contain secrets, tokens, and credentials. Exposing them in Git is a security risk.

---

## 4. Docker Questions

### Q16: What is a Docker image?
**Answer:**
An image is a reusable package that contains the application and its dependencies.

### Q17: What is a Docker container?
**Answer:**
A container is a running instance of an image.

### Q18: Difference between Docker and VM?
**Answer:**
Docker is lightweight because containers share the host kernel. VMs run full guest OSes and are heavier.

### Q19: Why do we use Docker?
**Answer:**
To ensure the same application runs consistently from development to production.

### Q20: How do you inspect a running container?
**Answer:**
```bash
docker ps
docker logs <container-id>
docker exec -it <container-id> bash
```

### Q21: What is `docker-compose` used for?
**Answer:**
It helps run multiple containers together such as app + database + cache.

### Q22: Why do we use `.dockerignore`?
**Answer:**
To avoid copying unnecessary files into the image, such as `.git`, node_modules, temporary files, and secrets.

### Q23: What is a multi-stage Docker build?
**Answer:**
A multi-stage build creates a build environment and then copies only the final required artifacts into the runtime image. This keeps images small and secure.

---

## 5. Kubernetes Questions

### Q24: What is Kubernetes?
**Answer:**
Kubernetes is a container orchestration platform used to deploy, scale, and manage containerized applications.

### Q25: What is a Pod?
**Answer:**
A Pod is the smallest deployable unit in Kubernetes. It can contain one or more containers.

### Q26: Difference between Deployment and Pod?
**Answer:**
- Pod = actual running instance
- Deployment = desired state manager that keeps desired number of pods running

### Q27: What is a Service?
**Answer:**
A Service exposes a set of pods so traffic can reach them internally or externally.

### Q28: What is an Ingress?
**Answer:**
Ingress routes external traffic to services based on host/path rules.

### Q29: What are readiness and liveness probes?
**Answer:**
- Readiness: tells Kubernetes if pod is ready to serve traffic
- Liveness: tells Kubernetes if container is alive; if not, it restarts the container

### Q30: What is a rollout?
**Answer:**
A rollout is a gradual deployment of a new application version with safe update strategy.

### Q31: What is `kubectl apply` used for?
**Answer:**
It applies the YAML definition to the cluster and creates or updates resources.

### Q32: How do you troubleshoot a CrashLoopBackOff pod?
**Answer:**
```bash
kubectl get pods
kubectl describe pod <pod-name>
kubectl logs <pod-name>
```

### Q33: What is kubectl port-forward used for?
**Answer:**
It exposes a pod or service locally for testing.

```bash
kubectl port-forward svc/myapp 8080:80
```

---

## 6. Jenkins Questions

### Q34: What is Jenkins?
**Answer:**
Jenkins is an automation server used for CI/CD pipelines.

### Q35: What is a Jenkins pipeline?
**Answer:**
A pipeline is a sequence of stages such as checkout, build, test, deploy.

### Q36: Difference between CI and CD in Jenkins?
**Answer:**
CI builds and tests code automatically.
CD deploys validated code to target environments.

### Q37: What is a Jenkinsfile?
**Answer:**
A Jenkinsfile is a script that defines the pipeline in code.

### Q38: How do you trigger Jenkins automatically on code push?
**Answer:**
Use GitHub or GitLab webhooks or SCM polling.

### Q39: How do you secure Jenkins credentials?
**Answer:**
Use Jenkins Credentials store and avoid hardcoding secrets in pipeline files.

---

## 7. Terraform Questions

### Q40: What is Terraform?
**Answer:**
Terraform is an Infrastructure as Code tool used to provision infrastructure declaratively.

### Q41: What is `terraform init`?
**Answer:**
It initializes the working directory and downloads provider plugins.

### Q42: What is `terraform plan`?
**Answer:**
It shows what Terraform intends to create, change, or destroy without applying it.

### Q43: What is `terraform apply`?
**Answer:**
It applies the changes to the actual infrastructure.

### Q44: What is Terraform state?
**Answer:**
It tracks the current infrastructure and is used to compare desired and actual states.

### Q45: Why is state important?
**Answer:**
It helps Terraform know what already exists and prevents duplicate resource creation.

### Q46: What are the risks of editing state manually?
**Answer:**
It can cause drift and inconsistencies between actual infrastructure and Terraform state.

---

## 8. AWS Questions

### Q47: What is IAM?
**Answer:**
IAM is AWS Identity and Access Management used to control access to AWS resources.

### Q48: What is EC2?
**Answer:**
EC2 provides virtual servers in the cloud.

### Q49: What is S3?
**Answer:**
S3 is object storage used for files, backups, static assets, and logs.

### Q50: What is VPC?
**Answer:**
VPC is a logically isolated network in AWS.

### Q51: Why use IAM roles instead of static credentials?
**Answer:**
They are more secure, easier to rotate, and reduce secrets sprawl.

### Q52: What is EKS?
**Answer:**
EKS is Amazon-managed Kubernetes.

### Q53: What is CloudWatch?
**Answer:**
CloudWatch is AWS monitoring and logging service used for metrics and alarms.

---

## 9. Monitoring Questions

### Q54: What is Prometheus?
**Answer:**
Prometheus is a monitoring and alerting tool used to collect metrics from systems and applications.

### Q55: What is Grafana?
**Answer:**
Grafana is used to visualize metrics from Prometheus and create dashboards.

### Q56: Difference between logs and metrics?
**Answer:**
- Logs = events and messages
- Metrics = numerical values over time

### Q57: Why is monitoring important in DevOps?
**Answer:**
It helps detect failures before users notice them and is critical for incident handling.

### Q58: What is an alert threshold?
**Answer:**
A threshold is the condition that triggers an alert, like CPU > 90% for 5 minutes.

---

## 10. Troubleshooting Scenario Questions

### Q59: A Kubernetes pod is in CrashLoopBackOff. What do you do?
**Answer:**
```bash
kubectl get pods
kubectl describe pod <pod-name>
kubectl logs <pod-name>
```
Then inspect config, env vars, memory limits, and image pull issues.

### Q60: Docker container exits immediately. What do you do?
**Answer:**
```bash
docker ps -a
docker logs <container-id>
docker inspect <container-id>
```
Then inspect command, ports, env vars, and dependencies.

### Q61: Jenkins build fails at checkout. What could be wrong?
**Answer:**
Possible causes:
- Git credentials wrong
- branch not found
- repo URL incorrect
- Jenkins agent not connected
- network or firewall issue

### Q62: An app returns 404 even though pod is running. What do you check?
**Answer:**
- app is listening on expected port
- route is defined correctly
- ingress or service rules are correct
- security group or firewall does not block requests

### Q63: An app returns 500. What do you check?
**Answer:**
- DB down
- missing env variables
- app crash or exception
- bad dependency
- secret missing

### Q64: Disk is full on Linux server. What do you do?
**Answer:**
```bash
df -h
du -sh /var/*
find /var/log -type f -size +100M
```
Then clean logs, temporary files, or resize disk if necessary.

### Q65: App process is using too much CPU. What do you do?
**Answer:**
```bash
top
ps aux | sort -nr -k3 | head
```
Then identify the process, logs, and recent deployment cause.

### Q66: Jenkins pipeline is stuck waiting on an agent. What do you do?
**Answer:**
Check agent status, executor availability, connectivity, and if the node is offline or disconnected.

---

## 11. Advanced DevOps Questions

### Q67: What is blue-green deployment?
**Answer:**
Deploy new version to a separate environment and switch traffic to it once testing is passed.

### Q68: What is canary deployment?
**Answer:**
Roll out the new version to a small subset of traffic first, then gradually increase.

### Q69: What is rollback strategy?
**Answer:**
Rollback means reverting to previous stable version when the new deployment causes issues.

### Q70: What is autoscaling?
**Answer:**
Autoscaling increases or decreases resources based on traffic or CPU usage.

### Q71: What is infrastructure drift?
**Answer:**
It happens when actual infrastructure differs from the desired configuration defined in code.

### Q72: Why do DevOps teams use secret management?
**Answer:**
To avoid storing passwords and credentials in code or configuration files.

### Q73: What is a health check in Kubernetes?
**Answer:**
It tells Kubernetes when a pod is ready to receive traffic and when it should restart it.

### Q74: Why is monitoring critical in production?
**Answer:**
It helps catch issues early, reduce downtime, and improve incident response times.

---

## 12. Good Answer Structure for Interview

When asked a troubleshooting question, use this pattern:

1. Understand the problem
2. Check if service is running
3. Check logs
4. Check resource usage
5. Check configuration
6. Check dependency connectivity
7. Identify root cause
8. Fix and verify

Example answer:

> I would first check whether the service is running and then look at the relevant logs. If the logs show an app startup error, I would inspect the configuration and environment variables. If there is a port mismatch or dependency issue, I would verify network connectivity and restart the service after the fix. Finally, I would verify the service is healthy and monitor it for stability.

---

## 13. Common Interview Mistakes

- Only memorizing commands without understanding meaning
- Not checking logs first
- Not validating the root cause before restarting
- Not considering dependencies like DB or network
- Ignoring resource limits (CPU, memory, disk)
- Not writing clean and clear documentation

---

## 14. Final Interview Tips

- Learn command names and purpose
- Practice real troubleshooting flow
- Understand architecture, not just commands
- Explain your logic clearly
- Always mention verification after fix

Example interview sentence:

> I would start with logs, check service health, then validate ports and dependencies before making any change. That helps isolate the root cause rather than applying a random fix.

---

This file is designed to help you answer DevOps interview questions with confidence and real-world reasoning.

